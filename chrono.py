import os
from bs4 import BeautifulSoup

cwd = input('Folder name:')
if cwd:
    os.chdir(cwd)

image_class = '_2yuc _3-96'
html_data = open('message_1.html', 'r', errors='ignore', encoding='utf-8')
soup = BeautifulSoup(html_data, 'html.parser')
images = soup.find_all(attrs={'class': image_class})

paths = []

for image in images:
    if 'photos' in image['src']:
        paths.append(image['src'])


for i, path in enumerate(reversed(paths), start=1):
    old_name = 'photos/' + os.path.basename(path)
    new_name = ''
    if '.png' in path:
        new_name = f'photos/{i}.png'
    elif '.jpg' in path:
        new_name = f'photos/{i}.jpg'
    else:
        print('No file extension')
        break
    #print(f'Renaming {old_name} to {new_name}')
    os.rename(old_name, new_name)

html_data.close()

