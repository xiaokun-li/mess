import pdfplumber

# 定义一个函数来提取和打印表格数据
def extract_and_print_table_data(file_path):
    # 打开PDF文件
    with pdfplumber.open(file_path) as pdf:
        # 遍历每一页
        for page_number, page in enumerate(pdf.pages):
            # 提取当前页面的表格
            tables = page.extract_tables()
            # 检查页面是否包含表格
            if tables:
                print(f"Tables on page {page_number + 1}:")
                # 遍历页面中的每个表格
                for table_index, table in enumerate(tables, start=1):
                    print(f"Table {table_index}:")
                    # 遍历表格中的每一行
                    for row in table:
                        # 打印每一行的数据
                        print(row)
                        # 如果需要，可以在这里添加代码来处理或保存数据
                    print("-" * 40)  # 打印分隔线

# 调用函数并传入PDF文件路径
extract_and_print_table_data(r'C:\Users\TERRYLI2\Desktop\IntelPLIN\1917867_0811264888_CI_EC.pdf')