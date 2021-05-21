from markupsafe import Markup
from flask_mail import Mail, Message
from flask import Blueprint, request, current_app, render_template

bp = Blueprint('send_email', __name__, url_prefix='/')
mail = Mail()


@bp.post('/send-email')
def send_email():
    """Send an e-mail.

    The keys 'name', 'email' and 'message' is required.
    
    Return a json with the result (if the e-mail was sent or not)
    and a message. 
    """
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    html_email = render_template('email.html',
                                 name=name, email=email, message=message)
    text_email = Markup(html_email).striptags()
    subject = f'E-mail enviado do seu portfólio por {name.split()[0]}'

    email_message = Message(subject=subject,
                            recipients=current_app.config.get('MAIL_RECEIVERS'),
                            body=text_email,
                            html=html_email)
    
    try:
        mail.send(email_message)
    except Exception as err:
        sent = False
        response_message = 'Ocorreu um erro ao enviar o e-mail. :('
        # Debug.
        current_app.logger.error(err)
    else:
        sent = True
        response_message = 'Seu e-mail foi enviado!'
    finally:
        return {
            'sent': sent,
            'message': response_message,
        }
