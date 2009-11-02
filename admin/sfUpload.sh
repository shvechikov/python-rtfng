. ./admin/repoVars.sh
scp $MIRROR/$DUMP.gz \
    $SF_USER@shell.sourceforge.net:/home/groups/$SF_GROUP/$SF_PROJECT
