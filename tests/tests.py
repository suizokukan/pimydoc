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
            return True, sha.hexdigest()
        except FileNotFoundError:
            return False, None

    for root, _, files in os.walk(path):
        for fpath in [os.path.join(root, f) for f in sorted(files)]:
            if not fpath.endswith("~"):
                is_ok, reshash = filehash(fpath)
                if is_ok:
                    sha.update(reshash.encode())

    return sha.hexdigest()

#print("??", dirhash(os.path.join(".", "tests", "test0")))
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

# ARGS : standard values
ARGS = Args(docsrcfile=os.path.join(PATH_TO_CURRENT_TEST, "pimydoc"),
            remove=False,
            securitymode=False,
            sourcepath=PATH_TO_CURRENT_TEST,
            verbose=0, vv=False, vvv=False)

# ARGS + --remove :
ARGS_R = Args(docsrcfile=os.path.join(PATH_TO_CURRENT_TEST, "pimydoc"),
              remove=True,
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
        # If you want to choose the test to be runned:
        #for test_number in [8,]:
        for test_number in range(8+1):

            test_path = os.path.join(os.getcwd(), "tests", "test"+str(test_number))
            print("Testing "+test_path)
            shutil.copytree(os.path.join(test_path), PATH_TO_CURRENT_TEST)

            pimydoc.pimydoc(args=ARGS,
                            docsrc=pimydoc.DocumentationSource(ARGS.docsrcfile))

            computed_hash = dirhash(PATH_TO_CURRENT_TEST)

            # if you want to display the computed hash, comment the test
            # (self.assertEqual(...) and uncomment the following line :
            #print(test_number, computed_hash)

            shutil.rmtree(PATH_TO_CURRENT_TEST)

            self.assertEqual(computed_hash, {0:"cb94b5865f7a48cf9c934e9afa9a55f1",
                                             1:"3d35e1af0b0350cf53645e3169149353",
                                             2:"43cf3a1be20e5e3ba08a205c4ec0a76f",
                                             3:"b16ac38da7d743c1e6b2b3036ea181cc",
                                             4:"5e2726dd3d036e09a25553826f06b1d3",
                                             5:"0babc63109c2c7fcf833429782a7e093",
                                             6:"d72da8d969b03abd18c192e1a7ae3466",
                                             7:"2ef2d151196e1cead4c584002ce59cdf",
                                             8:"fb80d1ded9adc9a5b7d31f33ae0259d3",
                                            }[test_number])

    #///////////////////////////////////////////////////////////////////////////
    def test_pimydoc_function__r(self):
        """
                Tests.test_pimydoc_function__r()
                ________________________________________________________________

                test of the pimydoc() function with the --remove option.
                ________________________________________________________________
        """
        test_path = os.path.join(os.getcwd(), "tests", "test5")
        print("Testing "+test_path)
        shutil.copytree(os.path.join(test_path), PATH_TO_CURRENT_TEST)

        pimydoc.pimydoc(args=ARGS_R,
                        docsrc=pimydoc.DocumentationSource(ARGS.docsrcfile))

        computed_hash = dirhash(PATH_TO_CURRENT_TEST)

        shutil.rmtree(PATH_TO_CURRENT_TEST)

        self.assertEqual(computed_hash, "7943d7569346d5ceba15dfd3eb34b71c")
