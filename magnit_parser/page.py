from models import PromoPage


class Page:

    def __init__(self, promo_data):
        self.data = promo_data

    def create_page(self):
        pages = []
        for title, url in self.data.items():
            page = PromoPage(
                promo_url=url,
                product_name=title,
            )
            pages.append(page)
        return pages
