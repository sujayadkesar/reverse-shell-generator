# reverse-shell-generator

![Como obtener una reverse shell - Nullsector.co](https://nullsector.co/wp-content/uploads/2017/12/Bash-new.sh_.png)

## Installation

``` 
 git clone https://github.com/sujayadkesar/reverse-shell-generator.git
 ```
``` 
cd reverse-shell-generator
```
``` 
python3 -m pip install -r requirements.txt 
```
``` 
python3 reverse-shell-generator.py 
```

> **Note** : To access this tool from any directory  
> ```
>  ln -sf <complete path to reverse-shell.py> /usr/local/bin/reverse-shell-generator
>  ```



``` bash
local_host@sujayadkesar:~/Desktop# python3 shell.py
 _____                                         _          _ _
|  __ \                                       | |        | | |
| |__) |_____   _____ _ __ ___  ___ ______ ___| |__   ___| | |
|  _  // _ \ \ / / _ \ '__/ __|/ _ \______/ __| '_ \ / _ \ | |
| | \ \  __/\ V /  __/ |  \__ \  __/      \__ \ | | |  __/ | |
|_|  \_\___| \_/ \___|_|  |___/\___|      |___/_| |_|\___|_|_|


                                 _
                                | |
  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __
 / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| (_| |  __/ | | |  __/ | | (_| | || (_) | |
 \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|
  __/ |
 |___/

*******************

@SUJAY_ADKESAR : https://sujayadkesar.github.io/portfolio
https://github.com/sujayadkesar/reverse-shell-generator

*******************

Local Area Connection* 9                 :          169.254.181.17
Local Area Connection* 10                :          169.254.101.232
VMware Network Adapter VMnet1            :          169.254.83.118
VMware Network Adapter VMnet8            :          169.254.149.155
Wi-Fi                                    :          192.168.74.132
vEthernet (WSL)                          :          172.31.208.1
Loopback Pseudo-Interface 1              :          127.0.0.1

*******************


Enter IP Address : 192.168.74.132
Enter Port Number : 4545
*******************






 _     _     _
| |   (_)___| |_ _ __   ___ _ __
| |   | / __| __| '_ \ / _ \ '__|
| |___| \__ \ |_| | | |  __/ |
|_____|_|___/\__|_| |_|\___|_|


1  nc                          7   rustcat +command history
2  ncat                        8   Windows ConPty
3  ncat(TLS)                   9   socat
4  rlwrap +nc                  10  socat TTY
5  rustcat                     11  powercat
6  pwncat                      12  msfconsole


 ____                                        _          _ _
|  _ \ _____   _____ _ __ ___  ___       ___| |__   ___| | |
| |_) / _ \ \ / / _ \ '__/ __|/ _ \_____/ __| '_ \ / _ \ | |
|  _ <  __/\ V /  __/ |  \__ \  __/_____\__ \ | | |  __/ | |
|_| \_\___| \_/ \___|_|  |___/\___|     |___/_| |_|\___|_|_|


1   Bash -i                    11  nc -e                      21  ncat -e
2   Bash 196                   12  ncmkfifo                   22  ncat.exe -e
3   Bash 5                     13  nc.exe -e                  23  awk
4   Bash udp                   14  nc -c                      24  rustcat
5   Bash readline              15  nc -c                      25  socat TTY
6   C Windows                  16  PHP exec                   26  Haskell
7   C# TCP client              17  PHP shell_exec             27  Powershell
8   Node js                    18  PHP system                 28  Python #2
9   PHP Emoji                  19  PHP popen                  29  telnet
10  PHP cmd                    20  PHP proc_open              30  Python Windows


rsg listning <number of the listner type>                = to generate the listner code
rsg reverse-shell <number of the reverse-shell type>     = to generate the reverse-shell code
exit                                                     = exit
clear                                                    = clear the screen

ifconfig                                                 = to get the ipv4 address of your system
set lhost                                                = to set or change the ip address
set lport                                                = to set or change the listing port number
show                                                     = to print the lhost and lport
rsg -h                                                   = list the reverse-shell and listners

example:-

rsg listner 4                  rsg reverse-shell 19

$
```


### Licensing

This project is licensed under the [MIT license](LICENSE).

![MIT License](https://danielmiessler.com/images/mitlicense.png)


NOTE: Downloading this repository is likely to cause a false-positive alarm by your anti-virus or anti-malware software, the filepath should be whitelisted. There is nothing in this that can harm your computer ; however it's not recommended to store these files on a server or other important system due to the risk of local file inclusion attacks
