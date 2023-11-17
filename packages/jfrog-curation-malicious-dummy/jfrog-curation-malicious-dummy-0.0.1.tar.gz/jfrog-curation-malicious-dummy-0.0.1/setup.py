from setuptools import setup

setup(
    name='jfrog-curation-malicious-dummy',
    version='0.0.1',
    packages=['jfrog_curation_malicious_dummy'],
    entry_points={
        'console_scripts': [
            'entry_point=main:hello_world',
        ],
    },
)