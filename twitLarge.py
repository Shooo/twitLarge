#! /usr/bin/python3

import os, bs4, requests, sys, pyperclip

#pictureDir = ''
#saveDir = os.path.join(pictureDir, 'twitLarge')

#os.makedirs(saveDir, exist_ok=True)
#os.chdir(saveDir)

if len(sys.argv) == 1:
    address = pyperclip.paste()
elif len(sys.argv) == 2:
    address = sys.argv[1]
else:
    sys.stderr.write('Error, too many arguments\n')
    sys.exit(1)

print('Accessing: ' + address)
res = requests.get(address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('.AdaptiveMedia-photoContainer > img')

for element in elems:
    imgURL = element.get('src')
    res = requests.get(imgURL + ':large')

    imageName = os.path.basename(imgURL)
    print('Downloading: ' + imageName + '...')

    imageFile = open(imageName,'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
