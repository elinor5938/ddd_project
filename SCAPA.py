import cv2
import time
import os
#pip install opencv-python

start_video = time.time()
# Specify the directory where you want to save the screenshots

#video_path = "C:/Users/elinorp/Desktop/Scapa/M_06052023102912_00000000U0558311_1_001-1.mkv"
video_path = "U:/ML7786/2024-02-06 12-28-40.mkv"
parts = video_path.split("/")
# Get the last part of the path
folder_name = parts[2]


# Path where you want to save the output images
#output_directory = "C:/Users/elinorp/Desktop/Scapa/output/"

# Create output directory if it does not exist
parent_directory = os.path.dirname(video_path)

def get_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s



cap = cv2.VideoCapture(video_path)

# Video parameters
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(fps)



# Set time (in hh:mm:ss format)
start_time = "00:00:24" ############################################ Put start time ###################################################################################
end_time = "00:08:52" ############################################## Put end time ###################################################################################

# Convert time to seconds and then to frames
start_frame = get_seconds(start_time) * fps
end_frame = get_seconds(end_time) * fps

# Snapshot interval (in frames) # capturing interval
# capturing every n seconds per frame rate return the number of frames to skip
snapshot_interval = 0.5 * fps  ############################################## Put Interval ###################################################################################

# Initialize the current frame
current_frame = start_frame

# Set the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
personal_path="C:/Users/elinorp/Desktop/"
output_directory=os.path.join(personal_path,folder_name)
output_directory=output_directory+"/output/"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

while cap.isOpened() and current_frame <= end_frame:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Save snapshot
    # Calculate the time in hh:mm:ss from current_frame and fps
    hours, remainder = divmod(current_frame // fps, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_stamp = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    left, upper, right, lower = 0, 0, 1350, 1080
    #frame_cropped = frame[upper:lower, left:right]

  #  output_directory="C:/Users/elinorp/Desktop/01.05.2023_0855/output/"
    time_stamp = time_stamp.replace(":", "_")

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

