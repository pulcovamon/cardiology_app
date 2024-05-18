# Aplikace pro sledovani a porovnani kvality ovzdusi v nekolika Evropskych mestech

### databaze
- tabulky pro jednotliva mesta, sloupce hodnoty
- sqlite + sqlalchemy

### sluzba pro nacitani + zpracovani dat
- requesty na https://openweathermap.org/api/air-pollution
- python knihovna requests
- urceni kategorie kvality ovzdusi na zaklade dat
- porovnani kvality ovzdusi v nekolika Evropskych mestech (jednoducha statistika)
- uklada do databaze
- pandas

### sluzba pro zpracovani dat + ovladani
- api vystavujici zpracovana data, data vezme z databaze
- fastapi

### sluzba pro vizualizaci dat (grafana)
- zobrazeni dat z databaze

### sluzba pro vizualizaci dat (frontend)
- zobrazeni dat pro jednotliva mesta vcetne grafu
- zobrazeni porovnani
- react nebo chart.js nebo oboji

### webova dokumentace Mcdocs
- dokumentace aplikace
