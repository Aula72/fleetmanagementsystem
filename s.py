import os
import shutil

srcfile = 'D:\\FLEET\\fleetmanagement\icons\\row.txt'
dstroot = './home/myhome/new_folder'
dstdir = '.\\aula'

'''assert not os.path.isabs(srcfile)
dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))

os.makedirs(dstdir) # create all directories, raise an error if it already exists
'''
shutil.copy2(srcfile, dstdir)