import os, sys

def downloader(url, name):
    cmd = "aria2c -x 4 -s 8 -j 12 -o " + name + ".jpg" + " " + url
