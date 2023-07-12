from app import db
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# #app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'  заменить на другую строчку  
# app.comfig['SQLALCHEMY_TRACK_MODIFICATIONS']=False


# db = SQLAlchemy(app)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    slug_name = db.Column(db.String(50), unique=True)

    def __init__(self, id, name, slug_name):
        self.id = id
        self.name = name
        self.slug_name = slug_name

    @property
    def serialize(self):
        return {
           'id'         : self.id,
           'name_category': self.name,
           'slug_name'  : self.slug_name
      }

    def __repr__(self):
        return f'<categories {self/id}>'


class Subcategories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    slug_name = db.Column(db.String)
    category_name= db.Column(db.String(50), db.ForeignKey(Categories.id))

    def __init__(self, id, name, slug_name, category_name):
        self.id = id
        self.name = name
        self.slug_name = slug_name
        self.category_name = category_name

    @property
    def serialize(self):
        return {
           'id'         : self.id,
           'name_subcategory': self.name,
           'slug_name'  : self.slug_name,
           'category_name'  : self.category_name
       }

    #  @staticmethod
    # def slugify(target, value, oldvalue, initiator):
    #     if value and (not target.slug or value != oldvalue):
    #         target.slug = slugify(value)

    def __repr__(self):
        return f'<subcategories {self.id}>'




