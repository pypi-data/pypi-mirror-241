import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # 初始化colorama库

class LogColors:
    INFO = Fore.WHITE
    WARNING = Fore.YELLOW
    SUCCESS = Fore.RED
    ERROR = Fore.CYAN
    DEBUG = Fore.BLUE

def cyprint(message, level='info',istime=None):
    levels = {'info': LogColors.INFO, 'warning': LogColors.WARNING, 'success': LogColors.SUCCESS, 'error': LogColors.ERROR, 'debug': LogColors.DEBUG}
    colors = {'WHITE': 'info', 'YELLOW': 'warning', 'RED': 'success', 'CYAN': 'error', 'BLUE': 'debug'}

    level_lower = level.lower()
    if level_lower not in levels:
        level_upper = level.upper()
        fore_color = getattr(Fore, level_upper)
        colored_level = fore_color + level_lower.upper() + Style.RESET_ALL
        if istime:
            level_lower = "Prompt"
            colored_level = fore_color + level_lower.upper() + Style.RESET_ALL
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f'{Fore.GREEN}[{current_time}]{Style.RESET_ALL}  {colored_level}  {message}'
        else:
            log_entry = f'{fore_color}{message}{Style.RESET_ALL}'
    else:
        colored_level = levels[level_lower] + level_lower.upper() + Style.RESET_ALL
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{Fore.GREEN}[{current_time}]{Style.RESET_ALL}  {colored_level}  {message}'
    print(log_entry)



# cyprint('测试', 'MAGENTA')
# cyprint('测试', 'info')
# cyprint('警告信息', "WARNING")
# cyprint('成功信息', "SUCCESS")
# cyprint('错误信息', "ERROR")
# cyprint('debug信息', "DEBUG")