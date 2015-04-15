from VmRecast.__version__ import version
from sys import version_info

if version_info < (2, 6):
    import sys
    print "Please use a newer version of python"
    sys.exit(1)


try:
    from setuptools import setup, find_packages
except ImportError:
	try:
            from distutils.core import setup
	except ImportError:
            from ez_setup import use_setuptools
            use_setuptools()
            from setuptools import setup, find_packages
# we want this module for nosetests
try:
    import multiprocessing
except ImportError:
    # its not critical if this fails though.
    pass

setup(name='vmrecaster',
    version=version,
    description="recast images in an image list",
    long_description="""recast images in an image list""",
    author="O M Synge",
    author_email="owen.synge@desy.de",
    license='Private',
    packages = ['VmRecast'],
    url = 'https://github.com/hepix-virtualisation/vmcatcher',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research'
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ],
    install_requires=[
       "vmcatcher",
        ],
    scripts=['vmrecaster'],
    data_files=[('/usr/share/doc/vmrecaster-%s' % (version),['README','ChangeLog','LICENSE'])],
    tests_require=[
        'coverage >= 3.0',
        'nose >= 1.1.0',
        'mock',
        'SQLAlchemy >= 0.7.8',
    ],
    setup_requires=[
        'nose',
        'SQLAlchemy >= 0.7.8',
    ],
    test_suite = 'nose.collector',
    )
