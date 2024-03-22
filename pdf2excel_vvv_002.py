import pdfplumber

# 定义一个函数来提取最右下角的单元格数据
def extract_bottom_right_cell(file_path):
    # 打开PDF文件
    with pdfplumber.open(file_path) as pdf:
        # 遍历每一页
        for page_number, page in enumerate(pdf.pages):
            # 提取当前页面的表格
            tables = page.extract_tables()
            # 检查页面是否包含表格
            if tables:
                for table in tables:
                    # 获取表格的行数和列数
                    rows = len(table)
                    cols = len(table[0]) if rows > 0 else 0
                    # 定位到最右下角的单元格
                    bottom_right_cell = table[rows - 1][cols - 1]
                    # 打印该单元格的内容
                    print(f"Bottom right cell content: {bottom_right_cell[1]}")

# 调用函数并传入PDF文件路径
extract_bottom_right_cell(r'C:\Users\TERRYLI2\Desktop\IntelPLIN\1917867_0811264885_CI_EC.pdf')

# 调用函数并传入PDF文件路径
#extract_bottom_right_cell(r'C:\Users\TERRYLI2\Desktop\IntelPLIN\1917867_0811264885_CI_EC.pdf')