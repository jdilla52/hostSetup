import os

def find_downloads(path):
    # Set the directory you want to start from
    for dirName, subdirList, fileList in os.walk(path):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname) 
