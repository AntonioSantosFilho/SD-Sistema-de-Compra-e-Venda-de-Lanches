import os

IS_PRODUCTION = os.getenv("IS_PRODUCTION", 'False').lower() in ('1', 'true', 't', 'yes', 'y')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

# Application definition
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.humanize', #Humanização
    'django.contrib.messages', #framework de mensagems

    # Enable the inner home (home)   
    'apps.registro',  
    'apps.marketplace',  
    'apps.pagamentos',
         # Django REST Framework
    'rest_framework',

]

MERCADO_PAGO_PUBLIC_KEY = "SUA KEY"
MERCADO_PAGO_ACCESS_TOKEN = "SEUA ACESS TOKEN"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',         # Renderiza JSON
       # 'rest_framework.renderers.BrowsableAPIRenderer', # Interface navegável da API
    ],
}



AUTH_USER_MODEL = 'registro.Usuario'  # Substitua 'app' pelo nome do seu app

LOGIN_REDIRECT_URL = '/login/'  # Redireciona para a página inicial, por exemplo
LOGOUT_REDIRECT_URL = '/login/'  # Substitua pela URL desejada, como a página de login




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}



# configurações servem apenas para send_common (SMTP using DJango)
# Recuperação de senha
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'SEUEMAIL@gmail.com' 
EMAIL_HOST_PASSWORD = 'SUA SENHA DE APP'  # foi usado a senha gerada pelo google
DEFAULT_FROM_EMAIL = 'no-reply@distribulanche.com.br'  
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

USE_I18N = True
USE_L10N = True

USE_TZ = True
TIME_ZONE = 'America/Recife'