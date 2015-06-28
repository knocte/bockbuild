class TangoIconThemePackage (FreeDesktopPackage):
        def __init__ (self):
		FreeDesktopPackage.__init__ (self, 'tango', 'tango-icon-theme', '0.8.90',
			configure_flags  = [
				'--disable-icon-framing'
			]
		)

	# workaround https://bugs.freedesktop.org/show_bug.cgi?id=91134
	def install (self):
		self.package_prefix = self.profile.prefix
		self.stage_root = self.profile.stage_root
		# see http://cgit.freedesktop.org/gstreamer-sdk/icon-naming-utils/tree/icon-name-mapping.pl.in?h=sdk-0.8.7
		self.makeinstall = 'INU_DATA_DIR=%{stage_root}%{package_prefix}/share/icon-naming-utils make install DESTDIR=%{stage_root}'
		Package.install (self)

TangoIconThemePackage()
