location_dir = "./"

include(location_dir .. "conandeps.premake5.lua")

workspace("nanovg")
	location(location_dir)
	conan_setup()

	project("nanovg")
		kind "StaticLib"
		language "C++"
		cppdialect "C++17"
		targetdir = location_dir .. "bin/%{cfg.buildcfg}"

		files{
			"nanovg/src/**",
		}

		links{"OpenGL32.lib"}
		defines{"FONS_USE_FREETYPE"}

		filter "configurations:Debug"
			defines { "DEBUG" }
			symbols "On"

		filter "configurations:Release"
			defines { "NDEBUG" }
			optimize "On"