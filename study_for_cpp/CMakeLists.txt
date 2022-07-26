cmake_minimum_required(VERSION 3.17)
project(study_for_cpp)

set(CMAKE_CXX_STANDARD 11)

# 头文件
include_directories(
        chapter_1/section_5/*.h
        chapter_2/section_6/*.h
        chapter_6/section_1/*.h
        )

# 不能添加多个源文件，想运行哪个源文件，临时放开（注释）
add_executable(main chapter_6/section_1/6.1.2.cpp)
#add_executable(main chapter_6/section_1/6.1.1.cpp)
#add_executable(main chapter_6/section_1/6.1.cpp)
#add_executable(main chapter_5/5.6.cpp)
#add_executable(main chapter_4/4.6.cpp)
#add_executable(main chapter_4/4.9.cpp)
#add_executable(main chapter_4/4.8.cpp)
#add_executable(main chapter_4/main_6.cpp)
#add_executable(main chapter_3/section_5/main_5.cpp)
#add_executable(main chapter_3/section_5/main_3.cpp)
#add_executable(main chapter_3/section_5/3.5.4.cpp)
#add_executable(main chapter_3/section_5/3.5.3.cpp)
#add_executable(main chapter_3/section_5/3.5.2.cpp)
#add_executable(main chapter_3/section_5/3.5.1.cpp)
#add_executable(main chapter_3/section_5/main_1.cpp)
#add_executable(main chapter_3/section_4/main.cpp)
#add_executable(main chapter_3/section_3/main_3.cpp)
#add_executable(main chapter_3/section_3/main.cpp)
#add_executable(main chapter_3/section_2/main_for.cpp)
#add_executable(main chapter_3/section_2/main.cpp)
#add_executable(main chapter_3/section_1/main.cpp)
#add_executable(main chapter_2/section_6/main.cpp)
#add_executable(main chapter_2/section_3/main.cpp)
#add_executable(main chapter_2/section_2/main.cpp)
#add_executable(main chapter_2/section_1/Main.cpp)
#add_executable(main-from-section_6 chapter_1/section_6/main_6.cpp)
#add_executable(main-from-section_5 chapter_1/section_5/main_5.cpp)
#add_executable(main-from-section_4 chapter_1/section_4/main_4.cpp)
#add_executable(main-from-section_2 chapter_1/section_2/main_2.cpp)
#add_executable(main-from-section_1 chapter_1/section_1/main.cpp)