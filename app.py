from flask import Flask
from flask_restful import Api
from resources.conjunto import ListaConjuntos, ListaConjunto, Limite


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ListaConjuntos, "/")
    api.add_resource(ListaConjunto, "/id/<num_id>")
    api.add_resource(Limite, "/limit/<limit>")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
