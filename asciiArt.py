from PIL import Image

# ASCII characters to represent different shades of gray
acsi = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

ascii_chars = []

for v in acsi:
    ascii_chars.append("".join(v))


# Resize image according to the new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayscale(image):
    return image.convert("L")

# Convert grayscale pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 25]
    return ascii_str

# Main function to convert image to ASCII
def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Convert image to grayscale
    image = grayscale(resize_image(image, new_width))

    # Convert pixels to ASCII
    ascii_str = pixels_to_ascii(image)

    # Format ASCII string
    pixel_count = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # Print result
    print(ascii_img)

if __name__ == '__main__':
    image_path = 'resized.jpg'  # Replace with your image file path
    main(image_path)
