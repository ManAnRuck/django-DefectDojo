#!/usr/bin/env python

from setuptools import setup

setup(
    name='DefectDojo',
    version='1.0.5',
    author='Greg Anderson',
    description="Tool for managing vulnerability engagements",
    install_requires=[
        'Django==1.11.2',
        'MySQL-python',
        'Pillow==4.1.1',
        'django-secure>1.0',
        'django-tastypie>=0.12.2',
        'django-tastypie-swagger',
        'gunicorn>=19.1.1',
        'python-nmap>=0.3.4',
        'pytz>=2013.9',
        'requests>=2.2.1',
        'wsgiref>=0.1.2',
        'django-filter==1.0.4',
        'supervisor',
        'humanize',
        'django-bower',
        'django-auditlog==0.3.3',
        'vobject',
        'html2text',
        'django-watson==1.3.1',
        'celery==3.1.24',
        'kombu==3.0.37',
        'sqlalchemy',
        'django-polymorphic==1.2',
        'pdfkit==0.5.0',
        'django-overextends',
        'defusedxml',
        'django-tagging',
        'django-custom-field',
        'django-imagekit',
        'jira',
        'pycrypto',
        'lxml'],
    dependency_links=[
        "https://github.com/grendel513/python-pdfkit/tarball/master#egg=pdfkit-0.5.0",
    ],
    url='https://github.com/owasp/django-DefectDojo'
)
