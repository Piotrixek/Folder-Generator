import argparse
import os
import random
import string

def create_folders_and_files(num_folders, location):
  # Create the specified number of folders
  for i in range(num_folders):
    # Generate a random name for the folder
    folder_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    # Create the folder at the specified location
    folder_path = os.path.join(location, folder_name)
    os.mkdir(folder_path)
    # Generate random names for the HTML, CSS, and JavaScript files
    html_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.html'
    css_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.css'
    js_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.js'
    # Create empty HTML, CSS, and JavaScript files in the folder
    html_path = os.path.join(folder_path, html_name)
    css_path = os.path.join(folder_path, css_name)
    js_path = os.path.join(folder_path, js_name)
    open(html_path, 'w').close()
    open(css_path, 'w').close()
    open(js_path, 'w').close()
    # Write the HTML code to the HTML file
    with open(html_path, 'w') as html_file:
      html_file.write('<!DOCTYPE html>\n')
      html_file.write('<html>\n')
      html_file.write('<head>\n')
      html_file.write('\t<meta charset="utf-8">\n')
      html_file.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
      html_file.write('\t<link rel="stylesheet" href="{}">\n'.format(css_name))
      html_file.write('\t<title></title>\n')
      html_file.write('</head>\n')
      html_file.write('<body>\n\n')
      html_file.write('</body>\n')
      html_file.write('</html>\n')

if __name__ == '__main__':
  # Parse the command-line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('num_folders', type=int, help='the number of folders to create')
  parser.add_argument('location', help='the location where the folders should be created')
  args = parser.parse_args()

# Create the folders and files
  create_folders_and_files(args.num_folders, args.location)