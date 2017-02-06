import sys
import glob
import errno
import re

path = str(sys.argv[-1]"*.txt"
files = glob.glob(path)

regex = "(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[789]\d{2}\s*\d{3}\s*\d{4}"

for name in files:
    try:
        with open (name) as f:
            lines = f.read()
            matches = re.finditer(regex, lines)
            for match in matches:
                print ("{match}".format (match = match.group()))
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
