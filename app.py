from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from db.service_db import mysql_connect
# from finance_app import executor, dp
import finance_app


app = Flask(__name__)

# Подключение к базе данных
# app.config['SQLALCHEMY_DATABASE_URI'] = mysql_connect 
# db = SQLAlchemy(app)


finance_app.start_bot()



if __name__=='__main__':
    app.run()