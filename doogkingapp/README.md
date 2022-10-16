# Documentació de minimal_api
**ALERTA**: Tot això està subjecte a canvis i pot quedar obsolet a favor de la branca que pengi la Maria.

## Configuració de l'entorn de desenvolupament 
El projecte funciona sobre Python 3.7 i té com a dependències Django i el Django REST Framework. Si teniu un virtual enviroment per l'aplicació entreu-hi (i si no en teniu us recomano que en creeu un) i instal·leu els següents paquets a través de PIP, si encara no els teniu:
```
pip install Django=3.2.12 djangorestframework
```
(Hauríem de generar un requirements.txt amb tots els paquets que fem servir, que aniria bé per autimatitzar la instal·lació i portar un registre del que necessitem).
Feu checkout de la branca `minimal_api`, i inicialitzeu la base de dades mitjançant 
```
python manage.py makemigrations
python manage.py migrate
```
Això de moment generarà una base de dades sqlite en local que contindrà tota la informació. Probablement mantindrem això així per fer testing i quan fem el deployment l'hi posarem una Postgres o alguna cosa així, però de moment no us en preocupeu. 
Ara podeu crear una conta d'administrador amb 
```
python manage.py createsuperuser
```
Us demanarà un email i contrassenya, que després podeu utilitzar per iniciar sessió a [http://localhost:8000/admin](), on podreu crear més instàncies dels models Profile i Housing.

Per engegar el servidor i poder accedir a la interfície d'admin i a la api executeu 
```
python manage.py runserver
```

## Endpoints de l'API
### Login
El login es pot fer des de l'endpoint `httplocalhost:8000/api/login/`. Si es passa una combinació correcta d'email i contrassenya, retornarà un token que servirà per autenticar-se a la resta de l'api. Amb curl es faria així:
```
curl -X POST http://localhost:8000/api/login/ -d '{"username":"admin@example.com", "password":"admin1234"}' -H "Content-Type: application/json"
```
(probablement s'hauria de canviar el nom del paràmetre username per email) i la resposta és amb el format
```
{"token":"bc6c61ffcc164bb62e869530f18333a93713037c"}
```

Aleshores, per fer requests a la resta de la API, s'ha de passar el token al header amb el següent format:
```
curl -X GET http://localhost:8000/api/profiles/  -H "Content-Type: application/json" -H "Authorization: Token bc6c61ffcc164bb62e869530f18333a93713037c"
```
(noteu l'espai entre la string "Token" i el token pròpiament).

### Profiles
Es pot fer el register fent un post a `http://localhost:8000/api/profiles/`. Els camps que accepta són els següents:
- url: només de lectura, no s'especifica en el POST. És la url de la api amb la que es pot accedir a cada element de manera individual. 
- email (obligatori)
- password (obligatori)
- first_name
- last_name

Tots els camps anteriors són de tipus text
El post a aquest endpoint el pot realitzar tothom, es passi token o no.
Si es fa un get del mateix endpoint amb un token d'una conta d'administrador, es retorna tota la llista d'usuaris.

### Housing
El model de housing es pot gestionar des de l'endpoint `http://localhost:8000/api/housing/`. Tal com abans, un get d'aquest endpoint mostrarà tota la llista de cases i un post en crearà una de nova. Els camps que conté són:
- url: només de lectura, dóna la url de l'element a la API
- house_id: només de lectura, és un enter que fa de clau primària 
- city: text
- street: text
- street_number: text
- floor: text
- door: text
- house_dimension: numèric
- house_owner: text, de moment és la url de la API de l'user a qui assignem la casa, del tipus "http://localhost:8000/api/profiles/3/", probablement s'hauria de canviar a email (o potser no, perquè estaríem exposant l'email del propietari i a l'url de la api només hi pot accedir l'admin...)

La lectura de tota la llista i d'elements particulars és oberta a tothom, passi token o no, però la escriptura només està permesa amb un token vàlid, sense caldre ser administrador.
