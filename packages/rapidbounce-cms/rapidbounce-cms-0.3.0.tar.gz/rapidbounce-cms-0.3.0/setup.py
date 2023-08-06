# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rapidbounce_cms', 'rapidbounce_cms.migrations']

package_data = \
{'': ['*'], 'rapidbounce_cms': ['templates/admin/*']}

install_requires = \
['Django>=3.2,<4.0',
 'django-ckeditor==6.0.0',
 'django-crispy-forms==1.11.2',
 'django-filer==2.0.2',
 'django-htmlmin==0.11.0',
 'django-imagekit==4.0.2',
 'django-modeltranslation==0.16.2',
 'django-mptt-admin==2.1.0',
 'django-mptt==0.12.0',
 'django-recaptcha==2.0.6',
 'django-reversion==3.0.9',
 'django-storages[google]==1.9.1',
 'django_compressor==2.4',
 'pillow==8.2.0']

setup_kwargs = {
    'name': 'rapidbounce-cms',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Rapidbounce',
    'author_email': 'customer.support@rapidbounce.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
