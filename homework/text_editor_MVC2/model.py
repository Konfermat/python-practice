import os
import uuid

# model
# create
# name
# if exist add suffix copy
# elif exist copy add suffix copy (2)
# elif exist copy and num add suffix copy ({num}+1)
# else dnno

# edit
# replace text
# replace text_data in file
# update text
# add data to a text file
# make recover copy before updating
# delete text
# delete recovery data
#
# recover
# history get
# input file name
# show file edit history
# enum, filename, action, time_stamp, file_data
# history met
# soft_recover
# save current file with one of the previous file_data add in history
# hard_recover
# replayce current file with one of the previous file_data and delete history from the exact file

'''
init folder
    if not create one
    init folder content

create file
show files list
delete file
    delete history    
open file
    show file data
    open history
        show file hisiory   3
    edit file
        update data
            init history    
            add history
            save file
            save history
        delete data
            init history    
            add history    
            save data
            save history
        replace data
            init history    
            add history
            save file
        close file without saveing
        close prog
            you sure? unsaved data wil be gone
    close file
close prog
'''

'''
intro
command list
1 create txt file 
2 open txt file
    txt file list
    edit
    close
close progf        
        
3 list txt files



'''

class Editor:
    def init(self):
        self.FILE_SUFFIX = '.txt'
        self.storage_path = 'file storage'

        # creats folder if not exist
        if not os.path.isdir(self.storage_path):
            os.mkdir(self.storage_path)

        self.edit_history = {}
        # file_name: [content:, history]

    #suffix checker
    @staticmethod
    def return_suffix(self, file_name) -> str:
        if not file_name.endswith(self.FILE_SUFFIX):
            file_name += self.FILE_SUFFIX
            return file_name
        elif file_name.endswith(self.FILE_SUFFIX):
            return file_name
    
    # file existence checker
    @staticmethod
    def is_file(self, file_name) -> bool:

        if file_name in Editor.get_folder_content():
            pass

    # show folder content
    @staticmethod
    def get_folder_content(self) -> list:
        return os.listdir(self.storage_path)

    # create file
    def create_file(self, file_name: str) -> None:
        # check if suffix
        file_name = Editor.return_suffix(file_name) 

        # folder content check
        folder_content = Editor.get_folder_content()

        # if file exist ask to change name


        if file_name in folder_content:
            print(
                f'File named "{file_name}" already exists. Pick another name.')
        elif not file_name in folder_content:
            with open(self.storage_path + '/' + file_name, 'w', encoding='utf-8') as f:
                f.write('')
            print(f'File "{file_name}" is created.')
        else:
            print('Error while creating file')



    # delete file
    def delete_file(self, file_name: str) -> None:
        file_name = Editor.return_suffix(file_name)

        
#     delete history
# open file
#     show file data
#     open history
#         show file hisiory   3
#     edit file
#         update data
#             init history
#             add history
#             save file
#             save history
#         delete data
#             init history
#             add history
#             save data
#             save history
#         replace data
#             init history
#             add history
#             save file
#         close file without saveing
#         close prog
#             you sure? unsaved data wil be gone
#     close file
# close prog
