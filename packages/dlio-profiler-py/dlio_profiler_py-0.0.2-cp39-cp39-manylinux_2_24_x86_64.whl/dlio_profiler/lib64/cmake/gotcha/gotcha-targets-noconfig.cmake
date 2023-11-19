#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gotcha" for configuration ""
set_property(TARGET gotcha APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(gotcha PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib64/libgotcha.so.2.2.2"
  IMPORTED_SONAME_NOCONFIG "libgotcha.so.2"
  )

list(APPEND _IMPORT_CHECK_TARGETS gotcha )
list(APPEND _IMPORT_CHECK_FILES_FOR_gotcha "${_IMPORT_PREFIX}/lib64/libgotcha.so.2.2.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
