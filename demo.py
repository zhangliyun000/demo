import os
# os.system('echo $PATH')
import time
import uiautomator2 as u2

# 在不同手机上，复现多次进退页面等反复操作出现问题的情况

device = u2.connect()
# print(device.app_current())
print(device.device_info)
device.app_start('com.smile.gifmaker')  # 通过包名启动app


i = 0
for i in range(1, 6):
    print(i)

# # 方法一： 引用shell命令
#     os.popen("adb shell input tap 588 1820")
#     time.sleep(5)
#     os.popen("adb shell input tap 67 65")
#     time.sleep(5)

# 方法二：定位元素
    device(resourceId="com.smile.gifmaker:id/btn_shoot_black").click()  #根据resourceId定位
    # device.click(0.504, 0.972)
    # device(text='消息').click()                   #根据text定位
    # device.xpath('//*[@text="消息"]')             #根据XPath定位
    # device.swipe_ext('right',scale=0.9)           #滑屏操作
    # device.screenshot('test.png')                 #截屏操作
    time.sleep(5)
    device(resourceId="com.smile.gifmaker:id/button_close").click()     #根据resourceId定位
    # device.click(0.504, 0.972)
    time.sleep(5)

device.app_stop('com.smile.gifmaker')

