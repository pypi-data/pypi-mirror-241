from setuptools import setup, find_packages

setup(
    name='alog_cmd',
    version='1.1.0',
    packages=find_packages(),
    # add any other dependencies your project needs
    install_requires=[
        'setuptools',
        'requests',
        # etc.
    ],
    entry_points={
        'console_scripts': [
            'kol_info = cli.an_es:main',
            'auto = cli.auto_test:main',
        ],
    },
)
