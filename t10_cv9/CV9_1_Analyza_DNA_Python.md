# CV9: Analýza údajov DNA

## Python knižnice na prácu s DNA/RNA sekvenciami

- predpripravený projekt je v priečinku dna_rna
#### Úloha 1: Načítajte sekvenciu z databázy Genbank

- Genbank: https://www.ncbi.nlm.nih.gov/nucleotide/
- SeqIO dokumentácia: https://biopython.org/docs/1.75/api/Bio.SeqIO.html 
  
+ Stiahnite z databázy Genbank sekvenciu nukleotidov NC_005816 vo formáte genbank a vložte ju do priečinka inputs
+ pomocou knižnice Bio s použitím SeqIO a metódy read() načítajte sekvenciu a vypíšte na konzolu, čo bolo načítané
 
#### Úloha 2: Vytvorte Komplementárny Reťazec

- Príklad: Pre DNA reťazec `5'- AGTCC -3'` je komplementárny reťazec `3'- TCAGG -5'`.
- Vytvorte komplementárny reťazec k nasledujúcej DNA sekvencii: `5'-TACCGGAT-3'`
- String v pythone má metódy, ktorými môžete v reťazci nahradiť písmená inými:
    - str.maketrans() - vytvorenie tabuľky pre preklad znakov - [Dokumentácia](https://docs.python.org/3/library/stdtypes.html#str.maketrans)
    - str.translate() - nahradenie znakov v reťazci s použitím vytvorenej tabuľky - [Dokumentácia](https://docs.python.org/3/library/stdtypes.html#str.translate)


#### Úloha 3: Vytvorte mutáciu génu

+ Stiahnite z databázy Genbank sekvenciu nukleotidov AE017046.1 vo formáte fasta a vložte ju do priečinka inputs
+ Načítajte túto sekvenciu a vypíšte ju na konzolu
+ Vytvorte funkciu mutate s parametrom dna, v ktorej na náhodnej pozícii v reťazci zmeníte hodnotu bázy na inú (z ATGC). (Konvertujte sekvenciu na list, na vygenerovanom indexe zmeňte hodnotu a vráťte nazad string)
    + na generovanie použite funkcie randint() a choice() knižnice random - [Dokumentácia](https://docs.python.org/3/library/random.html)
+ Pomocou cyklu zopakujte vykonanie 1000 náhodných mutácií
+ Vypíšte sekvenciu po mutáciách

#### Úloha 4: Vypočítajte podiel guanino-cytozínových komplementárnych párov v sekvencii

+ V načítanej sekvencii AE017046.1 spočítajte počet Cytozínových a Guanínových báz a vypočítajte ich podiel v celkovom DNA reťazci
    + Použite atribúty a ich metódy implementované v knižnici SeqIO, ktoré je možné použiť na načítanej sekvencii - záznam má atribút .seq, ktorý je objektového typu Seq - [Dokumentácia](https://biopython.org/wiki/Seq)





