#(1) Pimydoc

Pimydoc : [P]lease [i]nsert my doc[umentation]

A Python3/GPLv3/OSX-Linux-Windows/CLI project, using no additional modules
than the ones installed with Python3.

Insert documentation in text files and update it.

#(2) purpose

Pimydoc inserts in source files the text paragraphs stored in "pimydoc", the
documentation source file. Moreover, the script updates the text paragraphs
already present in the source files if the documentation source file has
changed.

#(3) installation and tests

    Don't forget : Pimydoc is Python3 project, not a Python2 project !

    $ pip3 install pimydoc

    or

    $ wget https://raw.githubusercontent.com/suizokukan/pimydoc/master/pimydoc/pimydoc.py
    Since pimydoc.py is a stand-alone file, you may place this file in the target directory.

    How to run the tests :
    
    $ python -m unittest tests/tests.py

    or
    
    $ nosetests

#(4) workflow

    $ pimydoc -h
    ... will display all known parameters.
    $ pimydoc --version
    ... will display the version of the current script.

#(5) project's author and project's name

Xavier Faure (suizokukan / 94.23.197.37) : suizokukan @T orange D@T fr

Pimydoc : [P]lease [i]nsert my doc[umentation]

#(6) arguments

	usage: pimydoc.py [-h] [--sourcepath SOURCEPATH] [--docsrcfile DOCSRCFILE]
	                  [--verbose {0,1,2}] [-vv] [-vvv] [--version] [--remove]
	                  [--securitymode]

	Pimydoc project, v.0.1.2

	optional arguments:
	  -h, --help            show this help message and exit
	  --sourcepath SOURCEPATH
	                        source path of the code (default:
	                        /Users/admin/pimydoc)
	  --docsrcfile DOCSRCFILE
	                        source documentation file name (default:
	                        /Users/admin/pimydoc/pimydoc)
	  --verbose {0,1,2}     degree of verbosity of the output. 0 : only the error
	                        messages; 1 : all messages except debug messages; 2 :
	                        all messages, including debug messages; See also the
	                        -vv and -vvv options. (default: 1)
	  -vv                   verbosity set to 1 (all messages except debug
	                        messages). (default: False)
	  -vvv                  verbosity set to 2 (all messages, including debug
	                        messages). (default: False)
	  --version, -v         show the version and exit
	  --remove, -r          Remove every pimydoc line in all the files of the
	                        source directory (default: False)
	  --securitymode, -s    Security mode : backup files created by Pimdoc are not
	                        deleted (default: False)
	
#(7) history / future versions

- 0.1.7 : documentation/alpha -> beta
- 0.1.6 : # and //

v 0.1.5(alpha) (2016_08_27) first unittests
    • add the "tests/" directory
    
    • fixed a bug in DocumentationSource.__init__() : .format() syntax has to
      be used anywhere except for logging messages.
    • fixed a bug in remove_and_return_linefeed() : I forgot to return an empty
      linefeed if the last characters are not "\n", "\r" or "\r\n"
    • fixed a bug in rewrite_new_targetfile() : if a docline doesn't end with
      a linefeed character, we have to add it manually in the target files.
    • fixed a bug in rewrite_new_targetfile() : the file opened is now explicitly
      closed.
    • added the README.rst file : the file is required by Pypi and should have
      been added since v 0.1.4.
    • documentation improved

    - unittests : 1 test (passed) 
    - raw Pylint invocation : 10.0/10.0 for all scripts.
    - version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
 
v 0.1.4(alpha) (2016_08_26) first version available on Pypi
    • Pimydoc is now available on Pypi : https://pypi.python.org/pypi/Pimydoc

    • improved the documentation

    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)

older versions :
    
    + 0.1.3(alpha) :
        • pimydoc is callable from a Python script.
        • in rewrite_new_targetfile(), FileNotFoundError is catched to prevent
          an error by reading some special files like temp files.
        • in pimydoc_a_file(), added a call to shutil.copystat() to correctly
          set the permissions of the new target file.
        • in DocumentationSource.__init__() added a test about the existence
          of the file to be read.
        • improved messages displayed by the script

        • raw Pylint invocation : 10.0/10.0

    + 0.1.2(alpha)
    	• improved documentation
    	• added the LICENSE.txt file
        • raw Pylint invocation : 10.0/10.0

    + 0.1.1(alpha)
    	• added -vv, -vvv options
    	• --verbosity > --verbose
        • raw Pylint invocation : 10.0/10.0

    + 0.1(alpha)     
        • added --securitymode/-s option
        • improved documentation
        • raw Pylint invocation : 10.0/10.0

    + 0.0.9(alpha) : two profiles are available : "Python" and "C++";
                     removed two useless constants (SOURCEPATH, DOCSRCFILENAME);
                     the exit values are {0, -1, -2};
                     try/except added around calls to re.compile() and around .group();
                     improved documentation;

    + 0.0.8(alpha) : added the --remove/-r option.
    
    + 0.0.7(alpha) : redefined --verbosity={0,1,2}, default=1;
                     improved documentation

    + 0.0.6(alpha) : removed the useless constant VERBOSITY;
                     improved the documentation;
                     the regexes are now compiled

    + 0.0.5(alpha) : fixed a bug. If REMOVE_FINAL_SPACES_IN_NEW_DOCLINES is set to "True", some
                     empty lines wanted by the definition in pimydoc may be cut. E.g. :
                        ( space character being replaced by _ )
                        STARTSYMB_IN_DOC :|_|_ 
                        REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True

                        [doc001]
                        line1
                                        <--- this an empty line

                        ... the expected result is :

                        But the rewrite_new_targetfile() function needs to identify the added lines : searching
                        "|_|_" wouldn't be sufficient to find to second line, hence the need to search
                        with REGEX_FIND_PIMYDOCLINE_IN_CODE2, i.e. REGEX_FIND_PIMYDOCLINE_IN_CODE
                        without final spaces (\_ here, since the REGEX_* constants are re.escape'd).

    + 0.0.4(alpha) : added a function : remove_and_return_linefeed(); 
                     improved the way final spaces are handled at the end of the added lines;
                     added a new setting : REMOVE_FINAL_SPACES_IN_NEW_DOCLINES

    + 0.0.3(alpha) : improved documentation; pylinted the code; REGEX_SOURCE_FILTER; project's name set to "pimydoc";
                     improved the way the regexes are read in the documentation source file.

    + 0.0.2(alpha) : --verbosity levels reduced to 3; improved documentation

    + 0.0.1(alpha) : Settings class, no more call to eval()

    + 0.0.0(alpha) : proof of concept

#(8) technical details

##(8.1) exit values :

    See the file named "pimydoc", section "exit codes"