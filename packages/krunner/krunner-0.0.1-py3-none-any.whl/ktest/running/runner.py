import inspect
import os
import pytest

from ktest.utils.config import config
from ktest.utils.log import logger
from ktest.utils.allure_util import AllureData
from ktest.core.api.request import formatting


class TestMain(object):
    """
    Support for app、web、http
    """
    def __init__(self,
                 plat: str = None,
                 path: str = None,
                 host: str = None,
                 headers: dict = None,
                 device_id: str = None,
                 pkg_name: str = None,
                 start: bool = True,
                 ocr_api: str = None,
                 browser: str = None,
                 headless: bool = False,
                 rerun: int = 0,
                 xdist: bool = False,
                 ):
        """
        @param plat: 所属平台，api、android、ios、web
        @param device_id: 设备id，针对安卓和ios，
        对安卓和ios来说也可以是远程服务
        @param pkg_name: 应用包名，针对安卓、ios、mac、win
        @param start: 是否默认启动应用，针对安卓和ios
        @param browser: 浏览器类型，chrome、firefox、webkit
        @param path: 用例目录，None默认代表当前文件
        @param rerun: 失败重试次数
        @param xdist: 是否使用多进程执行
        @param host: 域名，针对接口和web
        @param headers: {"token": "xxx"}
        @param headless: 是否使用无头模式
        """

        # 公共参数保存
        config.set_common("platform", plat)
        config.set_common("base_url", host)
        config.set_common("headers", headers)
        config.set_common("ocr_service", ocr_api)
        # app参数保存
        config.set_app("device_id", device_id)
        config.set_app("pkg_name", pkg_name)
        config.set_app("auto_start", start)
        # web参数保存
        config.set_web("browser_name", browser)
        config.set_web("headless", headless)

        # 执行用例
        cmd_list = [
            '-sv',
            '--reruns', str(rerun),
            '--alluredir', 'report', '--clean-alluredir'
        ]

        if path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            path = os.path.join(file_dir, this_file)

        cmd_list.insert(0, path)

        if xdist:
            cmd_list.insert(1, '-n')
            cmd_list.insert(2, 'auto')

        logger.info(cmd_list)
        pytest.main(cmd_list)

        logger.info("================================================================================================")
        logger.info("测试结果数据:")
        logger.info(formatting(AllureData().report_data))
        logger.info("================================================================================================")

        # api参数保存
        config.set_common("platform", None)
        config.set_common("base_url", None)
        config.set_common('headers', None)
        config.set_common("ocr_service", None)
        # app参数保存
        config.set_app("device_id", None)
        config.set_app("pkg_name", None)
        config.set_app("auto_start", False)
        # config.set_app("errors", [])
        # web参数保存
        config.set_web("browser_name", None)
        config.set_web("headless", False)


main = TestMain


if __name__ == '__main__':
    main()

