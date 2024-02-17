import os
import dask.bag as db
import dask.dataframe as dd
import ast  # Used to safely evaluate strings containing Python expressions


# 定义处理LOB文件每一行的函数
def process_line(line):
    try:
        # 首先，将所有单引号替换为双引号 确保内部的双引号被适当地转义
        fixed_line = line.replace("Exch0", '"Exch0"')
        # 使用ast.literal_eval安全地解析修正后的字符串，该函数只允许解析Python表达式
        # 如果不使用ast.literal_eval，可能会导致安全漏洞
        data = ast.literal_eval(fixed_line)

        # 提取时间戳、交易所和订单列表
        # data是一个元组，包含时间戳、交易所和订单列表
        timestamp, exchange, orders = data
        # 提取买方和卖方订单列表
        bids, asks = orders[0][1], orders[1][1]  # 提取出价和询价列表
        return {
            'Timestamp': timestamp,
            'Exchange': exchange,
            'Bids': bids,
            'Asks': asks
        }
    except (ValueError, SyntaxError):
        # 如果行无法解析，则返回None
        return None


# 定义读取和处理LOB文件的函数
def read_lob_files_dask(lob_directory):
    # 读取目录中的所有文本文件为Dask Bag
    # os.path.join(lob_directory, '*.txt') 用于获取lob_directory目录下的所有txt文件，返回一个包含所有文件路径的列表
    # map(process_line) 用于对每个文件路径调用process_line函数
    lob_bag = db.read_text(os.path.join(lob_directory, '*.txt')).map(process_line)

    # 过滤掉None值（无法解析的行）
    filtered_lob_bag = lob_bag.filter(lambda x: x is not None)

    # 指定转换为Dask DataFrame时的元数据（数据结构）
    meta = {
        'Timestamp': 'f8',
        'Exchange': 'object',
        'Bids': 'object',
        'Asks': 'object'
    }

    # 将Dask Bag转换为Dask DataFrame
    lob_ddf = filtered_lob_bag.to_dataframe(meta=meta)

    return lob_ddf


# 定义读取Tape文件的函数
def read_tape_files_dask(tape_directory):
    # 使用Dask DataFrame读取所有Tape CSV文件
    tape_ddf = dd.read_csv(os.path.join(tape_directory, '*.csv'), header=None, names=['Timestamp', 'Price', 'Volume'])
    return tape_ddf


# 指定LOB和Tape数据所在的目录路径
lob_directory = 'E:\\Bristol\\mini_project\\JPMorgan_Set01\\JPMorgan_Set01\\LOBs'
tape_directory = 'E:\\Bristol\\mini_project\\JPMorgan_Set01\\JPMorgan_Set01\\Tapes'

# 处理LOB数据 compute() 用于将Dask DataFrame转换为Pandas DataFrame
# 将LOB数据保存为CSV文件储存到本地
lob_data_ddf = read_lob_files_dask(lob_directory)
lob_data_pdf = lob_data_ddf.compute()  # 注意：确保有足够的内存容量
lob_data_pdf.to_csv('lob_data.csv', index=False)

# 处理Tape数据
# tape_data_ddf = read_tape_files_dask(tape_directory)
# tape_data_pdf = tape_data_ddf.compute()
# tape_data_pdf.to_csv('tape_data.csv', index=False)



print("Data saved successfully.")
