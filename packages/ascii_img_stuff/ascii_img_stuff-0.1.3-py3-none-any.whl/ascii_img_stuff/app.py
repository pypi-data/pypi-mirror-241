#!/usr/bin/python3
# https://github.com/hashirkz/ascii_stuff

from .ascii import *

def app():
    wd = os.getcwd()
    img_path = input('path to img: ')
    h = int(input('height for .txt file: '))
    inv = input('invert y/n: ').strip() != 'n'
    if not os.path.exists(img_path): 
        print(f'unable to read {img_path} from {wd}')
        return
    
    img = read_img(img_path, inv=inv)
    img = rescale(img, h=h)
    ascii = img_to_ascii(img)
    savepath = f'{os.path.basename(img_path).split(".")[0]}.txt'
    ascii = pretty_repr(ascii, show=False, save=True, savepath=savepath)
    print(ascii)

    print(f'saved to: {savepath}')

if __name__ == '__main__':
    app()