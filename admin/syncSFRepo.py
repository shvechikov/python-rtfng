#!/usr/bin/env python
import sys
import os.path
import pickle
from datetime import datetime

from adytum.util.sourceforge.base import login

# do a date check
filename, sfID, minDays, pickleFile = sys.argv[1:]
now = datetime.now()
minDays = int(minDays)
if os.path.exists(pickleFile):
    fh = open(pickleFile)
    lastSync = pickle.load(fh)
    fh.close()
    if (now - lastSync).days < minDays:
        print "A migration was performed less than %s day(s) ago." % minDays
        print "Aborting ... "
        sys.exit()

# define some URLs
host = 'https://sourceforge.net'
loginURL = '%s/account/login.php' % host
formURL = '%s/project/admin/svn_migration.php?group_id=%s' % (host, sfID)

# login and go to the migration page
#browser = login(loginURL, credFile='sourceforge_creds_test')
browser = login(loginURL, credFile='sourceforge_creds')
browser.open(formURL)
form = browser.getForm(name='migration')

# check to see if the page is a report page (in which case a migration has
# already occured, and we need to request another migration)
if form.getControl(name='action').value == 'migration_start':
    # this is the one we want; continue
    pass
elif form.getControl(name='action').value == 'migration_form':
    form.getControl(name='button').click()
    # we've submitted that form, now we need to get the "real" form
    form = browser.getForm(name='migration')
elif form.getControl(name='action').value == 'migration_progress':
    # still waiting ...
    print "Migration still in progress; please try later."
    print "Aborting ... "
    sys.exit()
else:
    # wtf?
    print "Got unexpected form!"
    print "\taction: %s" % form.getControl(name='action').value
    print "Aborting ... "
    sys.exit()

# submit the uploaded svn dump file
form.getControl(name='src_path_type3').value = filename
form.getControl(name='replace_type3').value = True
form.getControl(name='button').click()

# record the time this transaction was made
fh = open(pickleFile, 'w+')
pickle.dump(now, fh)
fh.close()

# last words
print "To view the results, visit the following URL:"
print "\t%s\n" % formURL
print "\n"
