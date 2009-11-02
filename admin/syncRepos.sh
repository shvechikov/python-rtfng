. ./admin/repoVars.sh
if [[ ! -x $MIRROR ]]; then
    echo "Creating local synced repository ..."
    ./admin/createLocalMirror.sh
fi
echo "Updating local mirror ..."
./admin/syncLocalRepo.sh
echo "Uploading to SourceForge ..."
./admin/sfUpload.sh
echo "Submitting migrate form on SourceForge ..."
./admin/syncSFRepo.py $MIRROR/$DUMP.gz \
    $SF_ID $MIN_DAYS $PICKLE_FILE
echo "Cleaning up ..."
rm $MIRROR/$DUMP.gz
