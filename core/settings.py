"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0f82=prz$4d0z^n0h$veut6r9x5=26wy43e-(5+b17f1s=rgl2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['http://astro-academy.uz','https://astro-academy.uz',' http://astro-academy.uz/',' https://astro-academy.uz/']

CORS_REPLACE_HTTPS_REFERER = True

CSRF_COOKIE_DOMAIN = 'astro-academy.uz'

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'home',
    'news',
    'users',
    'courses',
    'student',
    'master'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'custom_tags': 'home.custom_tags',
            }
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'Astro.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'markaz',
#         'USER': 'postgres',
#         'PASSWORD': '1',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = '/login/'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
if DEBUG:
  STATICFILES_DIRS =  [BASE_DIR / "static",]
else:
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}




#jazmin


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-light",
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": "",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
from typing import Any, Dict
JAZZMIN_SETTINGS: Dict[str, Any] = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Astro academy",
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Astro Academy",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "logo2.png",
    "site_brand": "Astro Academy",
    # Relative path to logo for your site, used for login logo (must be present in static files. Defaults to site_logo)
    "login_logo": "logo2.png",
    # Logo to use for login form in dark themes (must be present in static files. Defaults to login_logo)
    "login_logo_dark": "logo2.png",
    # CSS classes that are applied to the logo
    "site_logo_classes": "brand-image",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "logo.png",
    # Welcome text on the login screen
    "welcome_sign": "Astro academy xodimlar uchun",
    # Copyright on the footer
    "copyright": "Astro IT Academy",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "users.CustomUser",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'user.picture.url',
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Asosiy", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Studentlar", "url": "/admin/student/student/",},
        {"name": "Bizning kurslar", "url": "/admin/courses/course/",},
        {"name": "Yangiliklar", "url": "/admin/news/event/",},
        {"name": "Dars jadvali", "url": "/admin/courses/schedule/",},
        {"name": "Davomat", "url": "https://docs.google.com/spreadsheets/u/0/?tgif=d",},
        {"name": "Bosh sahifa", "url": "/",},
        # external url that opens in a new window (Permissions can be added)
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps to base side menu (app or model) ordering off of
    "order_with_respect_to": ["Make Messages", "auth", "books", "books.author", "books.book", "loans"],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "loans": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["loans.view_loan"],
            },
            {"name": "Custom View", "url": "admin:custom_view", "icon": "fas fa-box-open"},
        ]
    },
    # Custom icons for side menu apps/models See the link below
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,
    # 5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        "home.AboutUsComment": "fas fa-qrcode",
        "home.AboutInfoTab": "fas fa-code-branch",
        "home.Gallary": "far fa-images",
        "home.Messages": "far fa-flag",
        "courses.Course": "fas fa-home",
        "courses.CourseComment": "fas fa-comments",
        "courses.Course_outline": "fas fa-paperclip",
        "courses.WeekDay": "fas fa-receipt",
        "courses.OurGroup": "fab fa-microsoft",
        "courses.Schedule": "fas fa-school",
        "courses.EnrollCourse": "far fa-id-badge",
        "master.Master": "fas fa-book-reader",
        "news.Category": "fas fa-cubes",
        "news.Tag": "fas fa-indent",
        "news.Event": "fas fa-star",
        "news.PostCategory": "fas fa-project-diagram",
        "news.PostTag": "fas fa-hashtag",
        "news.Post": "fas fa-book-open",
        "news.PostComment": "fas fa-money-check",
        "student.Student": "fas fa-users",
        "users.CustomUser": "fas fa-user-tie",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Activate Bootstrap modal
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

