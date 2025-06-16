# هذا الملف يُستخدم لإنشاء التطبيق وضبط الإعدادات وتحميل الـ Blueprints
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app