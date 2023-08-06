from setuptools import setup, find_packages
from os.path import dirname, join

# Forked directly from https://github.com/LedgerHQ/btchip-python

here = dirname(__file__)
setup(
    name='gewel-btchip-python',
    version='0.1.1',
    author='gewel',
    author_email='mb@gewel.io',
    description='Python library to communicate with Ledger Nano dongle (Gewel fork)',
    long_description=open(join(here, 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gewelio/gewel-btchip-python',
    packages=find_packages(),
    install_requires=[
        'hidapi>=0.7.99'
    ],
    extras_require = {
	    'smartcard': [
            'python-pyscard>=1.6.12-4build1',
            'ecdsa>=0.9'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
	    'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
	    'Operating System :: MacOS :: MacOS X'
    ]
)
