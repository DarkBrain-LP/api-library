from enum import unique
from multiprocessing.spawn import old_main_modules
import os
from crypt import methods
from urllib.parse import quote_plus
from flask import Flask, jsonify, abort, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)

password = quote_plus(os.getenv('db_password'))
host = os.getenv('hostname')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@{}:5432/library'.format(
    password, host)
# permet de refuser mes warning dans le code sur le serveur flask
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#CORS(app, resources={r"*/api/*" : {origins: '*'}})
CORS(app)

"""
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PATCH, DELETE, OPTIONS')

"""
########################################################################################
#
#                                  Classe Categorie
#
########################################################################################


class Categorie(db.Model):
    __tablename__ = 'categories'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False, unique=True)

    def format(self):
        return {
            'id_cat': self.id_cat,
            'libelle': self.libelle
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


########################################################################################
#
#                                  Classe Livre
#
########################################################################################
class Livre(db.Model):
    __tablename__ = 'livres'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    isbn = db.Column(db.String(15), unique=True)
    titre = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    editeur = db.Column(db.String(100), nullable=True)
    id_cat = db.Column(db.Integer, db.ForeignKey(
        'categories.id_cat'), nullable=False)

    def format(self):
        return {
            'isbn': self.isbn,
            'id': self.id,
            'auteur': self.auteur,
            'date': self.date,
            'editeur': self.editeur,
            'titre': self.titre,
            'id_cat': self.id_cat
        }

    def __eq__(self, other): 
        if not isinstance(other, Livre):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id and self.isbn == other.isbn and self.auteur==other.auteur and self.date==other.date and self.editeur==other.auteur and self.titre==other.titre and self.id_cat==other.id_cat

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


db.create_all()

'''
Les endpoints de l'API

GET /categorie (liste de toutes catégories)
GET /categorie/id (sélectionner une catégorie en particulier)
POST /categorie (créer une nouvelle catégorie)
PATCH /categorie/id (Modifier une catégorie)
DELETE /categorie/id (Supprimer une catégorie)

GET /livres (liste de tous les livres)
GET /livres/id (sélectionner un livre en particulier)
GET /categories/id/livres (liste des livre d'une catégorie donnée)
DELETE /livres/id (supprimer un livre)
PATCH /livres/id (modifier les informations d'un livre)

'''

########################################################################################
#
#   Endpoint GET /categories (liste de toutes catégories)liste de toutes les catégories
#
########################################################################################


@app.route('/categories')
def get_all_categories():

    return jsonify({
        'success': True,
        'total categories': Categorie.query.count(),
        'categories': [cat.format() for cat in Categorie.query.all()]
    })


########################################################################################
#
#                         Endpoint une catégorie en particulier'
#
########################################################################################

@app.route('/categories/<int:id_cat>')
def get_one_categorie(id_cat):
    # requete SQLAlchemy pour sélectionner une catégorie
    cat = Categorie.query.get(id_cat)

    # On vérifie si la catégorie existe
    if cat is None:
        abort(404)  # 404 est le status code pour dire que la ressource n'existe pas
    # Si la catégorie existe alors on le retourne
    else:
        return jsonify({
            'success': True,
            'selected_id': id_cat,
            'categorie': cat.format()
        })


########################################################################################
#
#                         Endpoint ajouter une catégorie
#
########################################################################################
@app.route('/categories', methods=['POST'])
def create_categorie():
    # recupération des informations qui seront envoyées dans un format json
    body = request.get_json()
    new_libel = body.get('libelle')

    cat = Categorie(libelle=new_libel)
    cat.insert()

    return jsonify({
        'success': True,
        'total categories': Categorie.query.count(),
        'categories': [ct.format() for ct in Categorie.query.all()]
    })

########################################################################################
#
#                         Endpoint supprimer une categorie
#
########################################################################################


@app.route('/categories/<int:id_cat>', methods=['DELETE'])
def delete_categorie(id_cat):
    cat = Categorie.query.get(id_cat)

    if cat is None:
        abort(404)
    else:
        cat.delete()

        return jsonify({
            'success': True,
            'deleted id': id_cat,
            'deleted categorie': cat.format(),
            'total categories': Categorie.query.count()
        })


########################################################################################
#
#                         Endpoint modifier une categorie
#
########################################################################################
@app.route('/categories/<int:id_cat>', methods=['PATCH'])
def update_categorie(id_cat):
    # recupération de la categorie à modifier
    cat = Categorie.query.get(id_cat)

    if cat is None:
        abort(404)
    else:

        old_cat = Categorie(id_cat=cat.id_cat, libelle=cat.libelle)
        # recupération des informations qui seront envoyées dans un format json et modification de l'étudiant
        body = request.get_json()
        cat.libelle = body.get('libelle', None)

        cat.update()

        return jsonify({
            'success': True,
            'before updated' : old_cat.format(),
            'after updated': cat.format()
        })


"""
GET /livres (liste de tous les livres)
GET /livres/id (sélectionner un livre en particulier)
GET /categories/id/livres (liste des livre d'une catégorie donnée)
DELETE /livres/id (supprimer un livre)
PATCH /livres/id (modifier les informations d'un livre)

"""

########################################################################################
#
#                       Endpoint GET /livres (liste de tous les livres)
#
########################################################################################


@app.route('/livres')
def get_all_livres():

    return jsonify({
        'success': True,
        'total livres': Livre.query.count(),
        'livres': [lv.format() for lv in Livre.query.all()]
    })


########################################################################################
#
#                  GET /livres/id (sélectionner un livre en particulier)
#
########################################################################################

@app.route('/livres/<int:id>')
def get_one_livre(id):
    # requete SQLAlchemy pour sélectionner un livre
    book = Livre.query.get(id)

    # On vérifie si le livre existe
    if book is None:
        abort(404)  # 404 est le status code pour dire que la ressource n'existe pas
    # Si le livre existe alors on le retourne
    else:
        return jsonify({
            'success': True,
            'selected id': id,
            'livre': book.format()
        })


########################################################################################
#
#                         Endpoint ajouter un livre
#
########################################################################################
@app.route('/livres', methods=['POST'])
def create_livre():
    # recupération des informations qui seront envoyées dans un format json
    body = request.get_json()

    book = Livre(
        isbn=body.get('isbn'),
        titre=body.get('titre', None),
        date=body.get('date', None),
        auteur=body.get('auteur', None),
        editeur=body.get('editeur', None),
        id_cat=body.get('id_cat', None)
    )

    book.insert()

    return jsonify({
        'success': True,
        'total livres': Livre.query.count(),
        'livres': [bk.format() for bk in Livre.query.all()]
    })

########################################################################################
#
#                         DELETE /livres/id (supprimer un livre)
#
########################################################################################


@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_livre(id):
    book = Livre.query.get(id)

    if book is None:
        abort(404)
    else:
        book.delete()

        return jsonify({
            'success': True,
            'deleted id': id,
            'deleted livre': book.format(),
            'total livre': Livre.query.count()
        })


########################################################################################
#
#               PATCH /livres/id (modifier les informations d'un livre)
#
########################################################################################
@app.route('/livres/<int:id>', methods=['PATCH'])
def update_livre(id):
    # recupération de la categorie à modifier
    book = Livre.query.get(id)

    if book is None:
        abort(404)
    else:
        # sauvegarde de l'ancienne version
        old_book = Livre(id=book.id, isbn=book.isbn, titre=book.titre, 
                    date=book.date, auteur=book.auteur, editeur=book.editeur,
                    id_cat=book.id_cat)

        # recupération des informations qui seront envoyées dans un format json et modification de l'étudiant
        body = request.get_json()
        book.isbn = body.get('isbn',old_book.isbn)
        book.titre = body.get('titre', old_book.titre)
        book.date = body.get('date', old_book.date)
        book.auteur = body.get('auteur', old_book.auteur)
        book.editeur = body.get('editeur', old_book.editeur)
        book.id_cat = body.get('id_cat', old_book.id_cat)

        if book == old_book:
            abort(400)
        else:
            book.update()

            return jsonify({
                'success': True,
                'before updated': old_book.format(),
                'after updated' : book.format()
            })

########################################################################################
#
#     GET /categories/id/livres (liste des livre d'une catégorie donnée)
#
########################################################################################


@app.route('/categories/<int:id_cat>/livres')
def get_livres_categorie(id_cat):
    books = Livre.query.filter_by(id_cat=id_cat)

    return jsonify({
        'success': True,
        'selected categorie': id_cat,
        'livres': [book.format() for book in books]
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404


@app.errorhandler(500)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500


@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@app.errorhandler(403)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Not Allowed"
    }), 403

@app.errorhandler(503)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 503,
        "message": "Service unavailable"
    }), 503
