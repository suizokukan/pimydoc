#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
#    Pimydoc Copyright (C) 2012 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of Pimydoc.
#    Pimydoc is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Pimydoc is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Pimydoc.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    ❏Pimydoc❏ tests.py

        Unittests for the Pimydoc project.

        Use the following command to launch the tests :
        $nosetests
"""

import collections
import hashlib
import os
import shutil
import unittest

from pimydoc import pimydoc

#///////////////////////////////////////////////////////////////////////////////
def dirhash(path):
    """
        dirhash()
        ________________________________________________________________________

        Return the hash value of an directory tree. File whose name ends in
        "~" are discarded.
        ________________________________________________________________________

        ARGUMENT : (str)path, the path of the directory tree.

        RETURNED VALUE : the expected string.
    """
    sha = hashlib.md5()

    def filehash(filepath):
        """
            filehash()
            ____________________________________________________________________

            Return the hash value of a file : only the content of the file is
            used to compute the hash value (not the permissions or the date
            informations).
            ____________________________________________________________________

            ARGUMENT : (str)filepath, the path to the source file

            RETURNED VALUE : (bool)is_ok, (str)reshash
                             is_ok : False if the file can't be opened (e.g. temp file)

        """
        try:
            with open(filepath, 'rb') as srcfile:
                while True:
                    data = srcfile.read(64*1024)
                    if not data:
                        break
                    sha.update(data)
            #print("filehash()", filepath, sha.hexdigest())
            return True, sha.hexdigest()
        except FileNotFoundError:
            return False, None

    for root, _, files in os.walk(path):
        for fpath in [os.path.join(root, f) for f in files]:
            if not fpath.endswith("~"):
                is_ok, reshash = filehash(fpath)
                if is_ok:
                    sha.update(reshash.encode())

    return sha.hexdigest()

#print(dirhash(os.path.join(".", "tests", "test0")))
#print(dirhash(os.path.join(".", "tests", "current_test")))
#import sys
#sys.exit()

# path to the temp directory where the files will be modified :
PATH_TO_CURRENT_TEST = os.path.join(os.getcwd(), "tests", "current_test")

Args = collections.namedtuple("args",
                              ["docsrcfile",
                               "remove",
                               "securitymode",
                               "sourcepath",
                               "verbose", "vv", "vvv"])
ARGS = Args(docsrcfile=os.path.join(PATH_TO_CURRENT_TEST, "pimydoc"),
            remove=False,
            securitymode=False,
            sourcepath=PATH_TO_CURRENT_TEST,
            verbose=0, vv=False, vvv=False)

if os.path.exists(PATH_TO_CURRENT_TEST):
    shutil.rmtree(PATH_TO_CURRENT_TEST)

################################################################################
class Tests(unittest.TestCase):
    """
        class Tests

        test0 : one Python file to be modified (with a docstring), one doctitle
                the file has just a doc title, no doc paragraph has to be updated.
        test1 : one Python file to be modified (with a docstring), two doctitles
                the file has just a doc title, no doc paragraph has to be updated.
        test2 : zero file to be modified (with a docstring) (not the same doctitles)
                the file has just a doc title, no doc paragraph has to be updated.
        test3 : zero file to be modified (with a docstring) (empty documentation source file)
                the file has just a doc title, no doc paragraph has to be updated.
        test4 : a Python file with a doc paragraph (in a docstring) to be updated
        test5 : a Python file with two doc paragraphs (in a docstring) to be updated
        test6 : one Python file to be modified (with a commentary beginning by #)
        test7 : two Python file to be modified (docstring + commentary beginning by #)
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_pimydoc_function(self):
        """
                Tests.test_pimydoc_function()
                ________________________________________________________________

                test of the pimydoc() function

                Several subtests are defined : subtest #n will test the
                tests/test#n directory.
                ________________________________________________________________
        """
        # If you want to run only one test :
        #for test_number in [0, 1]:
        for test_number in range(8+1):

            test_path = os.path.join(os.getcwd(), "tests", "test"+str(test_number))
            print("Testing "+test_path)
            shutil.copytree(os.path.join(test_path), PATH_TO_CURRENT_TEST)

            pimydoc.pimydoc(args=ARGS,
                            just_remove_pimydoc_lines=False,
                            docsrc=pimydoc.DocumentationSource(ARGS.docsrcfile))

            computed_hash = dirhash(PATH_TO_CURRENT_TEST)

            # if you want to display the computed hash, comment the test
            # (self.assertEqual(...) and uncomment the following line :
            #print(test_number, computed_hash)

            shutil.rmtree(PATH_TO_CURRENT_TEST)

            self.assertEqual(computed_hash, {0:"6569d0db5c329fcd59fd1b00fa9ac29b",
                                             1:"79d6e8f0c8d066d2d799411dbed96e69",
                                             2:"eb9ffc72c7ae93693ab366b702ed85cb",
                                             3:"31d25cb498ea9bbac74cdc852d0ddf02",
                                             4:"912f1b692ca56ca80cfdf830b2b46b3a",
                                             5:"fee3837a00b1ac7f2def08d8a7db7792",
                                             6:"9c7296e16a52ce170abe2dcdf3ce1ca7",
                                             7:"cf7d921abeafe1a425eb96ca905e9e91",
                                             8:"e1dfda50d4588168691b8600a61f8d4c",
                                            }[test_number])
