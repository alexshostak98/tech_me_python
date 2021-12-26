page_link = {'a': {"class": "tm-article-snippet__title-link"}}
pagination_link = {'a': {"class": "tm-pagination__page"}}


def create_pattern(tag_name: str, tag_attrs: dict) -> dict:
    return {tag_name: tag_attrs}
