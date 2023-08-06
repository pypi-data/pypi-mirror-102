django-nofloc |nlshield|
========================

django-nofloc is a simple Django app that provides a middleware to let
Google Chrome know that your website should not be included in the
Google FLoC program. Essentially you're opting out of this privacy
invading program that is default for all Chrome users.

**Version:** 0.1.0

**Project Links:** `Mailing
List <https://lists.code.netlandish.com/~netlandish/public-inbox>`__ -
`Contributing <#contributing>`__

**Author:** Peter Sanchez (https://netlandish.com)

Because this is a simple middleware we have no issue tracker for it. If
there are any issues please send an email to the `mailing
list <https://lists.code.netlandish.com/~netlandish/public-inbox>`__.

Python / Django Support
-----------------------

-  Python 3.6+ for Django versions 2.2+

Installation
============

PIP:

::

   pip install django-nofloc

Basic Manual Install:

::

   $ python setup.py build
   $ sudo python setup.py install

Then just add the ``nofloc.middleware.NoFLoCMiddleware`` to your
``MIDDLEWARE`` setting. The placement order shouldn't matter.

::

   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
       'nofloc.middleware.NoFLoCMiddleware',
   ]

This will set the ``Permissions-Policy`` header to a value of
``interest-cohort=()`` for every request served by Django.

If you need to alter this header within a view or some other case, this
app may not be a good tool for you to use in it's current state. It's
set specifically to disable FLoC. Review your use case before installing
this app. You can also submit a patch to make this more configurable if
you'd like :)

Why?
----

Because we're tired of big tech spying on us. For more info see:

https://plausible.io/blog/google-floc

Contributing
============

We accept patches submitted via ``hg email`` which is the ``patchbomb``
extension included with Mercurial.

The mailing list where you submit your patches is
``~netlandish/public-inbox@lists.code.netlandish.com``. You can also
view the archives on the web here:

https://lists.code.netlandish.com/~netlandish/public-inbox

To quickly setup your clone of ``django-nofloc`` to submit to the
mailing list just edit your ``.hg/hgrc`` file and add the following:

::

   [email]
   to = ~netlandish/public-inbox@lists.code.netlandish.com

   [patchbomb]
   flagtemplate = "django-nofloc"

   [diff]
   git = 1

We have more information on the topic here:

-  `Contributing <https://man.code.netlandish.com/contributing.md>`__
-  `Using email with
   Mercurial <https://man.code.netlandish.com/hg/email.md>`__
-  `Mailing list
   etiquette <https://man.code.netlandish.com/lists/etiquette.md>`__

Copyright & Warranty
====================

All documentation, libraries, and sample code are Copyright 2021
Netlandish Inc. <hello@netlandish.com>. The library and sample code are
made available to you under the terms of the BSD license which is
contained in the included file, LICENSE.

.. |nlshield| image:: https://img.shields.io/badge/100%25-Netlandish-blue.svg?style=square-flat
   :target: http://www.netlandish.com
