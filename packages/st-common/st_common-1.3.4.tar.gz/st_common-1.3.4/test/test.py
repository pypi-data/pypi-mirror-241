import os
import shutil
def move_files_recursively(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            # 构建当前文件的路径
            file_path = os.path.join(root, filename)
            # 在目标文件夹中创建相同的目录结构
            rel_path = os.path.relpath(root, source_folder)  # 相对于源文件夹的路径
            dest_dir = os.path.join(destination_folder, rel_path)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            shutil.move(file_path, dest_dir)
            print(f"文件 {file_path} 已被移动到 {dest_dir}")
# 指定源文件夹和目标文件夹
source_folder = r'C:\Users\Administrator\Desktop\1.销售额增长模块'  # 替换为源文件夹的路径
destination_folder = r'C:\Users\Administrator\Desktop\sales_growth_module'  # 替换为目标文件夹的路径
move_files_recursively(source_folder, destination_folder)
print("所有文件递归移动完成。")
# import argparse
# from datetime import datetime
# from st_common.commonbase import fn_timer
# from st_common.msgreport import ISZ_main_exception_report_args
# @ISZ_main_exception_report_args("Test")
# @fn_timer
# def main(args):
#     print(f"argument mode is {args.mod}")
#     print(datetime.now().strftime('%Y-%m-%d'))



# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='tmp')
#     parser.add_argument('--mode', default="dev", choices=['dev', 'pro'],help="running mode")
#     args = parser.parse_args()
#     main(args=args)



# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime, func,TIMESTAMP
# engine = create_engine('mysql+pymysql://rpaer:Rpaer2023!@192.168.6.253:3306/rpa_data?charset=utf8mb4')
# metadata = MetaData()
# new_table = Table('new_table', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('update_at', TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
# )
# # 创建表
# metadata.create_all(engine)

# from sqlalchemy.sql import insert
# def insert_data(table, data):
#     """
#     Inserts data into a table.
    
#     :param table: The table to insert data into.
#     :param data: A dictionary where the keys are the column names and the values are the data to insert.
#     """
#     with engine.connect() as connection:
#         stmt = insert(table).values(data)
#         connection.execute(stmt)
# # 使用insert_data函数插入数据
# insert_data(new_table, {'id': 1})