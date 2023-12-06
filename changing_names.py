import os
import re
filter_list = ["BLI_", "LCI_", "WLI_"]
# change

# # Function to rename image files
# def rename_images_with_prefix(path):
#     try:
#         for root, dirs, files in os.walk(path):
#             # Get the last two folder names from the current subdirectory
#             folder_names = os.path.normpath(root).split(os.path.sep)[-3:]
#             prefix = '_'.join(folder_names)
#             prefix = prefix.upper()
#             patient_id=folder_names[0]
#             #print(patient_id)
#             for filename in files:
#                 # Check if the file is an image (you can customize this condition)
#                 if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', 'bmp',".JPG",".PNG",".TIF",".JPEG")):
#                     #patient_code_match = re.search(r'[a-zA-Z]{2}[0-9]{4}', filename)
#                     #patient_code = patient_code_match.group() if patient_code_match else None
#                     #if patient_code is not None:
#                    #  patient_zoom_match = re.search(r'(?i)zoom /d+', filename)
#                    #  patient_zoom = patient_zoom_match.group() if patient_zoom_match else None
#                    #  patient_new_zoom=re.search(r'ZOOM [a-zA-Z]', root)
#                    #  # Check if the filename doesn't contain "BLI", "LCI", or "WLI"
#                    #  if patient_zoom is not None:
#                    # # matches_filter = any(filter in filename for filter in filter_list)
#                    #     #if not matches_filter:
#                    #          # Rename the file with the desired prefix
#                    #      new_filename = f"{prefix}_{filename}"
#                    #      old_filepath = os.path.join(root, filename)
#                    #      new_filepath = os.path.join(root, new_filename)
#                    #      #os.rename(old_filepath, new_filepath)
#                    #      print(f"Renamed: {old_filepath} -> {new_filepath}")
#                    #  else:
#                    #      print("I don't have numerical ZOOM")
#                     if patient_id not in filename:
#                         new_filename = f"{patient_id}_{filename}"
#
#                         old_filepath = os.path.join(root, filename)
#                         new_filepath = os.path.join(root, new_filename)
#                         #os.rename(old_filepath, new_filepath)
#                         print(f"Renamed: {old_filepath} -> {new_filepath}")
#
#         print("Renaming completed.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

import os
import re

filter_list = ["BLI_", "LCI_", "WLI_"]

# Function to rename image files
# Function to rename image files
def rename_images_with_prefix(path):
    try:
        for root, dirs, files in os.walk(path):
            # Get the last two folder names from the current subdirectory
            folder_names = os.path.normpath(root).split(os.path.sep)[-3:]
            #else:
            if "מטופלים מוכנים" in folder_names :
                folder_names = os.path.normpath(root).split(os.path.sep)[-2:]
            prefix = '_'.join(folder_names)
            prefix = prefix.upper()
            patient_id = folder_names[0]

            for filename in files:
              #  if filename.startswith("snapshot"):
                    # Check if the file is an image (you can customize this condition)
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', 'bmp',".JPG",".PNG",".TIF",".JPEG",".tif")):
                        patient_zoom_match = re.search(r'(?i)ZOOM (/d+)', filename)
                        if patient_zoom_match:
                            digit = patient_zoom_match.group(1)
                            if digit.isdigit():
                                # Extract the letter from the folder name
                                patient_new_zoom_match = re.search(r'(?i)ZOOM ([a-zA-Z])', root)
                                if patient_new_zoom_match:
                                    letter = patient_new_zoom_match.group(1)
                                    new_zoom = f'ZOOM {letter}'
                                    new_filename = filename.replace(f'ZOOM {digit}', new_zoom)
                                    new_filepath = os.path.join(root, new_filename)
                                    old_filepath = os.path.join(root, filename)

                                    print(f"Renamed: {filename} -> {new_filename}")

                                    os.rename(old_filepath, new_filepath)
                                else:
                                    print(f"Warning: No letter found in folder name for '{filename}' in '{root}'")
                            else:
                                print(f"Warning: No digit found after 'zoom' in filename '{filename}' in '{root}'")
                        elif "ZOOM" not in filename: # cases where zoom was not in the file name but was added later
                            if "ZOOM" in root:
                                 new_filename = f"{prefix}_{filename}"
                                 old_filepath = os.path.join(root, filename)
                                 new_filepath = os.path.join(root, new_filename)
                                 os.rename(old_filepath, new_filepath)
                                 print(f"Renamed: {old_filepath} -> {new_filepath}")
                            else:
                                new_filename = f"{prefix}_{filename}"
                                old_filepath = os.path.join(root, filename)
                                new_filepath = os.path.join(root, new_filename)
                                os.rename(old_filepath, new_filepath)
                                print(f"Renamed: {old_filepath} -> {new_filepath}")
                        else:
                            new_filename = f"{prefix}_{filename}"
                            old_filepath = os.path.join(root, filename)
                            new_filepath = os.path.join(root, new_filename)
                            os.rename(old_filepath, new_filepath)
                            print(f"Renamed: {old_filepath} -> {new_filepath}")

            print("Renaming completed.")
    except Exception as e:
            print(f"An error occurred: {e}")



path="U:/מטופלים מוכנים/"
rename_images_with_prefix(path)


def rename_images_with_prefix_ex(path):
    try:
        for root, dirs, files in os.walk(path):
            # Get the last two folder names from the current subdirectory
            folder_names = os.path.normpath(root).split(os.path.sep)[-3:]
            prefix = '_'.join(folder_names)
            prefix = prefix.upper()
            patient_id = folder_names[0]

            # Check if "EX_VIVO" is in the path and add it to the prefix
            if "EX_VIVO" in root:
                prefix += "_EX_VIVO"

            for filename in files:
                # Check if the file is an image (you can customize this condition)
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', 'bmp',".JPG",".PNG",".TIF",".JPEG")):
                    patient_zoom_match = re.search(r'(?i)ZOOM (/d+)', filename)
                    if patient_zoom_match:
                        digit = patient_zoom_match.group(1)
                        if digit.isdigit():
                            # Extract the letter from the folder name
                            patient_new_zoom_match = re.search(r'ZOOM ([a-zA-Z])', root)
                            if patient_new_zoom_match:
                                letter = patient_new_zoom_match.group(1)
                                new_zoom = f'ZOOM {letter}'
                                new_filename = filename.replace(f'ZOOM {digit}', new_zoom)
                                new_filepath = os.path.join(root, new_filename)
                                old_filepath = os.path.join(root, filename)

                                print(f"Renamed: {filename} -> {new_filename}")

                                # Uncomment the line below to perform the actual renaming
                                os.rename(old_filepath, new_filepath)
                            else:
                                print(f"Warning: No letter found in folder name for '{filename}' in '{root}'")
                        else:
                            print(f"Warning: No digit found after 'zoom' in filename '{filename}' in '{root}'")
                    elif "ZOOM" not in filename:  # cases where zoom was not in the file name but was added later
                        new_filename = f"{prefix}_{filename}"
                        old_filepath = os.path.join(root, filename)
                        new_filepath = os.path.join(root, new_filename)
                        # Uncomment the line below to perform the actual renaming
                        os.rename(old_filepath, new_filepath)
                        print(f"Renamed: {old_filepath} -> {new_filepath}")
                    else:
                        new_filename = f"{prefix}_{filename}"
                        old_filepath = os.path.join(root, filename)
                        new_filepath = os.path.join(root, new_filename)
                        # Uncomment the line below to perform the actual renaming
                        os.rename(old_filepath, new_filepath)
                        print(f"Renamed: {old_filepath} -> {new_filepath}")

        print("Renaming completed.")
    except Exception as e:
        print(f"An error occurred: {e}")




#path="U:/AI Tumor Margin project/Data_Doc_new/EX_VIVO/"
#rename_images_with_prefix(path)

rename_images_with_prefix_ex(path)
# Specify the path to the directory containing the images
directory_path = r'U:/מטופלים מוכנים/KA2698/'

def remove_heabrew_string(path):
    for root, dirs, files in os.walk(path):
        # Get the last two folder names from the current subdirectory
        folder_names = os.path.normpath(root).split(os.path.sep)[-3:]
        prefix = '_'.join(folder_names)
        prefix = prefix.upper()
        patient_id = folder_names[0]

        for filename in files:
            # Check if the file is an image (you can customize this condition)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', 'bmp', ".JPG", ".PNG", ".TIF", ".JPEG")):
                ready_match = re.search(r'מטופלים מוכנים_', filename)
                if ready_match:
                    # Extract the matched string
                    ready_string = ready_match.group(0)

                    # Remove the matched string from the filename
                    new_filename = re.sub(re.escape(ready_string), '', filename)

                    # Optionally, you can rename the file
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, new_filename)
                    os.rename(old_path, new_path)

                     # Print for verification (you can remove this in the final version)
                     print(f"Renamed: {filename} -> {new_filename}")

remove_heabrew_string(directory_path)
# crea



