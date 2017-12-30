import os
import re
from setuptools import setup


def get_version():
    """Get version information from __init__.py file"""
    pwd = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(pwd, 'multiword_tokenization/__init__.py')
    re_version = re.compile(r"__version__ = '([0-9a-z\.]+)'")
    with open(file_path, 'r') as fp:
        lines = fp.read().splitlines()
        for line in lines:
            match = re_version.match(line)
            if match:
                return match.group(1)
    raise ValueError('Version information not found.')


setup(
    name='multiword_tokenization',
    packages=['multiword_tokenization'],
    version=get_version(),
    description='Multi-word tokenization',
    author='Katsuya Horiuchi',
    author_email='katsuya.horiuchi.biz@gmail.com',
    url='https://github.com/katsuya-horiuchi/multiword_tokenization',
    keywords=['NLP', 'tokenization'],
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
