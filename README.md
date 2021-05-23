# Portfólio Feliz - Backend 

The [Portfólio Feliz](https://github.com/willy-r/portfolio-feliz) Backend, implement features like sending e-mail. Developed using [Flask](https://flask.palletsprojects.com/en/2.0.x/).


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

[Enviroment variables](https://github.com/willy-r/portfolio-feliz-backend/blob/main/.env.example)


## Run Locally

Clone the project

```bash
git clone https://github.com/willy-r/portfolio-feliz-backend.git
```

Go to the project directory

```bash
cd portfolio-feliz-backend
```

Make a virtual enviroment and activate it

```bash
python -m venv venv # Using Python 3.9.5
source venv/bin/activate # Unix systems 
venv\Scripts\activate # Windows
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the server

```bash
flask run
```


## API Reference

#### Send e-mail

```http
POST /send-email
```

| Description                |
| :------------------------- |
| Send an e-mail. The keys `name`, `email` and `message` are required. |


## Demo

You can test [here](https://portfolio-feliz-backend.herokuapp.com/) sending me an e-mail.


## Contributing

Contributions are always welcome!

Fork this repo, create a PR and you're done, thanks! <3


## Authors

- [@willy-r](https://github.com/willy-r)
