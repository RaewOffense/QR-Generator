import qrcode

# Data to encode
data = input("Enter Url to make qrcode:")

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code (1-40, where 1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border thickness (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR Code image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
