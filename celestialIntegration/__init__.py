import os
from flask import Flask
# INF601 - Advanced Programming in Python
# Jacob Richmond
# Mini Project 3
'''so you'll see celestailIntegration all over this project. This was originally 
going to be for another project, but I diverted at the last second, and instead of doing 
a mad copy-paste, I figured that Ill make sure the repository is correctly named and that the 
project works correctly.'''
#DONE(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#DONE(5/5 points) Proper import of packages used.
#DONE(70/70 points) Using Flask you need to setup the following:
#DONE(10/10 points) Setup a proper folder structure, use the tutorial as an example.
#DONE(20/20 points) You need to have a minimum of 5 pages, using a proper template structure.
#DONE(10/10 points) You need to have at least one page that utilizes a form and has the proper GET and POST routes setup.
#DONE(10/10 points) You need to setup a SQLlite database with a minimum of two tables, linked with a foreign key.
#DONE(10/10) You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but
# the more practice here the better. You need to at least make use of a modal.
#DONE(10/10) You need to setup some sort of register and login system, you can use the tutorial as an example.
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'celestialIntegration.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app