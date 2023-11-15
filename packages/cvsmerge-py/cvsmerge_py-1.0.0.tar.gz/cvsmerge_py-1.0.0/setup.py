from setuptools import setup, find_packages

setup(
    name='cvsmerge_py',
    version='1.0.0',
    author='Sadlie Rose Indiana Nazaire et Adelson Polycarpe',
    author_email='nazairesadlierose@gmail.com',
    description='module permettant de fusionner les data de deux fichier csv vers un seul fichier csv',
    long_description_content_type='text/markdown',
    url='https://github.com/SadlieRose/Cvsmerge-_python_module.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)