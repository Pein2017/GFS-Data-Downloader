"""
Author: 卢沛安
Created Date: 2023/11/10 9:44
""""""
Author: 卢沛安
Created Date: 2023/11/10 9:44
"""

import os
import sys
from urllib.request import build_opener

# 设置下载目录和数据源路径
download_directory = 'download_data'
dspath = 'https://data.rda.ucar.edu/ds084.1/'


# 自定义下载的文件列表
def create_file_list(year, month, start_day, end_day, start_hour=0, end_hour=18, hour_interval=6, forcast_points=None):
    filelist = []
    for day in range(start_day, end_day + 1):
        for hour in range(start_hour, end_hour + 1, hour_interval):  # 起报时间每6小时
            if not forcast_points:
                for forecast in range(0, 385, 3):  # 预报时效，每3小时
                    filename = f'gfs.0p25.{year}{month:02d}{day:02d}{hour:02d}.f{forecast:03d}.grib2'
                    filelist.append(os.path.join(f'{year}/{year}{month:02d}{day:02d}', filename))
            else:
                for forecast in forcast_points:  # 自定义预报时效
                    filename = f'gfs.0p25.{year}{month:02d}{day:02d}{hour:02d}.f{forecast:03d}.grib2'
                    filelist.append(os.path.join(f'{year}/{year}{month:02d}{day:02d}', filename))
    return filelist


# 确保下载目录存在
os.makedirs(download_directory, exist_ok=True)


# 下载文件
def download_files(filelist, opener, download_directory, dspath):
    for file in filelist:
        file_path = os.path.join(download_directory, file)

        # 检查文件是否存在
        if os.path.exists(file_path):
            sys.stdout.write(f"File {file} already exists, skipping download.\n")
            continue

        try:
            file_url = dspath + file
            file_dir = os.path.dirname(file_path)
            # 确保子目录存在
            os.makedirs(file_dir, exist_ok=True)

            sys.stdout.write(f"Downloading {file_url} ... ")
            sys.stdout.flush()
            infile = opener.open(file_url)
            with open(file_path, 'wb') as outfile:
                outfile.write(infile.read())
            sys.stdout.write("done\n")
        except Exception as e:
            sys.stdout.write(f"failed on {file} \nError: {e}\n")


# 主程序
if __name__ == "__main__":
    opener = build_opener()
    year = 2023  # 示例年份
    month = 1  # 示例月份
    start_day = 1  # 示例开始日期
    end_day = 1  # 示例结束日期
    filelist = create_file_list(year, month, start_day, end_day, forcast_points=[0, 3,6 ])
    download_files(filelist, opener, download_directory, dspath)
