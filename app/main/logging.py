import logging.config

LOGGING_CONFIG = {
    'version': 1,

    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'mail'],
        },
        'console': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'info',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'mail': {
            'level': 'ERROR',
            'formatter': 'error',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': 'localhost',
            'fromaddr': 'monitoring@domain.com',
            'toaddrs': ['dev@domain.com', 'qa@domain.com'],
            'subject': 'Critical error with application name'
        }
    },

    'formatters': {
        'info': {
            'format': '%(asctime)s | %(levelname)s | %(name)s (%(module)s) | %(lineno)s | %(message)s'
        },
        'error': {
            'format': '%(asctime)s | %(levelname)s | %(name)s  (%(module)s) | %(lineno)s | %(message)s'
        },
    },

}

# Loggers
logging.config.dictConfig(LOGGING_CONFIG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.INFO)
