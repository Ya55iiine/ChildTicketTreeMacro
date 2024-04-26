#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

PACKAGE = 'childtickettree'

setup(
    name = 'Tracchildtickettreemacro',
    version = '1.1.1',
    packages = [PACKAGE],
    author = 'Mark Ryan',
    author_email = 'walnut.trac.hacks@gmail.com',
    description = 'Macro to see a complete tree/hierarchy of tickets under the given ticket number.',
    keywords = 'trac plugins ticket dependency childtickets',
    url = 'https://trac-hacks.org/wiki/ChildTicketTreeMacro',
    install_requires = ['Trac'],
    zip_safe = False,
    entry_points = {
        'trac.plugins': '%s = %s' % (PACKAGE, PACKAGE)
    },
)
