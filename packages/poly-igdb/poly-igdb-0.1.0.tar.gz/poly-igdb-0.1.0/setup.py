from setuptools import setup, find_packages

setup(
    name='poly-igdb',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        #requests,
        #json
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # If your library includes any command-line scripts, list them here
        ],
    },
)