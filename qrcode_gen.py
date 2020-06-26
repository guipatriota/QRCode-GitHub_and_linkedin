# Python script for QRCode generation to github repositories.

import pyqrcode

dev_name = input('What is your name?')
github_user_name = input('What is your GitHub user?')
linkedin_url = input('Paste your linkedin url profile here: ')
dev = ''.join(a for a in dev_name.title().replace(' ', '_'))
github_user = ''.join(a for a in github_user_name.lower().replace('@', ''))
print ('GitHub profile: '+'https://github.com/{}'.format(github_user))
qrcode_github = pyqrcode.create ('https://github.com/{}'.format(github_user), error = 'Q', version = 5, mode = 'binary')
qrcode_github.svg ('QRgithub_{}.svg'.format(dev), scale = 8, module_color = "black", background = "white")
qrcode_github.eps ('QRgithub_{}.eps'.format(dev), scale = 2)
qrcode_github.png ('QRgithub_{}.png'.format(dev), scale = 6, module_color = [0, 0, 0, 255], background = [0xFF, 0xFF, 0xFF])
qrcode_github.show ()

qrcode_linkedin = pyqrcode.create ('{}'.format(linkedin_url), error = 'Q', version = 5, mode = 'binary')
qrcode_linkedin.svg ('QRlinkedin_{}.svg'.format(dev), scale = 8, module_color = "black", background = "white")
qrcode_linkedin.eps ('QRlinkedin_{}.eps'.format(dev), scale = 2)
qrcode_linkedin.png ('QRlinkedin_{}.png'.format(dev), scale = 6, module_color = [0, 0, 0, 255], background = [0xFF, 0xFF, 0xFF])
qrcode_linkedin.show ()
print ('LinkedIn profile: '+linkedin_url)