# SSBU CV6: Framework Shiny

## Troubleshoot

#### Shiny for Python

- debug aplikácie - https://shiny.posit.co/py/docs/debug.html
- prípadne za behu aplikácie pomocou fukcie `print()` - výpisy nájdete v termináli medzi logmi aplikácie

#### Zastavenie behu Shiny 

- CTRL + C v termináli
- Niekedy sa stane, že sa proces neukončí správne, je potrebné ho zastaviť.
+ V príkazovom riadku si zobrazte zoznam procesov, ktoré bežia na porte 8000.
  
    `netstat -ano | findstr :8000`
  
+ V zozname nájdite PID (posledný stĺpec), a doplňte ho do príkazu pre zastavenie procesu.

    `taskkill /PID 'PID_procesu' /F`

