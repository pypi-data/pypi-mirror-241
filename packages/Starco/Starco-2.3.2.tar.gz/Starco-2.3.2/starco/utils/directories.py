import os

def path_maker(path_list,relative_path=''):
    p = os.path.abspath(os.path.join(os.getcwd(),relative_path))
    for i in path_list:
        p += '/'+str(i)
        if not os.path.exists(p):
            os.mkdir(p)
    return p


