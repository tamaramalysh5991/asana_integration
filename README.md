### Asana API integration

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

To run a application:
```bash
docker-compose up
```