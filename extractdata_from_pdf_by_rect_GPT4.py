# _*_  coding:utf-8 _*_
# r'C:\Users\TERRYLI2\Desktop\IntelPLIN\1917867_0811264885_CI_EC.pdf'

import re
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

coo = ''
pdf_filepath = r'C:\Users\TERRYLI2\Desktop\IntelPLIN\1917867_0811264885_CI_EC.pdf'  # 示例文件路径
# 调整搜索范围
target_area = {
    'x0': 50,
    'x1': 300,
    'y0': 300,
    'y1': 600,
}

with open(pdf_filepath, 'rb') as pdf_file:
    resource_manager = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)
        layout = device.get_result()

        for element in layout:
            if isinstance(element, LTTextBoxHorizontal):
                print(element.get_text())
                # x0, y0, x1, y1 = element.bbox
                # if (x0 >= target_area['x0'] and x1 <= target_area['x1'] and
                #     y0 >= target_area['y0'] and y1 <= target_area['y1']):
                #     extracted_text = element.get_text()[:]
                #     match = re.search(r'COO:\s+(\w+)', extracted_text)
                #     if match:
                #         coo = match.group(1)
                #         print(f"Extracted COO (Country of Origin): {coo}")
                #         break



