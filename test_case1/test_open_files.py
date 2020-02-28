import os
import shutil
import logging

from ddt import ddt, data

from businessView.homePageView import HomePageView
from common.myunit import StartEnd

path1 = r'C:\Users\DZPC1906167\Desktop\work'
file_names = []
sub_dirs_path = []
for root, dirs, files in os.walk(path1):
    for name in dirs:
        sub_dirs_path.append(os.path.join(root, name))
        print('dir: '+os.path.join(root, name))
target_path = sub_dirs_path[0:2]
for i in target_path:
    for root, dirs, files in os.walk(i):
        file_names = file_names + files
print('files>>>>> '+len(file_names))

@ddt
class OpenFiles(StartEnd):

    @data(*file_names[45:46])
    def test_bat_open_files(self, file_name=''):
        logging.info('==========正在打开%s==========' % file_name)

        type1 = os.path.splitext(file_name)[1]
        pc_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'wrong')
        if type1 != '.xls' and type1 != '.xlsx':
            shutil.copy(os.path.join(path1, file_name), pc_path)
            self.assertTrue(False, 'file format wrong')
        hp = HomePageView(self.driver)
        search_result = hp.search_file(file_name)
        self.assertTrue(search_result, 'cannot find file')
        open_result = hp.open_file(file_name)
        if not open_result:
            shutil.copy(os.path.join(path1, file_name), pc_path)
        self.assertTrue(open_result, 'open file failed')
        hp.close_file()
        self.assertTrue(hp.check_close_file(), msg='close file failed')

