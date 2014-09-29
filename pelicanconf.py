#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

NOMBRE_DEL_SITIO = 'Pylares'
SITEURL = 'http://pylares.org'
SLOGAN_DEL_SITIO ='Un proyecto para enseñar programación en las escuelas'
# Directorio desde donde se obtendrá el contenido del sitio
PATH = 'content'

TIMEZONE = "America/Argentina/Cordoba"

DEFAULT_LANG = 'es'

# Habilitar cuando este en producción
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

THEME = "themes/pylares"

# Deshabilitar Pygments
MD_EXTENSIONS = ['extra']

# Deshabilitar ('index', categories', 'authors', 'archives')
DIRECT_TEMPLATES = set()

PAGE_URL = '{url}/'
PAGE_SAVE_AS = '{url}/index.html'

STATIC_PATHS = [
  "imagenes",
  'extra/robots.txt',
  'extra/Instalador_Pylares- 0.1.exe',
]
EXTRA_PATH_METADATA = {
  'extra/Instalador_Pylares- 0.1.exe': {'path': 'Instalador_Pylares- 0.1.exe'},
  'extra/robots.txt': {'path': 'robots.txt'},
}

# Borrar esta linea para sitio en vivo.
RELATIVE_URLS = True
