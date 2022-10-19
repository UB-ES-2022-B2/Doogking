# Deploy
## Coses d'Azure
### Creació de la WebApp a Azure (només la primera vegada)
Aneu a [azure](https://portal.azure.com) i aneu a *App Services > Create*. Aneu omplint els camps segons veieu, els més importants són:
- Subscription: ha de ser **Azure for Students**
- Resource group: Qualsevol, si no n'hi ha cap, creeu-ne un
- Publish: ha d'estar seleccionada l'opció **Code**
- Runtime stack: **Python 3.7** en el nostre cas
- Operating System: **Linux** sempre
- Region: Aquí poseu el que vulgueu, la teoria diu que com més proper millor, així que jo poso **France Central**
- Linux Plan: Assegureu-vos que és el pla gratuït (crec que és el per defecte a France Central)

Premeu el botó **Review + create**, que a la resta de pestanyes no ens deixen modificar gaire res més, de moment i finalment **Create**. Azure crearà l'app service i si aneu a App Services ja l'hauríeu de veure allà.

### Creació de la base de dades PostgreSQL (només la primera vegada)
Torneu al portal d'Azure i aquesta vegafa aneu a *Azure Database for PostgreSQL flexible servers > Create*. Tal com abans, aneu omplint els camps. A continuació hi ha algunes anotacions sobre els camps:
- Subscription: ha de ser **Azure for Students**
- Resource group: El mateix que heu posat durant la creació d'App Service
- Server name: el que vulgueu, guardeu-lo per després, que és important
- Region: Com abans, tot i que crec que també hi ha **France South**
- PostgreSQL version: **14**
- Workload type: **Development**, que si no et fan pagar
- Compute + storage: El que posa *Free upto 750 hours/Free upto 32 GB*, crec que és el per defecte per *Workload type == Development*
- Availability Zone: **No preference**
- Enable High availability: **No**
- Authentication method: **PostgreSQL authentication only**

i ompliu les credencials d'*Admin username*, i *Password*. Passeu a la pestanya de **Networking** i configureu els següents camps:
- Conectivity Method: **Public access (allowed IP adresses)**
- Allow public access from any Azure service within Azure to this server: **Sí**

A les regles de firewall, premeu a **+ Add 0.0.0.0 - 255.255.255.255**, que permetrà que també hi puguem accedir des de l'exterior. Ara sí que podeu anar a **Review + create** > **Create**. Un cop Azure hagi creat el server, s'ha de crear la base de dades en sí. Per fer-ho, des del portal d'azure aneu a *Azure Database for PostgreSQL flexible servers*, seleccioneu el server que heu creat, aneu a l'opció *Settings > Databases* del menú de l'equerra i premeu el botó *Add*.

### Connexió de la base de dades (potencialment només la primera vegada)
La connexió de la base de dades amb el backend la farem per variables d'entorn, és a dir, definirem un conjunt de variables a nivell de sistema operatiu amb la informació de la base de dades i farem que el backend accedeixi a aquesta informació. Així, si volem modificar el servidor de bases de dades no cal tocar el backend, modificant les variables d'entorn en tenim prou. De fet, també les podem fer servir per canviar automàticament entre la base de dades d'SQLite en local i la de PostgreSQL en producció. Per fer-ho, modifiquem el fitxer `Doogking/settings.py`, afegint-hi:
```python
import os
if 'WEBSITE_HOSTNAME' in os.environ.keys():
    # Aleshores estem a Azure, fem servir les variables d'entorn per connectar-nos a Postgres
    # (a no ser que per algun motiu tingueu la variable d'entorn WEBSITE_HOSTNAME en local, però vaja, no ho crec)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['DBNAME'],
            'HOST': os.environ['DBHOST'],
            'USER': os.environ['DBUSER'],
            'PASSWORD': os.environ['DBPASS']
        }
    }
else:
    # Estem en local, podem fer servir la DB d'SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
**ATENCIÓ:** aquest canvi ja està inclòs a la branca `integration`, no cal que toqueu res!

Ara ens cal crear les variables d'entorn a l'App Service que hem creat a Azure. Per fer-ho anem a l'App Service i accedim a *Settings > Configuration*. Aquí haurem de crear múltiples Aplication Settings amb les següents parelles de clau/valor:
- DBHOST: `<server_name>.postgres.database.azure.com`, amb server_name el que heu posat al pas anterior que he dit que us guardéssiu
- DBNAME: El nom de la base de dades que heu creat al pas anterior
- DBUSER: El que heu posat a les credencials del pas anterior
- DBPASS: La contrassenya de l'usuari que heu creat

Assegureu-vos de prémer el botó **Save**, que si no no es guarda res.

### Configuració del deploy a Azure (només la primera vegada)
Finalment ens cal configurar el mecanisme de deploy per pujar les coses a Azure. Anant bé això ho hauríem de poder fer mitjançant Github Actions, però de moment ho fem manualment i simplement pujem la branca de la que volem fer deploy al server de git d'Azure. Per configurar-ho, aneu a l'App Service i accediu a *Deployment > Deployment Center*. A la pestanya de Settings, a Source seleccioneu **Local Git** i guardeu amb el botó de *Save* de dalt, que generarà un repo de git dins el server d'Azure. Guardeu-vos el **Git Clone Uri**, que serà important per després. A continuació aneu a la pestanya de **Local Git/FTPS credentials**. A **Aplication Scope** us donen un nom d'usuari i contrassenya que teòricament serveixen per autenticar-vos al repositori que acabem de crear, però jo mai he aconseguit que em funcionin, així que crec que el millor és que baixeu fins a **User Scope** i creeu un usuari i contrassenya pel repo. Guardeu-los que més endavant seràn útils.

I crec que amb tot això ja tenim la configuració d'Azure enllestida!

## Canvis al codi
A continuació explico els canvis que he hagut de fer al codi per fer-lo funcionar a Azure. Aquest apartat és a tall informatiu, en principi a la branca `integration` ja està tot adaptat i no cal que toqueu res.

### requirements.txt
En aquest fitxer s'especifiquen tots els paquets de Python que són necessaris per servir la web. Azure busca aquest fitxer al directori arrel i instal·la automàticament tots els paquets que s'especifiquin aquí. També és útil per instal·lar totes les dependències en virtual enviroments de python, que fent `pip install -r requirements.txt` ja els instal·la tots.

### Doogking/settings.py
Aquí és on hi ha la majoria de canvis:
- Afegir `import os`
- Afegir el domini `azurewebsite.com` a ALLOWED_HOSTS. Queda `ALLOWED_HOSTS = ['localhost', '.azurewebsites.net']`

##### Whitenoise i paths dels fitxers estàtics
Django no pot servir el fitxers estàtics en producció de manera que hem d'afegir un middleware que ho faci en el seu lloc, i en aquest cas fem servir Whitenoise. He afegit el paquet a `requirements.txt` i cal afegir la línia `'whitenoise.middleware.WhiteNoiseMiddleware',` a MIDDLEWARE de `settings.py`. L'ordre dels middlewares és important, el de whitenoise ha d'estar just després del de Security. La variable middleware queda una cosa així:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
```
Al final del fitxer, on es defineixen els directoris dels fitxers estàtics cal afegir les següents línies:
```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend/dist/static')]
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'frontend/dist/')
```
Hem de modificar també la variable TEMPLATES de `settings.py` per tal que agafi els fitxers generats per Vue. Només cal afegir el directori on vue genera els fitxers (en el nostre cas `frontend/dist`) a l'array de DIRS, quedant
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', os.path.join(BASE_DIR, 'frontend/dist')]
        ,
        [...]
    }
]
```

##### Base de dades
Per la connexió amb la base de dades, simplement afegim el fragment de codi de l'apartat de [connexió amb base de dades](#connexió-de-la-base-de-dades-(potencialment-només-la-primera-vegada)).


### Doogking/urls.py
Aquí cal afegir l'import `from django.views.generic import TemplateView` per poder carregar pàgines estàtiques. També cal afegir l'entrada `url(r'^.*$', TemplateView.as_view(template_name='index.html')),` a l'array urlpatterns. Aquest index.html fa referència a l'index que es genera en fer el build del frontend, i que ja inclou el router de vue i tot això. L'ordre dels elements de urlpatterns és molt important, ja que si un url coincideix amb el regex que definim aquí, es mostra aquella template i ja està. Així el que fem és posar primer els de l'api i interns de Django i al final aquest de vue amb un regex que ho captura tot fent que, en última instància, sigui el router de vue qui ho gestiona tot. L'array d'urlpatterns queda així:
```python
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', obtain_auth_token),
    path('admin/', admin.site.urls),
    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
```

## Com fer el deploy
### Configuració del remote (només la primera vegada)
Abans de fer res, hem d'afegir el repo de git que hem creat amb l'app service com a remote del repos de git local (és a dir, que a part de poder penjar les coses a github (`origin`), també les podrem penjar al remote `azure`). Entreu al directori que és el repositori de git de Doogking i executeu
```
git remote add azure <git_clone_uri>
```
on `git_clone_uri` és l'url que us ha donat l'app service en configurar el deploy.

### Fer el build del frontend
Si el deploy que voleu fer inclou canvis al frontend, aneu al directori frontend i executeu `npm run build` (feu `npm install` abans si és la primera vegada o es queixa de que falta alguna cosa). Això generarà un directori `dist` amb el projecte de vue compilat. Heu d'afegir aquesta carpeta a git:
```
git add dist/
```
Assegureu-vos que s'afegeixi, que per defecte hi ha un .gitignore a frontend que impedeix afegir-la, si cal modifiqueu-lo perquè no inclogui `dist/`.

### Pujanr el deploy a Azure
Si només heu tocat backend, no cal que feu el build del frontend, però si heu modificat el frontend, feu el build i assegureu-vos que s'ha fet l'add de `dist`. Assegureu-vos que esteu a la branca que voleu pujar a azure i feu commit dels canvis.

Per pujar-los a azure només cal fer
```
git push azure <branca_local>:master
```
on `branca_local` és la branca on heu fet els commits i voleu pujar a azure. Això tirarà els canvis de la branca local a la branca master d'azure, que és la única que permet fer deploy. Git us demanarà les credencials, que són les que hem generat durant la secció de configuració de deploy a azure. Amb el mateix output del push Azure us anirà mostrant el procés de deploy i, en cas que hi hagi algun error, el mostrarà per allà.

Si voleu pujar el commit també al repositori de github, feu-ho amb
```
git push origin <branca>
```

### Generant les migracions a Azure (només la primera vegada)
La primera vegada que feu deploy la base de dades serà buida, no hi haurà ni les dades ni l'estructura i no tindreu cap usuari per entrar a la interfície d'administrador de Django. Per fer les migracions, a l'App Service d'Azure, accediu a **Development Tools > SSH** i premeu **Go ->**. AUxò us obrirà una sessió d'SSH amb el server que està servint la web.
Primer s'ha de generar la carpeta de migrations, que no és al git però Django la necessita per fer les migracions. Per fer-ho, des del directori inicial, executeu:
```
mkdir doogkingapp/migrations
touch doogkingapp/migrations/__init__.py
```
Ara ja podem generar les migracions:
```
python manage.py makemigrations
python manage.py migrate
```
Si tot va bé, ara la base de dades ja té l'estructura que necessitem i ara podem crear un administrador:
```
python manage.py createsuperuser
```
Intorduïu email i contrassenya, i amb aquesta conta ja podreu accedir a la interfície d'admin de Django.


I això és tot! Si heu seguit tots aquests passos hauríeu d'acabar amb una web funcionant!
