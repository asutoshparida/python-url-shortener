# python-url-shortener

This repository is for managing all public/private entity specific api endpoints for an organisation.
In this case we have entity as URL shortener

## Project Structure

The basic project structure is as follows:

```bash
root/
 |-- app
 |   |-- controllers/
 |   |   |-- __init__.py
 |   |   |-- url_shortener_controller.py
 |   |-- services/
 |   |   |-- __init__.py
 |   |   |-- url_shortener_service.py
 |   |-- schemas/
 |   |   |-- __init__.py
 |   |   |-- url_shortener_schema.py
 |   |-- utilities/
 |   |   |-- __init__.py
 |   |   |-- url_shortener_utility.py
 |   |-- tests/
 |   |   |-- __init__.py
 |   |   |-- test_url_shortener_controller.py
 |   |   |-- test_url_shortener_utility.py
 |   |-- config.py
 |   |-- errors.py
 |   |-- routes.py
 |   |-- __init__.py
 |   build.sh
 |   logging.yaml
 |   setup.py
 |   README.md
```

# Synopsis

    There are two API endpoints exposed as part of this app
    1. /url/encode
    2. /url/decode
    
    /url/encode:  Will shorten a valid URL and returns a shorten URL(JSON) also 
    put origianl, shorten url in cache(We are using flask_caching for storage).

    /url/decode:  Will return a valid URL original URL(JSON) for a given shorten 
    url from cache(We are using flask_caching for storage).

    For request/response structure please reffer 
    Swagger URl after successful buld & run step.


# Requirements

    python 3.9
    Flask 2.0.2
    marshmallow 3.12.2
    flask_caching
    Werkzeug 2.0.2

    for detiled requirement please reffer setup.py

# Quick Start Setup

### Run Setup. 
This will create virtualenv and install all required packages and will allow you to run the app from anywhere on your machine.

```
$> cd the-shortest-url-1-uvpyns
$> ./build.sh
```

### Run the tests
```
$> cd the-shortest-url-1-uvpyns
$> pytest
```

### Running Locally
API can be executed as follows:

```
$> cd the-shortest-url-1-uvpyns
$> python api_gateway.py
```
Navigate to the posted URL in your terminal to be greeted with Swagger, where you can run the API endpoints.