### Asana API integration

## Asana credentials

Need to set to `.env` file `ASANA_ACCESS_TOKEN`.
It's need to access to Asana API.

Also, you can set `ASANA_WORKSPACE`.

[Asana API documentation](https://developers.asana.com/docs)

### Usage via virtual environment
Python version - 3.8.5

Need to create and activate virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

Also you can deactivate virtual environment if need
```bash
deactivate
```

More info about virtual environment
https://docs.python.org/3/library/venv.html

And then install requirements:
```bash
pip install -r requirements.txt
```

And then you can run to start the server

```bash
python3 manage.py runserver
```
## Usage via docker:
You should have Docker and docker compose

To run migrations (It's need only once):
```
docker-compose run web python3 manage.py migrate 
```
To run a application:
```bash
docker-compose up
```