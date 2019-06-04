import os

def make_sure_path_to_file_exists(path):
  folder = os.path.dirname(path)
  try:
    os.makedirs(folder)
  except:
    print("all good, ", folder, " already exists")
  return 


def download_small_gfile_from_id(file_id, output_file_with_path):
  make_sure_path_to_file_exists(output_file_with_path)
  ## WGET ##
  command = "sudo wget -O " + output_file_with_path + ' https://docs.google.com/uc?export=download&id=' + file_id
  print(command)
  os.system(command)

#example for file_link = 'https://drive.google.com/open?id=1vFsgvRaLrMzXPwxx45iGz7vMjiQa9Uuy'
file_id = '1vFsgvRaLrMzXPwxx45iGz7vMjiQa9Uuy'
filename = 'test.txt'

file_id = input("provide link to .env file from google drive ")
download_small_gfile_from_id(file_id, filename)
