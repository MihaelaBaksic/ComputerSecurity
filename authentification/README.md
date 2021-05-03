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

Svaki zapis u bazi podataka sastoji se od korisničkog imena, zastavice valid, salta i hashirane lozinke.

####Hashing

Postupak pohrane lozinke se sastoji od generiranja random salta koristeći kriptografski random generator.
Salt se konkatenira na lozinku i dobiveni string se hashira kriptografskom hash funkcijom.
U bazu se spremaju i salt i dobiveni hash.

#### Salting
Korištenje salta osigurava da svi hashevi u bazi budu različiti, čak i ako dva korisnika imaju istu lozinku te 
spriječava hash table napade.
Salt je jedinstven za svaku lozinku u bazi jer bi korištenje istog salta omogućilo napadaću da izračuna hash tablicu za taj salt unaprijed, čime salt postaje praktički bezvrijedan.

Zastavica valid služi kako bi se omogućilo administratorima prisiliti korisnika da izmjeni lozinku. \
Ukoliko je zastavica postavljena na false, korisnik će pri idućem loginu morati izmjeniti lozinku.



## Postupak prijave

Prilikom prijave korisnik unosi svoje korisničko ime i lozinku. \
Iz baze (u ovoj implementaciji iz datoteke) se dohvaća zapis za uneseno korisničko ime.
Unesena lozinka i salt iz zapisa se konkateniraju i hashiraju.

Ukoliko je dobiveni hash jednak hashu u zapisu iz baze, unesena je ispravna lozinka i prijava je uspješna.
U suprotnom prijava nije uspješna.


## Korištenje

Alat se koristi iz naredbenog retka te korisnik mora imati instaliran python3 i biblioteku pycryptodome.
Prije izvođenja korisnik se mora pozicionirati unutar direktorija `authentification `.

### usermgmt

Alat za upravljanje lozinkama podržava akcije: add (dodavanje), delete (brisanje), passwd (izmjena) i forcepass (prisilna izmjena).

Izvođenje odabrane akcije izvodi se naredbom u obliku:

    $ python3 ./usermgmt.py <naredba> <username>


### login

Alat za prijavu korisnika koristi se izvođenjem naredbe:

    $ python3 ./login.py <username>

