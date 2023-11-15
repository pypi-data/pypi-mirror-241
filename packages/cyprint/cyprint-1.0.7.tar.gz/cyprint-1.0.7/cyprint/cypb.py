def cypb(current_index, events, cyname=""):
    bar_length = 50

    # 检查传入的参数类型
    if isinstance(events, int):  # 如果是整数，认为是处理单个数字的情况
        total_events = events
    else:  # 否则，假设传入的是事件列表
        total_events = len(events)

    progress = (current_index + 1) / total_events
    block = int(round(bar_length * progress))
    progress_bar = str(cyname) + "|" + "█" * block + " " * (bar_length - block) + "|"

    if progress == 1:
        print(f"\r{progress_bar} {progress * 100:.2f}% ({current_index + 1}/{total_events})\n", end="", flush=True)
    else:
        print(f"\r{progress_bar} {progress * 100:.2f}% ({current_index + 1}/{total_events})", end="", flush=True)