cmake_minimum_required(VERSION 3.15)

project(PackageTest CXX)

find_package(nanovg CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example nanovg::nanovg)