# Обход дерева каталогов, отбор файлов с расширением .txt
# и копирование этих файлов в новую папку
import os
import sys
import glob
import shutil


def copy_files(
        from_dir_path: str, 
        to_dir_path: str,
        ext: str
):
    mask = from_dir_path + "/**/*" + ext
    files = glob.glob(mask, recursive=True)
    for file in files:        
        # find relpath of a given file from parent dir
        rel_path = os.path.relpath(file, start="/tmp/Temp")
        dirs = os.path.dirname(rel_path)

        if dirs == "":
            shutil.copy(file, to_dir_path)
        else:

            p = to_dir_path + "/" + dirs
            os.makedirs(p, exist_ok=True)
            shutil.copy(file, p)


if __name__ == "__main__":
        
    args = sys.argv[1:]
    
    from_dir = args[0]
    to_dir = args[1]
    ext = args[2]
    copy_files(from_dir, to_dir, ext)
    


