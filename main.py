from PIL import Image

backgroundColor = [31, 44, 36]
transitColor = [72, 102, 73]
accentColor = [255, 240, 222]

def convert_to_grayscale(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
    except FileNotFoundError:
        return print("Faulty input.")

    img = img.convert("RGB")  # Ensure image is in RGB mode

    # Create a new image for the grayscale version
    grayscale_img = Image.new("RGB", img.size)

    # Process each pixel
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            gray = (r + g + b) // 3
            if gray > 255 * 0.50 and gray < 255 * 0.60:
                grayscale_img.putpixel((x, y), (transitColor[0], transitColor[1], transitColor[2]))
            elif gray >= 255 * 0.60:
                grayscale_img.putpixel((x, y), (backgroundColor[0], backgroundColor[1], backgroundColor[2]))
            else:
                grayscale_img.putpixel((x, y), (accentColor[0], accentColor[1], accentColor[2]))


    # Save the grayscale image
    grayscale_img.save(output_path)
    print(f"Grayscale image saved to {output_path}")

# Example usage
convert_to_grayscale(input("Which image do you want to convert? "), input("What should the new image be called? "))
