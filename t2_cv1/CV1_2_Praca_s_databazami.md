# SSBU CV1: Úvod do softvérových nástrojov pre analýzu biomedicínskych dát

## Práca s databázami

#### National Center for Biotechnology Information 
- súbor biomedicínskych a biotechnologických databáz
- voľne prístupné - www.ncbi.nlm.nih.gov/
- GenBank - DNA databáza
- PubMed - publikačná databáza

##### GenBank
- prístup buď cez Google Search: genbank, alebo priamo - www.ncbi.nlm.nih.gov/genbank/

<img src="data/genbank1.png" alt="Workflow diagram" width="80%"/>

- vyhľadávanie - možnosť vybrať si konkrétnu databázu a hľadať konkrétny gén v orghanizme (napr. P53 homo sapiens)
   - v rámčeku na začiatku výsledkov sú zobrazené informácie o hľadanom géne ako aj jeho ďalšie kódovania

<img src="data/genbank2.png" alt="Workflow diagram" width="80%"/>

- taxonómia - zaradenie organizmov (druh, rod, čeľaď, ..) na základe ich vzájomných príbuzenských a evolučných vzťahov
   - zobrazenie vo forme listu alebo stromu

 <img src="data/genbank3.png" alt="Workflow diagram" width="80%"/>
 
+ výsledky vyhľadávania - označenie
   +  kompletná alebo čiastočná kódovacia sekvencia (complete cds/partial cds)
   + prístupové číslo - AB082923.1
   + GenInfo Identifier - 23491728

 <img src="data/genbank4.png" alt="Workflow diagram" width="80%"/>
     
+ zobrazenie výsledku - po otvorení vybraného výsledku (napr. Homo sapiens mRNA for P53, complete cds)
   + štruktúrovaná forma

   + základné údaje
  
 <img src="data/genbank5.png" alt="Workflow diagram" width="80%"/>

   + zdroj a organizmus

 <img src="data/genbank6.png" alt="Workflow diagram" width="80%"/>
  
   + informácie o publikácii
 
 <img src="data/genbank7.png" alt="Workflow diagram" width="80%"/>
  
   + sekvencia (súbor údajov) - originálna nukleotidová sekvencia proteínu

 <img src="data/genbank8.png" alt="Workflow diagram" width="80%"/>
  
   + vlastnosti - metadáta
  
  <img src="data/genbank9.png" alt="Workflow diagram" width="80%"/>
  
   + zdroj, gén a kódovacia sekvencia CDS (kliknutím sa sekvencia zvýrazní v pôvodných údajoch)

 <img src="data/genbank10.png" alt="Workflow diagram" width="80%"/>
 
   + translácia - preklad genetickej informácie nukleotidov na poradie aminokyselín

 <img src="data/genbank11.png" alt="Workflow diagram" width="80%"/>

   + Kódovanie aminokyselín:
     
 <img src="data/translation.png" alt="Workflow diagram" width="80%"/>
 
   + zobrazenie detailov - spodný panel - dobré pri dlhých pôvodných sekvenciách (ostáva na obrazovke pri posúvaní sa smerom dolu)

 <img src="data/genbank12.png" alt="Workflow diagram" width="80%"/>
   
   - export údajov do súboru

 <img src="data/genbank13.png" alt="Workflow diagram" width="80%"/>
 
   - formát sekvencie
     - FASTA
     - Grafický
       
 <img src="data/genbank14.png" alt="Workflow diagram" width="80%"/>
  
 <img src="data/genbank15.png" alt="Workflow diagram" width="100%"/>
  
 - zobrazenie detailov - nabehnutím myšou na jednotlivé úseky (región, poloha, dĺžka, odkazy na databázy)

   <img src="data/genbank16.png" alt="Workflow diagram" width="80%"/>
   
 - CDD (Conserved Domain Database) - anotácie proteínov, popis funkcie génu (zobrazenie podrobnejších informácií - obrázok, vlastnosti, taxonómia, ..)

  <img src="data/genbank17.png" alt="Workflow diagram" width="80%"/>
             
##### PubMed
- prístup buď cez Google Search: pubmed, alebo priamo - www.pubmed.ncbi.nlm.nih.gov/

 <img src="data/pubmed1.png" alt="Workflow diagram" width="80%"/>
 
- jednoduché vyhľadávanie alebo možnosť "Advanced"
  - vytváranie dotazu podľa konkrétnych atribútov, alebo ich kombinácie (dáva aj nápovedu)

 <img src="data/pubmed2.png" alt="Workflow diagram" width="80%"/>
 <img src="data/pubmed3.png" alt="Workflow diagram" width="80%"/>
 <img src="data/pubmed4.png" alt="Workflow diagram" width="80%"/>
 
- zoradenie výsledkov

 <img src="data/pubmed5.png" alt="Workflow diagram" width="50%"/>
 
- filtrovanie výsledkov (full text, free full text)

 <img src="data/pubmed6.png" alt="Workflow diagram" width="30%"/>

- výsledky vyhľadávania

 <img src="data/pubmed7.png" alt="Workflow diagram" width="80%"/>

- detailné zobrazenie článku
   - PMID (PubMed Identifier), PMCID (PubMed Central Identifier), DOI (Digital Object Identifier)

  <img src="data/pubmed8.png" alt="Workflow diagram" width="80%"/>
 
   - abstrakt a kľúčové slová

  <img src="data/pubmed9.png" alt="Workflow diagram" width="80%"/>
  
   - obrázky

  <img src="data/pubmed10.png" alt="Workflow diagram" width="80%"/>
  
   - podobné články

  <img src="data/pubmed11.png" alt="Workflow diagram" width="80%"/>
  
   - citácie článku

  <img src="data/pubmed12.png" alt="Workflow diagram" width="80%"/>

   - referencie v článku

  <img src="data/pubmed13.png" alt="Workflow diagram" width="80%"/>

   - link na celý obsah článku
 
  <img src="data/pubmed14.png" alt="Workflow diagram" width="80%"/>
  
   - vygenerovanie citácie, výber formátu citácie

  <img src="data/pubmed15.png" alt="Workflow diagram" width="80%"/>

   - stiahnutie do súboru (citácia, abstrakt, PMID, ..)

  <img src="data/pubmed16.png" alt="Workflow diagram" width="80%"/>

  <img src="data/pubmed17.png" alt="Workflow diagram" width="80%"/>

----
##### Referencie
https://towardsdatascience.com/starting-off-in-bioinformatics-rna-transcription-and-translation-aaa7a91db031

www.ncbi.nlm.nih.gov/genbank/

www.pubmed.ncbi.nlm.nih.gov/
