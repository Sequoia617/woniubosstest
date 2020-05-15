# 公共模块
from tools.service import Service


class Common:

    def __init__(self):
        self.driver = Service.get_driver()

    def input_name(self, username):
        uname = self.driver.find_element_by_name('userName')
        Service.input_txt(uname, username)

    def input_password(self, password):
        upass = self.driver.find_element_by_name('userPass')
        Service.input_txt(upass, password)

    def input_checkcode(self, checkcode):
        check = self.driver.find_element_by_name('checkcode')
        Service.input_txt(check, checkcode)

    def check_login_button(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()

    def do_login(self, login_data):
        Service.open_startpage(self.driver)
        self.input_name(login_data['userName'])
        self.input_password(login_data['userPass'])
        self.input_checkcode(login_data['checkcode'])
        self.check_login_button()

    def do_logout(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()


if __name__ == '__main__':
    login_data = {"userName": "WNCD000", "userPass": "woniu123", "checkcode": "0000"}
    Common().do_login(login_data)
