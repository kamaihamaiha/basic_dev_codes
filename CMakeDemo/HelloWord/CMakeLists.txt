cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

project(Hello LANGUAGES CXX)


set(demo_dir ${PROJECT_SOURCE_DIR}/demo)
file(GLOB demo_codes ${demo_dir}/*.cpp)

foreach(code_file ${demo_codes})
    # 将 cpp 文件的全路径转成 文件名
    string(REGEX MATCH "[^/]+$" demo_file ${code_file}) 
    message("code_file: "${code_file} ", demo_file: " ${demo_file})
    # 将 cpp 文件名转成 没有扩展名的文件名，作为下一步可执行程序名
    string(REPLACE ".cpp" "" demo_basename ${demo_file})
    message("demo_basename: " ${demo_basename})
    add_executable(${demo_basename} ${code_file})
    
endforeach()
