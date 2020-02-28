from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()
    print(readme)

setup(
    name='forex-converter',
    version='0.5',
    license='MIT',
    description='A simple python package for currency conversion',
    long_description_content_type='text/x-rst',
    long_description=readme,
    author='Jithin VG',
    author_email='jithinvg@accubits.com, aj@accubits.com',
    url='https://github.com/accubits/currency-converter-python.git',
    download_url='https://github.com/accubits/currency-converter-python/archive/0.3.1.tar.gz',
    keywords=['currency', 'forex-converter', 'currency converter', ' converter currency', 'forex'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={
        "forex-converter": "forex-converter",
        "forex-converter.classes": "forex-converter/classes",
    },
    packages=["forex-converter", "forex-converter/classes"]

)
