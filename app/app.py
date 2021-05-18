import os

from markupsafe import Markup
from flask_mail import Mail, Message
from flask import (
    Flask, request, render_template, redirect, url_for, flash, abort,
)

app = Flask(__name__, instance_relative_config=True)
env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)

# URL to redirect after sending the e-mail.
REDIRECT_TO = os.getenv('REDIRECT_TO')

mail = Mail(app)


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/send-email/')
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name and not email and not message:
        # Method not allowed without this informations.
        abort(405)

    html_email = render_template('email.html', 
                                 name=name, email=email, message=message)
    text_email = Markup(html_email).striptags()
    subject = f'E-mail enviado do seu portfólio por {name.split()[0]}'
    
    email_message = Message(subject=subject,
                            recipients=app.config.get('MAIL_DEFAULT_RECEIVERS'),
                            body=text_email,
                            html=html_email)
    
    try:
        mail.send(email_message)
    except Exception as err:
        print(err)
        flash('Ocorreu um erro ao enviar o e-mail. :(', 'error')
    else:
        flash('Seu e-mail foi enviado!', 'success')
    finally:
        return redirect(REDIRECT_TO or url_for('index'))


@app.errorhandler(404)
def page_not_found(err):
    return render_template('errors/404.html'), 404


@app.errorhandler(405)
def method_not_allowed(err):
    return render_template('errors/405.html'), 405


@app.errorhandler(500)
def internal_server_error(err):
    return render_template('errors/500.html'), 500
