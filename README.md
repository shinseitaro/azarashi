# azarashi


# How to setup dev env 
### Step1. Makemigrations
`python manage.py makemigrations --settings config.settings.development`
### Step2. Migrate
`python manage.py migrate --settings config.settings.development`

### Step3. データの読み込み
`python manage.py shell --settings config.settings.development`

shellに入って,

`>>from utils.data_loader import run`

`>>run()`

### Step4. Createsuperuser
`python manage.py createsuperuser --settings config.settings.development`


### Step5. Runserver
`python manage.py runserver 8000 --settings config.settings.development`


# packages 

```
Django==2.1.11
djangorestframework==3.9.4
djangorestframework-gis==0.14
django-filter==2.0.0
```