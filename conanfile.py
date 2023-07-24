from conan import ConanFile

class MoxPPRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "PremakeDeps"

    def requirements(self):
        # Unit test
        # self.requires("gtest/cci.20210126")

        # Logging
        self.requires("spdlog/1.11.0")

        # Project files
        self.requires("pugixml/1.13")
        self.requires("nlohmann_json/3.11.2")


    def configure(self):
    # This only works on windows (we added this so that you can see
    # how to change settings of packages)
    # self.options["spdlog"].wchar_support = True

    # Spdlog allow wchar + shared
        self.options["spdlog"].wchar_support = True
        self.options["spdlog"].shared = True

    # FMT
    # Make shared
        self.options["fmt"].shared = True

    # PUGI
    # Make shared
        self.options["pugixml"].shared = True

    # GTest
    # No generate main
        # self.options["gtest"].no_main = True
    #pass

