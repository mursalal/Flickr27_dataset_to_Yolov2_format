import os
import shutil
from PIL import Image

images_dir = '/home/user_name/flickr_logos_27_dataset/flickr_logos_27_dataset_images/'
file_path = 'flickr_logos_27_dataset_training_set_annotation.txt'

def convert(sz, bx):
    dw = 1./sz[0]
    dh = 1./sz[1]
    x = dw * (float(bx[0]) + float(bx[2]))/2.0
    y = dh * (float(bx[1]) + float(bx[3]))/2.0
    w = dw * (float(bx[2]) - float(bx[0]))
    h = dh * (float(bx[3]) - float(bx[1]))
    return (x,y,w,h)


with open(file_path) as f:
	content = f.readlines()
els = []

d = {'Adidas' : 0, 'Apple' : 1, 'BMW' : 2, 'Citroen' : 3, 'Cocacola' : 4, 'DHL' : 5, 'Fedex' : 6, 'Ferrari' : 7, 'Ford' : 8, 'Google' : 9, 'Heineken' : 10, 'HP' : 11, 'Intel' : 12, 'McDonalds' : 13, 'Mini' : 14, 'Nbc' : 15, 'Nike' : 16, 'Pepsi' : 17, 'Porsche' : 18, 'Puma' : 19, 'RedBull' : 20, 'Sprite' : 21, 'Starbucks' : 22, 'Texaco' : 23, 'Unicef' : 24, 'Vodafone' : 25, 'Yahoo' : 26}

if os.path.isdir('labels/') is False:
    os.mkdir('labels/')
if os.path.isdir('train_imgs/') is False:
    os.mkdir('train_imgs/')

print ("Wait a minute...")
for i in range(0, len(content)):
    if (os.path.isfile('flickr_logos_27_dataset_images/' + content[i].split()[0])):
    	w, h = Image.open('flickr_logos_27_dataset_images/' + content[i].split()[0]).size
        shutil.copy('flickr_logos_27_dataset_images/' + content[i].split()[0], 'train_imgs/')

    if not os.path.isfile('labels/' + content[i].split()[0][:-4] + '.txt'):
        k = 1

        coords = convert((w,h), [float(j) for j in (content[i].split()[3:])])
        str1 = str(d[content[i].split()[1]]) + ' ' + str(coords[0]) + ' ' + str(coords[1]) + ' ' + str(coords[2]) + ' ' + str(coords[3]) + '\n'
        while(content[i].split()[0] == content[i + k].split()[0]):
            coords = convert((w,h), content[i + k].split()[3:])
            str1 += str(d[content[i + k].split()[1]]) + ' ' + str(coords[0]) + ' ' + str(coords[1]) + ' ' + str(coords[2]) + ' ' + str(coords[3]) + '\n'
            k += 1

        f = open('labels/' + content[i].split()[0][0:-4] + '.txt', 'w')
        f.write(str1)
        f.close()

print ("Done.")