import os

HEADER = (
  '\n'
  '# For both C and C++\n'
  'set(COMMON_FLAGS "-pedantic -Wall")\n'
  'if (WIN32)\n'
  '  set(COMMON_FLAGS "-D_WIN32_WINNT=0x501") # Set min. Windows version to XP\n'
  'else(WIN32)\n'
  '  set(COMMON_FLAGS "${COMMON_FLAGS} -pthread")\n'
  'endif (WIN32)\n'
  'if (NOT CMAKE_COMPILER_IS_GNUCC)\n'
  '  # Then, it must be clang/clang++\n'
  '  set(COMMON_FLAGS "${COMMON_FLAGS} -Qunused-arguments")\n'
  'endif ()\n'
  '\n'
  '# Force __LP64__ scheme on Mac OSX\n'
  'if(APPLE)\n'
  '  set(CMAKE_MACOSX_RPATH TRUE CACHE BOOL "Enables the MACOS_RPATH feature for MacOSX builds" FORCE)\n'
  '  set(COMMON_FLAGS "${COMMON_FLAGS} -m64")\n'
  'endif(APPLE)\n'
  '\n'
  '# For both RELEASE and DEBUG builds\n'
  'if(APPLE AND CMAKE_COMPILER_IS_GNUCC)\n'
  '  if(CMAKE_CXX_COMPILER_VERSION VERSION_LESS "4.4")\n'
  '    message(FATAL_ERROR "Minimum GCC version required on OSX is 4.4, but you have ${CMAKE_CXX_COMPILER_VERSION}")\n'
  '  endif()\n'
  '  set(COMMON_FLAGS "${COMMON_FLAGS} -Wno-long-long -Wno-variadic-macros")\n'
  '  set(COMMON_CXX_FLAGS "-std=c++0x")\n'
  '  set(COMMON_C_FLAGS "-std=c99")\n'
  'elseif(WIN32)\n'
  '  set(COMMON_CXX_FLAGS "-std=gnu++0x")\n'
  '  set(COMMON_C_FLAGS "-std=gnu99")\n'
  'else()\n'
  '  set(COMMON_CXX_FLAGS "-std=c++0x")\n'
  '  set(COMMON_C_FLAGS "-std=c99")\n'
  'endif()\n'
  '\n'
  '# These are used in type checks for cmake, be aware and don\'t change those\n'
  'set(CMAKE_CXX_FLAGS "${COMMON_CXX_FLAGS} ${COMMON_FLAGS} $ENV{CXXFLAGS} $ENV{CPPFLAGS}" CACHE STRING "Flags used by the compiler during release builds" FORCE)\n'
  'set(CMAKE_C_FLAGS "${COMMON_C_FLAGS} ${COMMON_FLAGS} $ENV{CFLAGS} $ENV{CPPFLAGS}" CACHE STRING "Flags used by the compiler during release builds" FORCE)\n'
  '\n'
  'set(BUILD_SHARED_LIBS "ON" CACHE BOOL "Build shared libs")\n\n'
)


class CMakeListsGenerator:
  """Generates a CMakeLists.txt file for the given sources, include directories and libraries."""

  def __init__(self, name, sources, target_directory, version = '1.0.0', include_directories = [], system_include_directories=[], libraries = [], library_directories = [], macros = []):
    """Initializes the CMakeLists generator.

    Keyword parameters:

    name : string
      The name of the library to generate

    sources : [string]
      The list of source files that should be compiled with CMake

    target_directory : [string]
      The directory where the final library should be placed

    version
      The version of the library, major.minor.patch

    include_directories : [string]
      A list of include directories required to compile the ``sources``

    system_include_directories : [string]
      A list of include directories required to compile the ``sources``, which will be added as SYSTEM includes

    libraries : [string]
      A list of libraries to be linked into the generated library

    library_directories : [string]
      A list of directories, where the ``libraries`` can be found.
      Note that the order of this list might be important.

    macros : [(string, string)]
      A list of preprocessor defines ``name=value`` that will be added to the compilation
    """

    self.name = name
    self.sources = sources
    self.target_directory = target_directory
    self.version = version
    self.includes = include_directories
    self.system_includes = system_include_directories
    self.libraries = libraries
    self.library_directories = library_directories
    self.macros = macros

  def generate(self, source_directory, build_directory):
    """Generates the CMakeLists.txt file in the given directory."""

    # check if CFLAGS or CXXFLAGS are set, and set them if not
    if 'CFLAGS' not in os.environ:
      os.environ['CFLAGS'] = '-O3 -g0 -DNDEBUG -mtune=native'
    if 'CXXFLAGS' not in os.environ:
      os.environ['CXXFLAGS'] = '-O3 -g0 -DNDEBUG -mtune=native'

    source_dir = os.path.realpath(source_directory)

    # source and target in different directories -> use absolute paths
    source_files = [os.path.join(source_dir, s) for s in self.sources]

    filename = os.path.join(build_directory, "CMakeLists.txt")
    with open(filename, 'w') as f:
      f.write('# WARNING! This file is automatically generated. Do not change its contents.\n\n')
      f.write('cmake_minimum_required(VERSION 2.8)\n')
      f.write('project(%s)\n' % self.name)
      f.write(HEADER)
      # add include directories
      for directory in self.includes:
        f.write('include_directories(%s)\n' % directory)
      for directory in self.system_includes:
        f.write('include_directories(SYSTEM %s)\n' % directory)
      # add link directories
      # TODO: handle RPATH and Non-RPATH differently (don't know, how, though)
      for directory in self.library_directories:
        f.write('link_directories(%s)\n' % directory)
      # add defines
      for macro in self.macros:
        f.write('add_definitions(-D%s=%s)\n' % macro)
      # compile this library
      f.write('\nadd_library(${PROJECT_NAME} \n\t' + "\n\t".join(source_files) + '\n)\n')
      f.write('set_target_properties(${PROJECT_NAME} PROPERTIES POSITION_INDEPENDENT_CODE TRUE)\n')
      f.write('set_target_properties(${PROJECT_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY %s)\n\n' % self.target_directory)
      # link libraries
      if self.libraries:
        f.write('target_link_libraries(${PROJECT_NAME} %s)\n\n' % " ".join(self.libraries))
