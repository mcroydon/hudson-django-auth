#!/usr/bin/env python

__AUTHOR__ = 'Matt Croydon'
__LICENSE__ = 'BSD'

from django.contrib.auth import authenticate as django_authenticate
import os, sys

def authenticate(username, password):
    """
    Authenticate a given username/password with Django and make sure
    they're also a staff user.
    """
    user = django_authenticate(username=username, password=password)
    if not user or not user.is_staff:
        return False
    else:
        return True

if __name__ == '__main__':
    """Hudson provides access to username/password by two environment variables,
    ``U`` and ``P``.  An exit code of 0 means they're authenticated, anything else
    means they're not."""
    authenticated = authenticate(username=os.environ.get('U', ''), password=os.environ.get('P', ''))
    if authenticated:
        sys.exit(0)
    else:
        sys.exit(1)
