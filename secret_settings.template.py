"""
This a template for secret_settings.py, a file for storing sensitive data and
email login settings.

If you downloaded this from my github, rename this file to secret_settings.py
for it to take effect.

You can generate a new secret key with

    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
"""

SECRET_KEY = '<PASTE_NEW_SECRET_KEY_HERE'

EMAIL_HOST_USER = '<EMAIL_HOST_USER>'
EMAIL_HOST_PASSWORD = '<EMAIL_HOST_PASSWORD>'
DEFAULT_FROM_EMAIL = '<DEFAULT_FROM_EMAIL>'