import os

def rename_files(file_name, dir_name):
  files = os.listdir(os.getcwd() + '/imgs/' + dir_name + '/' + file_name +'/')
  for i, old_name in enumerate(files):
    number = old_name.split('.')[0]
    new_name = number + '.jpg'
    os.rename(os.getcwd() + '/imgs/' + dir_name + '/' + file_name +'/' + old_name, os.getcwd() + '/imgs/' + dir_name + '/' + file_name +'/' + new_name)
    if(new_name == '.jpg' or new_name == "jpg"):
      os.remove(os.getcwd() + '/imgs/' + dir_name + '/' + file_name +'/' + new_name)
      print("deleted .jpg or jpg")
    print(old_name + '→' + new_name)
rename_files('kinmedai', 'sushi/test_images')
