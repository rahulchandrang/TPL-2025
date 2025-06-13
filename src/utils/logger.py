class Logger:
    def __init__(self, config_file='config/logging.yaml'):
        import logging
        import logging.config
        import yaml

        with open(config_file, 'r') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(__name__)

    def log_message(self, message, level='info'):
        log_levels = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical
        }
        log_levels.get(level, self.logger.info)(message)