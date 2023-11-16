cmake_minimum_required(VERSION 3.20)

set(Boost_VERSION_STRING 1.83.0)

project(cmeel-boost VERSION ${Boost_VERSION_STRING})

# helper strings for Boost
string(REPLACE "." "_" Boost_VERSION_UNDERSCORES ${Boost_VERSION_STRING})
set(Boost_ARCHIVE "boost_${Boost_VERSION_UNDERSCORES}.tar.bz2")

find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

configure_file(python.jam.in python.jam)

if(APPLE)
  set(ORIGIN "@loader_path")
else()
  set(ORIGIN "\$ORIGIN")
endif()

set(CONFIGURE_COMMAND "./bootstrap.sh" "--prefix=${CMAKE_INSTALL_PREFIX}")

set(BUILD_COMMAND "./b2" "hardcode-dll-paths=true" "dll-path='${ORIGIN}'"
                  "link=shared" "python=3.${Python3_VERSION_MINOR}")

if(APPLE AND CMAKE_HOST_SYSTEM_PROCESSOR STREQUAL "arm64")
  set(CONFIGURE_COMMAND ${CONFIGURE_COMMAND} "cxxflags=\"-arch arm64\""
                        "cflags=\"-arch arm64\"")
  set(BUILD_COMMAND
      ${BUILD_COMMAND} "toolset=clang-darwin" "target-os=darwin"
      "architecture=arm" "abi=aapcs" "cxxflags=\"-arch arm64\""
      "cflags=\"-arch arm64\"" "linkflags=\"-arch arm64\"")
endif()

message(STATUS "CONFIGURE_COMMAND: ${CONFIGURE_COMMAND}")
message(STATUS "BUILD_COMMAND: ${BUILD_COMMAND}")

include(ExternalProject)
ExternalProject_Add(
  Boost
  URL "https://boostorg.jfrog.io/artifactory/main/release/${Boost_VERSION_STRING}/source/${Boost_ARCHIVE}"
  URL_HASH
    "SHA256=6478edfe2f3305127cffe8caf73ea0176c53769f4bf1585be237eb30798c3b8e"
  DOWNLOAD_EXTRACT_TIMESTAMP OFF
  BUILD_IN_SOURCE ON
  CONFIGURE_COMMAND ${CONFIGURE_COMMAND}
  # append python configuration to generated project-config.jam
  COMMAND
    ${Python3_EXECUTABLE} "-c"
    "with open('${CMAKE_BINARY_DIR}/python.jam', 'a+') as a, open('project-config.jam') as b: a.write(b.read())"
  COMMAND ${CMAKE_COMMAND} "-E" "rename" "${CMAKE_BINARY_DIR}/python.jam"
          "project-config.jam"
  BUILD_COMMAND ${BUILD_COMMAND}
  INSTALL_COMMAND ${BUILD_COMMAND} "install")

# dummy file for install target
install(FILES README.md DESTINATION share/cmeel-boost/)
