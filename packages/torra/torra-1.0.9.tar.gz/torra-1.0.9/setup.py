#setuptools.setup is looking at one argv parameter; to "build" and "install":
#python3 setup.py install

pkname='torra'

import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

from setuptools import setup
setup(name=pkname,
	version='1.0.9',
	packages=[pkname],
	#opt
	python_requires='>=3',
	install_requires=["appdirs>=1.4.3"],
	extras_require={#python-libtorrent has no src for rpi,is old,and bin is new but no src
		'libtorrent':['python-libtorrent>=2.0.2'],
		'libtorrent-bin':['python-libtorrent-bin>=2.0.2']
	},
	description='Torrent client',
	long_description=README,
	long_description_content_type="text/markdown",
	url='https://github.com/colin-i/tora',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	zip_safe=False,
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
