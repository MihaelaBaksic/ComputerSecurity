Laboratorijske vježbe iz predmeta Sigurnost računalnih sustava, FER, Sveučilište u Zagrebu

# Autentifikacija upotrebom lozinki

U sklopu laboratorijske vježbe razvijen je alat za autentifikaciju upotrebom lozinki i namjenjen je korištenju u naredbenom retku.
Sastoji se od alata za upravljanje lozinkama (usermgmt) i alata za prijavu korisnika (login). Alat je implementiran koristeći programski jezik Python.

## Sigurnosni zahtjevi

Iako su lozinke često korišten način autentifikacije, postoje brojne ranjivosti i prijetnje na sigurnost lozinki.
1. Niska razina kompleksnosti
2. Krađa lozinki
3. Nesipravna pohrana lozinki


Implementacija ovog alata ima sljedeća svojstva koja smanjuju ranjivost lozinki:
1. Određena je minimalna prihvatljiva duljina lozinke
2. Lozinka mora sadržavati barem jednu znamenku i barem jedno veliko slovo
3. Lozinke nisu vidljive tijekom unosa
4. Administratori mogu forsirati korisnika da promjeni lozinku
5. Lozinke su spremljene kao sažetci (hashevi)

Svojstva 1 i 2 odnose se na rješavanje problema niske razine kompleksnosti lozinke - otežavaju brute force i dictionary napade. 
Svojstvo 3 smanjuje mogućnost krađe/snimanja lozinke tokom unosa.
Svojstvo 5 osigurava pravilno spremanje lozinki u bazu.

## Pohrana lozinki

Svaki zapis u bazi podataka sastoji se od korisničkog imena, zastavice valid, hashirane lozinke i popratnih podataka (salt i konfiguracijski podaci).

#### Hashing

Za postupak hashiranja koristise funkcija za derivaciju ključa `argon2`. 
Svako hashiranje se sastoji od generiranja random salta i hashiranja plaintext lozinke zajedno sa generiranim saltom.
Razlog za korištenje funkcije za derivaciju ključa umjesto neke od klasičnih hash funkcija poput SHA256 je njena veća otpornost na napade GPU-om.

Funkcija za hashiranje za povratnu vrijednost ima izračunati hash, korišteni salt i popratne parametre.

#### Salting
Korištenje salta osigurava da svi hashevi u bazi budu različiti, čak i ako dva korisnika imaju istu lozinku te 
spriječava hash table napade.
Salt je jedinstven za svaku lozinku u bazi jer bi korištenje istog salta omogućilo napadaću da izračuna hash tablicu za taj salt unaprijed, čime salt postaje praktički bezvrijedan.
Implementacija hashiranja algoritmom argon2 interno generira random salt prilikom svakog hashiranja, a kod validacije koristi salt spremljen u zapisu u bazi.

Zastavica valid služi kako bi se omogućilo administratorima prisiliti korisnika da izmjeni lozinku. \
Ukoliko je zastavica postavljena na false, korisnik će pri idućem loginu morati izmjeniti lozinku.



## Postupak prijave

Prilikom prijave korisnik unosi svoje korisničko ime i lozinku. \
Iz baze (u ovoj implementaciji iz datoteke) se dohvaća zapis za uneseno korisničko ime.
Unesena lozinka i hash dohvaćen iz baze su ulazni parametri funkcije za validaciju.

Validacija se sastoji od ekstrakcije salta iz zapisa u bazi, hashiranja te usporedbe dobivenog hasha i hasha iz zapisa u bazi.
Ukoliko je dobiveni hash jednak hashu u zapisu iz baze, unesena je ispravna lozinka i prijava je uspješna.
U suprotnom prijava nije uspješna.


## Korištenje

Alat se koristi iz naredbenog retka te korisnik mora imati instaliran python3 i biblioteku `argon2_cffi`.
Prije izvođenja korisnik se mora pozicionirati unutar direktorija `authentification `.

### usermgmt

Alat za upravljanje lozinkama podržava akcije: add (dodavanje), delete (brisanje), passwd (izmjena) i forcepass (prisilna izmjena).

Izvođenje odabrane akcije izvodi se naredbom u obliku:

    $ python3 ./usermgmt.py <naredba> <username>


### login

Alat za prijavu korisnika koristi se izvođenjem naredbe:

    $ python3 ./login.py <username>

