from setuptools import setup, find_packages

setup(
    name='package_ilogger_Nouvelle_version',
    version='1.1.0',
    packages=find_packages(),
    author="Nelson Baouly",
    python_requires=">=2.9",
    url="https://github.com/BaoulyNelson/package_ilogger-version2.git",
    description="ceci est la nouvelle version du package ilogger",
    author_email="elconquistadorbaoulyn@gmail.com",
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'monprojetpython = monprojetpython.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        # Ajoutez d'autres classifications appropriées
    ],
)
