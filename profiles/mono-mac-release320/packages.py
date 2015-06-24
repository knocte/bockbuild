import os
from bockbuild.darwinprofile import DarwinProfile

class MonoReleasePackages:
	def __init__(self):

		# Toolchain
		#package order is very important.
		#autoconf and automake don't depend on CC
		#ccache uses a different CC since it's not installed yet
		#every thing after ccache needs a working ccache
		self.packages.extend ([
			'autoconf.py',
			'automake.py',
			'ccache.py',
			'libtool.py',
			'xz.py',
			'tar.py',
			'gettext.py',
			'pkg-config.py'
		])

		#needed to autogen gtk+
		self.packages.extend ([
			'gtk-osx-docbook.py',
			'gtk-doc.py',
		])

		# # Base Libraries
		self.packages.extend([
				'libpng.py',
				'libjpeg.py',
				'libtiff.py',
				'libgif.py',
				'libxml2.py',
				'freetype.py',
				'fontconfig.py',
				'pixman.py',
				'libffi.py',
				'glib.py',
				'cairo.py',
				'pango.py',
				'atk.py',
				'intltool.py',
				'gdk-pixbuf.py',
				'gtk+.py',
				'libglade.py',
				'sqlite.py',
				'expat.py',
				'ige-mac-integration.py'
				])

		# # Theme
		self.packages.extend([
				'libcroco.py',
				'librsvg.py',
				'hicolor-icon-theme.py',
				'gtk-engines.py',
				'murrine.py',
				'xamarin-gtk-theme.py',
				'gtk-quartz-engine.py'
				])

		# Mono
		self.packages.extend([
				'mono-llvm.py',
				'mono-master.py',
				'libgdiplus.py',
				'xsp.py',
				'gtk-sharp-2.12-release.py',
				'boo.py',
				# 'nant.py',
				'ironlangs.py',
				'fsharp-3.0.py',
				'mono-addins.py',
				'mono-basic.py',
				])

		self.packages = [os.path.join('..', '..', 'packages', p) for p in self.packages]
