import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

URL = os.getenv('URL')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
PAUSE_DURATION_SECONDS = 5

if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    driver.maximize_window()
    login_button = driver.find_element(
        By.CSS_SELECTOR, 'a[data-role="login"].btn'
    )
    login_button.click()
    popup_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'ndbox-1'))
    )
    username_input = popup_box.find_element(By.NAME, 'email')
    username_input.send_keys(EMAIL)
    password_input = popup_box.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)
    # Задержка для прохождения капчи
    sleep(PAUSE_DURATION_SECONDS)
    submit_button = popup_box.find_element(
        By.CSS_SELECTOR, 'button.btn.btn-block.btn-primary'
    )
    submit_button.click()
    WebDriverWait(driver, 10).until(EC.url_changes(URL))
    proxies = driver.find_elements(By.XPATH, '//tr[starts-with(@id, "el-")]')
    for proxy in proxies:
        proxy_ip = proxy.find_element(
            By.XPATH,
            './/div[contains(text(), "Прокси")]/following-sibling::div'
        )
        proxy_date = proxy.find_element(
            By.CSS_SELECTOR, 'td.mobile-hide div.right'
        )
        print(f'{proxy_ip.text} - {proxy_date.text}')
    driver.quit()
