# Contenido de setup.py

from setuptools import setup, find_packages

setup(
    name='contador_de_letrasv2.0',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'contador_de_letras = contador_de_letrasvs2.0.contador_de_letras:main',
        ],

    },
)
