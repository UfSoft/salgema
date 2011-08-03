# -*- coding: utf-8 -*-
"""
Salgema
=======

* **Salgema in Portuguese, Halite in English, (pronounced /ˈhælaɪt/), commonly known as
rock salt, is the mineral form of sodium chloride (NaCl).** *

This project name changed because there's already a bittorrent client named *Halite*.
It's just the Portuguese translation of the same name.

This project aims to be a *selective* fork of the salt_ project.

The purpose is to extract the daemon/client connection encryption code from salt_ and
make it a generic library to be used in other projects, ie, those that do not need the
full power of salt_.

.. _salt: http://saltstack.org/

"""

__version__     = '0.1-dev'
__package__     = 'Salgema'
__summary__     = "ZMQ connection authorization/encryption"
__author__      = 'Pedro Algarvio'
__email__       = 'pedro@algarvio.me'
__license__     = 'BSD'
__url__         = 'http://dev.ufsoft.org/projects/salgema'
__description__ = __doc__
