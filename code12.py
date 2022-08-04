import qrcode
from PIL import Image

#  Banner 
print("\n***** QR Code Generator ***** \n")
a = input("Enter the Link : ")

# qr code customization 
qr = qrcode.QRCode (
  version = 1,
  error_correction = qrcode.constants.ERROR_CORRECT_H,
  box_size = 20,
  border = 3,
)

qr.add_data(a)
qr.make(fit = True)

# Change the parameters of the next line to edit the colors of the qrcode
img = qr.make_image(fill_color = "black", back_color = "white")

img.save("qrcode.png")

print("\n DONE! ")