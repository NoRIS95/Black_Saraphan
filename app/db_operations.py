from flask import Flask, redirect, request
import os
from PIL import Image
from app.models import Category, Subcategory, Product
from flask import jsonify
from dotenv import load_dotenv
from app import db
import os
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")
PER_PAGE_LIMIT = 100

def check_token(user_token):
    return user_token == ADMIN_TOKEN
        

def authorize(check_token_func=check_token):
    # import pdb; pdb.set_trace()
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kws):
            api_token = request.headers.get('Admin_token')
            is_valid_api_token = check_token_func(api_token)
            if is_valid_api_token:
                return f(*args, **kws)

            return 'Invalid API Token', 401

        return decorated_function

    return decorator

"""Methods for categories"""
    
def get_categories():
    per_page = int(request.args.get('per_page', PER_PAGE_LIMIT))
    page = int(request.args.get('page', 1))
    if per_page > PER_PAGE_LIMIT or per_page < 1:
        return f"per_page must be <= {PER_PAGE_LIMIT} and >= 1", 403
    # if page < 1:
    #     return "page must be >= 1", 403        
    categories = Category.query.order_by(Category.id).paginate(page=page, per_page=per_page).items
    return jsonify(result = [x.serialize() for x in categories], success=True)


def add_category():
    name = request.args.get('name')    
    slug_name = request.args.get('slug_name')   
    category = Category(name=name, slug_name=slug_name)
    img = Image.open(request.files['image'])
    db.session.add(category)
    db.session.commit()
    db.session.flush()
    db.session.refresh(category)
    img.save(os.path.join(basedir, f'static/category_photo/{category.id}.jpeg'))
    return jsonify(success=True)

            
            
def delete_category():
    # name = request.args.get('name')  
    category_id = request.args.get('id')
    category = Category.query.filter_by(id=category_id).first()
    location = 'home/ivan/PycharmProjects/Black_Saraphan/app/static/category_photo'
    path = os.path.join(basedir, f'static/category_photo/{category.id}.jpeg')
    os.remove(path)
    # data = Categories(name, slug_name) 
    db.session.delete(category)
    db.session.commit()    
    return jsonify(success=True)



def edit_category():
    delete_category()
    add_category()
    return jsonify(success=True)


"""Methods for SUBcategories"""

def get_subcategory():
    per_page = int(request.args.get('per_page', PER_PAGE_LIMIT))
    page = int(request.args.get('page', 1))
    if per_page > PER_PAGE_LIMIT or per_page < 1:
        return f"per_page must be <= {PER_PAGE_LIMIT} and >= 1", 403
    subcategories = Subcategory.query.order_by(Subcategory.id).paginate(page=page, per_page=per_page).items
    return jsonify(result = [x.serialize() for x in subcategories], success=True)

def add_subcategory():
    category_id = request.args.get('category_id')     
    name = request.args.get('name')
    slug_name = request.args.get('slug_name')             
    subcategory = Subcategory(category_id=category_id, name=name, slug_name=slug_name)
    img = Image.open(request.files['image'])
    db.session.add(subcategory)
    db.session.commit()
    db.session.flush()
    db.session.refresh(subcategory)
    img.save(os.path.join(basedir, f'static/subcategory_photo/{subcategory.id}.jpeg'))
    return jsonify(success=True)


def delete_subcategory():
    subcategory_id = request.args.get('id')
    subcategory = Subcategory.query.filter_by(id=subcategory_id).first()
    path = os.path.join(basedir, f'static/subcategory_photo/{subcategory.id}.jpeg')
    os.remove(path)  
    db.session.delete(subcategory)
    db.session.commit()
    return jsonify(success=True)

def edit_subcategory():
    delete_subcategory()
    add_subcategory()
    return jsonify(success=True)


"""Methods for products"""
def get_products():
    per_page = int(request.args.get('per_page', PER_PAGE_LIMIT))
    page = int(request.args.get('page', 1))
    if per_page > PER_PAGE_LIMIT or per_page < 1:
        return f"per_page must be <= {PER_PAGE_LIMIT} and >= 1", 403
    # if page < 1:
    #     return "page must be >= 1", 403        
    products = Product.query.order_by(Product.id).paginate(page=page, per_page=per_page).items
    return jsonify(result = [x.serialize() for x in products], success=True)


def add_product():
    subcategory_id = request.args.get("subcategory_id")
    name = request.args.get("name")
    slug_name = request.args.get("slug_name")
    product = Product(subcategory_id=subcategory_id, name=name, slug_name=slug_name)
    db.session.add(product)
    db.session.commit()
    db.session.flush()
    db.session.refresh(product)
    for img_size in ['small', 'medium', 'large']:
        img = Image.open(request.files['image_'+img_size])
        img.save(os.path.join(basedir, f'static/product_photo/{product.id}_{img_size}.jpeg'))  
    return jsonify(success=True)


def delete_product():    
    product_id = request.args.get('id')
    product = Product.query.filter_by(id=product_id).first()
    import pdb; pdb.set_trace
    for img_size in ['small', 'medium', 'large']:
        path = os.path.join(basedir, f'static/product_photo/{product.id}_{img_size}.jpeg')
        os.remove(path)
    db.session.delete(product)
    db.session.commit()
    return jsonify(success=True)



def edit_product():
    delete_product()
    add_product()
    return jsonify(success=True)







