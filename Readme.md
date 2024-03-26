### The frontend of the website can be found [here](https://github.com/Istiaq-Fuad/PetFinderFrontend)

First, make sure you have python installed in your system. The create and activate a virtual environment.

To run this application clone this repository and run:

```shell
pip install -r requirements.txt
```

To run staticfiles with whitenoise, make sure to run the command:

```shell
python manage.py collectstatic
```

Then run the server using:

```shell
python manage.py runserver
```

This will run the server on `localhost:8000`


