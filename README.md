## 蘑菇丁App自动签到

蘑菇丁app自动签到，提供2个解决方案。
- serverless，可以使用腾讯云、阿里云等平台提供的函数计算服务，并且免费额度足够签到使用。代码文件在仓库serverless目录下。
- 将程序设置成工作电脑的开机自启项或定时任务，每天开机时即自动签到。代码文件在仓库pc目录下。
- 将两种方案进行综合，因为函数计算是定时执行代码签到，长期固定时间签到生活过分规律，可采取工作日电脑自启签到方式+周末函数计算签到方式。

## 使用

选择2种解决方案之一（或全选），去对应的目录下载代码文件修改配置信息，目前只提供了python版。

将代码里的配置信息修改成自己的信息：

```python
phone = ""    # 登录手机号
password = ""  # 登录密码
desc = "我在这里"   #签到文本
longitude = "116.404267"  #经度
latitude = "39.910131"   #纬度
address = "天安门广场"   #签到地点名
```

代码中引入了`sched`模块是为了在定时任务执行函数后可以间隔随机数时间再签到，打破规律性。随机数范围起初想设置成60-1800，即定时触发后半小时内(1800s)随机时间进行签到。后发现腾讯云不能超出3s。So 可去掉该模块也可设置将随机数设置成0-2。。PC方式里已去掉该模块。

### serverless

这里以[腾讯云函数计算服务](https://cloud.tencent.com/product/scf)举例，代码文件在[阿里云](https://www.aliyun.com/product/fc?spm=5176.10695662.1112509.1.70384357PNxEJS&aly_as=iPNjgEb7)同样可用。

1. 创建函数。在函数服务控制台新建函数时运行环境选择python 3.6，在提交方法选在线编辑后完成创建。在函数代码页面的编辑器里新建文件名为"index.py"，将本仓库的代码复制进去，设置执行方法为`index.main_handler`后保存即完成函数计算的部署。
![image](https://user-images.githubusercontent.com/29170320/67254232-97d02c00-f4ae-11e9-832c-ddc8ec532f29.png)

2. 设置定时触发器。保存并测试成功后，添加触发方式为定时触发，自定义触发周期的Cron表达式，比如 `	
0 0 9 * * * *` ,意思是每天9点触发。表达式详细用法请参考官方文档。

腾讯云函数计算文档：https://cloud.tencent.com/document/product/583

阿里云函数计算文档：https://help.aliyun.com/product/50980.html?spm=a2c4g.11174283.6.540.24995212EDY4iS

### PC （Windows）

#### Python

1. 安装python3 环境 （https://python.org）和 requests库（pip install requests） 。

2. 下载仓库中的`mogudStart.bat`文件(用来运行脚本)，修改其中代码文件的路径。

3. 将该`mogudStart.bat`文件放到`C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` 目录下，重启。

#### 其他系统

[Bing](https://cn.bing.com/)