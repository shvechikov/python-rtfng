LIB=pymon
svn stat|egrep -v ".swp|.swo|.pyc|.pid|.egg|${LIB}/os|${LIB}/net|state/"
