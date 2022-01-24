from os import link
import time
import util
import random
import json
import selenium
from selenium.webdriver.chrome.webdriver import WebDriver


def save(driver: WebDriver, url, pwd=None):
  if "?pwd=" not in url:
    assert pwd is not None
    url = f'{url}?pwd={pwd}'
  driver.get(url)
  driver.find_element_by_css_selector(
      '#layoutMain > div.frame-content > div.module-share-header > div > div.slide-show-right > div > div > div.x-button-box > a.g-button.tools-share-save-hb').click()
  driver.find_element_by_css_selector(
      '#fileTreeDialog > div.dialog-footer.g-clearfix > a.g-button.g-button-blue-large').click()


def get_cookies():
    with open("cookies.json", "r", encoding="utf-8") as cks:  # 从json文件中获取之前保存的cookie
        return json.load(cks)


if __name__ == '__main__':
  driver = util.build_driver()
  driver.implicitly_wait(20)
  driver.get('https://pan.baidu.com')
  # 添加cookies
  cookies = get_cookies()
  # print(cookies)
  for i in cookies:
    driver.add_cookie(i)
  # 链接文件
  with open('links.json', 'r', encoding='utf-8') as jsn:
    links = json.load(jsn)
  # 保存
  # save(driver, "https://pan.baidu.com/s/1vzQlZ8gvDzZRdR0b7fP2yg?pwd=pgfc")
  for dict_key in links:
    save(driver, dict_key, links[dict_key])
    print(f'SAVED {dict_key}')
    time.sleep(random.choice([5, 7]))
