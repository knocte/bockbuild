class CmakePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'cmake', '3.2.2',
			sources = ['http://www.cmake.org/files/v3.2/%{name}-%{version}.tar.gz'])

		self.sources.extend ([
			#https://github.com/BansheeMediaPlayer/bockbuild/blob/master/packages/cmake.py
			'patches/cmake/macports.cmake',

			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-CMakeFindFrameworks.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-FindFreetype.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-FindQt4.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-Platform-Darwin.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-Platform-Darwin-Initialize.cmake.diff',
			'https://trac.macports.org/export/136239/trunk/dports/devel/cmake/files/patch-Modules-noArchCheck.diff'
		])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p0 --ignore-whitespace < "%{sources[' + str (p) + ']}"')
			self.sh ('cp %{sources[1]} .')
			self.sh ('sed -ie "s:__PREFIX__:%{prefix}:g" "macports.cmake"')
			self.sh ('sed -ie "s:__PREFIX__:%{prefix}:g" "Modules/CMakeFindFrameworks.cmake"')

	def build (self):

		self.package_prefix = self.profile.prefix
		self.mac_sdk_path = self.profile.mac_sdk_path
		self.target_osx = self.profile.target_osx
		print '_______________________going to check SDKsss BEFORE CMAKE %s' % self.target_osx

		self.sh (
			# Let's set a bunch of variables, to make cmake feel loved
			'export CMAKE_PREFIX_PATH=%{package_prefix}',
			'export CMAKE_LIBRARY_PATH=%{package_prefix}/lib',
			'export CMAKE_INSTALL_PREFIX=%{package_prefix}',
			'export CMAKE_OSX_SYSROOT="%s"' % self.mac_sdk_path,
			'export CMAKE_OSX_DEPLOYMENT_TARGET=%s' % self.target_osx,

			# and let's bootstrap
			'./bootstrap --init=macports.cmake --prefix=%{package_prefix} --docdir=share/doc/cmake',

			# build and install
			'CMAKE_OSX_SYSROOT=%{mac_sdk_path} make; make install',
			)

CmakePackage ()
