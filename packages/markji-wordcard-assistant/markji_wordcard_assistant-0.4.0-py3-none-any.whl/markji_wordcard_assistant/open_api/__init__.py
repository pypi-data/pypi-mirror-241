# 日志记录器
import logging

logger = logging.getLogger()

# 设置日志级别，只有大于等于这个级别的日志才能输出
logger.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter(
    "%(levelname)s  %(asctime)s %(module)s-%(funcName)s-line:%(lineno)d %(message)s"
)

# 输出到控制台
to_console = logging.StreamHandler()
to_console.setFormatter(formatter)
logger.addHandler(to_console)

# 输出到文件中
to_file = logging.FileHandler(filename="log.txt")
to_file.setFormatter(formatter)
logger.addHandler(to_file)
