SET(CMAKE_C_COMPILER avr-g++)
SET(CMAKE_CXX_COMPILER avr-g++)

SET(CWARN "-Wall")
SET(COPT "-Os")
SET(CMCU "-fno-exceptions -mmcu=atmega324p")
SET(CDEFS "-DF_CPU=20000000L")


SET(CFLAGS "${CMCU} ${CDEFS} ${COPT} ${CWARN}")
SET(CXXFLAGS "${CMCU} ${CDEFS} ${COPT} ${CWARN}")
SET(CMAKE_SHARED_LIBRARY_LINK_CXX_FLAGS "")
SET(CMAKE_EXE_LINK_CXX_FLAGS "--gc-sections")

SET(CMAKE_C_FLAGS  ${CFLAGS})
SET(CMAKE_CXX_FLAGS ${CXXFLAGS})
