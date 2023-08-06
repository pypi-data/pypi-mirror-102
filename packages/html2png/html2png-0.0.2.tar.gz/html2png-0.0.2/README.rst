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
