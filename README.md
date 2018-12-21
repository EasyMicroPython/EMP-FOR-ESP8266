# EMP FOR ESP8266
[中文文档](./README_CN.md)

Due to the lack of memory in ESP8266, it always fails when using upip for installation. To this end, we created the EMP-FOR-ESP8266 compatibility solution.


## Quick Start

### Install emp-1zlab with emptool
first of all, we need emptool
```sh
pip install emptool
```

then, use it to install the `emp-1zlab` packages that esp8266 needed:
```sh
sudo emptool /dev/ttyUSB0  # change to your serialport
```

Make sure that no terminal emulators occupy the REPL during this process.

### Initialize your ESP8266

Enter to the REPL of your ESP8266:
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
Enter 2, then your board will be reboot.
Don't walk away. After rebooting, please follow the prompts to select the WiFi you need to access and enter your password to link to the network.

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

When you are properly connected to the network, you will see the following output:
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

## Contact Us
When you find any bugs during use, please help us improve this project in ISSUE.
Or you have any idea to communicate with us 1ZLAB, please email:

Fuermohao@outlook.com