import os
import pandas as pd
import re
from PIL import Image


# Define the root folder path
#root_folder = r'U:/AI Tumor Margin project/Data_Doc_new/IN_VIVO/'
root_folder="U:/AI Tumor Margin project/Data_Doc_new/IN_VIVO/" ########################## the modt updated folder path #######################################

# Define a list of image file extensions to consider
image_extensions = ['.png', '.jpg', '.tif',".jpeg",".JPG",".PNG",".TIF",".JPEG",".BMP",".bmp"]

# Initialize empty lists to store extracted data
comments=[]
patient_ids = []
patient_names = []
patient_codes = []
ages = []
genders = []
indications = []
tumor_types = []
filters = []
zooms = []
lvi_values = []
grade_in_numbers = []
depth_of_invasion = []
img_names = []
pixles=[]
type=[]
grade=[]
stage=[]
Tumor_budding=[]
layer=[]
deapth_micrometer=[]
other=[]
user=[]
Computer_tag=[]
# Check if the CSV file already exists
if os.path.exists("28_11.csv"): ########################### PUT OLD DF DOWNLOADED FROM TEAMS ###############################
    # Load the existing DataFrame from the CSV file
    try:
        existing_df = pd.read_csv("28_11.csv", encoding='latin-1')
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    # If the CSV file doesn't exist, create an empty DataFrame
    existing_df = pd.DataFrame(columns=['img_name'])
# Walk through the directory structure
for root, dirs, files in os.walk(root_folder):
    for filename in files:
        if filename.endswith(tuple(image_extensions)):
            img_name = filename
            if img_name in  existing_df['img_name'].values:
               #print("Image ecxists !!!!!")
               continue
            else:
            # Extract information from the directory structure
                img_path = os.path.join(root,img_name)
            try:
                image = Image.open(img_path)  # Replace 'your_image.jpg' with the path to your image

                # Get the dimensions (width and height) of the image
                width, height = image.size

                # Calculate the total number of pixels
                total_pixels = str(width) + "," + str(height)
                folder_parts = root.split(os.path.sep)

                if "EX VIVO" in folder_parts or "TBD" in folder_parts or "color" in folder_parts or "Normal Tissue" in folder_parts or "Not Relevant" in folder_parts or "חיתוך" in folder_parts or "tbd" in folder_parts or "To be deleted" in folder_parts or "To be delete" in folder_parts or "Surgery" in folder_parts:
                    continue

                else:

                    indication_match = re.search(r"(?i)(Colon|Esophagus|Stomach)", root)
                    indication = indication_match.group() if indication_match else None
                    filter_match= re.search(r'(?i)(BLI|WLI|LCI)', root)
                    filter_type = filter_match.group() if filter_match else None
                    patient_code_match = re.search(r'[a-zA-Z]{2,}[0-9]{4}', root)
                    patient_code = patient_code_match.group() if patient_code_match else None
                    patient_zoom_match = re.search(r'(?i)zoom [a-zA-Z]|NO ZOOM', root)


                    patient_zoom = patient_zoom_match.group() if patient_zoom_match else None
                    patient_tumor_type_match = re.search(r'(?i)(adenoma|adenocarcinoma|SCC|Normal_Tissue)', root)
                    tumor_type = patient_tumor_type_match.group() if patient_tumor_type_match else None
                    #if img_name not in img_names:
                        # Append extracted information to the respective lists
                    patient_ids.append(None)  # You can fill this in if you have patient IDs
                    patient_names.append(None)  # You can fill this in if you have patient names
                    patient_codes.append(patient_code)
                    zooms.append(patient_zoom)
                    ages.append(None)  # You can fill this in if you have patient ages
                    genders.append(None)  # You can fill this in if you have patient genders
                    indications.append(indication)
                    tumor_types.append(tumor_type)  # You can fill this in if you have tumor types
                    filters.append(filter_type)
                    lvi_values.append(None)  # You can fill this in if you have LVI values
                    grade_in_numbers.append(None)  # You can fill this in if you have grade in numbers
                    grade.append(None)
                    depth_of_invasion.append(None)  # You can fill this in if you have depth of invasion
                    deapth_micrometer.append(None)
                    comments.append(None)
                    stage.append(None)
                    Tumor_budding.append(None)
                    layer.append(None)
                    other.append(None)
                    user.append(None)
                    Computer_tag.append(None)
                    pixles.append(total_pixels)
                    type.append(filename[-3:])
                    img_names.append(img_name)
            except Exception as e:
                print(f"The image cannot be open: {e}")

# Create a DataFrame from the extracted data
data = {
    'Patient_ID': patient_ids,
    'Patient_Name': patient_names,
    'Patient_Code': patient_codes,
    'Age': ages,
    'Gender': genders,
    'Indication': indications,
    'Tumor_Type': tumor_types,
    'Filter': filters,
    'ZOOM': zooms,
    'GRADE':grade,
    'LVI': lvi_values,
    'Grade_In_Numbers': grade_in_numbers,
    'DEEP\ SUPERFICIAL': depth_of_invasion,
    'TISSIU LAYER INVASION':layer,
    'Depth_of_invasion (MICROMETER)':deapth_micrometer,
    'img_name': img_names,
    "pixels":pixles,
    "format":type,
    "Healthy/Other":comments,
    'Tumor budding':Tumor_budding,
    "Stage":stage,
    "other":other,
"Computer tag":Computer_tag,
    "User":user
}

# Combine the new data with the existing DataFrame
if os.path.exists("28_11.csv"):  ########################### PUT OLD DF DOWNLOADED FROM TEAMS ###############################
    combined_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
else:
    combined_df = pd.DataFrame(data)

# Save the combined DataFrame to the CSV file
combined_df=combined_df[['Patient_Code', 'Indication', 'Tumor_Type', 'img_name',
       'Patient_ID', 'Patient_Name', 'Age', 'Gender', 'ZOOM', 'GRADE',
       'Grade_In_Numbers', 'Stage', 'LVI', 'DEEP\ SUPERFICIAL','TISSIU LAYER INVASION','Depth_of_invasion (MICROMETER)','pixels',
       'format', 'Filter', 'Healthy/Other',
       'Tumor budding']]
print(existing_df["Patient_Code"].nunique()) # old n
print(combined_df["Patient_Code"].nunique()) # new n
print(combined_df["Patient_Code"].unique()) # new n
new_df=pd.DataFrame(data)
print(new_df["Patient_Code"].unique()) # new n
[ i for i in new_df["Patient_Code"].unique() if i not in existing_df["Patient_Code"].unique() ]
combined_df.to_csv("NEW_COMBINED_DF.csv", index=False) ########################### created new df  ###############################


