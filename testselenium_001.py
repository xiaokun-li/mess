# _*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Edge(service=Service(r'c:\windows\system32\msedgedriver.exe'))

wd.get(r'https://www.baidu.com')

ele1 = wd.find_element(By.ID, 'kw')

ele1.send_keys('dbschenker\n')

