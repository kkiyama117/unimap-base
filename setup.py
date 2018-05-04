import os
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = '0.1.2'


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = f"Git tag: {tag} does not match " \
                   f"the version of this app: {VERSION}"
            sys.exit(info)


setup(
    name='unimap-base',
    version=VERSION,
    packages=find_packages(exclude=['config', 'docs']),
    include_package_data=True,
    license='GPLv3',
    description='A simple Django app to manage university.',
    long_description=README,
    url='https://github.com/kkiyama117/unimap-base/',
    author='kkiyama117',
    author_email='k.kiyama117@gmail.com',
    install_requires=['django', 'django-model-utils'],
    # setup.py内でpytestのimportが必要
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-django',
        'pytest-sugar',
        'django-webtest',
        'django-coverage-plugin',
        'factory-boy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "License :: OSI Approved :: GNU General Public License "
        "v3 or later (GPLv3+)",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
