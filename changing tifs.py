from PIL import Image
import os

# Input directory containing TIFF files
input_directory = "U:/מטופלים מוכנים/SR0091/"

for root, dirs, files in os.walk(input_directory):
    for filename in files:
        # Check if the file is a TIFF image

        if filename.lower().endswith('.tif'):
            tiff_path = os.path.join(root, filename)
            output_path = os.path.splitext(tiff_path)[0] + ".png"

            tiff_image = Image.open(tiff_path)
            tiff_image.close()

            try :
                tiff_image = Image.open(tiff_path)
                tiff_image.save(output_path, "PNG")
                os.remove(tiff_path)   # Delete the original TIFF file

                print(f"Conversion successful. Image saved as {output_path}")

            except Exception as e:
                print(f"An error occurred: {e}")

