from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--window-size=1920x1080")

def test_python_org():
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://www.python.org")
    assert "Python" in browser.title
    #browser.get_screenshot_as_file("screens/screen_python_org.png")

