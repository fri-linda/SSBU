# SSBU CV6: Framework Shiny

## Úvod do Shiny pre Python

- Shiny pre Python je webový aplikačný rámec navrhnutý na premenenie vašich projektov analýzy dát na interaktívne webové aplikácie.
- Na začiatok nie sú potrebné žiadne zručnosti webového vývoja.
- Pôvodne vyvinutý pre **R**, pre Python len nedávno.
- dokumentácia a **príklady** - https://shiny.posit.co/py/docs/overview.html

## Základné koncepty

### Štruktúra Shiny aplikácie

- **UI (Používateľské rozhranie):** Definuje rozloženie a vzhľad vašej aplikácie.
  - Použite funkcie ako `shiny.ui.page()` na vytvorenie rozloženia stránky.
  - Widgety ako tlačidlá, posúvače a textové vstupy sa používajú na interakciu s aplikáciou.

+ **Serverová funkcia:** Obsahuje pokyny na vytvorenie reakcií vašej aplikácie.
  - Prijíma vstupné hodnoty z UI, spracováva ich a vracia výstup späť do UI.

### Reaktivita

- **Reaktívne dekorátory:** Automaticky aktualizujú výstupy, keď sa zmenia vstupy.
- Použite `@shiny.input` na prístup k vstupným hodnotám a `@shiny.output` na definovanie výstupov.

## Kľúčové komponenty

### Vstupné widgety

- **Tlačidlo akcie:** `shiny.ui.button()` - spustí akciu po kliknutí.
- **Posúvač:** `shiny.ui.slider_input()` - umožňuje užívateľom vybrať hodnotu z rozsahu.
- **Textový vstup:** `shiny.ui.text_input()` - umožňuje užívateľom zadávať text.

### Výstupné widgety

- **Výstup grafu:** `shiny.ui.plot_output()` - zobrazuje grafy.
- **Výstup tabuľky:** `shiny.ui.table_output()` - zobrazuje dáta vo formáte tabuľky.
- **Textový výstup:** `shiny.ui.text_output()` - zobrazuje text.

### Rozloženie

- **Bočný panel** `shiny.ui.sidebar()` - napr. vstupy na bočnom paneli vľavo.
- **Karty** `shiny.ui.card()` - napr. spájanie spoločného obsahu do kariet.
- **Box** `shiny.ui.value_box()` - napr. zvýraznenie výstupov.
- **Rozdelenie podľa stĺpcov** `ui.layout_columns()` - napr. nastavenie šírky obsahu
- dokumentácia - https://shiny.posit.co/py/docs/user-interfaces.html

### Best Practices
- Udržiavajte kód UI a servera oddelený.
- Používajte reaktívne výrazy s rozumom (optimalizácia výkonu aplikácie).
- Testujte aplikáciu s rôznymi prehliadačmi a zariadeniami, aby ste zaistili kompatibilitu.

