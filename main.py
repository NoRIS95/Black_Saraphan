from app import app, db
from app.models import Category, Subcategory


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Category': Category, 'Subcategory': Subcategory, 'Product': Product}
