import requests

req=requests.get('https://gist.githubusercontent.com/matheesha-pathirana/8973bf4f96912e28791a41def878f68d/raw/4f6e972663fe1b0e6f32d5f1c81a23d672901e0d/AIO_installer_insiders.txt')
print(req.text)