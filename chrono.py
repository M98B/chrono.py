import os
from bs4 import BeautifulSoup

cwd = input('Folder name:')
if cwd:
    os.chdir(cwd)

name_convention = input("Give the naming convention")

starting_index = 1
image_class = '_2yuc _3-96'
html_data = open('message_1.html', 'r', errors='ignore', encoding='utf-8')
soup = BeautifulSoup(html_data, 'html.parser')
images = soup.find_all(attrs={'class': image_class})

paths = []

for image in reversed(images):
    if 'photos' in image['src']:
        paths.append(image['src'])


for i, path in enumerate(paths, start=starting_index):
    old_name = 'photos/' + os.path.basename(path)
    new_name = ''
    if '.png' in path:
        new_name = f'photos/{name_convention}_{i}.png'
    elif '.jpg' in path:
        new_name = f'photos/{name_convention}_{i}.jpg'
    else:
        print('No file extension')
        break

    os.rename(old_name, new_name)

html_data.close()


