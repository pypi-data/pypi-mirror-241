import configparser

class TangazifyConfig:
    def __init__(self, config_file='tangazify_config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        # Set default values if not present in the config file
        self.api_key = self.config.get('TANGAZIFY', 'api_key', fallback='your_api_key')
        self.secret_key = self.config.get('TANGAZIFY', 'secret_key', fallback='your_secret_key')
        self.server_url = self.config.get('TANGAZIFY', 'server_url', fallback='http://127.0.0.1:8000')
        self.video_width = int(self.config.get('DISPLAY', 'video_width', fallback='640'))
        self.video_height = int(self.config.get('DISPLAY', 'video_height', fallback='480'))
        # Add other configuration options as needed
