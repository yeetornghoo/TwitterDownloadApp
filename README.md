# How to consume
### Consume the library
- Add `git+https://git@github.com/yeetornghoo/TwitterDownloadApp.git@0.0.2#egg=TwitterDownloadApp` to you requirements.txt
- Or can run `pip install git+https://git@github.com/yeetornghoo/TwitterDownloadApp.git@0.0.2#egg=TwitterDownloadApp`
### Setup MongoDS
- Add Mongo DB configuration file `config/db_config.ini`
- Add following items to the file
```
MONGO_DB_CONNECTION_STRING=mongodb://localhost:27017
MONGO_DB_NAME=political_data_analysis
```

# Development
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

