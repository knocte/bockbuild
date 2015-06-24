import os
from bockbuild.darwinprofile import DarwinProfile

class MonoDevelopPackages:
	def __init__ (self):
		# Toolchain
		self.packages.extend ([
			'autoconf.py',
			'automake.py',
			'libtool.py',
			'gettext.py',
			'pkg-config.py'
		])

		# Base Libraries
		self.packages.extend ([
			'libpng.py',
			'libjpeg.py',
			'libxml2.py',
			'freetype.py',
			'fontconfig.py',
			'pixman.py',
			'glib.py',
			'cairo.py',
			'pango.py',
			'atk.py',
			'intltool.py',
			'gtk+.py',
			'libglade.py',
			'sqlite.py'
		])

		# Theme
		self.packages.extend ([
			'librsvg.py',
			'icon-naming-utils.py',
			'hicolor-icon-theme.py',
			'tango-icon-theme.py',
			'murrine.py'
		])

		# Mono
		self.packages.extend ([
			'mono.py',
			'gtk-sharp.py',
			'mono-addins.py',
		])

		self.packages = [os.path.join ('..', '..', 'packages', p)
			for p in self.packages]

		self.packages.extend ([
			'monodevelop-svn.py'
		])
