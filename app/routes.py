from flask import Flask, request
from app import app
from app.db_operations import *


@app.route("/categories", methods=['GET', 'POST', "PUT", "DELETE"])
def categories():
    callbacks = {"POST":add_category, "DELETE":delete_category, 'PUT': edit_category, "GET": get_categories}
    fn = callbacks[request.method]
    response = fn()
    return response




@app.route("/subcategories", methods=['GET', 'POST', "PUT", "DELETE"])
def subcategories():
    callbacks = {"POST":add_subcategory, "GET": get_subcategory, "PUT":edit_subcategory, "DELETE": delete_subcategory}
    fn = callbacks[request.method]
    response = fn()
    return response


@app.route("/products", methods=['GET', 'POST', "PUT", "DELETE"])
def products():
    callbacks = {'POST':add_product, "GET":get_products, "PUT":edit_product, "DELETE": delete_product}
    fn = callbacks[request.method]
    response = fn()
    return response