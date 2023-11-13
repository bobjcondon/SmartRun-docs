# https://medium.com/practical-coding/c-documentation-with-doxygen-cmake-sphinx-breathe-for-those-of-use-who-are-totally-lost-7d555386fe13
# https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/
cmake_minimum_required (VERSION 3.20)
project (
    "SmartRun "
    VERSION 1.0
    LANGUAGES CXX
)
set(CMAKE_MODULE_PATH "cmake" ${CMAKE_MODULE_PATH})

#find_package(Doxygen REQUIRED)
# find_package (Python3 COMPONENTS Interpreter)
# execute_process (COMMAND "${Python3_EXECUTABLE}" -m venv "/path/to/venv")
# 
# # Here is the trick
# ## update the environment with VIRTUAL_ENV variable (mimic the activate script)
# set (ENV{VIRTUAL_ENV} "/path/to/venv")
# ## change the context of the search
# set (Python3_FIND_VIRTUALENV FIRST)
# ## unset Python3_EXECUTABLE because it is also an input variable (see documentation, Artifacts Specification section)
# unset (Python3_EXECUTABLE)
# ## Launch a new search
# find_package (Python3 COMPONENTS Interpreter Development)

find_package(Sphinx REQUIRED)

set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR}/sphinx)
set(INDEX_HTML ${SPHINX_BUILD}/index.html)
set(WIP_HTML ${SPHINX_BUILD}/index.html)

# We don't build slides currently because hieroglyph seems broken on ec machines
set(SPHINX_SLIDES ${SPHINX_BUILD}/slides)
set(SPHINX_INSTALL_DIR ../../docs)

message("SPHINX_EXECUTABLE ${SPHINX_EXECUTABLE}")
message("CMAKE_BINARY_DIR ${CMAKE_BINARY_DIR}")
message("SPHINX_INSTALL_DIR ${SPHINX_INSTALL_DIR}")


# Regenerate html when:
# - Our doc files have been updated or the Sphinx config has been updated
add_custom_command( OUTPUT ${INDEX_HTML}
                  COMMAND  
                  ${SPHINX_EXECUTABLE} -b html 
                  ${SPHINX_SOURCE} ${SPHINX_BUILD}
                  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                  DEPENDS
                  # Other docs files you want to track should go here (or in some variable)
                  ${SPHINX_SOURCE}/index.rst
                  ${SPHINX_SOURCE}/Jupyter.rst
                  ${SPHINX_SOURCE}/SmartRun.rst
                   MAIN_DEPENDENCY ${SPHINX_SOURCE}/conf.py
                   COMMENT "Generating documentation with Sphinx"
)

add_custom_command(OUTPUT ${WIP_HTML}
                  COMMAND  
                  ${SPHINX_EXECUTABLE} -b html 
                  ${SPHINX_SOURCE} ${SPHINX_BUILD}
                  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                  DEPENDS
                  # Other docs files you want to track should go here (or in some variable)
                  ${SPHINX_SOURCE}/wip.rst
                  ${SPHINX_SOURCE}/flow.rst
                  ${SPHINX_SOURCE}/todo.rst
                   MAIN_DEPENDENCY ${SPHINX_SOURCE}/conf.py
                   COMMENT "Generating documentation with Sphinx")

add_custom_command(OUTPUT ${SPHINX_SLIDES}
                   COMMAND 
                   ${SPHINX_EXECUTABLE} -b slides 
                   ${SPHINX_SOURCE} ${SPHINX_SLIDES}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                   DEPENDS
                   # Other docs files you want to track should go here (or in some variable)
                   ${SPHINX_SOURCE}/InstructorLedTraining.rst
                    MAIN_DEPENDENCY ${SPHINX_SOURCE}/conf.py
                    COMMENT "Generating documentation with Sphinx")
 

                   # Nice named target so we can run the job easily
add_custom_target(Sphinx ALL DEPENDS ${INDEX_HTML}  )

add_custom_target(install_docs ALL 
   COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_BINARY_DIR}/sphinx ${SPHINX_INSTALL_DIR}
   DEPENDS Sphinx)

