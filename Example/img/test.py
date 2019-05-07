from PIL import Image

pil_im = Image.open('n.jpg')
box = (800, 0, 1100, 300)
region = pil_im.crop(box)

region.save('new.jpg')
print(region)
