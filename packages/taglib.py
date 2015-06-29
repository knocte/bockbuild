class TaglibPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'taglib', '1.8',
			sources = [
				'http://taglib.github.io/releases/%{name}-%{version}.tar.gz'
			])

	def build (self):
		self.sh (
			# Let's set a bunch of variables, to make cmake feel loved
			'CMAKE_PREFIX_PATH=%{prefix}',
			'CMAKE_LIBRARY_PATH=%{prefix}/lib',
			'CMAKE_INSTALL_PREFIX=%{prefix}',

			# build and install
			'cmake -DCMAKE_INSTALL_PREFIX=%{prefix} . && make all install',
			)

TaglibPackage ()
