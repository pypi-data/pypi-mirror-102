##############################################################################
bvl-api 0.5.1
##############################################################################

.. image:: https://travis-ci.com/alanverresen/bvl-api.svg?branch=master
    :target: https://travis-ci.com/alanverresen/bvl-api
    :alt:

.. image:: https://readthedocs.org/projects/bvl-api/badge/?version=latest
    :target: https://bvl-api.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This Python package can be used to retrieve data about Flemish basketball
teams. It sends queries directly to the official API of Basketbal Vlaanderen
in order to get the latest information.


==============================================================================
Features
==============================================================================

The `API's official documentation <https://www.basketbal.vlaanderen/faq/detail/waar-vind-ik-de-api-documentatie>`_
includes the following warning:

.. epigraph::

    De API's vermeld in dit document mogen enkel gebruikt worden voor de
    integratie van wedstrijdkalenders, wedstrijdresultaten en rangschikkingen
    op websites van clubs die bij de Vlaamse Basketballiga vzw aangesloten
    zijn. Alle andere partijen of organisaties die de API's wensen te
    gebruiken, dienen contact op te nemen.

The package was designed with these restrictions in mind, and thus, the
package only provides partial coverage of the official API's functionality.
This package can be used to retrieve information about:

* a team's competitions
* a team's competitive game schedule

Check out the `documentation <https://bvl-api.readthedocs.io/en/latest/>`_
for more information.

==============================================================================
Install
==============================================================================

You can install this package using pip:

.. code-block:: sh

    $ pip install --user bvl-api


==============================================================================
License
==============================================================================

This project is released under the MIT license.
