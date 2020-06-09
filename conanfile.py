from conans import ConanFile, tools

# automatically choose Premake generator
def run_premake(self):
	if "Visual Studio" in self.settings.compiler:
		_visuals = {'8': '2005',
					'9': '2008',
					'10': '2010',
					'11': '2012',
					'12': '2013',
					'14': '2015',
					'15': '2017',
					'16': '2019'}
		premake_command = "premake5 vs%s" % _visuals.get(str(self.settings.compiler.version), "UnknownVersion %s" % str(self.settings.compiler.version))
		self.run(premake_command)
	else:
		self.run("premake5 gmake2")

class NanovgConan(ConanFile):
	name = "nanovg"
	version = "master"
	license = "zlib"
	url = "https://github.com/Enhex/conan-nanovg"
	description = "Antialiased 2D vector drawing library on top of OpenGL for UI and visualizations."
	settings = "os", "compiler", "build_type", "arch"
	options = {"shared": [True, False]}
	default_options = "shared=False"
	generators = "premake"
	exports = "premake5.lua"
	requires = (
		"freetype/2.10.1"
	)
	
	def source(self):
		self.run("git clone --depth=1 https://github.com/memononen/nanovg.git")

	def configure(self):
		self.options["freetype"].with_png = False;
		self.options["freetype"].with_zlib = False;
	
	def build(self):
		run_premake(self)
		self.run("build")
		
	def package(self):
		self.copy("*.h", dst="include", src="nanovg/src")
		self.copy("*.lib", dst="lib", keep_path=False)
		self.copy("*.dll", dst="bin", keep_path=False)
		self.copy("*.so", dst="lib", keep_path=False)
		self.copy("*.dylib", dst="lib", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["nanovg"]

