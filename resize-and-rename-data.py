import PIL
from PIL import Image
import os, sys
import time


Width, Height = 1280, 1280
number = 6

path1 = f"DATASETs/wm{number}/" 
color_mode1 = "L"

path2 = f"DATASETs/cover{number}/" 
color_mode2 = "RGB" 


def resize(path, color_mode):
    dirs = os.listdir(path)
    print('before resize ', len(dirs))
    for item in dirs:
        try:
            # print(item)
            with Image.open(fr'{path}{item}') as im:
                resized = im.convert(f'{color_mode}').resize((Width,Height))
                resized.save(fr'{path}{item}')
                time.sleep(0.0003)
                # print(fr'for {item} have been done')
        except PIL.UnidentifiedImageError:
            print(fr"Confirmed: This image {path}{item} cannot be opened!")
            # os.remove(f'{path}{item}')
        except OSError:
            im = Image.open(fr'{path}{item}').convert(f'{color_mode}').resize((Width,Height))
            im.save(fr'{path}{item}')
            print(fr"Chanched by hands for {path}{item}")
    dirs = os.listdir(path)
    print('after resize ', len(dirs))


resize(path1, color_mode1)
resize(path2, color_mode2)


def test_size(path):
    dirs = os.listdir(path)
    print('before test ', len(dirs))
    for item in dirs:
        try:
            with Image.open(fr'{path}{item}') as im:
                width, height = im.size
                if (width == Width) and (height == Height):
                    pass
                else:
                    print(fr'for {item} not true size')
                time.sleep(0.0003)
        except PIL.UnidentifiedImageError:
            print(fr"Confirmed: This image {item} cannot be opened! We removed it")
            os.remove(f'{path}{item}')
    dirs = os.listdir(path)
    print('after test ', len(dirs))


test_size(path1)
test_size(path2)


def renameimg(path):
    os.getcwd()
    # print(os.getcwd())
    for i, filename in enumerate(os.listdir(path)):
        try:
            os.rename(path + "/" + filename, path + "/" + str(i) + ".jpeg")
        
        except FileExistsError:
            pass

renameimg(path1)
renameimg(path2)