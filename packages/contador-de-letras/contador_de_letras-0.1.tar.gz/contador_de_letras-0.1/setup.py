# Contenido de setup.py

from setuptools import setup, find_packages

setup(
    name='contador_de_letras',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'contador_de_letras = contador_de_letras.contador_de_letras:main',
        ],

    },
)
