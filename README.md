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

## documentation source file format
The file "pimydoc" is mandatory : it contains the documentation to be inserted
in the source directory. After an optional header beginning with the string
"[pimydoc]", the documentation itself is divided along doctitles written
in brackets, like "[doctitle1]".

    ### a simple example of a "documentation source file" :
    [pimydoc]
    REGEX_SOURCE_FILTER : .+py$

    [doctitle1]
    This line will be added as the first line of the "doctitle1"  
    This line will be added as the first line of the "doctitle1"  

    [doctitle2]
    This line will be added as the first line of the "doctitle2"

This example will find all Python files (see REGEX_SOURCE_FILTER) and add after
each "doctitle1" mention the two lines given, and add after each "doctitle2"
the line given.

### comments
Comments are lines beginning with the "###" string. Comments added at the end of
a line like "some stuff ### mycomment" are not allowed.

### header

The header is optional and always begin with the "[pimydoc]" string.
The header's content is made of single lines following the "KEY:VALUE"
format. The available keys are (the values are given as examples) :

REGEX_SOURCE_FILTER : .+py$

REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$

STARTSYMB_IN_DOC :| | 

PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4

REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True

! Beware, the syntax "KEY = VALUE" is not supported.
    
#### REGEX_SOURCE_FILTER : .+py$
Python regex describing which file in the source directory have to be read
and -if required- modified.

Examples :

REGEX_SOURCE_FILTER : .+py$
... for Python files
    
REGEX_SOURCE_FILTER : .+cpp$|.+h$
... for C++ files

Beware, the format string "*.py" is not supported.

#### REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$
Python regex describing in the documentation source file the way the doctiles
appear. The group name (?P<doctitle>) is mandatory.

Examples :

REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$
... if doctitles appear as "[mydoctitle]" in the documentation source file.

REGEX_FIND_DOCTITLE : ^\<(?P<doctitle>.+)\>$
... if doctitles appear as "<mydoctitle>" in the documentation source file.

#### STARTSYMB_IN_DOC :| |
Characters appearing in source files juste before a doc line.
The STARTSYMB_IN_DOC characters may be preceded by other characters, like
spaces, "#", "//", and so on :

    """
       | | doctitle
    """
    
    # | | doctitle
    
    // | | doctitle

    /*
       | | doctitle
    */

You may want to add a space before and after STARTSYMB_IN_DOC; there's a
difference between "STARTSYMB_IN_DOC :| |" and "STARTSYMB_IN_DOC :| | ".
    
#### PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4
For Python files : a tabulation in a docline may be replaced by spaces. The
PROFILE_PYTHON_SPACENBR_FOR_A_TAB key sets the number of spaces replacing each
tabulation. If you don't want any replacement, set this key to 0.

Examples :

PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4

(standard; see https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
    
PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 0

(no replacement)
    
#### REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True
If set to True, the leading spaces at the end of docline added by Pimydoc are
removed.
    
Examples :

REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True

REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : False
        
## how to add doctitles in the source directory
todo

## profiles
According to the extension of the files read in the source directories, Pimydoc
slightly changes the way it adds and updates the documentation. The known
profiles are :

### "Python"
for files written in Python2 or Python3.

• see PROFILE_PYTHON_SPACENBR_FOR_A_TAB .
    
### "CPP" (i.e. C++)
nothing is changed compared to the default profile.

### "default"
default profile
        
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
    ... displays all known parameters.
    $ pimydoc --version
    ... displays the version of the current script.
    
## basic options
    
    $ pimydoc
    ... searches a "pimydoc" file in the current directory, reads it and parses
        the current directory, searching files to be modified.

    $ pimydoc --sourcepath path/to/the/targetpath --docsrcfile name_of_the_docsrc_file
    ... gives to the script the name of the source path (=to be modified) and
        the name of the documentation source file (e.g. "pimydoc")

## advanced options

### removing the documentation added by Pimydoc

    $ pimydoc --remove
    $ pimydoc -r
    ... will remove the documentation added by Pimydoc.
    
### security mode

    $ pimydoc --securitymode
    $ pimydoc -s
    ... will not delete the backup files created by Pimydoc before modifying the
        source files.
    
### verbosity

    $ pimydoc --verbose 0
    ... displays only error messages

    $ pimydoc --verbose 1
    $ pimydoc -vv
    ... both display only error messages and info messages

    $ pimydoc --verbose 2
    $ pimydoc -vvv
    ... both display all messages, including debug messages
        
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
	  --securitymode, -s    Security mode : backup files created by Pimydoc are not
	                        deleted (default: False)
	
#(7) history / future versions

##v 0.1.7(beta) (2016_08_29) : documentation/project in beta phase

    • improved the documentation

    • added tests/test8/ which should have been added in 0.1.6
    • improved error message in newline()
    • modified rewrite_new_targetfile() : if PROFILE_PYTHON_SPACENBR_FOR_A_TAB
      is set to 0, no tabulation is replaced.
    • DocumentationSource.newline() is now a method (not a subfunction
      of DocumentationSource.__init__() anymore)
    
    • unittests : 1 test (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
 
##v 0.1.6(alpha) (2016_08_28) a docline can be inside a commentary beginning
                            with "#" or "//"

    • modified rewrite_new_targetfile() to handle doclines to be added after
      some symbols like "#" (Python) or "//" (C/C++). Added some tests to test
      this feature.

    • simplified the documentation source file : no more "REGEX_FIND_PIMYDOC*"
      keys. 
    • improved the documentation

    • unittests : 1 test (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
    
##v 0.1.5(alpha) (2016_08_27) first unittests

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
 
##v 0.1.4(alpha) (2016_08_26) first version available on Pypi

    • Pimydoc is now available on Pypi : https://pypi.python.org/pypi/Pimydoc

    • improved the documentation

    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)

##older versions :
    
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