from distutils.core import setup

setup(
    name='currency-converter',
    packages=['currency-converter'],
    version='0.1',
    license='MIT',
    description='A simple python package for currency conversion',
    author='Jithin VG',
    author_email='jithinvg@accubits.com, aj@accubits.com',  # Type in your E-Mail
    url='https://github.com/accubits/currency-converter-python.git',  # Provide either the link to your github or to your website
    download_url='https://github.com/accubits/currency-converter-python/archive/0.1.tar.gz',  # I explain this later on
    keywords=['currency', 'currency-converter', 'currency converter', ' converter currency'],  # Keywords that define your package best
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
)
