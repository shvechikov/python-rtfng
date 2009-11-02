svn update
for LIB in `ls -1 lib/|egrep -v '__|app'`
    do
    cd lib/$LIB;
    svn update
    cd ../..
    done
