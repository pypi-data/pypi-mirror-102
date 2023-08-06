from setuptools import setup

setup(
    name='pykahoot',
    version='1.0.0',
    packages=['pykahoot'],
    scripts=['scripts/chromedriver.exe'],
    description='A working kahoot python API, to replace the terminated KahootPY',
    long_description=open('README.txt').read() + '\n\n'
    )
