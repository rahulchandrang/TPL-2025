import logging
import logging.config
from pythonjsonlogger import jsonlogger


class AppInsightsHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        # Integrate with Azure Application Insights SDK or exporter here
        # For production, use Azure Monitor OpenCensus/Opentelemetry exporters
        pass


class Logger:
    def __init__(self, config_file='config/logging.yaml'):
        import yaml

        with open(config_file, 'r') as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(__name__)

        # Add JSON formatter for structured logging
        for handler in self.logger.handlers:
            handler.setFormatter(jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s'))

        # Add Azure Application Insights handler (stub)
        self.logger.addHandler(AppInsightsHandler())

    def log_message(self, message, level='info', extra=None):
        log_levels = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical
        }
        if extra is not None:
            log_levels.get(level, self.logger.info)(message, extra=extra)
        else:
            log_levels.get(level, self.logger.info)(message)