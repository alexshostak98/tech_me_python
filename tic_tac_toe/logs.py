from constants import LOGS_FILE_NAME
from templates import log_templates


def logging(template_name: str, **log_data) -> None:
    try:
        file = open(LOGS_FILE_NAME, 'a', encoding='UTF-8')
        if template_name in log_templates:
            file.write(log_templates[template_name](**log_data))
        else:
            file.write(template_name)
    finally:
        file.close()
