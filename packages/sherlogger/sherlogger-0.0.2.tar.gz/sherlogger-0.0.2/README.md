# sherlog

# Usage

### Default logger
By default, logger will record everything in the directory
where you calling it
```python
from sherlogger import logger

logger.info("THIS IS LOG MESSAGE")
```
To change logs directory call `.set_stream()` method
```python
from sherlogger import logger
from sherlogger import FileSystemHandler


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
from pathlib import Path

from sherlogger import get_telegram_logger

ABS_PATH = Path().resolve()


logger = get_telegram_logger(
  filename=__name__,
  ini_file_path=f"{ABS_PATH}/plugins.ini"
)
logger.info("Some message")
```
