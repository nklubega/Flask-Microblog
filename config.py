import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'admin123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/nabill/Desktop/microblog/app.db'
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(base_dir, "app/translations")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['nklubega@gmail.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']
