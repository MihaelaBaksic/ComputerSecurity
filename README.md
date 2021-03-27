Laboratorijske vježbe iz predmeta Sigurnost računalnih sustava, FER, Sveučilište u Zagrebu

# Password manager

U sklopu laboratorijske vježbe razvijen je Password manager u programskom jeziku Python. Program je razvijen koristeći biblioteku pycriptodome i namjenjen je za korištenje u naredbenom retku.

## Zahtjevi

Zahtjevi koje rješenje mora zadovoljavati su sljedeći:
1. Povjerljivost zaporki
2. Povjerljivost adresa
3. Integritet adresa i zaporki

Zahtjevi su ispunjeni korištenjem autentificirane šifre i funkcije za derivaciju ključa iz zaporke.

## Funkcija za derivaciju ključa  



## Autentificirana šifra

## Korištenje

Program se koristi iz naredbenog retka te korisnik mora imati instaliran python3 i biblioteku pycriptodome.
Korištenje se sastoji od 3 koraka: inicijalizacije (init), postavljanja lozinke za adresu (put) te dohvata lozinke za zadanu adresu (get).

1. Na samom početku korisnik treba odabrati svoj master password koji će mu služiti za pristup bazi. Pomoću njega izvršava inicijalizaciju password managera naredbom:

    $ ./passManager init <master_password>
    
    Navedena naredba predviđena je za izvršavanje na samom početku korištenja te će njezino ponavljanje uzrokovati brisanje baze i ponovnu inicijalizaciju.
    
2.
