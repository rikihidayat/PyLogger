#
# Authors: Riki Hidayat <riki.hidayat.91@gmail.com>
#

import os
import logging

class PyLogger(object):
    
    _CURRENT_PATH = os.path.realpath(os.path.dirname(__file__))
    
    # Default Configuration
    _DEFAULT_CONF = {
        'formatter': '%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s:%(lineno)s %(message)s',
        'level': logging.INFO,
        'disabled': False,
        'logdir': os.path.join(_CURRENT_PATH, 'logs')
    }

    def __init__(self, name, **kwargs):
        """
        @type name: str
        @param name: logger name, also used as log filename
        @param kwargs:
            - disabled: set True to disable logger
            - level: set level logger
            - console_print: set True to show log message on screen
            - formatter: specify the layout of log records in the final output.
            - write2file: write log message to file
        """
        level = kwargs.get('level', self._DEFAULT_CONF['level'])
        formatter = logging.Formatter(kwargs.get('formatter', \
                        self._DEFAULT_CONF['formatter']), "%Y-%m-%d %H:%M:%S")
        
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(level)
        self.logger.disabled = kwargs.get('disabled', self._DEFAULT_CONF['disabled'])
        
        # create console handler
        if kwargs.get('enable_console', True): 
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

        # file handle
        if kwargs.get('write2file', False):
            logdir = kwargs.get('logdir', self._DEFAULT_CONF['logdir']) 
            if not os.path.exists(logdir):
                os.mkdir(logdir)

            fh = logging.FileHandler(os.path.join(logdir, '%s.log' % name), mode="wb")
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger
