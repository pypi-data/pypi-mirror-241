from setuptools import setup, find_packages

setup(
    name='PruebasLoewe',
    version='4.2',
    packages=find_packages(),
    license='MIT',
    description='Una biblioteca de ejemplo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Carlos Moreno',
    author_email='carlos_moreno@loewe.com',
    url='https://github.com/tu_usuario/my_library',
    install_requires=[
        'numpy>=1.11.1',
        'pandas>=0.23.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)