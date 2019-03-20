from PIL import Image
import pytesseract

Image = Image.open('1.png')  # 打开图片
text = pytesseract.image_to_string(Image, lang='chi_sim')  # 使用简体中文解析图片
print(text)
a = dir(Image)
print(Image.palette)
