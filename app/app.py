from flask import Flask, redirect, url_for, request
import os
from PIL import Image
from models import Categories, Subcategories
from flask import jsonify

# app = Flask(__name__)

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return '<h1>Hello, World!</h1>'



PER_PAGE_LIMIT = 100


ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")


@app.route('/all_subcategories/<int:page>',methods=['GET'])
def get_subcategories(request):
    if request.args.per_page > PER_PAGE_LIMIT:
        return f"per_page must be <= {PER_PAGE_LIMIT}", 403
    subcategories = Subategories.query.order_by(Subcategories.id).paginate(request.args.page, request.args.per_page)
    return jsonify(json_list = subcategories)



@app.route('/all_categories/<int:page>',methods=['GET'])
def get_categories():
    if request.args.per_page > PER_PAGE_LIMIT:
        return f"per_page mest be <= {PER_PAGE_LIMIT}", 403 
    categories = Categories.query.order_by(Categories.id).paginate(request.args.page, request.args.per_page)
    return jsonify(json_list = categories)
    ###какой return тут сделать




def check_token(user_token):
    return user_token == ADMIN_TOKEN
        
def authorize(check_token_func=check_token):
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
    

def add_category(request):
    pass
    name = request.args.get('name')         
    slug_name = request.args.get('slug_name')   
    data = Categories(name, slug_name) 
    img = Image.open(request.files['image_small'])
    img.save('web/static/categories/1_small.jpeg')
    db.session.add(data)
    db.session.commit()
        # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))

            # category = request.args.get('category')
            # categories[category] = {}
            # return "Категория успешно добавлена"
            
            
def delete_category(request):
    pass
    name = request.args.get('name')  
    slug_name = request.args.get('slug_name')              #Нужно как-то сделать проверку на наличие КАтегории
    data = Categories(name, slug_name) 
    db.session.delete(data)
    db.session.commit()    
    # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))     

    # if request.args.get('category') not in categories:
            #   return "Категория отсутствует"
            # categories.pop(request.args.get('category'))
            # return "Категория успешно удалена"

def rename_category(request):
    pass
    slug_name = request.args.get('slug_name')            
    data = Categories(name, slug_name) 
    db.session.add(data)
    db.session.commit()
    # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))


            # if request.args.get('category') not in categories:
            #   return "Категорию невозможно переименовать, т.к. она отсутствует"
            # categories[request.args.get('category')] = request.args.get('new_name_category')
            # return "Название категории успешно изменено"
            


#В одном терминале развернуть клиента, в другом сервер, в третьем открыть Flask Shell.


def add_subcategory(request):
    name_category = request.args.get('category_name')     #Нужно как-то сделать проверку на наличие КАтегории
    name = request.args.get('name')
    slug_name = request.args.get('slug_name')              ###КАК ТУТ ПРАВИЛЬНО?
    data = Subcategories(name_category, name, slug_name) 
    db.session.add(data)
    db.session.commit()
    img = Image.open(request.files['image_small'])
    img.save('web/static/subcategories/<category_slug>/<subcategory_slug>_small.jpeg') 



    # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))



            # img_small = Image.open(request.files['image_small'])
            # img_medium = Image.open(request.files['image_medium'])
            # img_large = Image.open(request.files['image_large'])
            # name_small = "Black_Saraphan/static/subcategories/" + str(Subcategory.slug_name) + "image_small.jpeg"
            # name_medium = "Black_Saraphan/static/subcategories/" + str(Subcategory.slug_name) + "image_medium.jpeg"
            # name_large = "Black_Saraphan/static/subcategories/" + str(Subcategory.slug_name) + "image_large.jpeg"
            # img_small.save('Black_Saraphan/static/subcategories/1_small.jpeg')
            # img_medium.save('Black_Saraphan/static/subcategories/1_medium.jpeg')
            # img_large.save('Black_Saraphan/static/subcategories/1_large.jpeg')



            # if request.args.get('category') not in categories:              ###Как ввести категорию пользователю
            #   return "Подкатегория не добавлена, т.к. отсутствует категория, которыю Вы указали. Выберите другую категорию или добавьте категорию"
            # category = categories[request.args.get('category')] 
            # categories[request.args.get('category')][request.args.get('subcategory')] = []
            # return "Подкатегория успешно добавлена"

def delete_subcategory(request):
    name_category = request.args.get('category_name')           #Нужно как-то сделать проверку на наличие КАтегории
    name = request.args.get('name')
    slug_name = request.args.get('slug_name')          
    data = Subcategories(name_category, name, slug_name) 
    db.session.delete(data)
    db.session.commit()
    # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))


            # category_slack = request.args.get('category') #посмотреть, как пишется слак имя       
            # if category not in categories:
            #   return "Категория отсутствует"
            # if request.args.get('subcategory') not in categories[category]:
            #   return "Отсутствует подкатегория"
            # subcategory = categories[category]   ###Не похожа ли эта строчка на затыкивание дырки?                           #ПОМЕНЯТЬ ВСЁ!!!!!!!!!!!!!!!!!
            # categories[category].pop(request.args.get('subcategory'))
            # return "Категория успешно удалена"

def rename_subcategory(request):
    name_category = request.args.get('category_name')           #Нужно как-то сделать проверку на наличие КАтегории
    name = request.args.get('name')
    slug_name = request.args.get('slug_name')          
    data = Subcategories(name_category, name, slug_name) 
    db.session.add(data)
    db.session.commit()
    # По-хорошему здесь должна выводиться страничка (что-то вроде строчки return render_template("create.html"))



            # category = request.args.get('category')
            # if categories[request.args.get('category')] not in categories[category]:
            #   return "Подкатегорию невозможно переименовать, т.к. она отсутствует. Или неправильно введено название категории."
            # category = categories[category]
            # category[request.args.get('subcategory')] = request.args.get('new_name_category')
            # return "Название подкатегории успешно изменено"






@app.route("/categories", methods=['POST', "PUT", "DELETE"])
@authorize
def categories():
    if request.method == "POST":
        adding = add_category(request)
    elif request.method == "DELETE":
        deleting = delete_category(request)
    elif request.method == "PUT":
        renaming = rename_category(request)
    elif request.method == "GET":
        all_categories = get_categories(request)





@app.route("/subcategories", methods=['POST', "PUT", "DELETE"])
@authorize
def subcategories():
    if request.method == "POST":
        adding = add_subcategory(request)
    elif request.method == "DELETE":
        deleting = delete_subcategory(request)
    elif request.method == "PUT":
        renaming = rename_category(request)
    elif request.method == "GET":
        all_subcategories = get_categories(request)
    
if __name__ = '__main__':
    app.run(debug=True)