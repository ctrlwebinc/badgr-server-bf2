import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='badgr-server-bf2',
    version='1.0.0-alpha',
    packages=['bf2'],
    include_package_data=True,
    license='BSD-3-Clause',
    description='An add-on to Badgr Server to make it compatible with BadgeFactor 2',
    long_description=README,
    url='https://github.com/ctrlwebinc/badgr-server-bf2',
    author='ctrlweb',
    author_email='daniel@ctrlweb.ca',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-3-Clause License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: OpenBadges :: WordPress Bridge',
    ],
    install_requires=[
        "Django>=1.11,<3.0",
    ],
    tests_require=[
        'mock',
    ],
    zip_safe=False,
)
