import .secret_settings

MAIL_SERVER = 'smtp.zoho.eu'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = secret_settings.MAIL_USERNAME
MAIL_PASSWORD = secret_settings.MAIL_PASSWORD