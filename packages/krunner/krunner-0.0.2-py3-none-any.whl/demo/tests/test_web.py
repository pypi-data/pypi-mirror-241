"""
@Author: kang.yang
@Date: 2023/11/16 17:50
"""
import krunner
# from pub import Pub


class TestWebDemo(krunner.TestCase):

    # def start(self):
    #     self.pub = Pub(self.driver)

    @krunner.title("登录")
    def test_login(self):
        self.driver.open_url("https://www-test.qizhidao.com/")
        # self.pub.pwd_login()
        self.driver.assert_url("https://www-test.qizhidao.com/")
        self.screenshot("首页")


if __name__ == '__main__':
    krunner.main(
        plat='web',
        host="https://www-test.qizhidao.com/"
    )
