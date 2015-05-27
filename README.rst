=======
Mélange
=======

Mélange is a base package and concept for html page composition.

Mélange is not tied to an specific CMS or framework, but as created with Pyramid and Plone in mind.

Mélange is declarative and hands over the power of page control away from Python into user-space.

Mélange Workflow
================

Mélange expects a design workflow with the following roles involved:

- Designer and template builder: HTML, CSS, JS only.
- CMS Integrator with HTML and no or little Python knowledge
- Page Editor with layout competence (no HTML knowledge)
- Content editor (Single content page)

In a Mélange design workflow:

1. a designer creates a modern webdesign.
   Using some poular grid system such as bootstrap, foundation or similar she creates a reusable set of modular pages.
   Another alternative is to buy a standard design from one of the sales platforms.

2. An integrator takes the design and cuts it down into logical fragments.
   Each fragment gets an manifest, defines the editorial parts of the element (edit form information) and dynamic parts, i.e. pointing to lists of existing content.
   He uses the base package together with the CMS intgration packages to register the fragments persisten for lat er use in the CMS.

3. The Page-Editor creates a new page.
   She is able to select fragments from the library in order to compose a page from them.
   Layouts are stored then for later usage.

4. A content editor creates an empty page, chooses a layout and starts filling in content.

Source Code
===========

.. image:: https://secure.travis-ci.org/jensens/melange.png
    :target: http://travis-ci.org/#!/jensens/melange

.. image:: https://coveralls.io/repos/jensens/melange/badge.png
    :alt: Coverage
    :target: https://coveralls.io/r/jensens/melange

The sources are in a GIT DVCS with its main branches at
`github <http://github.com/jensens/melange>`_.

We'd be happy to see many forks and pull-requests to make Mélange even better.

Please follow the `plone.api code style conventions <http://ploneapi.readthedocs.org/en/latest/contribute/conventions.html>`_


Contributors
============

- Jens W. Klein ``<jk@kleinundpartner.at>``
