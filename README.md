# azarashi


# How to setup dev env 
### Step1. Makemigrations
`python manage.py makemigrations --settings config.settings.development`
### Step2. Migrate
`python manage.py migrate --settings config.settings.development`

### Step3. データの読み込み
`python manage.py loaddata --settings config.settings.development`

### Step4. Createsuperuser
`python manage.py createsuperuser --settings config.settings.development`


### Step5. Runserver
`python manage.py runserver 8000 --settings config.settings.development`
