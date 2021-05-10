pip install cloudsight
pip install pillow

from PIL import Image
import cloudsight

im = Image.open('YOURIMAGE.jpg')
im.thumbnail((600,600))
im.save('cloudsight.jpg')

auth = cloudsight.SimpleAuth('YOUR KEY')
with open('cloudsight.jpg', 'rb') as f:
    response = api.image_request(f, 'cloudsight.jpg',  {'image_request[locale]': 'en-US',})
status = api.wait(response['token'], timeout=30)
print status