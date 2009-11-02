. ./admin/repoVars.sh
svnadmin create $MIRROR
echo '#!/bin/sh' > $MIRROR/hooks/pre-revprop-change
chmod 755 $MIRROR/hooks/pre-revprop-change
svnsync init file://$MIRROR_PATH/$MIRROR $SOURCE_REPO
