find_package(PythonInterp 3.6 REQUIRED)
set(PYBIND11_PYTHON_VERSION 3.6)
set(PYBIND11_CPP_STANDARD -std=c++1z)
#
#find_package(Protobuf REQUIRED)
#include_directories(${Protobuf_INCLUDE_DIRS})
#
#include_directories(${CMAKE_CURRENT_BINARY_DIR})

include(GoogleTest)

#add_subdirectory(proto)

add_library(align_lib align.cc align.h)
target_link_libraries(align_lib PRIVATE absl::strings absl::str_format absl::flat_hash_map ${LINUX_EXTRA_LIBS})

add_executable(align_test align_test.cc)
target_link_libraries(align_test align_lib gtest gmock gtest_main ${LINUX_EXTRA_LIBS} absl::flat_hash_map)

add_test(align_test align_test)

pybind11_add_module(cspeech_lib pywrap.cc)

target_link_libraries(cspeech_lib PRIVATE align_lib absl::strings absl::str_format absl::flat_hash_map)

add_executable(align_benchmark align_benchmark.cc)
target_link_libraries(align_benchmark benchmark::benchmark align_lib absl::str_format )