from constants import LOGS_FILE_NAME
from templates import log_templates, log_string


def logging(template_name: str, **log_data) -> None:
    try:
        file = open(LOGS_FILE_NAME, 'a', encoding='UTF-8')
        file.write(log_templates[template_name](log_string[template_name], **log_data))
    finally:
        file.close()