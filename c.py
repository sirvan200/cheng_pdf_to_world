from pdf2docx import Converter

# مسیر فایل PDF و فایل Word که می‌خواهید ایجاد کنید
pdf_file = r'C:\Users\lenovo\Desktop\aa.pdf'
docx_file = r'C:\Users\lenovo\Desktop\output.docx'

# ایجاد یک شیء از کلاس Converter
cv = Converter(pdf_file)

# تبدیل فایل PDF به فایل Word
cv.convert(docx_file, start=0, end=None)

# پایان تبدیل
cv.close()

print("finish")

