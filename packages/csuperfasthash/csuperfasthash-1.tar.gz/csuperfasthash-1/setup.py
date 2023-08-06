from setuptools import setup
from Cython.Build import cythonize

setup(
	name = 'csuperfasthash',
	packages = ['csuperfasthash'],
	version = '1',
	license='LGPL',
	description = 'Cython port of SuperHash',
	author = 'JUAN MENDEZ',
	author_email = 'vpsink@gmail.com',
	url = 'https://gitlab.com/lifelover/superfasthash',
	download_url = 'https://gitlab.com/lifelover/superfasthash/-/archive/master/superfasthash-master.tar.gz',
	keywords = ['superfasthash', 'cython', 'python'],
	install_requires=[
		'cython',
	],
	py_modules=['superfasthash'],             # Name of the python package
	ext_modules = cythonize("superfasthash/src/superfasthash.pyx")
)
