from dotenv import load_dotenv
from flask import Flask, render_template

from app import send_email

load_dotenv()


def create_app():
    """Create and configure the app."""
    app = Flask(__name__)
    app.config.from_object('app.config.ProductionConfig')
    
    if app.config['ENV'] == 'development':
        app.config.from_object('app.config.DevelopmentConfig')
    
    send_email.mail.init_app(app)


    @app.get('/')
    def index():
        """Show a simple form to test the application."""
        return render_template('index.html')
    

    @app.errorhandler(404)
    def page_not_found(err):
        return render_template('errors/404.html'), 404


    @app.errorhandler(405)
    def method_not_allowed(err):
        return render_template('errors/405.html'), 405


    @app.errorhandler(500)
    def internal_server_error(err):
        return render_template('errors/500.html'), 500
    

    app.register_blueprint(send_email.bp)

    return app
