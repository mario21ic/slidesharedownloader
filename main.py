#!/usr/bin/env python

import urllib
import sys

from html_filter import Html_Filter

if __name__ == "__main__":
    print "Link: ",sys.argv[1]
    usock = urllib.urlopen(sys.argv[1])
    parser = Html_Filter()
    parser.feed(usock.read())
    parser.close()
    usock.close()

    for img in parser.images:
        print img

    print "Pages: ",len(parser.divs)
