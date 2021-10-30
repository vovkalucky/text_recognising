#https://www.jaided.ai/easyocr/documentation/


import easyocr

autonumber = '01234567890АВЕКНОРСТУХRUS'
def text_recognition(file_path, text_file_name='result.txt'):
    reader = easyocr.Reader(['ru'])
    result = reader.readtext(file_path, detail =1, paragraph = True, allowlist=autonumber) #detail = 0 без вывода доп инфы
    with open(text_file_name, 'w') as file:
        for line in result:
            file.write(f"{line}\n\n")
    return f"Result wrote into {text_file_name}"


# import pillow
# im = pillow.Image.open('auto_number3.jpg')
# def draw_boxes(image, bounds, color='yellow',width=2):
#     draw = ImageDraw.Draw(image)
#     for bound in bounds:
#         p0, p1, p2, p3 = bound[0]
#         draw.line([*p0,*p1,*p2,*p3,*p0], fill=color, width=width)
#         return image.show()


def main():
    file_path = 'auto_number3.jpg' #input('Enter file path: ')
    print(text_recognition(file_path=file_path))
    # draw_boxes(im, [[157, 33], [221, 33], [221, 67], [157, 67]])
if __name__ == '__main__':
    main()

