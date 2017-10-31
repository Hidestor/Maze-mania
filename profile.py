#!/usr/bin/env python
from bprofile import BProfile

# This module generates temporary files and directories
import tempfile
from solve import solve
from factory import SolverFactory

methods = [
    "astar",
    # "breadthfirst",
    # "depthfirst",
    "dijkstra",
    # "leftturn",
]
inputs = [
    # "tiny",
    # "small",
    # "normal",
    # "braid200",
    "logo",
    "combo400",
    "braid2k",
    "perfect2k",
    # "perfect4k",
    # "combo6k",
    # "perfect10k",
    # "vertical15k",
]

# NamedTemporaryFile:
# This function operates exactly as TemporaryFile() does, except that the file is guaranteed to have a visible name in the file system 
# (on Unix, the directory entry is not unlinked). That name can be retrieved from the name attribute of the returned file-like object.
# Whether the name can be used to open the file a second time, while the named temporary file is still open, varies across platforms 
# (it can be so used on Unix; it cannot on Windows NT or later). If delete is true (the default), the file is deleted as soon as 
# it is closed.

# The returned object is always a file-like object whose file attribute is the underlying true file object. This file-like object
# can be used in a with statement, just like a normal file.

def profile():
    for m in methods:
        for i in inputs:
            with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
                solve(SolverFactory(), m, "examples/%s.png" % i, tmp.name)

profiler = BProfile('profiler.png')
with profiler:
    profile()
