"""Configuration management utilities"""
import os, time
import json
import types
import threading
from ..common import getLogger


__copyright__ = "Copyright 2023 binchoo"
__license__ = "GPLv3"
__author__ = "Jaebin Joo"
__email__ = "jaebin.joo@megazone.com"


_logger_ = getLogger(__name__)


def import_config(path: str):
    '''
    Reads json-formatted file and creates a configuration object from it
    :return: config
    '''
    try:
        with open(path, 'r') as fp:
            config = json.load(fp, object_hook=lambda x: types.SimpleNamespace(**x))
            return config
    except json.JSONDecodeError:
        _logger_.error(f"{path} has invalid format")
    except Exception:
        _logger_.error(f"{path} is not readable")
    return None


class ConfigLoader:

    def __init__(self, path: str, interval: float):
        '''Creates ConfigLoader.
        It periodically detects modification of the configuration file, and updates values.
        :param path: configuration file path
        :param interval: hot replacement interval
        '''
        self.path = path

        self.config = None
        self.modified_time = None
        self.previous_config = None

        self.interval = min(interval, 60)
        self.runnable = True

    def is_valid(self):
        return self.config is not None

    def keep_replacing(self):
        while self.runnable:
            if self.check_modification():
                self.replace_config()
            time.sleep(self.interval)


    def check_modification(self):
        modified = None
        try:
            modified = os.path.getmtime(self.path) != self.modified_time
            if modified:
                _logger_.debug("Change detected")
            else:
                _logger_.debug("Change not detected")
        except Exception as e:
            _logger_.warning(f"Error in reading config file '{self.path}': {e}")
        return modified

    def replace_config(self):
        self.previous_config = self.config
        self.config = import_config(self.path)
        self.modified_time = os.path.getmtime(self.path)

        _logger_.info(f"Configuration has been changed\n"
                      f"\tFrom: {self.previous_config}\n"
                      f"\tTo: {self.config}")

    def run(self):
        hot_replacer = threading.Thread(target=self.keep_replacing)
        hot_replacer.start()

    def close(self):
        self.runnable = False
        _logger_.debug("ConfigLoader will stop")

    def read(self, keypath: str=None, config=None):
        obj = self.config if config is None else config
        keys = keypath.split("/")
        if keys is None or len(keys) == 0:
            return obj
        else:
            for i, key in enumerate(keys):
                if hasattr(obj, key):
                    if i + 1 == len(keys):
                        return getattr(obj, key)
                    else:
                        obj = getattr(obj, key)
                else:
                    return None
            return obj

    @DeprecationWarning
    def is_key_modified(self, keys=None):
        current_value = self.read(keys, self.config)
        previous_value = self.read(keys, self.previous_config)

        if hasattr(current_value, '__dict__') \
                and hasattr(previous_value, '__dict__'):

            return not (current_value.__dict__ == previous_value.__dict__)

        elif not hasattr(current_value, '__dict__') \
                and not hasattr(previous_value, '__dict__'):

            return current_value == previous_value

        return False


def automatic_loader(path: str='config.json', poll_interval: float = 5) -> ConfigLoader:
    '''
    :param poll_interval: poll interval seconds
    :return: ConfigLoader
    '''
    config_loader = ConfigLoader(path, poll_interval)
    config_loader.run()
    return config_loader
