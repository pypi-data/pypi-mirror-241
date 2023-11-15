from setuptools import setup, find_packages

setup(
    name='deploy_sre',
    version='1.0.1',
    packages=find_packages(),
    # add any other dependencies your project needs
    install_requires=[
        'setuptools',
        'requests',
        # etc.
    ],
    entry_points={
        'console_scripts': [
            'deploy_sre = deploy_cmd.cli:main',
        ],
    },
)
