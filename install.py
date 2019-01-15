import os
import logging
import string


def console_out(logFilename):
    ''' Output log to file and console '''
    # Define a Handler and set a format which output to file
    logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename=logFilename,  # log文件名
        filemode='w')  # 写入模式“w”或“a”
    # Define a Handler and set a format which output to console
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)  # 实例化添加handler


def install_node():
    logging.debug("开始安装Node")
    # 检查环境
    checkGCCVersion = os.popen('gcc -v').read()
    checkGCCPlusVersion = os.popen('gcc-c++ -v').read()


def install():
    console_out('log.text')
    logging.debug("开始安装")
    checkNodeVersion = os.popen('node -v').read()
    checkValue = 'v'
    # 检查Node版本
    if checkValue not in checkNodeVersion:
        install_node()
    else:
        logging.debug("Node版本:" + str(checkNodeVersion))

    os.system('cat log.text')


if __name__ == '__main__':
    install()
