import os
from crypt import methods
from urllib.parse import quote_plus
from flask import Flask, jsonify, abort, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

app=Flask(__name__)

password=quote_plus(os.getenv('db_password'))
host=os.getenv('hostname')
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:{}@{}:5432/library'.format(password,host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # permet de refuser mes warning dans le code sur le serveur flask

db=SQLAlchemy(app)
#CORS(app, resources={r"*/api/*" : {origins: '*'}})
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')

########################################################################################
#
#                                  Classe Categorie
#
########################################################################################

class Categorie(db.Model):
    __tablename__ = 'categories'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False)

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
    isbn = db.Column(db.Integer, nullable=False)
    titre = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    editeur = db.Column(db.String(100), nullable=True)
    id_cat = db.Column(db.Integer, db.ForeignKey(
        'categories.id_cat'), nullable=False)


def format(self):
    return {
        'isbn': self.isbn,
        'id': self.id,
        'nom': self.nom,
        'auteur': self.auteur,
        'date': self.date,
        'editeur': self.editeur,
        'titre': self.titre,
        'id_cat': self.id_cat,
        'libelle': self.libelle
    }
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
#   Endpoint GET /categorie (liste de toutes catégories)liste de toutes les catégories
#
########################################################################################

@app.route('/categories')
def get_all_categorie(): 
    # requete avec SQLAlchemy pour recuperer la liste de tous les étudiants
    categories = Categorie.query.all()
    formated_cat = [cat.format() for cat in categories]

    return jsonify({
        'success' : True,
        'total categories' : len(categories), #Categorie.query.count()
        'categories' : formated_cat
    })

    
########################################################################################
#
#                         Endpoint une catégorie en particulier'
#
########################################################################################

@app.route('/categories/<int:id_cat>')
def get_one_student(id_cat):
    # requete SQLAlchemy pour sélectionner un étudiant
    cat = Categorie.query.get(id_cat)

    # On vérifie si la catégorie existe
    if cat is None:
        abort(404) # 404 est le status code pour dire que la ressource n'existe pas
    # Si la catégorie existe alors on le retourne
    else:
        return jsonify({
            'success' : True,
            'selected_id' : id,
            'categorie' : cat.format()
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
    new_libel = body.get('libelle', None)

    cat = Categorie(libelle=new_libel)
    cat.insert()

    return jsonify({
        'success' : True,
        'total etudiants' : Categorie.query.count(),
        'etudiants' : [ct.format() for ct in Categorie.query.all()]
    })


########################################################################################
#
#                         Endpoint supprimer un étudiant
#
########################################################################################
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_categorie(id):
    cat = Categorie.query.get(id)

    if cat is None:
        abort(404)
    else:
        cat.delete()
        return jsonify({
            'success' : True,
            'id_cat' : id,
            'etudiant' : cat.format(),
            'total_categories' : Categorie.query.count()
        })



########################################################################################
#
#                         Endpoint modifier un étudiant
#
########################################################################################
@app.route('/categories/<int:id>', methods=['PATCH'])
def update_categorie(id):
    # recupération de l'etudiant à modifier
    cat = Categorie.query.get(id)
    
    if student is None:
        abort(404)
    else:

        # recupération des informations qui seront envoyées dans un format json et modification de l'étudiant
        body = request.get_json()
        cat.libelle = body.get('libelle', None)

        cat.update()

        return jsonify({
            'success' : True,
            'updated_id' : id,
            'categorie' : cat.format()
        })



@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 404,
        "message" : "Not Found"
    }), 404

@app.errorhandler(500)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 500,
        "message" : "Internal Server Error"
    }), 500


@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 400,
        "message" : "Bad Request"
    }), 400


@app.errorhandler(403)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 403,
        "message" : "Not Allowed"
    }), 403