# -*- encoding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h_iu84z!!g9jf9pf7#hv3%dgkt&draf6!(1fuw00^$-pfk=r9b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #A.P.I.
    'rest_framework',
    'social.apps.django_app.default',
    'embed_video',
    #Class Abstract 
    'infos_systems.apps.InfosSystemsConfig',
    #Assist Control
    'auth_users.apps.AuthUsersConfig',
    'identification_documents.apps.IdentificationDocumentsConfig',
    'civil_states.apps.CivilStatesConfig',
    'blood_groups.apps.BloodGroupsConfig',
    #Web Sites
    #'web_sites.apps.WebSitesConfig',
    #'web_headers.apps.WebHeadersConfig',
    #'web_sections.apps.WebSectionsConfig',
    #'web_portals.apps.WebPortalsConfig',
    #'web_slides.apps.WebSlidesConfig',
    #'web_sliders.apps.WebSlidersConfig',
    'index.apps.IndexConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
]

ROOT_URLCONF = 'app_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['templates'])],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Python Social Auth Context Processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'app_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'App_Main',
        'USER': 'sa',
        'PASSWORD': 'S1st3mas',
        'HOST': 'localhost',
        'PORT': '',

        'OPTIONS': {
            #'driver': 'ODBC Driver 13 for SQL Server',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es_pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
#MEDIA -> STATIC
if DEBUG == False:
    STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])
else:
    STATICFILES_DIRS = [os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])]

STATICFILES_FINDERS = {
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    }

#Imagenes, audios y videos
MEDIA_URL  = '/media/'
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])


#Configuración de Usuario
AUTH_USER_MODEL = 'auth_users.AuthUser'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '1826914080927037'
SOCIAL_AUTH_FACEBOOK_SECRET = '2b8f6339be1d827d335e4605c6de8cdf'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}