# look for dirs
# if one found - add the file to sqlite
# look at the contents and if the file is not an mp4 attempt to convert it
# move the file with rclone


import os


def find_downloads(path):
    for root, dirs, files in os.walk(path):
        print(dirs)
