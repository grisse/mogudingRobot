## 蘑菇丁App自动签到

蘑菇丁App自动签到无服务器解决方案：
- serverless，可以使用腾讯云、阿里云等平台提供的函数计算服务，并且免费额度足够签到使用。代码文件在仓库serverless目录下。
- 将程序设置成工作电脑的开机自启项，每天开机时即自动签到。代码文件在仓库pc目录下。
- 将以上两种方案进行综合，工作日电脑自启签到方式+周末函数计算签到方式。
- server。如果你自己有云服务器，可以设置定时任务，仓库server目录和pc目录下代码文件都可以用，区别是server版本代码可以设置随机签到时间(I am not a robot! :) )，pc版本是立即签到。

## 使用

选择上述解决方案之一，去对应的目录下载代码文件修改配置信息，目前只提供了python版。

将代码里的配置信息修改成自己的信息：

```python
#配置信息
phone = ""    # 登录手机号
password = ""  # 登录密码
desc = "我在这里"   #签到文本
longitude = "116.404267"  #经度
latitude = "39.910131"   #纬度
address = "天安门广场"   #签到地点名
stateType = "START"  #START 上班 END 下班
sec = 890  # 延迟签到的上限时间，单位为秒，pc方式无需关心此变量
#配置信息
```

server和serverless方式代码中引入了`sched`模块是为了在定时任务执行函数后可以延迟随机数时间再进行签到，打破规律性（我不是机器人:)），PC方式里去掉了该模块。
![image](https://user-images.githubusercontent.com/29170320/71053973-3fa26700-218b-11ea-9bfb-12a582382355.png)

### server

安装python环境和设置定时任务这里不赘诉，代码配置信息里修改`sec`，这个数值是随机延迟签到的上限时间，单位为秒。即 假设定时任务执行时间为7:00，`sec`设为900(s),签到时间会随机在7:00-7:15区间内。

### serverless

这里以[腾讯云函数计算服务](https://cloud.tencent.com/product/scf)举例，代码文件在[阿里云](https://www.aliyun.com/product/fc?spm=5176.10695662.1112509.1.70384357PNxEJS&aly_as=iPNjgEb7)同样可用。

修改代码配置信息`sec`，这个数值是随机延迟签到的上限时间，单位是秒，设置在`0-890`范围之间（腾讯云函数免费额度，其他平台可能不同）。

1. 创建函数。在函数服务控制台新建函数时运行环境选择python 3.6，在提交方法选在线编辑后完成创建。在函数代码页面的编辑器里新建文件名为"index.py"，将本仓库的代码复制进去，设置执行方法为`index.main_handler`后保存即完成函数计算的部署。
![image](https://user-images.githubusercontent.com/29170320/67254232-97d02c00-f4ae-11e9-832c-ddc8ec532f29.png)

2. 设置定时触发器。保存并测试成功后，添加触发方式为定时触发，自定义触发周期的Cron表达式，比如 `0 30 7 * * * *` , 意思是每天7点30分触发；每个周末中午12点触发的Cron表达式为`0 0 12 * * SAT,SUN *`,Cron表达式详细用法请参考各平台的官方文档。
![image](https://user-images.githubusercontent.com/29170320/71050975-ad499580-2181-11ea-963b-82287109ff50.png)

3. I am not a robot! 在函数配置页面**修改超时时间**为免费额度最大值900秒（初始默认为3秒），所以配置信息中的`sec`需要设置在0-890范围之间，即可实现如定时触发时间为每天7:00，则签到时间随机落在7:00~7:15区间内。
![image](https://user-images.githubusercontent.com/29170320/71050916-85f2c880-2181-11ea-8857-301ceadd2489.png)

腾讯云函数计算文档：https://cloud.tencent.com/document/product/583

阿里云函数计算文档：https://help.aliyun.com/product/50980.html?spm=a2c4g.11174283.6.540.24995212EDY4iS

### PC （Windows）

#### Python

1. 安装python3 环境 （https://python.org） 和 requests库（`pip install requests`） 。

2. 下载仓库中的`mogudStart.bat`文件(用来运行脚本)，**修改其中代码文件的路径**。

3. 将`mogudStart.bat`文件放到`C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` 目录下，重启。

#### 其他系统

[Bing](https://cn.bing.com/)