import pymysql.cursors

from peewee import *
from flask import Flask
from routers import app

if __name__ == '__main__':

    # Загрузка стандартных настроек
    app.config.from_object(__name__)
    app.debug = True
    app.run()

