#!/usr/bin/env python3

import os
import sys

# Samba Library folders
samba_libs = ['/usr/lib/python2.7/dist-packages',
             '/usr/local/samba/lib/python2.7/site-packages',
             '/usr/local/samba/lib64/python2.7/site-packages'
]

for i in samba_libs:
    if (os.path.exists(i)):
        sys.path.append(i)
