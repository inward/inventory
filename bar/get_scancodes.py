from io import BytesIO
import barcode
from barcode.writer import ImageWriter
from PIL import Image


# rv = BytesIO()
# EAN13(str(100000902922), writer=ImageWriter()).write(rv)

def create_barcode(text):
    with open('temp.png', 'wb') as f:
        barcode.Code128(text, writer=ImageWriter()).write(f)

def crop_code():
    image = Image.open('temp.png')
    code = image.crop((0, 10, 220, 50))
    text = image.crop((0, 247, 220, 270))
    res = Image.new('RGB', (222, 64))
    res.paste(code, (0, 0))
    res.paste(text, (0, 40))
    res.save('file.png')
    return res

def create_big(img_ar):
    img_by_x = 10
    img_by_y = 15
    big_img = Image.new('RGB', (222*img_by_x, 64*img_by_y))
    for x in range(img_by_x):
        for y in range(img_by_y):
            big_img.paste(img_ar.pop(), (x*222, y*64))
    big_img.save('big.png')





def main():
    ids_ar = []
    with open('ids.txt') as fr:
        for line in fr:
            ids_ar.append(line.strip())
    img_ar = []
    for ids in sorted(ids_ar):
        create_barcode(ids)
        img = crop_code()
        img_ar.append(img)

    create_big(img_ar)



if __name__ == '__main__':
    main()

