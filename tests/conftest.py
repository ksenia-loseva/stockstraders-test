import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    yield wd
    wd.quit()