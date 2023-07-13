from app import db
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(50), unique=True)
    slug_name = db.Column(db.String(50), unique=True)

    def serialize(self):
        return {
           'id'         : self.id,
           'name_category': self.name,
           'slug_name'  : self.slug_name
      }

    def __repr__(self):
        return f'Category {self.id}-"{self.name}"-{self.slug_name}'


class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(50), unique=True)
    slug_name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))

    def serialize(self):
        return {
           'id'         : self.id,
           'name_subcategory': self.name,
           'slug_name'  : self.slug_name,
           'category_id'  : self.category_id
       }

    def __repr__(self):
        return f'Subcategory {self.id}-"{self.name}"-{self.category_id}-{self.slug_name}'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    name = db.Column(db.String(50), unique=True)
    slug_name = db.Column(db.String(50), unique=True)
    subcategory_id = db.Column(db.Integer, db.ForeignKey(Subcategory.id))

    def serialize(self):
        return {
        'id'              : self.id,
        'name_product': self.name,
        'slug_name'   : self.slug_name,
        'subcategory_id' : self.subcategory_id
        }

    def __repr__(self):
        return f'Product {self.id}-"{self.name}"-{self.subcategory_id}-{self.slug_name}'




