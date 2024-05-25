
import os
from tqdm import tqdm
import argparse
import shutil
import hashlib,datetime

def calculate_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()
    
def compare_files(file1, file2):
    if os.path.getsize(file1) != os.path.getsize(file2):
        return False
    if calculate_md5(file1) == calculate_md5(file2):
        return True
    else:
        return False


def copy_folder(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    for root, dirs, files in tqdm(os.walk(src_folder), desc='Copying files'):
        for file in files:
            
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_folder, os.path.relpath(src_path, src_folder))
            destination_dir = os.path.dirname(dst_path)

            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            if os.path.isfile(src_path):
                if os.path.exists(dst_path):
                    if compare_files(src_path, dst_path):
                        continue
                    else:
                        print(f"\nFile \"{file}\" already exists in destination folder but with different content.")
                        print("Source file:")
                        print(f"  File name: {file}")
                        print(f"  File path: {src_path}")
                        print(f"  Created time: {datetime.datetime.fromtimestamp(os.path.getctime(src_path))}")
                        print(f"  File size: {os.path.getsize(src_path)} bytes")
                        print("Destination file:")
                        print(f"  File name: {file}")
                        print(f"  File path: {dst_path}")
                        print(f"  Created time: {datetime.datetime.fromtimestamp(os.path.getctime(dst_path))}")
                        print(f"  File size: {os.path.getsize(dst_path)} bytes")
                        while True:
                            choice = input(f"\nFile \"{file}\" already exists in destlination folder. Replace it? [Y/N] ")
                            if choice.lower() == 'n':
                                print(f"Keep the existing file {file}. Skip.")
                                break
                            elif choice.lower() == 'y' or choice == '':
                                shutil.copy2(src_path, dst_path)
                                print(f"Replace the existing file {file}.")
                                break
                            else:
                                print("Invalid input. Please input 'Y' or 'N'.")
                else:
                    shutil.copy2(src_path, dst_path)
            
    print(f"Copy files from {src_folder} to {dst_folder} completed.")


if __name__ == "__main__":

    logo='''      
          _   _             ____  _       _        __      
     /\  | | | |           |  _ \(_)     (_)      / _|     
    /  \ | |_| | __ _ ___  | |_) |_  ___  _ _ __ | |_ ___  
   / /\ \| __| |/ _` / __| |  _ <| |/ _ \| | '_ \|  _/ _ \ 
  / ____ \ |_| | (_| \__ \ | |_) | | (_) | | | | | || (_) |
 /_/    \_\__|_|\__,_|___/ |____/|_|\___/|_|_| |_|_| \___/  

        `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"
        `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/
            y==/        y==/        y==/        y==/
        ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.
        ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_
                
    '''


    description_text = '''{} 
    This script is used to copy files from source folder to destination folder.'''.format(logo)

    parser = argparse.ArgumentParser(description=description_text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('source_folder', help='Source folder path')
    parser.add_argument('destination_folder', help='Destination folder path')

    args = parser.parse_args()

    copy_folder(args.source_folder, args.destination_folder)



