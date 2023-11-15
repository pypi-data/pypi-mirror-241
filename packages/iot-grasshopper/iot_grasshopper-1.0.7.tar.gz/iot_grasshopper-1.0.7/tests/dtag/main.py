import logging
import grasshopper
from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from grasshopper.config import automatic_loader
from grasshopper.modbus import ModbusTCPConnection, GGv2ModbusConnector


logger = grasshopper.common.getLogger(__name__)
grasshopper.common.setLogLevel(level=logging.INFO)


if __name__ == '__main__':
    connector = GGv2ModbusConnector(
        ipc=None,
        conn=ModbusTCPConnection(),
        cfg=automatic_loader())

    try:
        connector.start() # synchronous
    except Exception as e:
        logger.exception(e)
    finally:
        connector.close()
