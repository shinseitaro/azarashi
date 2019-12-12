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


## Frontend setup
※ `frontend` フォルダの直下に **.env** あるいは **.env.local** ファイルが必要です。
```
$ cd frontend
$ npm install
$ npm run serve
```
フロントエンドのローカルサーバー `http://localhost:8080/`

### エラー画面が表示されたら
`npm run lint` を試してください。自動で修正されるかもしれません。


# packages 

```
Django==2.1.11
djangorestframework==3.9.4
djangorestframework-gis==0.14
django-filter==2.0.0
django-cors-headers==3.2.0
```

# issue_44 

https://github.com/shinseitaro/azarashi/issues/44



