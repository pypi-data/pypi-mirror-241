import krunner
from krunner import *

from pages.adr_page import DemoPage


@story('测试demo')
class TestAdrDemo(TestCase):
    def start(self):
        self.page = DemoPage(self.driver)

    @title('进入设置页')
    def test_go_setting(self):
        self.page.adBtn.click_exists(timeout=5)
        self.page.myTab.click()
        self.page.settingBtn.click()
        self.driver.assert_act('.me.MeSettingActivity')
        self.screenshot("设置页")


if __name__ == '__main__':
    krunner.main(
        plat='android',
        device_id="UJK0220521066836",
        pkg_name='com.qizhidao.clientapp'
    )
