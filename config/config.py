import os
import yaml

class Config:
    _instance = None

    def __new__(cls, env=None, path="../config"):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            # Ensure instance gets initialized with env and path on first instantiation
            cls._instance._init(env, path)
        return cls._instance

    def __init__(self, env=None, path="../config"):
        # Make sure __init__ does not reinitialize if it has already been initialized
        if not hasattr(self, 'initialized'):
            self.config = self.load_config()

    def _init(self, env, path):
        """
        Private initialization method to initialize env and path
        only when the singleton is first created.
        """
        self.env = env or os.getenv('STAGE', 'local')
        self.path = path

    def load_config(self):
        config_file = os.path.join(self.path, f'{self.env}.yaml')
        # Load from local file system for 'local' environment using self.path
        try:
            with open(config_file, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Local configuration file {config_file} not found")
        except Exception as e:
            raise FileNotFoundError(f"Error loading local configuration file {config_file}: {str(e)}")

    def get(self, key, default=None):
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
        except KeyError:
            return default
        return value

    def setup_config(self):
        self.__setup_simulation_path__()

    def __setup_simulation_path__(self):
        simulation_path = self.get("simulation_path")
        os.system("mkdir ./" + simulation_path)

    def __setup_example_path__(self):
        example_path = self.get("example_path")
        os.system("mkdir ./" + example_path)