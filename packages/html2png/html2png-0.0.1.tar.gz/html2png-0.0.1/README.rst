## -*- coding: utf-8 -*-
##-----------------------------------------------------------------------------
## file: $Id$
## auth: metagriffin <mg.github@metagriffin.net>
## date: 2021-04-13
## copy: (C) Copyright 2021-EOT metagriffin -- see LICENSE.txt
##-----------------------------------------------------------------------------
## This software is free software: you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## This software is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see http://www.gnu.org/licenses/.
##-----------------------------------------------------------------------------

========
html2png
========

.. IMPORTANT::

  This package is still in the planning/pre-alpha phase.


Overview
========

A Python library and command-line utility to rasterize an
HTML page into a PNG file.


TL;DR
=====

Installation::

  pip install html2png


Command-line usage::

  html2png {URL} > output.png


Python usage::

  import html2png

  png = html2png.render('<html><body><p>Hello, world!</p></body></html>')
  png = html2png.render_url('http://example.com/')


##-----------------------------------------------------------------------------
## end of $Id$
## $ChangeLog$
##-----------------------------------------------------------------------------
