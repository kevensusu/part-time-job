# coding:UTF-8


from lib.logging_lib import log
import fetch.scau_scautiu
import fetch.scau_arts
import fetch.scau_slxy
import fetch.scau_gongguan
import fetch.scau_info
import traceback


def main():
    log.info("爬虫启动！")

    fetchs = []
    # 电子工程
    fetchs.append(fetch.scau_scautiu.init)
    # 艺术学院
    fetchs.append(fetch.scau_arts.init)
    # 水利学院
    fetchs.append(fetch.scau_slxy.init)
    # 公管学院
    fetchs.append(fetch.scau_gongguan.init)
    # 信息学院
    fetchs.append(fetch.scau_info.init)

    for func in fetchs:
        try:
            func()
        except:
            traceback.print_exc()

    log.info("爬虫结束！")


if __name__ == '__main__':
    main()
