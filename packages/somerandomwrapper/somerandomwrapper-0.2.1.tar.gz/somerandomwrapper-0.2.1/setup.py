from setuptools import setup

with open('README.md', 'r') as file:
    description = file.read()

setup(
    name='somerandomwrapper',
    version='0.2.1',
    description='A small local Wrapper for Some Random API written on Python.',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=['somerandomwrapper'],
    author_email='support@kerdokan.co',
    url='https://github.com/Kerdokan/SomeRandomWrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
        'googletrans'
    ]
)