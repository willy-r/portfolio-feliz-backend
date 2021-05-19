from markupsafe import Markup
from flask_mail import Mail, Message
from flask import (
    Blueprint, request, current_app, render_template, redirect, url_for, flash,
)

bp = Blueprint('send_email', __name__, url_prefix='/')
mail = Mail()
app = current_app


@bp.post('/send-email')
def send_email():
    """Send e-mail from a form.

    The form must have the 'name', 'email' and 'message' name attributes.
    
    After sending the e-mail (or not) the response will be redirected to
    the index page, or if specified, to REDIRECT_TO enviroment variable.
    """
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

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
        app.logger.error(err)
        flash('Ocorreu um erro ao enviar o e-mail. :(', 'error')
    else:
        flash('Seu e-mail foi enviado!', 'success')
    finally:
        return redirect(app.config.get('REDIRECT_TO') or url_for('index'))
