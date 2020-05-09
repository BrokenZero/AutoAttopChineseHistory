# coding=utf-8
import time
from selenium import webdriver
import importlib
import sys

importlib.reload(sys)

username = ""
pwd = ""

urls = ['http://www.attop.com/wk/learn.htm?id=74&jid=2048', 'http://www.attop.com/wk/learn.htm?id=74&jid=2050',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2051', 'http://www.attop.com/wk/learn.htm?id=74&jid=2053',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2054', 'http://www.attop.com/wk/learn.htm?id=74&jid=2055',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2057', 'http://www.attop.com/wk/learn.htm?id=74&jid=2058',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2059', 'http://www.attop.com/wk/learn.htm?id=74&jid=2062',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2063', 'http://www.attop.com/wk/learn.htm?id=74&jid=2064',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2065', 'http://www.attop.com/wk/learn.htm?id=74&jid=2066',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2067', 'http://www.attop.com/wk/learn.htm?id=74&jid=2068',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2069', 'http://www.attop.com/wk/learn.htm?id=74&jid=2070',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2071', 'http://www.attop.com/wk/learn.htm?id=74&jid=2072',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2073', 'http://www.attop.com/wk/learn.htm?id=74&jid=2074',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2075', 'http://www.attop.com/wk/learn.htm?id=74&jid=2076',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2077',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2078', 'http://www.attop.com/wk/learn.htm?id=74&jid=2079',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2080', 'http://www.attop.com/wk/learn.htm?id=74&jid=2081',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2082', 'http://www.attop.com/wk/learn.htm?id=74&jid=2083',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2084', 'http://www.attop.com/wk/learn.htm?id=74&jid=2085',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2086', 'http://www.attop.com/wk/learn.htm?id=74&jid=2087',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2088', 'http://www.attop.com/wk/learn.htm?id=74&jid=2089',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2090', 'http://www.attop.com/wk/learn.htm?id=74&jid=2091',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2092', 'http://www.attop.com/wk/learn.htm?id=74&jid=2093',
        'http://www.attop.com/wk/learn.htm?id=74&jid=2094', 'http://www.attop.com/wk/learn.htm?id=74&jid=2095']

driver = webdriver.Chrome()
driver.get('http://www.attop.com/wk/index.htm?id=74')
element = driver.find_element_by_link_text("登录").click()
time.sleep(1)
alert = driver.switch_to.frame("pageiframe")
time.sleep(1)  # 转化到登录界面的 iframe
alert = driver.find_element_by_id("username").send_keys(username)
alert = driver.find_element_by_id("password").send_keys(pwd)
time.sleep(6)  # 等待输入验证码
alert = driver.switch_to.default_content()
select_title = driver.find_element_by_link_text("课程学习").click()
# 登陆一次后，有了cookie，打开新的网址就无需登录

file = open('my_answer.txt', 'w+')


def write_this_page_test_bank():
    # 爬取题目并录入
    for xt_id in range(1, num_Of_Quest + 1):
        time.sleep(3)
        question = driver.find_element_by_xpath(  # question的xpath
            "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[" + str(xt_id) + "]/p").text.rstrip().rstrip(
            '（）。')  # 部分答案中末尾没有 '（）。' ,所以进行处理
        file.write('Question:' + question)
        file.write('\n')
        print("找到题目:" + question)

        # 爬取答案并录入
        # 答案最多有五个，所以就从1到5循环一遍
        for i in range(1, 6):
            try:
                option = driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[" + str(xt_id) + "]/ul/li[" + str(
                        i) + "]")
                check = driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[" + str(xt_id) + "]/ul/li[" + str(
                        i) + "]/input").is_selected()
                if check == 1:
                    file.write("√ " + option.text)
                    print("找到正确答案:" + option.text)
                    file.write('\n')
                else:
                    file.write(" " + option.text)
                    print("找到错误答案:" + option.text)
                    file.write('\n')
            except Exception as e:
                # 出错有一种情况: 本题最多就 i 个选项。 可以break
                print("no options:", e)
                break


for url in urls:
    driver.get(url)
    search_window = driver.current_window_handle
    time.sleep(3)
    num_Of_Quest = int(driver.find_element_by_xpath('//*[@id="showajaxinfo"]/div[2]/dl/dt/span[2]')
                       .text.strip('题目总数：'))  # 题目总数
    num_Of_Answer = int(driver.find_element_by_xpath('//*[@id="showajaxinfo"]/div[2]/dl/dt/span[3]')
                        .text.strip('答题正确：'))  # 已答数
    write_this_page_test_bank()
    print(url + ":本章节已录入")

file.close()
