from conans import ConanFile, tools

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
		"premake_generator/master@enhex/stable"
	)
	
	def source(self):
		self.run("git clone --depth=1 https://github.com/memononen/nanovg.git")

	def build(self):
		from premake import run_premake
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

