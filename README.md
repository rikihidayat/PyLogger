# PyLogger
Is a wrapper for creating logger object.

## How To Use
```
from PyLogger import PyLogger
mylogger = PyLogger('sample', level='DEBUG', write2file=True).get_logger()

mylogger.info('This is INFO')
mylogger.debug('This is DEBUG')
```
