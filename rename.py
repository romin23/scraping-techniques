import os

def change_name():
    i = 1
    path = 'C:/Users/boby/Desktop/internship/day 3/un_Images/'
    
    for images in os.listdir(path):
        destination = 'romin_parts' + str(i) + '.jpg'
        source = path + images
        destination = path + destination
        os.rename(source, destination)
        i += 1

change_name()
