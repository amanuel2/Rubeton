#						#
#   Rubeton MAKEFILE	#		
#						#

PLATFORM := $(shell uname)

run:
	$(info	OS is $(PLATFORM))
	$(warning  RUNNING GAME)
	chmod +x ./setup.py
	./setup.py
	

all : $(run)


#.PHONY: all test clean	
