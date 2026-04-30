#####
# version: 1.0.0
#####

import logging.config
import tomllib

from rich.text import Text


class CustomFormatter(logging.Formatter):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GREY = "\x1b[90m"
    BOLD_GREY = "\x1b[90;1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    BOLD_RED = "\x1b[31;1m"

    PREFIX = f"{CYAN}%(asctime)s{RESET} - {GREY}[%(name)s]{RESET} - "
    SUFFIX = (
        f"%(levelname)s{RESET} - %(message)s {GREY}(%(filename)s:%(lineno)d){RESET}"
    )

    FORMATS = {
        logging.DEBUG: f"{PREFIX}{GREEN}{SUFFIX}",
        logging.INFO: f"{PREFIX}{BLUE}{SUFFIX}",
        logging.WARNING: f"{PREFIX}{YELLOW}{SUFFIX}",
        logging.ERROR: f"{PREFIX}{RED}{SUFFIX}",
        logging.CRITICAL: f"{PREFIX}{BOLD_RED}{SUFFIX}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class PlainFormatter(logging.Formatter):
    def format(self, record):
        # 1. 获取原始消息
        msg = super().format(record)

        # 2. 利用 Rich 的 Text 对象解析并去除标签
        # Text.from_markup 会把 "[bold]Hi[/bold]" 解析为对象
        # .plain 属性会直接返回不带样式的纯文本 "Hi"
        # 这比正则更安全，因为它能处理复杂的嵌套和转义
        try:
            clean_msg = Text.from_markup(msg).plain
        except Exception:
            # 如果解析失败（比如格式错误），降级使用原始消息
            clean_msg = msg

        return clean_msg


def init_logging_config(config_file: str = "log_config.toml"):
    with open(config_file, "rb") as f:
        cfg = tomllib.load(f)
    logging.config.dictConfig(cfg)
