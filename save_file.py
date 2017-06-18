'''Use os module to create a blank directory with more directories within.'''

import os

dir_name = 'example_dir'

def make_file(dir_name):
    #Make initial directory to desired path.
    path = 'C:\\path\\to\\final\\destination'
    dir_name = dir_name
    full_path = os.path.join(path, dir_name)
    os.mkdir(full_path)

def make_secondary_file(dir_name):
    #Make directories within initial directory.
    path = 'C:\\path\\to\\final\\destination\\' + dir_name
    ex_folder_1 = 'example_folder_1'
    ex_folder_2 = 'example_folder_2'
    fp_folder_1 = os.path.join(path, ex_folder_1)    
    fp_folder_2 = os.path.join(path, ex_folder_2)
    os.mkdir(fp_folder_1)
    os.mkdir(fp_folder_2)




