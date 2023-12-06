import cv2
import time
import os
#pip install opencv-python

start_video = time.time()
# Specify the directory where you want to save the screenshots

#video_path = "C:/Users/elinorp/Desktop/Scapa/M_06052023102912_00000000U0558311_1_001-1.mkv"
video_path = "U:/TE/WIN_20230907_13_43_25_Pro.mp4"
parts = video_path.split("/")
# Get the last part of the path
folder_name = parts[1]


# Path where you want to save the output images
#output_directory = "C:/Users/elinorp/Desktop/Scapa/output/"

# Create output directory if it does not exist
parent_directory = os.path.dirname(video_path)


# Function to calculate contrast of an image
def calculate_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = cv2.Laplacian(gray, cv2.CV_64F).var()
    return contrast


def get_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s


# Function to get the best frame per second within intervals
def get_best_frames_per_interval(cap, start_frame, end_frame, snapshot_interval):
    best_frames = {}
    current_frame = start_frame
    while current_frame <= end_frame:
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cap.read()
        if not ret:
            break

        current_second = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)

        current_contrast = calculate_contrast(frame)

        if current_second not in best_frames or current_contrast > best_frames[current_second]['contrast']:
            best_frames[current_second] = {'frame': frame.copy(), 'contrast': current_contrast}

        current_frame += snapshot_interval

    return best_frames

cap = cv2.VideoCapture(video_path)

# Video parameters
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Set time (in hh:mm:ss format)
start_time = "00:00:00" ############################################ Put start time ###################################################################################
end_time = "00:04:00" ############################################## Put end time ###################################################################################

# Convert time to seconds and then to frames
start_frame = get_seconds(start_time) * fps
end_frame = get_seconds(end_time) * fps
# Get best frames per second within intervals


# Get best frames per second within intervals

# Snapshot interval (in frames)
snapshot_interval = 1 * fps  ############################################## Put Interval ###################################################################################

# Initialize the current frame
current_frame = start_frame

# Set the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
personal_path="C:/Users/elinorp/Desktop/"
output_directory=os.path.join(personal_path,folder_name)
output_directory=output_directory+"/output/"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

best_frames = {}
current_frame = start_frame

while cap.isOpened() and current_frame <= end_frame:
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    current_second = int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
    current_contrast = calculate_contrast(frame)

    if current_second not in best_frames or current_contrast > best_frames[current_second]['contrast']:
        best_frames[current_second] = {'frame': frame.copy(), 'contrast': current_contrast}

    current_frame += snapshot_interval

for second, data in best_frames.items():
    frame = data['frame']
    time_stamp = f"{second:06}"

    snapshot_name = output_directory + f"snapshot_{current_frame}_{time_stamp}.png"
    print(output_directory)
    #snapshot_name = output_directory+f"snapshot_{current_frame}.jpg"
    cv2.imwrite(snapshot_name, frame)
    print(f"Saved snapshot {snapshot_name}")

    # Increment frame count by snapshot_interval
    current_frame += snapshot_interval

    # Jump to next snapshot frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
end_video = time.time()
total_time = end_video - start_video
print(f"Total execution time: {total_time} seconds")
print("Done!!!!!")

# Release video capture
cap.release()
cv2.destroyAllWindows()
