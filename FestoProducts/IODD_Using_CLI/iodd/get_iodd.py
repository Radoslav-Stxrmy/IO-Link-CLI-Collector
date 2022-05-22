import iodd_download
import sys
import time


product_name = sys.argv[1]
iodd_download.get_iodd(product_name)
time.sleep(1)
iodd_download.rename_and_move_file(product_name)
time.sleep(1)
iodd_download.unzip_and_delete_zip_file(product_name)

