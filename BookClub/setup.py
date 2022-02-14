from setuptools import setup

setup(
    name='BookClub',
    packages=['BookClub'],
    include_package_data=True,
    install_requires=[
        'flask',
        'SQLAlchemy'
    ],

)
