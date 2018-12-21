# EMP FOR ESP8266

由于esp8266缺少内存，总是在使用upip进行安装时失败
为此，我们创建了 EMP-FOR-ESP8266这一兼容性解决方案


## 快速开始

### 使用emptool安装emp-1zlab
首先我们需要获取到emptool
```sh
pip install emptool
```

然后，我们使用emptool来为ESP8266安装他所需要的emp-1zlab库
```sh
sudo emptool /dev/ttyUSB0  # change to your serialport
```

确保在此过程中你没有使用任何终端模拟器占用ESP8266的REPL

### 初始化你的ESP8266

进入ESP8266的REPL:
```python
>>> from emp_boot import set_boot_mode
>>> set_boot_mode()
[0]     Boot with nothing
        attention: this option will clear up boot.py, careful!
[1]     Boot with wifi startup
        this mode will auto start wifi connect program.
[2]     Easy to develop
        this mode is for developers.In this mode you can develop much easier via EMP-IDE(emp.1zlab.com)
Please input your choice [0-2]: 
```
选择第二项，你的设备将重启
不要走开，重启之后，请按照命令行提示将你的设备连接到WiFi网络。
```python
[0] How_Router_Home                          -61 dBm
[1] 501                                      -92 dBm
[2] CMCC-iEPD                                -69 dBm
[3] TP-LINK_301                              -75 dBm
[4] MERCURY_401                              -86 dBm
No record available
scaning networks...
[0] How_Router_Home                          -64 dBm
[1] 501                                      -90 dBm
[2] CMCC-iEPD                                -69 dBm
[3] TP-LINK_301                              -76 dBm
[4] MERCURY_401                              -87 dBm
Which one do you want to access? [0-4]
```

当你正确的连接到网络之后，你将看到类似如下的输出：
```python
connecting to network...
You are connected to How_Router_Home
IP: 192.168.0.121
Netmask: 255.255.255.0
Gateway: 192.168.0.1
Added record: How_Router_Home
You are connected to How_Router_Home
IP: 192.168.0.121
Netmask: 255.255.255.0
Gateway: 192.168.0.1
WebREPL daemon started on ws://192.168.4.1:8266
WebREPL daemon started on ws://192.168.0.121:8266
WebREPL started.
```

现在你便可以开始访问
<http://emp.1zlab.com>
来使用我们的EMP-IDE了。


## 联系我们
当你使用过程中有遇到任何的BUG，欢迎在ISSUE中帮助我们完善此项目。
或者你有任何的想法想与我们1ZLAB进行交流合作，请邮件：
Fuermohao@outlook.com