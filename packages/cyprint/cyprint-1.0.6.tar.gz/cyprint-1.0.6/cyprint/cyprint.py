import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # 初始化colorama库

class LogColors:
    INFO = Fore.WHITE
    WARNING = Fore.YELLOW
    SUCCESS = Fore.RED
    ERROR = Fore.CYAN
    DEBUG = Fore.BLUE

def cyprint(message, level='info'):
    levels = {'info': LogColors.INFO, 'warning': LogColors.WARNING, 'success': LogColors.SUCCESS, 'error': LogColors.ERROR, 'debug': LogColors.DEBUG}

    if level.lower() not in levels:
        raise ValueError(f"Invalid log level '{level}'. Supported levels: {', '.join(levels)}")

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    colored_level = levels[level.lower()] + level.upper() + Style.RESET_ALL
    log_entry = f'{Fore.GREEN}[{current_time}]{Style.RESET_ALL}  {colored_level}  {message}'
    print(log_entry)


# 使用默认级别 INFO
# cyprint('上传接口刷新成功')

# 也可以指定其他级别
# cyprint('警告信息', 'warning')
