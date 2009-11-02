PYPREFIX=`python -c "import sys;print sys.prefix;"`
sudo rm -rf ${PYPREFIX}/lib/python2.4/site-packages/adytum/app/pymon
sudo rm -rf ${PYPREFIX}/lib/python2.4/site-packages/PyMonitor-*.egg
sudo rm -rf build/
sudo rm -rf setuptools-*.egg
sudo find . -name "*.pyc"|xargs rm
