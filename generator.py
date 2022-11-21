import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 20,
    border = 4,
)

url = "https://neolux.ie/"
logo_link = "logo.png"
colour = "#233DFF"
logo = Image.open(logo_link)
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

qr.add_data(url)
qr.make(fit=True)

# img = qr.make_image(fill_color="white",back_color="#3B51FF")

# img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), ill_color="white",back_color=colour)

# img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

img = qr.make_image(fill_color="white",back_color=colour)

pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
# img.paste(logo, pos)

# type(img)
img.save("qrcode_neolux.png")