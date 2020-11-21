from setuptools import find_packages
from setuptools import setup

setup(
    name='simple_web_app',
    description="Simple web app for test CI",
    author='aromanov',
    url='',
    packages=find_packages('app'),
    package_dir={
        '': 'app'},
    include_package_data=True,
    keywords=[
        'web_app', 'test', 'flask'
    ],
    entry_points={
        'console_scripts': [
            'simple-web-app = app:main']},
)