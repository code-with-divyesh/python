import qrcode

# Data to encode
data = "https://github.com/code-with-divyesh" 

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # size of the QR code (1 = small, 40 = large)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,   # size of each box
    border=4,      # thickness of border
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code as image
img.save("ab_code.png")

print("QR Code generated and saved as 'qr_code.png'")
