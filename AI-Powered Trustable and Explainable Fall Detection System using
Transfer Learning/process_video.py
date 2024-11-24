import cv2
import os

fall_videos_path = "/home/pranav/Projects/Research/data/fall_videos"  # Replace with the path to fall videos
non_fall_videos_path = "/home/pranav/Projects/Research/data/non_fall_videos"  
output_fall_path = "processed_dataset/fall"  # Path to save fall frames
output_non_fall_path = "processed_dataset/non_fall"  # Path to save non-fall frames

# Create output directories if they don't exist
os.makedirs(output_fall_path, exist_ok=True)
os.makedirs(output_non_fall_path, exist_ok=True)

def process_video(video_path, output_path, label):
    """Processes a video, extracting and saving frames."""
    video_name = os.path.splitext(os.path.basename(video_path))[0]  # Get video name
    cap = cv2.VideoCapture(video_path)  # Open video
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Break if no frames left

        # Save frame as image
        frame_filename = os.path.join(output_path, f"{label}_{video_name}_frame{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Processed {video_name}: {frame_count} frames extracted.")

# Process fall videos
fall_videos = [os.path.join(fall_videos_path, v) for v in os.listdir(fall_videos_path) if v.endswith(('.mp4', '.avi', '.mkv'))]
for video in fall_videos:
    process_video(video, output_fall_path, label="fall")

# Process non-fall videos
non_fall_videos = [os.path.join(non_fall_videos_path, v) for v in os.listdir(non_fall_videos_path) if v.endswith(('.mp4', '.avi', '.mkv'))]
for video in non_fall_videos:
    process_video(video, output_non_fall_path, label="nonfall")

print("Video processing complete. Frames saved to 'processed_dataset/'.")

