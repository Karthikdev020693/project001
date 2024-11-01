from flask import Blueprint, render_template, request, jsonify
from config.Database import Database
from schema.schema import ArticleSchema
from models.Stockdata import Stocks
import pandas as pd

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return "This is an example home"

@home.route('/blogs')
def get_blogs():

    database = Database()

    articles = database.get_all_record('articles')

    return jsonify(articles)


@home.route('/insert')
def new_collection():

    schema = ArticleSchema()

    data={'title':"01newname","content":"new title", "status":"new content"}

    articles = schema.save('articles',data)

    return jsonify(articles)

@home.route('/stockinfo')
def stock_info():

    stock  = Stocks()

    info = stock.get_stock_info('HDFCBANK.NS')

    return jsonify(info)

@home.route('/stockdata/<symbol>/<int:days>')
def stock_data(symbol, days):

    stock  = Stocks()

    info = stock.get_return_data(symbol, days)

    print(info)

    return jsonify(info)