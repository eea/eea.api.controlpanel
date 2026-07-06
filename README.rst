==========================
eea.api.controlpanel
==========================
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.api.controlpanel/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.api.controlpanel/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.api.controlpanel/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.api.controlpanel/job/master/display/redirect
  :alt: Master

The eea.api.controlpanel is a Plone add-on to be used together
with `volto-controlpanel <https://github.com/eea/volto-controlpanel>`_ Volto add-on

.. contents::


Main features
=============

1. Easy to install/uninstall via Site Setup > Add-ons
2. RestAPI for controlpanel versions details


Environment variables
=====================

- `BACKEND_VERSION` - Backend version to be saved to registry when Plone instance starts. You should update this environment variable every time you deploy a new version of your backend. 


Install
=======

* Add eea.api.controlpanel to your eggs section in your buildout and re-run buildout::

    [buildout]
    eggs +=
      eea.api.controlpanel

* Or via docker::

    $ docker compose up plone6

* Or via pip::

    $ pip install eea.api.controlpanel

* Install *eea.api.controlpanel* within Site Setup > Add-ons


Develop
=======
::

    $ git clone https://github.com/eea/eea.api.controlpanel.git
    $ cd eea.api.controlpanel
    $ git checkout develop
    $ make help


Source code
===========

- `Github <https://github.com/eea/eea.api.controlpanel>`_


Eggs repository
===============

- https://pypi.python.org/pypi/eea.api.controlpanel
- http://eggrepo.eea.europa.eu/simple


Plone versions
==============
It has been developed and tested for Plone 5 and 6. It should work on any Plone version that supports Volto.


How to contribute
=================
See the `contribution guidelines (CONTRIBUTING.md) <https://github.com/eea/eea.api.controlpanel/blob/master/CONTRIBUTING.md>`_.

Copyright and license
=====================

eea.api.controlpanel (the Original Code) is free software; you can
redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place, Suite 330, Boston, MA 02111-1307 USA.

The Initial Owner of the Original Code is European Environment Agency (EEA).
Portions created by Eau de Web are Copyright (C) 2009 by
European Environment Agency. All Rights Reserved.


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
.. _`EEA Web Systems Training`: http://www.youtube.com/user/eeacms/videos?view=1

Secret Scanning
===============

This repository uses the Betterleaks GitHub Action to scan the current
repository content on every push and pull request. The scan uses the rules in
``.gitleaks.toml`` and uploads a ``betterleaks-report`` artifact when a finding
is detected.

If the optional SMTP secrets are configured, failed scans also send an email to
the last commit committer. The workflow expects these repository or
organization secrets:

- ``SMTP_URL``
- ``SMTP_PORT`` (optional, defaults to ``25``)
- ``SMTP_EMAIL``
- ``SMTP_PASSWORD`` (optional if the SMTP server does not require authentication)

Port ``465`` is sent with direct TLS; other ports use the default SMTP
handshake. The email includes a short finding summary from the redacted
Betterleaks report, including the redacted matched line from each finding.

There are three common outcomes:

1. Everything is OK. The ``Betterleaks / Scan for secrets`` check is green and
   no action is needed. Regular references to runtime values are OK, for example::

     token_from_cookie = request.cookies.get("auth_token")

2. A real secret was found. The check is red and the workflow log asks you to
   download the ``betterleaks-report`` artifact. Open the artifact from the
   GitHub Actions run and check the reported file, line and rule. Remove the
   committed value, move it to the proper secret store, and rotate it if it was
   exposed. A report entry looks like this::

     {
       "RuleID": "secret-literal-assignment",
       "File": "src/config.py",
       "StartLine": 12,
       "Secret": "[REDACTED]"
     }

3. The finding is a false positive. Keep the value only if it is clearly not
   sensitive, such as a test fixture, placeholder, or public example. Add
   ``betterleaks:allow`` on the same line and include a short explanation in the
   pull request::

     test_password = "admin"  #betterleaks:allow

Do not add ``betterleaks:allow`` to real credentials.
