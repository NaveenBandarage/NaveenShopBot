#https://www.adidas.co.nz/stan-smith-shoes/EE5818.html?forceSelSize=EE5818_630
from stockChecker import checkStock


def UrlGenerator(model, size):
    BaseSize = 530 #This is saying the shoesize is 6.5
    ShoeSize = size - 4
    ShoeSize = ShoeSize *20
    Rawsize = ShoeSize + BaseSize
    ShoeSizeCode = int(Rawsize)
    URL = 'https://www.adidas.co.nz/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    return URL
# Model = raw_input('Model #')
# Size = input('Size: ')

#URL = UrlGenerator(model, Size)
#print(str(URL))

def Main(model, size):

    URL = UrlGenerator(model, size)
    checkStock(URL, model)
