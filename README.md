Pyschotests: website
====================

[![Build Status](https://travis-ci.org/psychotests/psychotests.github.io.svg?branch=sources)](https://travis-ci.org/psychotests/psychotests.github.io)


This repository contains the source code of our website:

- branch ``sources``: source code, pages and blog of the pelican website
- branch ``master``: generated HTML (by Travis).


All Pull Requests should be merged in the ``sources`` branch.


How to build
------------

This website is generated with [Pelican](https://blog.getpelican.com/).

To test this website, you should use the following:

    pip install -r requirements.txt
    make devserver
