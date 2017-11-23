# SMS REST API
API for disponibilizate the informations and indicators the SMS

**This API is developed in Flask**

#### Install dependencies
```
pip install -r requirements.txt
```

#### Start API
```
gunicorn -c gunicorn.conf.py run:app
```

Default start mode is Development

##### Start production mode
```
gunicorn --env FLASK_CONFIG='Production'  -c gunicorn.conf.py run:app
```

> The env variable FLASK_CONFIG set flask_app.config.from_object

#### Config

Config host and port the server **gunicorn.conf.py**

Config Flask **settings.py**

### Documentation
[Documentação no swagger](https://app.swaggerhub.com/apis/jefersonpassos/sms/1.1.0#/)

