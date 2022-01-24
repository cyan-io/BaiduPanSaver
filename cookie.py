import selenium
import util
import json

if __name__ == '__main__':
    driver = util.build_driver()
    driver.get('https://pan.baidu.com/')
    input('Input Anything To Continue...')
    cookies = driver.get_cookies()  # 已经获取到了cookies
    with open("cookies.json", "w", encoding="utf-8") as jsn:
        json.dump(cookies, jsn)
