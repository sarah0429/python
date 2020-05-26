import json

import requests
import schedule
import time
from selenium import webdriver
import wechat

openid = [" ", " ", " ",]  # 微信消息模板发送对象
name = ["小明", "小蓝", "小绿"]  # 微信消息模板发送姓名
account = [" ", " ", " "]  # 登录账号
password = ["456123", "123456", "321233"]  # 登录密码
place = ["广东省广州市南沙区", "广东省广州市白云区"]  # 打卡需填写地址


def job():
    for i in range(len(account)):
        code = requests.get("http://eswis.gdpu.edu.cn/Default.aspx").status_code
        if code == 200:
            print("true")
            driver = webdriver.Chrome(r"C:\Users\Administrator\PycharmProjects\untitled\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用谷歌浏览器驱动
            driver.maximize_window()  # 最大化窗口
            driver.get("http://eswis.gdpu.edu.cn/Default.aspx")  # 打开学校网页
            driver.find_element_by_css_selector("span#ctl00_gologin>a").click()
            driver.find_element_by_css_selector("input#log_username").send_keys(account[i])
            driver.find_element_by_css_selector("input#log_password").send_keys(password[i])
            driver.find_element_by_css_selector("a#logon").click()
            driver.find_element_by_xpath("//li[@class='bdpink bg_grant ']/a").click()
            driver.find_element_by_css_selector("ul#ctl00_cph_right_myapps>li>a").click()
            driver.find_element_by_css_selector("input#ctl00_cph_right_ok_submit").click()
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_atschool_1").click()
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_location").send_keys(place[i])
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_observation_0").click()
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_health_0").click()
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_temp").send_keys('36.5')
            driver.find_element_by_css_selector("input#ctl00_cph_right_e_submit").click()
            my_wechat = wechat.WeChat(openid[i], name[i])
            my_wechat.post_data()
            continue
        else:
            time.sleep(600)
            continue


schedule.every().day.at("07:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
