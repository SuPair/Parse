# coding:utf-8
import os
import logging

install_node_count = 0    # 失败超过3次自动退出程序


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
    global install_node_count
    logging.debug("开始安装Node")
    # 检查环境
    check_gcc_version = os.popen('gcc -v').read()
    logging.debug(check_gcc_version)
    check_gcc_value = "gcc"
    if check_gcc_value not in check_gcc_version:
        logging.debug("未安装GCC，开始安装GCC")
        install_gcc_file = os.popen("yum install gcc  gcc-c++ -y")
        logging.debug(install_gcc_file.read())
        logging.debug("GCC安装完毕")
    else:
        logging.debug("GCC已安装！")

    # 下载文件并解压编译
    logging.debug("下载并编译文件：")
    nodeVersion = "node-v10.15.0"
    node_file_path = "/usr/local/src/" + nodeVersion + ".tar.gz"
    node_dir_path = "/usr/local/src/" + nodeVersion
    download_cmd = "cd /usr/local/src && wget https://nodejs.org/dist/v10.15.0/"+nodeVersion+".tar.gz "
    download_counts = 0
    while not os.access(node_file_path, os.F_OK):
        download_counts += 1
        if download_counts < 3:
            logging.debug("尝试第"+str(download_counts)+"下载！")
            downLoad_file = os.popen(download_cmd)
            logging.debug(downLoad_file.read())
        else:
            logging.debug("下载文件："+nodeVersion+".tar.gz失败，退出程序！")
            exit(0)

    logging.debug("解压文件")
    tar_cmd = "tar xvf "+nodeVersion+".tar.gz"
    tar_file = os.popen(tar_cmd)
    logging.debug(tar_file.read())

    logging.debug("编译安装Node")
    make_cmd = "cd "+node_dir_path+"&& ./configure && make && make install"
    make_file = os.popen(make_cmd)
    logging.debug(make_file.read())
    logging.debug("编译安装完毕")
    checkNodeVersion = os.popen('node -v').read()
    checkValue = 'v'
    # 检查Node版本
    if checkValue not in checkNodeVersion:
        logging.debug("Node安装失败，清除安装数据第" + str(install_node_count) + "次！")

        node_dir_path = "/usr/local/src/" + nodeVersion
        # 清理文件
        if os.access(node_file_path, os.F_OK):
            logging.debug("清理文件")
            clearn_node_cmd = "rm -f "+node_file_path
            clearn_file = os.popen(clearn_node_cmd)
            logging.debug(clearn_file.read())
            logging.debug("文件清理完毕")
        # 清理目录
        if os.path.exists(node_dir_path):
            logging.debug("清理文件夹")
            clearn_node_cmd = "rm -rf " + node_dir_path
            clearn_file = os.popen(clearn_node_cmd)
            logging.debug(clearn_file.read())
            logging.debug("文件夹清理完毕")
        # 失败尝试
        if install_node_count < 3:
            logging.debug("Node安装失败，尝试第"+str(install_node_count)+"次！")
            install_node_count += 1
            install_node()
        else:
            logging.debug("Node安装失败，尝试第" + str(install_node_count) + "次,退出程序！")
            exit()
    else:
        logging.debug("Node版本:"+checkNodeVersion.read())


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
