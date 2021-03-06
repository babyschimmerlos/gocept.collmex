import os.path
from setuptools import setup, find_packages


setup(
    name='gocept.collmex',
    version='1.10.dev0',
    author='gocept',
    author_email='mail@gocept.com',
    description='Python-bindings for the Collmex import/export API',
    url='https://github.com/gocept/gocept.collmex',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    long_description=(
        open('README.rst').read() +
        '\n\n' +
        open(os.path.join('src', 'gocept', 'collmex', 'doctest.rst')).read() +
        '\n\n' +
        open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL 2.1',
    namespace_packages=['gocept'],
    install_requires=[
        'gocept.cache >= 0.6.1',
        'setuptools >= 1.0',
        'transaction >= 1.4',
        'zope.deprecation >= 4.0',
        'zope.interface >= 4.0',
        'webtest >= 2.0',
        'wsgiproxy2',
        'six >= 1.7.0'
    ],
    extras_require=dict(
        test=[
            'zope.testing >= 4.0',
            'mock >= 1.0',
        ]),
)
