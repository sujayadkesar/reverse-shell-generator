# reverse-shell-generator

![Como obtener una reverse shell - Nullsector.co](https://nullsector.co/wp-content/uploads/2017/12/Bash-new.sh_.png)



##  Welcome to the Reverse Shell Generator 🔀🤖

The Reverse Shell Generator is a tool that enables you to quickly and easily generate reverse shells for a variety of operating systems and platforms. With its user-friendly interface, you can easily customize the settings for your reverse shell, such as the host and port to connect to, and generate the command to execute on the target machine.

Whether you're a penetration tester, a network administrator, or a developer, the Reverse Shell Generator can save you time and effort by automating the process of generating reverse shells. Plus, with support for multiple languages and platforms, the Reverse Shell Generator is a versatile tool that can be used in a variety of scenarios.

## Some of the features of Reverse Shell Generator include:

-   😀User-friendly interface
-   🚨Multiple languages supported (e.g. Bash, Python, PowerShell, etc.)
-   ⚡Multiple platforms supported (e.g. Windows, Linux, macOS, etc.)
-   🐺Customizable settings (e.g. host, port, etc.)
-   🤹Generate command with one click

Ready to start generating reverse shells? Try the Reverse Shell Generator now! 🚀



## :teacher: Installation
> **Note** : python3 and pip must be installed **ignore this if installed**
> ```
> sudo apt update
> sudo apt install python3
> sudo apt install python3-pip
>  ```

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

## Contribution 🤝 <br>
If you're interested in contributing to the development of Reverse Shell Generator, we would love to have you on board! We are constantly looking for ways to improve and add new features, and your contributions can help make Reverse Shell Generator even more powerful and useful.

## Here are a few ways you can contribute to the project:

-   Report bugs or request new features by creating an issue on our GitHub repository.🐛
-   Help us improve the documentation by submitting updates or corrections.📚
-   Contribute code by submitting pull requests with bug fixes or new features.💻
-   Share Reverse Shell Generator with your friends, colleagues, and on social media to help spread the word and grow the community.📣

No matter how you choose to contribute, your help is greatly appreciated! Together, we can make Reverse Shell Generator the best tool for generating reverse shells. Thank you for your support! 🙏

Please make sure to read the [Code of Conduct](https://chat.openai.com/CODE_OF_CONDUCT.md) and [CONTRIBUTING.md](https://chat.openai.com/CONTRIBUTING.md) before contributing to the project.

> :warning: **Please note that using this tool for illegal or unauthorized purposes is strictly prohibited and the developers take no responsibility for any misuse of the tool. Use at your own risk.**


### Licensing

This project is licensed under the [MIT license](LICENSE).

![MIT License](https://danielmiessler.com/images/mitlicense.png)


NOTE: Downloading this repository is likely to cause a false-positive alarm by your anti-virus or anti-malware software, the filepath should be whitelisted. There is nothing in this that can harm your computer ; however it's not recommended to store these files on a server or other important system due to the risk of local file inclusion attacks
