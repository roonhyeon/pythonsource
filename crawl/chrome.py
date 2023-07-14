# webdriver
# 방법 1) 브라우저에 맞는 드라이버를 다운로드 한 후 폴더에 옮겨놓고 사용하기
# 방법 2) 추천방법
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

if __name__ == "__main__":
    driver = set_chrome_driver()
    driver.get("https://www.naver.com")