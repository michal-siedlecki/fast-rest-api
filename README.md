# Dates REST API

Dates REST API application implements a simple REST API using FastAPI. It is
a basic dates database interacting with an external API.
### Deployed app
https://ngdates-rest-api.herokuapp.com/
### API DOCUMENTATION
https://ngdates-rest-api.herokuapp.com/docs

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed `python` >= 3.6.2
* You have a `<Windows/Linux/Mac>` machine.

## Installing Dates REST API

To install Dates REST API, follow these steps:

Linux and macOS:

```
git clone https://github.com/michal-siedlecki/ngdates-rest-api
cd ngdates-rest-api
python -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
```

## Using Dates REST API

To use Dates REST API follow these steps:
Export database credentials and app secret key to .env file
```
touch .env
```
As a template you can use this:

```
DATABASE_URL_local=postgresql://postgres:mysecretpassword@127.0.0.1:5432/postgres
DATABASE_URL=postgresql://datesapp:dates@db:5432/DatesDB
DB_USER=datesapp
DB_PASSWORD=dates
DB_NAME=DatesDB
SECRET_KEY=supersecret
```
You need to create and run docker
container with clusters inside
```
docker-compose build
docker-compose up
```
Now app is avilable at `localhost:8000`

## Development
To develop application locally you need either set up postgreSQL database on your computer
or run database in docker container
```
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
```
This command will run postgresql database from latest image in local container. It starts local postgres with
default settings which means you can connect as user `postgres` with `POSTGRES_PASSWORD` as password
to database named `postgres`

## Unit testing

There are prepared some unit tests which can be run with this:
```
pytest
```

## Contributors

Thanks to the following people who have contributed to this project:

* [@michal-siedlecki](https://github.com/michal-siedlecki) 😎 [author]


## Contact

If you want to contact me you can reach me at <siedlecki.michal@gmail.com>.

## License

This project uses the following license: MIT (<https://github.com/michal-siedlecki/ngdates-rest-api/blob/master/LICENSE>).
