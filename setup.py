from setuptools import setup, find_packages

setup(
    name='imhotep_pylint',
    version='0.0.3',
    packages=find_packages(),
    url='https://github.com/justinabrahms/imhotep_pylint',
    license='MIT',
    author='Justin Abrahms',
    author_email='justin@abrah.ms',
    description='An imhotep plugin for pylint validation',
    requires=['pylint'],
    entry_points={
        'imhotep_linters': [
            '.py = imhotep_pylint.plugin:PyLint'
        ],
    },
)
