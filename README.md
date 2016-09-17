#(1) Pimydoc

Pimydoc : [P]lease [i]nsert my doc[umentation]

A Python3/GPLv3/OSX-Linux-Windows/CLI project, using no additional modules
than the ones installed with Python3.

Insert documentation in text files and update it.

Example :

    -> inside "pimydoc", documentation source file.
    [pimydoc]
    STARTSYMB_IN_DOC :¤ 
    [ressource::001]
    An interesting ressource.
    [ressource::002]
    Another interesting ressource.

    -> inside a source file :
    def foo(arg):
        """
           ressource::001
        """
        # ressource::002
        print("...")

The source file becomes :

    def foo(arg):
        """
           ressource::001
           ¤ An interesting ressource.
        """
        # ressource::002
        # ¤ another interesting ressource.
        print("...")
    
#(2) purpose and file format

Pimydoc inserts in source files the text paragraphs stored in "pimydoc", the
documentation source file. Moreover, the script updates the text paragraphs
already present in the source files if the documentation source file has
changed.

## (2.1) documentation source file (docsrc) format
The file "pimydoc" is mandatory : it contains the documentation to be inserted
in the source directory. After an optional header beginning with the string
"[pimydoc]", the documentation itself is divided along doctitles written
in brackets, like "[doctitle1]", followed by **docline**, a line followed
by linefeed character(s).

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

###(2.1.1) a special case

If a docline is not followed by some linefeed character(s) (e.g. if this line
is the last of the file), the script will automatically add a linefeed.
The added linefeed is either the last linefeed detected by reading the file,
either "\r\n" for Windows systems either "\n" in the other cases.

###(2.1.2) comments
Comments are lines beginning with the "###" string. Comments added at the end of
a line like "some stuff ### mycomment" are not allowed.

###(2.1.3) header

The header is optional and always begin with the "[pimydoc]" string.
The header's content is made of single lines following the "KEY:VALUE"
format. The available keys are (the values are given as examples) :

    REGEX_SOURCE_FILTER : .+py$
    REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$
    STARTSYMB_IN_DOC :| | 
    PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4
    REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True

! Beware, the syntax "KEY = VALUE" is not supported.
    
#### • REGEX_SOURCE_FILTER : .+py$
Python regex describing which file in the source directory have to be read
and -if required- modified.

Examples :

REGEX_SOURCE_FILTER : .+py$
... for Python files
    
REGEX_SOURCE_FILTER : .+cpp$|.+h$
... for C++ files

Beware, the format string "*.py" is not supported.

#### • REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$
Python regex describing in the documentation source file, NOT in the source files
the the way the doctiles appear. The group name (?P<doctitle>) is mandatory.

Examples :

REGEX_FIND_DOCTITLE : ^\[(?P<doctitle>.+)\]$

... if doctitles appear as "[mydoctitle]" in the documentation source file.

REGEX_FIND_DOCTITLE : ^\<(?P<doctitle>.+)\>$

... if doctitles appear as "<mydoctitle>" in the documentation source file.

#### • STARTSYMB_IN_DOC :| |

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
    
#### • PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4
For Python files : a tabulation in a docline may be replaced by spaces. The
PROFILE_PYTHON_SPACENBR_FOR_A_TAB key sets the number of spaces replacing each
tabulation. If you don't want any replacement, set this key to 0.

Examples :

PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 4

(standard; see https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
    
PROFILE_PYTHON_SPACENBR_FOR_A_TAB : 0

(no replacement)
    
#### • REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True
If set to True, the leading spaces at the end of docline added by Pimydoc are
removed.
    
Examples :

REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : True

REMOVE_FINAL_SPACES_IN_NEW_DOCLINES : False
        
##(2.2) how to add doctitles in the files stored in the source directory
You juste have to add on a line the name of a doctitle (do **not follow the
format described in REGEX_FIND_DOCTITLE, e.g. "[ressource::001]"**, this
regex being used only in the documentation source file).
The documentation (the doclines) is added by inserting the doclines **after the
line containing the doctitle**. **Pimydoc will add before each docline the same
characters appearing before the doctitle.**

By example :

    -> inside "pimydoc", documentation source file.
    [ressource::001]
    An interesting ressource.

    -> inside a source file :
    def foo(arg):
        """
           ressource::001
        """
        print("...")

The source file becomes :

    def foo(arg):
        """
           ressource::001
           ¤ An interesting ressource.
        """
        print("...")
    
##(2.3) profiles
According to the extension of the files read in the source directories, Pimydoc
slightly changes the way it adds and updates the documentation. The known
profiles are :

### • "Python"
for files written in Python2 or Python3.

• see PROFILE_PYTHON_SPACENBR_FOR_A_TAB .
    
### • "CPP" (i.e. C++)
nothing is changed compared to the default profile.

### • "default"
default profile
        
#(3) installation and tests

    Don't forget : Pimydoc is Python3 project, not a Python2 project !

    $ pip3 install pimydoc

    or

    $ wget https://raw.githubusercontent.com/suizokukan/pimydoc/master/pimydoc/pimydoc.py
    Since pimydoc.py is a stand-alone file, you may place this file in the target directory.

    How to run the tests :
    
    $ python3 -m unittest tests/tests.py

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

    $ pimydoc --downloadpimydoc
    ... downloads the default documentation source file (named 'pimydoc') and exits.
    
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
	                  [--securitymode] [--downloadpimydoc]

	optional arguments:
      -h, --help            show this help message and exit
      --sourcepath SOURCEPATH
                            source path of the code (default:
                            /home/suizokukan/projets/pimydoc/pimydoc)
      --docsrcfile DOCSRCFILE
                            source documentation file name (default:
                            /home/suizokukan/projets/pimydoc/pimydoc/pimydoc)
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
      --downloadpimydoc     download a default pimydoc file in the current
                            directory and exit (default: False)
	
#(7) history / future versions

##v 0.2.5(beta) (2016_09_11) added two debug messages

    • added two debug messages in rewrite_new_targetfile().

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
        
##v 0.2.4(beta) (2016_09_08) : fixed a minor bug in DocumentationSource.__init__()

    • DocumentationSource.__init__() : if the documentation source file is
      a directory, an error is raised to prevent the directory to be opened.

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
    
##v 0.2.3(beta) (2016_09_08) : fixed the default value of REGEX_FIND_DOCTITLE

    • Settings.__init__() : fixed the default value of REGEX_FIND_DOCTITLE
      to "^\\[(?P<doctitle>.+)\\]$"

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
    
##v 0.2.2(beta) (2016_09_08) : fixed a bug in DocumentationSource.newline()

    • DocumentationSource.newline() handles correctly the case where a doctitle
      is ill-formed.
    • improved messages : the line number is now marked by the word "line".    

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
   
##v 0.2.1(beta) (2016_09_08) : fixed an error in pimydoc

    • added the accidently deleted "STARTSYMB_IN_DOC :| |" in pimydoc

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)

##v 0.2(beta) (2016_09_08) : messages display improvement

    • added an info message at the end of the download_default_pimydoc() function.
    • improved the final message of the pimydoc() function.
    • improved a message in the rewrite_new_targetfile() function.

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
    
##v 0.1.9(beta) (2016_09_08) : fixed issue #002, --downloadpimydoc option

    • rewrite_new_targetfile : a new exception is caught (UnicodeDecodeError)
      when reading a binary file
    • --downloadpimydoc option : the function download_default_pimydoc()
      downloads from the default "pimydoc" file.
    
    • updated the documentation

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
    
##v 0.1.8(beta) (2016_09_07) : fixed issue #001

    • rewrite_new_targetfile() : fixed the way a linefeed is added to a docline
      without linefeed : either the last linefeed characters read in the file,
      either \r\n on Windows systems, either "\n".
    • rewrite_new_targetfile() opens the files in binary mode to avoid that
      Windows OS modified the linefeed characters to be added at the end
      of doclines. Without this modification, the tests can't pass on Windows
      systems since the test files use the \n linefeed, NOT the \r\n one. 
    • open() uses the option "encoding='utf-8" so that the script doesn't use
      the cp1252 encoding on Windows systems.
    • (tests.py) the PATH_TO_CURRENT_TEST directory is removed at the
      beginning of each test function.
    • added a rewrite_new_targetfile__line() function to size down the
      rewrite_new_targetfile() function.
    
    • improved the documentation

    • unittests : 2 tests (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
              
##v 0.1.7(beta) (2016_08_29) : documentation improved/project in beta stage.

    • improved the documentation

    • fixed a bug in the tests : the filenames have to be sorted in order to
      hash a directory exactly the same way on different computers.
    • Fixed a bug in rewrite_new_targetfile() : lines containing STARTSYMB_IN_DOC or
      STARTSYMB_IN_DOC.rstrip() have to be discarded.
      Fixed the corresponding tests.
    • Fixed a bug in tests/tests.py : files whose name ends in "~" are discarded.

    • removed from the pimydoc() function the "just_remove_pimydoc_lines" argument,
      since the value can be deduced from args.remove
    • added a test : Tests.test_pimydoc_function__r() to test the --remove argument.  
    • added the file : tests/__init__.py
    • removed the unused constant STARTSYMB_IN_DOC__ESCAPE
    • rewrite_new_targetfile() : added a debug message    
    • added tests/test8/ which should have been added in 0.1.6
    • improved error message in newline()
    • modified rewrite_new_targetfile() : if PROFILE_PYTHON_SPACENBR_FOR_A_TAB
      is set to 0, no tabulation is replaced.
    • DocumentationSource.newline() is now a method (not a subfunction
      of DocumentationSource.__init__() anymore)
    
    • unittests : 1 test (passed) 
    • raw Pylint invocation : 10.0/10.0 for all scripts.
    • version packaged and sent to Pypi (https://pypi.python.org/pypi/Pimydoc)
 
##v 0.1.6(alpha) (2016_08_28) : a docline can be inside a commentary beginning with "#" or "//"

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