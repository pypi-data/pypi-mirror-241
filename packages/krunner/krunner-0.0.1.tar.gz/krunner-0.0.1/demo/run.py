import krunner


if __name__ == '__main__':
    # 执行多个用例文件，主程序入口

    krunner.main(
        plat='android',
        path='tests',
        device_id="UJK0220521066836",
        pkg_name='com.qizhidao.clientapp',
    )



