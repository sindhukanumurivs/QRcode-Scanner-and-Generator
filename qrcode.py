import qrcode
from PIL import Image
import matplotlib.pyplot as plt

def create_and_show_qr_code(data, filename):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Controls how many pixels each “box” of the QR code is
        border=4,  # Controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)
    print(f"QR Code saved as {filename}")
    
    # Display the image using Pillow
    img.show()
    
    # Display the image using matplotlib
    img = img.convert("RGB")  # Convert the image to a format compatible with matplotlib
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

# Example usage
data = "https://www.example.com"
filename = "example_qr_code.png"
create_and_show_qr_code(data, filename)

