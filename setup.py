from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forex-converter',
    packages=['forex-converter'],
    version='0.2',
    license='MIT',
    description='A simple python package for currency conversion',
    author='Jithin VG',
    author_email='jithinvg@accubits.com, aj@accubits.com',
    url='https://github.com/accubits/currency-converter-python.git',
    download_url='https://github.com/accubits/currency-converter-python/archive/0.3.tar.gz',
    keywords=['currency', 'forex-converter', 'currency converter', ' converter currency', 'forex'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Currency Conversion',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',

)
