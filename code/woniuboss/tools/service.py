# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         service
# Description:  
# Author:       Administrator
# Date:         2020/3/23
# -------------------------------------------------------------------------------
from selenium.webdriver.support.select import Select

from tools.util import Utility


class Service:

    # 对可输入的元素执行点击、清理和输入
    @classmethod
    def input_txt(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    @classmethod
    def input_content(cls, ele, value):
        ele.click()
        ele.send_keys(value)

    # 打开开始页面
    @classmethod
    def open_startpage(cls, driver):
        contents = Utility.get_json('..\\conf\\base')
        url = "%s://%s:%s/%s" % (contents['PROTOCOL'], contents['HOSTNAME'], contents['PORT'], contents['PROGRAM'])
        driver.get(url)

    # 打开菜单页面
    @classmethod
    def openpage(cls, driver, menu_name):
        driver.find_element_by_partial_link_text(menu_name).click()

    # 判断某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 选择下拉框的一个具体的值
    @classmethod
    def select_value(cls, ele, value):
        Select(ele).select_by_visible_text(value)

    # 忽略登录过程
    @classmethod
    def ignore_login(cls, driver):
        cls.open_startpage(driver)
        contents = Utility.get_json('..\\conf\\base')
        driver.add_cookie({'name': 'username', 'value': contents['USERNAME']})
        driver.add_cookie({'name': 'password', 'value': contents['PASSWORD']})
        cls.open_startpage(driver)

    # 对日期控件直接输入
    @classmethod
    def input_date(cls, driver, id, date):
        ele = driver.find_element_by_id(id)
        driver.execute_script('document.getElementById("%s").readOnly=false;' % (id))
        ele.send_keys(date)

    # 随机选择下拉框中的选项
    @classmethod
    def select_random_content(cls, ele):
        from selenium.webdriver.support.select import Select
        import random
        # 获取select中的option元素的数量
        max = len(Select(ele).options)
        index = random.randint(0, max - 1)
        Select(ele).select_by_index(index)

    # 提供driver
    @classmethod
    def get_driver(cls):
        from selenium import webdriver
        contents = Utility.get_json('..\\conf\\base')
        driver = getattr(webdriver, contents['BROWSER'])()
        driver.implicitly_wait(5)
        return driver


if __name__ == '__main__':
    drvier = Service.get_driver()
    Service.ignore_login(drvier)
