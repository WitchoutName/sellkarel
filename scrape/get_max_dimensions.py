from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from spider.Spider import Spider

PAGE_COUNT_PATH = '//*[@id="js-product-list-container"]/div[4]/ul/li'


class Nest:
    def __init__(self):
        print("Starting page spider...")
        self.page_spider = Spider("https://www.odkarla.cz/o-tretinu-levnejsi")
        print("Starting product spider...")
        self.product_spider = Spider(headless=True)
        print("Starting cart spider...")
        self.cart_spider = Spider("https://www.odkarla.cz/nakupni-kosik", headless=False)

        self.page_spider.open()
        element = self.page_spider.driver.find_elements(By.XPATH, PAGE_COUNT_PATH)[-1]
        page_count = element.get_attribute("textContent").replace('\n', '')
        print("Page count: " + page_count)
        while 1:
            pass

        # for page_number in range(int(page_count, 10)):
        #     self.crawl_page(page_number+1)

    def crawl_page(self, page_number):
        self.page_spider.open(f'https://www.odkarla.cz/o-tretinu-levnejsi?page={page_number}')
        sleep(1)


if __name__ == "__main__":
    Nest()
