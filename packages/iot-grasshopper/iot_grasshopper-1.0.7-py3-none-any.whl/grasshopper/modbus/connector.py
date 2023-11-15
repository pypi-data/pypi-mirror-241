"""AWS IoT Greengrass custom modbus connector"""
import time
import json
from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import QOS, PayloadFormat, PublishMessage, JsonMessage
from ..config.configloader import ConfigLoader
from ..common import getLogger
from .connection import SingleModbusConnection

__copyright__ = "Copyright 2023 binchoo"
__license__ = "GPLv3"
__author__ = "Jaebin Joo"
__email__ = "jaebin.joo@megazone.com"


_logger_ = getLogger(__name__)


class GGv2ModbusConnector:

    AWS_IOT_CORE = 'IotCore'
    LOCAL_PUBSUB = 'PubSub'

    def __init__(self, ipc: GreengrassCoreIPCClientV2, conn: SingleModbusConnection, cfg: ConfigLoader, callback=None):
        '''Creates a GGv2ModbusConnector.This component reads modbus holding registers
        and send values to greengrass local PubSub.
        The runtime **must provide** AWS IoT Greengrass V2 Nucleus, local PubSub, and MQTT Bridge.
        Current component **must be privileged** in use of those GGv2 components.

        :param conn_factory: SingleModbusConnection that creates modbus connection to host:port
        :param cfg: ConfigLoader that provides configuration value
        '''
        self.ggv2_ipc = ipc
        self.conn_factory = conn
        self.config = cfg
        self.callback = callback
        self.modbus_client = None

        self.conn_factory.get_host      = lambda: self.config.read('server/host')
        self.conn_factory.get_port      = lambda: self.config.read('server/port')
        self.conn_factory.get_max_retry = lambda: self.config.read('server/max_retry')
        self.conn_factory.get_wait_sec  = lambda: self.config.read('server/wait_sec')
        self.conn_factory.get_timeout   = lambda: 2*int(self.config.read('client/wait_sec'))


    def start(self):
        '''Periodically retrieves holding registers from server.
        Values will soon be sent to Greengrass local PubSub via IPC.
        When appropriate configuration not provided, it talks to 127.0.0.1:502 by default.

        :raises RuntimeError when connection finally not established
        '''
        while True:
            if self.config.is_valid():
                self.setup_modbus()
                registers = self._read_holding_registers()
                if registers is not None:
                    self._publish_registers(registers)
                    self._wait()

    def setup_modbus(self):
        '''Get connected to modbus server'''
        if not self.check_modbus() \
                or (self.conn_factory.get_host() != self.modbus_client.comm_params.host) \
                or (self.conn_factory.get_port() != self.modbus_client.comm_params.port):

            self.close_modbus()
            self.modbus_client = self.conn_factory.get()

    def close_modbus(self):
        '''Cleans-up modbus connection'''
        if self.modbus_client is not None:
            self.modbus_client.close()
        self.modbus_client = None

    def check_modbus(self):
        '''Verify connection is non-null and actually connected to the server
        :return: True if connection is established else False
        '''
        return self.modbus_client is not None \
            and self.modbus_client.connected

    def _read_holding_registers(self):
        '''Read holding registers from server

        :raises RuntimeError when connection is invalid
        :raises Exception when impossible in reading registers
        '''
        registers = None
        try:
            slave = max(0, self.config.read('holding_register/slave'))
            start, end_exclusive = self.config.read('holding_register/range')
            rr = self.modbus_client.read_holding_registers(address=start, count=(end_exclusive - start), slave=slave)
            registers = rr.registers
        except Exception as e:
            self.close_modbus()
            _logger_.exception(e)
            _logger_.warning(f"Failed to read holding registers: {e}")
        return registers

    def _parse(self, registers, mapping):
        data = {}
        for attr, index in zip(mapping.attributes, mapping.indices):
            try:
                data[attr] = registers[index]
            except Exception as e:
                _logger_.exception(e)
        return data

    def _publish_registers(self, registers):
        '''Publish to local PubSub after converting registers in json-formatted data\n
        :param registers: values retrieved from server
        '''
        try:
            iot_mappings = self.config.read('iot_mapping')
            for place, mapping in iot_mappings.__dict__.items():
                target = getattr(mapping, 'target')
                topic = getattr(mapping, 'topic')
                model = self._parse(registers, mapping)
                self._publish_to(target, topic, model)
        except Exception as e:
            _logger_.warning(e)
        finally:
            self._run_callback(self.callback, registers)

    def _publish_to(self, target, topic, model):
        if self.ggv2_ipc is not None:
            _logger_.debug(f"{time.ctime()} {topic}: {model} via {target}")
            if self.AWS_IOT_CORE == target:
                self._publish_to_iotcore(topic, model)
            elif self.LOCAL_PUBSUB == target:
                self._publish_to_pubsub(topic, model)
            else:
                _logger_.warning(f"Wrong target destination: {target}")
        else:
            _logger_.warning("IPC client is missing")

    def _publish_to_iotcore(self, topic, model):
        message = json.dumps(model)
        self.ggv2_ipc.publish_to_iot_core_async(topic_name=topic, qos=QOS.AT_LEAST_ONCE,
                                                payload=message, payload_format=PayloadFormat.UTF8)

    def _publish_to_pubsub(self, topic, model):
        message = PublishMessage(json_message=JsonMessage(message=model))
        self.ggv2_ipc.publish_to_topic_async(topic=topic, publish_message=message)

    def _run_callback(self, func, model):
        if func is not None:
            func(model)

    def _wait(self):
        wait_sec = max(0, self.config.read('client/wait_sec'))
        time.sleep(wait_sec)

    def close(self):
        self.close_modbus()
        if self.ggv2_ipc is not None:
            self.ggv2_ipc.close()
        if self.config is not None:
            self.config.close()
