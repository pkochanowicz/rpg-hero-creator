import os

def download_small_gfile_from_id(file_id, output_file_with_path):
  make_sure_path_to_file_exists(output_file_with_path)
  output_file_with_path = wget.download('https://docs.google.com/uc?export=download&id=' + file_id)
  ## WGET ##
  os.system("wget -O " + $output_file_with_path + ' https://docs.google.com/uc?export=download&id=' + file_id)

#example for file_link = 'https://drive.google.com/open?id=1vFsgvRaLrMzXPwxx45iGz7vMjiQa9Uuy'
file_id = '1vFsgvRaLrMzXPwxx45iGz7vMjiQa9Uuy'
filename = '/content/tmp.txt'

file_link = input("provide link to .env file from google drive ")
download_small_gfile_from_id(file_id, filename)