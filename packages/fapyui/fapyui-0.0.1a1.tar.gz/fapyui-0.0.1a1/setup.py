import codecs
import re

from setuptools import setup

# https://packaging.python.org/en/latest/distributing/

INFO = {}

with codecs.open('README.md', mode='r', encoding='utf-8') as f:
    INFO['long_description'] = f.read()

REQUIRES = []
SETUP_REQUIRES = ['pytest-runner>=4.4']
TEST_REQUIRES = [
    # 'black>=18.9-beta.0',
    'flake8>=3.7',
    'isort>=4.3',
    'pytest>=4.3',
    'pytest-asyncio>=0.10',
    'pytest-runner>=4.4',
    'pytest-isort>=0.3',
    'pytest-flake8>=1.0',
    'pytest-mock>=1.10.1',
]
PACKAGES = []
PACKAGE_DATA = {}

setup(
    name='fapyui',
    version='0.0.1a1',
    description='short desctiption',
    long_description=INFO['long_description'],
    long_description_content_type='text/markdown',
    author='ForceFledgling',
    author_email='pvenv@icloud.com',
    license='MIT License',
    url='https://github.com/ForceFledgling/fapyui',
    install_requires=REQUIRES,
    setup_requires=SETUP_REQUIRES,
    tests_require=TEST_REQUIRES,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    platforms='any',
    python_requires='>=3',
    entry_points={'console_scripts': []},
    classifiers=[],
    keywords=[],
    zip_safe=False,
    test_suite='tests',
)
