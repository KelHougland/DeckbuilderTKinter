 # numbers for pulling opus III - http://a4.res.cloudinary.com/csicdn/image/upload//v1/Images/Products/Misc%20Art/Opus%20III/full/ff3_3-001.jpg
# opusii=["{0:03}".format(i) for i in range(1,149)] # numbers for pulling opus III - http://a3.res.cloudinary.com/csicdn/image/upload//v1/Images/Products/Misc%20Art/Opus%20II/full/ff_2-001.jpg
# opusi=["{0:03}".format(i) for i in range(1,216)] # numbers for pulling opus III - http://a5.res.cloudinary.com/csicdn/image/upload//v1/Images/Products/Misc%20Art/Opus%20I/full/ff_1-001.jpg
import io
import requests
from PIL import Image

# opusiii=["{0:03}".format(i) for i in range(1,155)]
# for i in opusiii:
#     img = requests.get(" http://a4.res.cloudinary.com/csicdn/image/upload//v1/Images/Products/Misc%20Art/Opus%20III/full/ff3_3-{0}.jpg".format(i))
#     im = Image.open(io.BytesIO(img.content))
#     im.save('opusiii_{0}.jpg'.format(i))


opusii=["{0:03}".format(i) for i in range(20,149)]
for i in opusii:
    img = requests.get("http://fftcgmognet.com/images/cards/1/2/{0}.jpg".format(i))
    im = Image.open(io.BytesIO(img.content))
    im.save('opusii_{0}.jpg'.format(i))

opusi=["{0:03}".format(i) for i in range(1,216)]
for i in opusi:
    img = requests.get("http://fftcgmognet.com/images/cards/1/1/{0}.jpg".format(i))
    im = Image.open(io.BytesIO(img.content))
    im.save('opusi_{0}.jpg'.format(i))

