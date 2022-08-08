from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from db.service_db import mysql_connect
from finance_app import executor, dp

app = Flask(__name__)

# Подключение к базе данных
# app.config['SQLALCHEMY_DATABASE_URI'] = mysql_connect 
# db = SQLAlchemy(app)


executor.start_polling(dp, skip_updates=True)

if __name__=='__main__':
    app.run()