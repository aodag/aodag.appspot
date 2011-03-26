from paver.easy import *

import sys
import os

options(
    deploy={
        "sdk_path":"/tools/google_appengine"
    },
)

@task
def deploy(options):
    sys.path.append(options.sdk_path)
    cmd = "%s %s update src" % (sys.executable, os.path.abspath(os.path.join(options.sdk_path, 'appcfg.py')))
    print cmd
    os.system(cmd)
