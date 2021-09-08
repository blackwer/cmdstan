#!/usr/bin/env python
from ctypes import CDLL, c_char_p
import os

libc_version = CDLL("libc.so.6").gnu_get_libc_version
libc_version.restype = c_char_p

# arbitrarily picking 2.25 as the cutoff. I don't know what's ideal
if libc_version() < '2.25':
    amdpath = os.path.join(os.getcwd(), 'lib/amd-libm/lib')
    print("-L'{0}' -Wl,-rpath,'{0}' -lalm -lm".format(amdpath))
