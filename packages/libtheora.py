class LibTheoraPackage (XiphPackage):
	def __init__ (self):
		XiphPackage.__init__ (self, 'theora', 'libtheora', '1.1.1',
			configure_flags = [
				'--disable-docs',
				'--disable-oggtest',
				'--disable-vorbistest',
				'--disable-example',
				'--disable-asm'
			])

		if Package.profile.name == 'darwin':
			self.sources.extend ([
				# Fix building with libpng 1.6+
				'patches/libtheoraMacPorts1.diff',
				# Patch from MacPorts to fix compilation with some versions of xcode's clang
				'patches/libtheoraMacPorts2.diff'
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			self.sh ('patch -p1 --ignore-whitespace < "%{local_sources[1]}"')
			for p in range (2, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{local_sources[' + str (p) + ']}"')

LibTheoraPackage ()
