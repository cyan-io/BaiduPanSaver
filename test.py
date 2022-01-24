#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Yang Chen
yangchen1024@hotmail.com
21/11/13 16:56
"""

import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

chrome = webdriver.Chrome('./chromedriver.exe', options=options)
chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

url = r"https://i.taobao.com/my_taobao.htm"
chrome.get(url)
chrome.implicitly_wait(10)

html = chrome.execute_script("return document.getElementsByTagName('html')[0] .innerHTML")
print(html)
