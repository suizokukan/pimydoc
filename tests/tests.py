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

        Return the hash value of an directory tree.
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
            return True, sha.hexdigest()
        except FileNotFoundError:
            return False, None

    for root, _, files in os.walk(path):
        for fpath in [os.path.join(root, f) for f in files]:
            is_ok, reshash = filehash(fpath)
            if is_ok:
                sha.update(reshash.encode())

    return sha.hexdigest()

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
        # for test_number in [8,]:
        for test_number in range(8+1):

            test_path = os.path.join(os.getcwd(), "tests", "test"+str(test_number))
            shutil.copytree(os.path.join(test_path), PATH_TO_CURRENT_TEST)

            pimydoc.pimydoc(args=ARGS,
                            just_remove_pimydoc_lines=False,
                            docsrc=pimydoc.DocumentationSource(ARGS.docsrcfile))

            computed_hash = dirhash(PATH_TO_CURRENT_TEST)

            # if you want to display the computed hash, comment the test
            # (self.assertEqual(...) and uncomment the following line :
            #print(test_number, computed_hash)

            shutil.rmtree(PATH_TO_CURRENT_TEST)

            self.assertEqual(computed_hash, {0:"3e6ce8685299f20d79fcf12e50e34a33",
                                             1:"8e3204c77be1637a326171f67307146e",
                                             2:"6bfd068924de5a2c1dcfda3251392831",
                                             3:"de2aab410c93d14460c9655114991657",
                                             4:"9a71553228c3b8ca9c85e50ca766d37f",
                                             5:"ca16119770f0309c09770233a47b78c1",
                                             6:"e5d05f057e6b72e261c3a09bc2bd0317",
                                             7:"e10aadbb96a51ea8be9f821000aa15c4",
                                             8:"447a6203c5c4630b6fd96d7cff6260a6",
                                            }[test_number])
