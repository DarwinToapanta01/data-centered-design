from flask import Flask
from config.configuracion import Configuracion

from models import db
from models.autor import Autor
from models.paper import Paper

from routes.autor import autor_bp
from routes.paper import paper_bp

def iniciar_app(configuracion=Configuracion):
    app = Flask(__name__)
    app.config.from_object(configuracion)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(autor_bp)
    app.register_blueprint(paper_bp)
    
    return app

if __name__ == '__main__':
    app = iniciar_app()
    app.run(debug=True, port=500)
    