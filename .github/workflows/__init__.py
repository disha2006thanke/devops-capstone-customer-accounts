from flask_talisman import Talisman

talisman = Talisman()

def init_app(app):
    talisman.init_app(
        app,
        content_security_policy={
            "default-src": "'self'"
        },
        force_https=False
    )
