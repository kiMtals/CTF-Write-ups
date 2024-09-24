это мой первый райтап, надеюсь его кто-то прочитает)
## Начем с анализа исходника [app.py(https://github.com/kiMtals/CTF-Write-ups/edit/main/Patriot%20CTF%202024/WEB/Impersonate(medium)/app.py)]
Видим что нужно зайти в админку для получения флага, пытаемся пройти сквозь валидацию
пробуем раздичные кодировки и escape символы. Но ничего не выходит и видим, что секретный ключ для подписи куки генерится 
от времени сервера, а у нас как раз есть доуступ к нему .../status
Дальнейшее шаги решеняи в [Impesonate_solution.py(https://github.com/kiMtals/CTF-Write-ups/edit/main/Patriot%20CTF%202024/WEB/Impersonate(medium)/Impesonate_solution_.py)]
- Соотвественно парсим время
- Получаем секретный ключи
- Подписываем нужные куки  и отпрваляем их, любым удобным способов(curl, burp, requests и тд)
## получаем флан PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}
