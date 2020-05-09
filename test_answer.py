# coding=utf-8
import time
from selenium import webdriver
import importlib
import sys

importlib.reload(sys)

username = ""
pwd = ""

'''
#获取所有url
for m in range(1, 15):
    for n in range(1, 5):
        try:
            urls.append(driver.find_element_by_xpath(
                "/html/body/div[4]/div/div[1]/div/dl/dd[" + str(m) + "]/ul/li[" + str(n) + "]/a")
                        .get_attribute('href'))
        except:
            pass
print(urls)
'''

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
select_title = driver.find_element_by_link_text("课程学习").click()  # 登陆一次后，有了cookie，打开新的网址就无需登录


# 本函数来源于 https://github.com/smallzhu/-/blob/master/ClickMedia.py
def evaluate_media():
    search_window = driver.current_window_handle  # 定位到url的页面
    temp = 1
    for i in range(1, 90):
        temp = temp + 1
        myKeys = 0
        findEvaluate = 0
        try:
            mySelector_evaluate = "#showajaxinfo > div:nth-child(2) > dl > dd > p:nth-child(%d)" % i
            evaluate = driver.find_element_by_css_selector(mySelector_evaluate)
            # 利用css定位元素 媒体评价
        except Exception as e:
            print("这个不用评", e)
        #    findEvaluate = findEvaluate + 1
        # if findEvaluate == 2:
        #    break
        try:
            driver.execute_script("arguments[0].click();", evaluate)
            # 利用script点击按钮，可以防止元素未出现在界面中而不能点击出现异常
            evaluate = driver.switch_to.frame("pageiframe")  # 转换到媒体评价的iframe
            evaluate = driver.find_element_by_class_name("ping_btn_3").click()  # 点击“很好”评价
            time.sleep(1)
            evaluate = driver.find_element_by_class_name("aui_state_highlight").click()  # 点击确定评价
            evaluate = driver.switch_to.default_content()  # 回到主界面不用点击关闭按钮就可以直接定位主界面的元素
            myKeys = 1
        except:
            print("进行下一个评价")
            if myKeys == 0:
                evaluate = driver.switch_to.default_content()
        else:
            print("进行下一个评价")
        print(temp)
        # 最开始是2034
        # j_2046 > a
        # j_2045 > a
    print(url, ":本章评价完啦")


def ans_this_url():
    search_window = driver.current_window_handle  # 定位到url的页面
    time.sleep(3)
    for xt_id in range(1, num_Of_Quest + 1):
        time.sleep(3)
        #    /html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[1]/p
        question = driver.find_element_by_xpath(  # question的xpath
            "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[" + str(xt_id) + "]/p").text.rstrip().rstrip(
            '（）。')  # 部分答案中末尾没有 '（）。' ,所以进行处理
        print('Question:', question)

        file = open('my_answer.txt')
        flag = 0  # 判断是否找到答案
        ans = []  # 用于保存答案的列表
        for line in file.readlines():
            if question in line:
                # 找到题目了
                print("find question in .txt")
                flag = 1
                continue
            if flag == 1:
                # 找答案
                if 'Question' in line:
                    # 已经到了下一个题目,所以跳出循环
                    break
                if '√' in line:
                    ans.append(line.replace('√ ', '').replace(' \n', '').replace('\n', ''))
                    # 对答案进行处理，保存到一个列表里

        print("find ans:", ans)
        # 答案最多有五个，所以就从1到5循环一遍
        for i in range(1, 6):
            try:
                temp = driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li[" + str(xt_id) + "]/ul/li[" + str(
                        i) + "]")

                if temp.text in ans:
                    print("find right options", temp.text)
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div[2]/div[2]/div[2]/dl/dd[1]/ul/li["
                        + str(xt_id) + "]/ul/li[" + str(i) + "]/input") \
                        .click()  # 点击事件要定位到input
            except Exception as e:
                # 出错有两种情况。1:本题已经答过了;2:本题最多就 i 个选项。 都可以break
                print("cant click or no options:", e)
                break


for url in urls:
    driver.get(url)
    time.sleep(6)
    evaluate_media()
    # 重新进入该url
    driver.get(url)
    time.sleep(3)
    search_window = driver.current_window_handle  # 定位到url的页面
    num_Of_Quest = int(driver.find_element_by_xpath('//*[@id="showajaxinfo"]/div[2]/dl/dt/span[2]')
                       .text.strip('题目总数：'))  # 题目总数
    num_Of_Answer = int(driver.find_element_by_xpath('//*[@id="showajaxinfo"]/div[2]/dl/dt/span[3]')
                        .text.strip('答题正确：'))  # 已答数
    if num_Of_Answer == num_Of_Quest:
        print(url + ": 本章已经满分辣")
        continue
    ans_this_url()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="s2"]/a').click()  # 提交
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]').click()  # 弹窗确认
    print(url + "本章已经答完了")

print("结束")
