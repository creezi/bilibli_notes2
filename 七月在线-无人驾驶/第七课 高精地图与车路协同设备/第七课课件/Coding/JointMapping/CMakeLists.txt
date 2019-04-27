cmake_minimum_required( VERSION 2.8 )
project( joinMap )

set( CMAKE_BUILD_TYPE Release )
set( CMAKE_CXX_FLAGS "-std=c++11 -O3" )

# opencv
include_directories( "/usr/local/opt/opencv@3/include" )

# eigen
include_directories( "/usr/include/eigen3/" )

# pcl
find_package( PCL REQUIRED COMPONENT common io )
include_directories( ${PCL_INCLUDE_DIRS} )
add_definitions( ${PCL_DEFINITIONS} )

add_executable( joinMap joinMap.cpp )
target_link_libraries( joinMap "/usr/local/opt/opencv@3/lib/" ${PCL_LIBRARIES} )
