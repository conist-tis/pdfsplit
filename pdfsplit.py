import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time

def merge_pages(input_file, start_page, end_page):
    reader = PdfFileReader(open(input_file, "rb"))
    pageCount = reader.getNumPages()
    output = PdfFileWriter()

    # 获取原文件的目录和文件名（不含扩展名）
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = os.path.dirname(input_file)
    output_file = os.path.join(output_dir, f"{base_name}_splited.pdf")

    # 确保输入的页数在有效范围内
    if start_page < 1 or end_page > pageCount or start_page > end_page:
        print("页数超出范围，请检查输入！")
        return

    # 添加指定页数到新的PDF文件
    for page_num in range(start_page - 1, end_page):
        output.addPage(reader.getPage(page_num))

    # 写入到目标PDF文件
    with open(output_file, "wb") as outputStream:
        output.write(outputStream)
    print("合并完成，文件已保存为", output_file)

if __name__ == '__main__':
    # 提示用户输入文件路径
    input_file = input("请输入PDF文件路径或将文件拖入窗口(path)：").strip('"')

    # 检查文件是否存在
    if not os.path.isfile(input_file):
        print("文件不存在，请检查路径！")
    else:
        start_page = int(input("请输入开始的页数(begin_page)："))
        end_page = int(input("请输入结束的页数(end_page)："))

        time1 = time.time()
        merge_pages(input_file, start_page, end_page)
        time2 = time.time()
        print('合并完成，用时 %.2f 秒,已保存在原文件所在目录下' % (time2 - time1))
        a=input("按任意键退出")
