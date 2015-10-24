"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

db.session.query(Model).filter(Model.year < 1960).all()

### QUESTION: I got this error:
#   Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 38: ordinal not in range(128)
#   Is this because of Citroen? How do I fix this?


# Get all brands that were founded after 1920.

db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.

db.session.query(Brand).filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()


###QUESTION: Got same error here with the unicode character

# Get any model whose brand_name is not Chevrolet.

db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model).filter_by(year=year).all()

    for model in model_info:
        print "Model: {}, brand_name: {}, headquarters: {}".format(model.name, model.brand_name, model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_info = db.session.query(Brand).all()

    for brand in brand_info:
        print "{}: ".format(brand.name)
        models = brand.model
        for model in models:
            print "Model: {}".format(model.name)
        print "-------------"




# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
