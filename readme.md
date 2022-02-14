# API LIBRARY

## Getting Started

### Installing Dependencies

#### Python 3.8.10
#### pip 22.0.3 from /usr/lib/python3/dist-packages/pip (python 3.8)

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Environment variable file

You must install the dotenv package with the command:
pip install python-dotenv

- Create your own .env file
- In the .env file, create the variable :
    . db_password that is your database password 
    . hostname that is the host of your api

#### PIP Dependencies

Install dependencies by running:

```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the plants_database.sql file provided. From the backend folder in terminal run:
```bash
psql plants_database < plants_database.sql
```

## Running the server

From within the `plants_api` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request"
}

The API will return four error types when requests fail:
. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found
. 403: Forbiden

## Endpoints
. ## GET/categories

    GENERAL:
        This endpoints returns a list of categorie object, success value, total number of the categorie. 
    
        
    SAMPLE: curl http://localhost:5000/categories

    {
    "categories": [
        {
            "id_cat": 1,
            "libelle": "Policiere"
        },
        {
            "id_cat": 4,
            "libelle": "Romanciere"
        },
        {
            "id_cat": 5,
            "libelle": "Scientifique"
        },
        {
            "id_cat": 6,
            "libelle": "Psychologique"
        },
        {
            "id_cat": 7,
            "libelle": "Médécine"
        },
        {
            "id_cat": 8,
            "libelle": "Informatique"
        },
        {
            "id_cat": 9,
            "libelle": "Business"
        },
        {
            "id_cat": 10,
            "libelle": "Politique"
        },
        {
            "id_cat": 11,
            "libelle": "Football"
        },
        {
            "id_cat": 2,
            "libelle": "Animale"
        }
    ],
    "success": true,
    "total categories": 10
}
```


. ## GET /categories (categorie_id)

    GENERAL:
        Select the categorie of the given ID if it exists. Return the categorie, the id of the selected categorie, success value

        SAMPLE: curl -X DELETE http://localhost:5000/livres/8
```
        {
            "categorie": {
                "id_cat": 8,
                "libelle": "Informatique"
            },
            "selected_id": 8,
            "success": true
        }
```

. ## DELETE /categories (categorie_id)

    GENERAL:
        Delete the categorie of the given ID if it exists. Return the categorie, the id of the deleted categorie, success value, total of categorie

        SAMPLE: curl -X DELETE http://localhost:5000/categories/10
```
        {
            "deleted categorie": {
                "id_cat": 10,
                "libelle": "Politique"
            },
            "deleted id": 10,
            "success": true,
            "total categories": 9
        }
```
. ## PATCH /categories/(categorie_id)
  GENERAL:
  This endpoint is used to update a categorie
  It returns categorie after updated, before updated and success status that should be true

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/categories/1 -H "Content-Type:application/json" -d "{ "libelle" : "Litterature" }"
  ```
  ```
    {
        "after updated": {
            "id_cat": 1,
            "libelle": "Litterature"
        },
        "before updated": {
            "id_cat": 1,
            "libelle": "Policiere"
        },
        "success": true
    }
    ```

. ## POST /categories

    GENERAL:    
    This endpoint is used to create a new categorie 
    We return the ID of the new categorie created, the categorie that was created, the list of categorie and the number of categorie.

    SAMPLE.....:
    ```
    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"libelle" : "Gastronomie"}"
    ```
    ```
        {
            "categories": [
                {
                    "id_cat": 4,
                    "libelle": "Romanciere"
                },
                {
                    "id_cat": 5,
                    "libelle": "Scientifique"
                },
                {
                    "id_cat": 6,
                    "libelle": "Psychologique"
                },
                {
                    "id_cat": 7,
                    "libelle": "Médécine"
                },
                {
                    "id_cat": 8,
                    "libelle": "Informatique"
                },
                {
                    "id_cat": 9,
                    "libelle": "Business"
                },
                {
                    "id_cat": 11,
                    "libelle": "Football"
                },
                {
                    "id_cat": 2,
                    "libelle": "Animale"
                },
                {
                    "id_cat": 1,
                    "libelle": "Litterature"
                },
                {
                    "id_cat": 12,
                    "libelle": "Gastronomie"
                }
            ],
            "success": true,
            "total categories": 10
        }
    ```      

. ## GET /livres

    GENERAL:
        This endpoints returns a list of livre object, success value, total number of the livre. 
    
        
    SAMPLE: curl http://localhost:5000/livres

    {
    "livres": [
        {
            "auteur": "Stephen hawking",
            "date": "Sun, 05 May 2019 00:00:00 GMT",
            "editeur": "Philippe Goutiers",
            "id": 3,
            "id_cat": 7,
            "isbn": "123-10-1",
            "titre": "Une merveilleuse histoire du temps"
        },
        {
            "auteur": "Le Phoulosophe",
            "date": "Mon, 10 Oct 2022 00:00:00 GMT",
            "editeur": "Espoir LeCharpentier",
            "id": 4,
            "id_cat": 11,
            "isbn": "010-11-10",
            "titre": "100 Raisons de vivre"
        },
        {
            "auteur": "Jean Dupond",
            "date": "Thu, 12 Oct 2017 00:00:00 GMT",
            "editeur": "Jeanette DuBridge",
            "id": 2,
            "id_cat": 8,
            "isbn": "978-3-16-1",
            "titre": "Hands on machine learning with scikit learn v2"
        },
        {
            "auteur": "Jean Dupond",
            "date": "Thu, 12 Oct 2017 00:00:00 GMT",
            "editeur": "Jean DuBridge",
            "id": 1,
            "id_cat": 8,
            "isbn": "978-3-16",
            "titre": "Hands on machine learning with scikit learn"
        }
    ],
    "success": true,
    "total livres": 4
}
```

. ## GET /livres (livre_id)

    GENERAL:
        Select the livre of the given ID if it exists. Return the livre, the id of the selected livre, success value, total of livre

        SAMPLE: curl -X DELETE http://localhost:5000/livres/4
```
        {
            "livre": {
                "auteur": "Le Phoulosophe",
                "date": "Mon, 10 Oct 2022 00:00:00 GMT",
                "editeur": "Espoir LeCharpentier",
                "id": 4,
                "id_cat": 11,
                "isbn": "010-11-10",
                "titre": "100 Raisons de vivre"
            },
            "selected id": 4,
            "success": true
        }
```

. ## DELETE /livres (livre_id)

    GENERAL:
        Delete the livre of the given ID if it exists. Return the livre, the id of the deleted livre, success value, total of livre

        SAMPLE: curl -X DELETE http://localhost:5000/livres/2
```
        {
            "deleted id": 2,
            "deleted livre": {
                "auteur": "Jean Dupond",
                "date": "Thu, 12 Oct 2017 00:00:00 GMT",
                "editeur": "Jeanette DuBridge",
                "id": 2,
                "id_cat": 8,
                "isbn": "978-3-16-1",
                "titre": "Hands on machine learning with scikit learn v2"
            },
            "success": true,
            "total livre": 3
        }
```
. ## PATCH /livres/(livre_id)
  GENERAL:
  This endpoint is used to update a livre
  It returns livre after updated, before updated and success status that should be true

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/categories/1 -H "Content-Type:application/json" -d "{ "auteur": "Jean Dupond","date": "Thu, 12 Oct 2017 00:00:00 GMT", "editeur": "Jean DuBridge","id_cat": 8,"isbn": "978-3-16","titre": "Hands on machine learning with scikit learn-Update" }"
  ```
  ```
    {
        "after updated": {
        "auteur": "Jean Dupond",
        "date": "Thu, 12 Oct 2017 00:00:00 GMT",
            "editeur": "Jean DuBridge",
            "id": 1,
            "id_cat": 8,
            "isbn": "978-3-16",
            "titre": "Hands on machine learning with scikit learn-Update"
        },
        "before updated": {
            "auteur": "Jean Dupond",
            "date": "Thu, 12 Oct 2017 00:00:00 GMT",
            "editeur": "Jean DuBridge",
            "id": 1,
            "id_cat": 8,
            "isbn": "978-3-16",
            "titre": "Hands on machine learning with scikit learn"
        },
        "success": true
    }
    ```

. ## POST /categories

    GENERAL:    
    This endpoint is used to create a new categorie 
    We return the ID of the new categorie created, the categorie that was created, the list of categorie and the number of categorie.

    SAMPLE.....:
    ```
    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"isbn" : "978-0-321","titre" : "The art of computer programming","date" : "2020-03-26","auteur" : "Donald Knuth","editeur" : "Addenda","id_cat" : 11}"
    ```
    ```
        {
            "livres": [
                {
                    "auteur": "Stephen hawking",
                    "date": "Sun, 05 May 2019 00:00:00 GMT",
                    "editeur": "Philippe Goutiers",
                    "id": 3,
                    "id_cat": 7,
                    "isbn": "123-10-1",
                    "titre": "Une merveilleuse histoire du temps"
                },
                {
                    "auteur": "Le Phoulosophe",
                    "date": "Mon, 10 Oct 2022 00:00:00 GMT",
                    "editeur": "Espoir LeCharpentier",
                    "id": 4,
                    "id_cat": 11,
                    "isbn": "010-11-10",
                    "titre": "100 Raisons de vivre"
                },
                {
                    "auteur": "Jean Dupond",
                    "date": "Thu, 12 Oct 2017 00:00:00 GMT",
                    "editeur": "Jean DuBridge",
                    "id": 1,
                    "id_cat": 8,
                    "isbn": "978-3-16",
                    "titre": "Hands on machine learning with scikit learn-Update"
                },
                {
                    "auteur": "Donald Knuth",
                    "date": "Thu, 26 Mar 2020 00:00:00 GMT",
                    "editeur": "Addenda",
                    "id": 6,
                    "id_cat": 11,
                    "isbn": "978-0-321",
                    "titre": "The art of computer programming"
                }
            ],
            "success": true,
            "total livres": 4
        }
    ```      




## Testing
To run the tests, run
```
dropdb plants_database
createdb plants_database
psql plants_database_test < plants_database.sql
python test_flaskr.py
```