version = "0.0.1"
from sys import version_info


try:
	from distutils.core import setup
except:
	try:
        	from setuptools import setup, find_packages
	except ImportError:
        	from ez_setup import use_setuptools
        	use_setuptools()
        	from setuptools import setup, find_packages


setup(name='vmrecaster',
    version=version,
    description="start and stop chroot sessions",
    long_description="""mount unmoun, kill remaining processes etc""",
    author="O M Synge",
    author_email="owen.synge@desy.de",
    license='Private',
    
    url = 'none',
    classifiers=[
        'Development Status :: 1 - UnStable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research'
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        ],

    scripts=['vmrecaster'],
    data_files=[('/usr/share/doc/vmrecaster-%s' % (version),['README','ChangeLog','LICENSE'])]
    )
