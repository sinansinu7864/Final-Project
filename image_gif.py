import imageio.v3 as iio

filenames =['Rizwan.jpg','Rashid.jpg']
images =[]
for filename in filenames:
    images.append(iio.imread(filename))
    
iio.imwrite('Riz.gif',images, duration = 500, loop =0)

