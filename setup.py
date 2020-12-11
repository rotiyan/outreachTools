
setup(
     name='outreachTools',
     version='0.0.1',
     description='package for tracking charge particles',
     )


from setuptools import setup
import sys

requirements = ['h5py','h5hep']

if sys.version_info < (3, 3):
    sys.stdout.write("At least Python 3.3 is required.\n")
    sys.exit(1)
elif sys.version_info < (3, 6):
    # typing was added in 3.5, and we rely on critical features that were
    # introduced in 3.5.2+, so for versions older than 3.6 we rely on
    # a backport
    requirements.append('backports.typing')

#import versioneer

setup(
    name='outreachTools',
    version="0.1",
    description='Simple tools for accessing particle physics data for outreach and education',
    url='https://github.com/rotiyan/outreachTools.git'
    author='R Narayan',
    author_email='rohin.tn@gmail.com',
    license='GNU General Public License v3.0',
    packages = ['outreachTools'],
    install_requires = ['numpy']
    #tests_require = ['pytest', 'pytest-cov'],
    classifiers=[ # HAVE TO FIX ALL THIS
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'License :: Public Domain',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
    ],
)
