# sherlog

# Usage

### Default logger
By default, logger will record everything in the directory
where you calling it
```python
from sherlog import logger

logger.info("THIS IS LOG MESSAGE")
```
To change logs directory call `.set_stream()` method
```python
from sherlog import logger
from sherlog import FileSystemHandler


logger.set_stream(  # <path_to_dir>, <Handler>
    "~/home/ubuntu/...", FileSystemHandler
)
logger.info("THIS IS LOG MESSAGE")
```

### Telegram logger

#### Setup
* **.ini file**
    
    Create plugins.ini file. Format of file and required
    data is located in plugins.ini.example

Logger sends your message to telegram in asynchronous manner.

`tlogger` will run in separated thread.
```python
from sherlog import tlogger

tlogger.info("This is log message")
```
