import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    # Comment out the next line if you want to watch the browser run
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield drv
    drv.quit()
