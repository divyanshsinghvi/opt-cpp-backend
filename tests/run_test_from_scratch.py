import os
import subprocess
import sys

bn = os.path.splitext(sys.argv[1])[0]
trace_f = bn + '.trace'
if os.path.exists(trace_f):
    os.remove(trace_f)

subprocess.call(["make", trace_f]) # synchronous

# print out trace_f to stdout
for line in open(trace_f):
    print line,
