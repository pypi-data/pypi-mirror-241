from setuptools import setup, find_packages

setup(
    name='alog_auto_viton',
    version='1.0.8',
    packages=find_packages(),
    # add any other dependencies your project needs
    install_requires=[
        'setuptools',
        'requests',
        # etc.
    ],
    entry_points={
        'console_scripts': [
            'alog_auto = cli.main:main',
            'kol_info = cli.an_es:main',
        ],
    },
)
