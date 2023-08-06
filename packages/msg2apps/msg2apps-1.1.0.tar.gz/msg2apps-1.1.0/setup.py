from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='msg2apps',
    version='v1.1.0',
    description='A module for sending messages to communication apps',
    py_modules=['msg2apps'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Daksimz',
    author_email='daksimzhang@gmail.com',
    url='https://github.com/daksim/msg2apps',
    requires=['requests', 'json'],
    license='MIT'
)