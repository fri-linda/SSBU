# SSBU CV2: Úvod do R

## Inštalácia potrebných nástrojov

#### Inštalácia Python

Potrebné stiahnuť inštalačný súbor - www.python.org/downloads/

<img src="data/python1.png" width="70%"/>


<img src="data/python2.png"  width="70%"/>

V príkazovom riadku:
- Overenie nainštalovanej verzie Pythonu:
`python -V`

<img src="data/python3.png" width="70%"/>

- Overenie nainštalovanej verzie Pip:
`pip -V`

<img src="data/python4.png" width="100%"/>

----

#### Inštalácia Jupyter Lab

V príkazovom riadku:
- inštalácia jupyter lab
`pip install jupyterlab`

- spustenie jupyter lab
`jupyter lab`

<img src="data/python5.png" width="100%"/>

<img src="data/python6.png" width="100%"/>

----
#### Inštalácia R

Potrebné stiahnuť inštalačný súbor - www.cran.r-project.org/bin/windows/base/

- stačí preklikať cez "Next"

<img src="data/r1.png" width="40%"/>
<img src="data/r2.png" width="60%"/>
<img src="data/r3.png" width="60%"/>
<img src="data/r4.png" width="60%"/>
<img src="data/r5.png" width="60%"/>
<img src="data/r6.png" width="60%"/>
<img src="data/r7.png" width="60%"/>
<img src="data/r8.png" width="60%"/>

----
#### Inštalácia R kernelu

V príkazovom riadku:
- Zobrazenie dostupnych jupyter kernelov:

`jupyter kernelspec list` 

Spustenie R v konzole (z miesta kde sa nachadza R.exe (podľa inštalácie), predvolene C:\ProgramFiles\R\bin) - **spustiť ako administrátor**

<img src="data/r_kernel1.png " alt="Workflow diagram" width="60%"/>
<img src="data/r_kernel2.png " alt="Workflow diagram" width="60%"/>

V R konzole:

`install.packages('IRkernel')`

<img src="data/r_kernel3.png " alt="Workflow diagram" width="60%"/>

V R konzole:

`IRkernel::installspec()`

`quit()`

`Save workspace image?: n`

<img src="data/r_kernel4.png " alt="Workflow diagram" width="60%"/>

----
#### Clone/Fork Git repozitára
(ak ešte nemáte)


##### Clone
V príkazovom riadku:

`git clone https://github.com/fri-linda/SSBU`

<img src="data/git_clone.png " alt="Workflow diagram" width="60%"/>

`git checkout ssbu_cv2`


##### Fork

- Na Githube nájdete repozitár https://github.com/fri-linda/SSBU
- Napravo je tlačidlo Fork - fork vytvorí kópiu repozitára na vašom Github účte a prepojí ju s pôvodným repozitárom.

<img src="data/git_fork1.png " alt="Workflow diagram" width="100%"/>

- Odznačte checkbox "Copy the master branch only"
  
<img src="data/git_fork2.png " alt="Workflow diagram" width="60%"/>

<img src="data/git_fork3.png " alt="Workflow diagram" width="60%"/>

- Pomocou tlačidla "Sync fork" si synchronizujete zmeny v pôvodnom repozitári s vaším repozitárom 
  
<img src="data/git_fork4.png " alt="Workflow diagram" width="35%"/>

Následne je ešte potrebný clone svojho repozitára.

#### Vytvorenie R skriptu v Jupyter Lab

V príkazovom riadku v naklonovanom git repozitári:

- spustenie jupyter lab
  
`jupyter lab`

<img src="data/final1.png " alt="Workflow diagram" width="100%"/>

- už je dostupný aj R kernel
- Vyberte R skript

<img src="data/final2.png " alt="Workflow diagram" width="80%"/>

- Zobrazenie aktuálneho kernelu - R, Python

<img src="data/final3.png " alt="Workflow diagram" width="100%"/>

<img src="data/final4.png " alt="Workflow diagram" width="100%"/>

- Vytvorenie novej bunky v skripte

<img src="data/final5.png " alt="Workflow diagram" width="100%"/>

- Možnosti skriptu - uloženie, nová bunka, spustenie bunky/skriptu ..
    - Typ bunky - Markdown - formátovaný text, Code - spustiteľný kód, Raw - text 

<img src="data/final6.png " alt="Workflow diagram" width="50%"/>

- Výstup pre bunku po spustení skriptu

<img src="data/final7.png " alt="Workflow diagram" width="50%"/>


