"""
@Author: kang.yang
@Date: 2023/11/16 17:52
"""
import krunner


class TestApiDemo(krunner.TestCase):
    """接口demo"""

    def test_normal_req(self):
        payload = {"type": 2}
        headers = {
            "user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"
        }
        self.post('/qzd-bff-app/qzd/v1/home/getToolCardListForPc',
                  json=payload, headers=headers)
        self.assert_eq('code', 0)


if __name__ == '__main__':
    """仅执行本模块"""
    krunner.main(
        plat='api',
        host='https://app-test.qizhidao.com'
    )

