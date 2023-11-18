import kytest


if __name__ == '__main__':
    # 执行多个用例文件，主程序入口

    kytest.main(
        plat="web",
        path="tests/test_web.py",
        host='https://app-test.qizhidao.com'
    )



