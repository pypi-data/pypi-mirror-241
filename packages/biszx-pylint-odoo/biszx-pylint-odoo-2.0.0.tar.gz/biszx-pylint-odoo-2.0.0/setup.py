from setuptools import find_packages, setup

setup(
    version='2.0.0',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    test_suite='biszx_pylint_odoo.tests',
    packages=find_packages(),
    package_dir={'biszx_pylint_odoo': 'biszx_pylint_odoo'},
    install_requires=[
        'astroid',
        'pylint-odoo',
    ],
)
