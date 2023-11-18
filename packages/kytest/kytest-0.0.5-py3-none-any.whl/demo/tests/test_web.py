"""
@Author: kang.yang
@Date: 2023/11/16 17:50
"""
import kytest
from pages.web_page import IndexPage, LoginPage


class TestWebDemo(kytest.TestCase):

    def start(self):
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    @kytest.title("登录")
    def test_login(self):
        self.index_page.open()
        self.index_page.loginBtn.click()
        self.sleep(5)
        self.login_page.pwdLoginTab.click()
        self.login_page.userInput.input("13652435335")
        self.login_page.pwdInput.input("wz123456@QZD")
        self.login_page.licenseBtn.click()
        self.login_page.loginBtn.click()
        self.login_page.firstCompanyIcon.click()
        self.driver.assert_url("https://www-test.qizhidao.com/")
        self.screenshot("首页")


if __name__ == '__main__':
    kytest.main(
        plat='web',
        host="https://www-test.qizhidao.com/"
    )
