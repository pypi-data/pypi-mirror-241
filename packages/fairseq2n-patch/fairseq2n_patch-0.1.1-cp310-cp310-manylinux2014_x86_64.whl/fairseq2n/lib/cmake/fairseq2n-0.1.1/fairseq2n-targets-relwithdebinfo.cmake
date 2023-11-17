#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "fairseq2n::fairseq2n" for configuration "RelWithDebInfo"
set_property(TARGET fairseq2n::fairseq2n APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(fairseq2n::fairseq2n PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELWITHDEBINFO "SndFile::sndfile;TBB::tbb"
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libfairseq2n.so.0.1.1"
  IMPORTED_SONAME_RELWITHDEBINFO "libfairseq2n.so.0"
  )

list(APPEND _cmake_import_check_targets fairseq2n::fairseq2n )
list(APPEND _cmake_import_check_files_for_fairseq2n::fairseq2n "${_IMPORT_PREFIX}/lib/libfairseq2n.so.0.1.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
