# do not forget to install the following packages :
# o python-wheel
# o python-pip

echo "=== Pimydoc ==="
echo "=== tests, pipy and git for a new version"

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ pylint pimydoc/pimydoc.py"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

pylint pimydoc/pimydoc.py

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ pylint setup.py"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

pylint setup.py

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ pylint tests/tests.py"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

pylint tests/tests.py

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ nosetests"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

nosetests

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ python setup.py sdist bdist_wheel register -r test"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi
    
python3 setup.py sdist bdist_wheel register -r test

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ python setup.py sdist bdist_wheel upload -r test"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

python3 setup.py sdist bdist_wheel upload -r test

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ python setup.py sdist bdist_wheel register -r pypi"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi
    
python3 setup.py sdist bdist_wheel register -r pypi

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ python setup.py sdist bdist_wheel upload -r pypi"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

python3 setup.py sdist bdist_wheel upload -r pypi

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ sudo pip3 uninstall pimydoc"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

sudo pip3 uninstall pimydoc

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ sudo pip3 install pimydoc"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

sudo pip3 install pimydoc

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ pimydoc --version"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

pimydoc --version

#-------------------------------------------------------------------------------
echo
echo    "  = next step : $ git commit -a"
read -p "  = go on ? ('y' to continue) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

git commit -a
