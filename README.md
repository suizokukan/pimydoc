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

#(4) workflow

    $ pimydoc -h
    ... will display all known parameters.
    $ pimydoc --version
    ... wil display the version of the current script.

#(5) project's author and project's name
Xavier Faure (suizokukan / 94.23.197.37) : suizokukan @T orange D@T fr
Pimydoc : [P]lease [i]nsert my doc[umentation]

#(6) arguments
	
#(7) history / future versions

    - x.y.z        : pypy
    - x.y.z        : unittests

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


exit values :
    0 if success
    -1 if the documentation source file doesn't exist
    -2 if the documentation source file is ill-formed