import os
# set secret key to protect
# import secrets
# secrets.token_hex(16)
class Config:
    SECRET_KEY = 'd5b8c8da164d522c534c5b4ed21098e4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_use_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')