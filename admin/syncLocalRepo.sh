. ./admin/repoVars.sh
svnsync sync file://$MIRROR_PATH/$MIRROR $SOURCE_REPO
svnadmin dump $MIRROR > $MIRROR/$DUMP
gzip --best $MIRROR/$DUMP
