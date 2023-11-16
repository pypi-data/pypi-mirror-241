from setuptools import setup, find_packages

setup(
    name='PruebasLoewe',
    version='4.1',
    description='Paquete de saludos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Carlos Moreno Barrado',
    author_email='carlos_moreno@loewe.com',
    url='http://www.loewe.com',
    license_files=['LICENSE'],
    packages=find_packages(),
    install_requires=['numpy']
)