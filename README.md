# habiproperties

## How the project will be approached:

1. Verify the requested requirements
2. Make the connection to the database to check the structure of the table
3. Make the query with the structure to return to customers
4. Carry out the construction of the API with Python, setting up a local server
5. Make the request (in this case GET method)
6. Perform database connection and query with filters
7. Perform error handling
8. Make the structure of the project (In this case something similar to modern frameworks)
9. Perform unit tests

## Technologies

> ### Python

# Getting started

## Installation

Please check the official Python installation guide for server requirements before you start. [Official Documentation](https://docs.python.org/3.9/installing/index.html)

> Please Refer to [Github and ssh keys help page](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) before start.

Clone the repository with SSH

    git@github.com:JhonMora1407/habiproperties.git

Or clone the repository with HTTPS

    https://github.com/JhonMora1407/habiproperties.git


Switch to the repo folder

    cd habiproperties

Create the venv folder

    python3 -m venv venv

Install all the dependencies using pip

    pip install -r requirements.txt

Activate the environment with the dependencies

    source env/bin/activate

Start the local development server

    python HabiPropertiesAPI/main.py

You can now access the server at http://localhost:8080


## API Documentation

This is the documentation for consumption via Rest API.

> [Full API Spec](http://localhost:8000/swagger)

---

## Successful Request

```
status 200 OK
[
    {
        "address": "calle 95 # 78 - 49",
        "city": "bogota",
        "status": "pre_venta",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar"
    },
    {
        "address": "calle 95 # 78 - 123",
        "city": "bogota",
        "status": "pre_venta",
        "price": 120000000,
        "description": "hermoso acabado, listo para estrenar"
    }
]
```
## Failed Request

```
Error response
Error code: 422 |...| 501

Message: url not found.

Error code explanation: 422 - .
```

# Testing API

The api can now be accessed at

    http://localhost:8080/properties?year=2020&city=Bogota&status=pre_venta

Request Query Params

| **Required** | **Key**      | **Value**        |
| ------------ | ------------ | ---------------- |
| Optional     | year         |  int             |
| Optional     | city         |  str             |
| Optional     | status       |  str             |


    python -m unittest HabiPropertiesAPI/test/test_connection.py
    python -m unittest HabiPropertiesAPI/properties/test/test_filters.py 

---
