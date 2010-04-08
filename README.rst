Authenticate Hudson against a Django installation using the
`Script Security Realm`_ plugin.  It currently checks each configured authentication
backend and ensures that the user is authenticated and also a staff user.  It is possible
to check if a user is a member of a specific group or has a specific permission as well.

To use this script, you'll need to make sure that your hudson user has its ``PYTHONPATH``
and ``DJANGO_SETTINGS_MODULE`` set correctly.  You can add the following to the hudson
user's .bashrc or .bash_profile::

    export PYTHONPATH=/any/custom/pythonpaths:/beyond/system/defaults
    export DJANGO_SETTINGS_MODULE=myproject.mysettings

You'll also need to install the `Script Security Realm`_ plugin and then check
``Enable security`` under the ``Manage Hudson`` -> ``Configure System`` menu.  To
use this script select ``Authenticate via custom script`` and add the following to the
``Command`` field::

    python /path/to/hudson_django_auth.py

You'll also want to select an appropriate option under ``Authorization`` in order for the
plugin to take affect.  ``Logged-in users can do anything`` may be a sane default here.

Note: This script requires at least version 1.1. of the `Script Security Realm`_ plugin.
Version 1.0 will likely yield a stacktrace.

.. _Script Security Realm: http://wiki.hudson-ci.org/display/HUDSON/Script+Security+Realm
