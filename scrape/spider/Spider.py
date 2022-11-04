from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Spider:
    def __init__(self, url=None, headless=False):
        self.url = url or "https://www.example.com"

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    def open(self, url=None):
        self.driver.get(url if url else self.url)
        WebDriverWait(self.driver, timeout=3).until(lambda d: d.execute_script("return 1"))

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    spider = Spider("")
