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
        test1 : one file to be modified (with a docstring), two doctitles
        test2 : zero file to be modified (with a docstring) (not the same doctitles)
        test3 : zero file to be modified (with a docstring) (empty documentation source file)
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
#        for test_number in [3,]:
        for test_number in range(4):

            test_path = os.path.join(os.getcwd(), "tests", "test"+str(test_number))
            shutil.copytree(os.path.join(test_path), PATH_TO_CURRENT_TEST)

            pimydoc.pimydoc(args=ARGS,
                            just_remove_pimydoc_lines=False,
                            docsrc=pimydoc.DocumentationSource(ARGS.docsrcfile))

            computed_hash = dirhash(PATH_TO_CURRENT_TEST)

            shutil.rmtree(PATH_TO_CURRENT_TEST)

            self.assertEqual(computed_hash, {0:"b1f9b5a06ed96056006338876a4eff4e",
                                             1:"2e8a0e5f87133d8d2a252e2dfcef096b",
                                             2:"7d941b05a9903de24774b0a9f239ce14",
                                             3:"15c89f259f92f019f5ef736ab7b4c4bc",}[test_number])
