from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = 'botdash.pro',
    version = '0.0.1',
    license = 'MIT',
    author = 'Seer#6054',
    author_email = 'admin@seer-software.com',
    description = 'API wrapper for BotDash',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = [
        'BotDash',
        'discord',
        'dashboard',
        'official'
    ],
    install_requires = [
        'setuptools',
        'requests',
        'six',
        'ujson'
    ],
    setup_requires = [
        'wheel'
    ],
    packages = find_packages()
)
