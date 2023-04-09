"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)   
app.config.from_pyfile("settings.ini")

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import routes """

"""
İlk olarak Flask, Flask SQLAlchemy ve Flask Marshmallow modüllerini projemize dahil ediyoruz. 

`app = Flask(__name__)` bu satırdaki kod, Flask uygulamamızı oluşturmamızı sağlar. 

`app.config.from_pyfile("settings.ini")` satırı, projemizin ayarlarının yer aldığı "settings.ini" dosyasındaki yapılandırma ayarlarını projemize yüklüyor. 

`db = SQLAlchemy(app)` satırı, SQLAlchemy veritabanı işlemleri için projemizi hazırlıyor.

`ma = Marshmallow(app)` satırı, Marshmallow modülünü kullanarak JSON verileri dönüştüreceğimiz için projemizi hazırlıyoruz.

En son satırda, `routes` modülünü projemize dahil ediyoruz. Bu modülde REST API endpointlerimizi tanımlayacağız.

"""



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['JWT_SECRET_KEY'] = 'secret-key'

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    from app import routes

    return app