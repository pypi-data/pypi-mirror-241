import time
import pyautogui  # pip install pyautogui -i https://mirrors.aliyun.com/pypi/simple/
import yaml


def file_upload(driver, file_locatio=1, yamlpath=None, data=0):
    """
    :param driver: 浏览器对象
    :param file_locatio: mac系统想要上传的第几个文件，从左上角开始
    :param yamlpath: 配置文件路径
    :param data: 使用第几组数据
    :return: 文件上传操作
    """

    # 读取配置文件
    file = open(yamlpath, 'r', encoding='utf-8')
    coordinate = yaml.load(file, Loader=yaml.FullLoader)[data]

    driver.maximize_window()
    # 点击"文稿"
    pyautogui.moveTo(coordinate['draft'][0], coordinate['draft'][1])
    time.sleep(2)
    pyautogui.click()

    # 点击"图片"
    pyautogui.moveTo(coordinate['image'][0], coordinate['image'][1])
    time.sleep(2)
    pyautogui.click()

    # 点击"打开"(因为mac系统有权限问题，可能双击不成功，所以采取最原始的方式)
    pyautogui.moveTo(coordinate['open'][0], coordinate['open'][1])
    pyautogui.click()

    # 判断传入页面第几个文件，从左到右
    x, y = coordinate['first_file_coordinates'][0], coordinate['first_file_coordinates'][1]

    # 使用了两个偏移量 offset_x 和 offset_y 进行辅助计算
    offset_x = ((file_locatio - 1) % 5) * 125
    offset_y = ((file_locatio - 1) // 5) * 130

    x += offset_x
    y += offset_y

    # 选择上传的文件
    pyautogui.moveTo(x, y)
    pyautogui.click()

    time.sleep(3)

    # 点击"打开"(因为mac系统有权限问题，可能双击不成功，所以采取最原始的方式)
    pyautogui.moveTo(coordinate['open'][0], coordinate['open'][1])
    pyautogui.click()
