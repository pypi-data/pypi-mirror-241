import cv2
import numpy as np
from .utils import urljoin, seconds_to_hms
from .config import VadsConfig

class VadsDisplay:
    def __init__(self, config=None):
        if config is None:
            config = VadsConfig()

        self.video_width = config.video_width
        self.video_height = config.video_height

    def display_ads(self, ads):
        for ad in ads:
            if ad.get('video_file'):
                self.display_video(ad['video_file'], ad['qr_code'], ad['image_file'], ad['whatsapp_number'])
            elif ad.get('image_file'):
                self.display_image(ad['image_file'])
            elif ad.get('qr_code'):
                self.display_qr_code(ad['qr_code'])
            else:
                print("No valid content to display.")

    def display_video(self, video_file, qr_code_url, image_file, whatsapp_number):
        try:
            cap = cv2.VideoCapture(urljoin('http://127.0.0.1:8000', video_file))

            if not cap.isOpened():
                print("Error: Unable to open video stream.")
                return

            # Set custom width and height
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_height)

            # Get the total number of frames and frame rate
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

            # Check if frame rate is zero or total frames is negative
            if frame_rate <= 0 or total_frames <= 0:
                print("Unable to determine frame rate or total frames. Using default values.")
                frame_rate = 29  # Set a default frame rate
                total_frames = 1000  # Set a default total frames

            print(f"Total Frames: {total_frames}, Frame Rate: {frame_rate}")

            # Load the QR code image
            qr_code_data = requests.get(urljoin('http://127.0.0.1:8000', qr_code_url)).content
            qr_code_array = np.frombuffer(qr_code_data, dtype=np.uint8)
            qr_code = cv2.imdecode(qr_code_array, cv2.IMREAD_COLOR)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Get the current frame number
                current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

                print(f"Processing Frame {current_frame} of {total_frames}")

                # Calculate the remaining time for the ad
                remaining_time_seconds = (total_frames - current_frame) / frame_rate
                remaining_time_hours, remaining_time_minutes, remaining_time_seconds = seconds_to_hms(remaining_time_seconds)

                # Create a black strip at the bottom
                strip = np.zeros((STRIP_HEIGHT, int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), dtype=np.uint8)

                # Resize QR code to a smaller size
                qr_code_data = requests.get(urljoin('http://127.0.0.1:8000', qr_code_url)).content
                qr_code_array = np.frombuffer(qr_code_data, dtype=np.uint8)
                qr_code = cv2.imdecode(qr_code_array, cv2.IMREAD_COLOR)
                qr_code_resized = cv2.resize(qr_code, (100, 100))

                # Define the position to display the QR code (bottom right corner)
                qr_code_position = (frame.shape[1] - 120, frame.shape[0] - 120)

                # Add QR code to the video frame
                frame[qr_code_position[1]:qr_code_position[1] + 100, qr_code_position[0]:qr_code_position[0] + 100] = qr_code_resized

                # Combine video frame and strip
                combined_frame = np.vstack([frame, strip])

                # Display remaining time at the bottom
                if remaining_time_seconds >= 0:
                    time_str = f"Time Remaining: {remaining_time_hours:02d}:{remaining_time_minutes:02d}:{remaining_time_seconds:02d}"
                else:
                    time_str = "Ad Ended"

                cv2.putText(combined_frame, time_str,
                            (10, frame.shape[0] + STRIP_HEIGHT - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Display contact information at the bottom
                cv2.putText(combined_frame, f"Contact: {whatsapp_number}", (frame.shape[1] // 2, frame.shape[0] + STRIP_HEIGHT - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Resize the window based on the combined frame size
                cv2.namedWindow('Video Display', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('Video Display', frame.shape[1], frame.shape[0] + STRIP_HEIGHT)

                cv2.imshow('Video Display', combined_frame)

                if cv2.waitKey(30) & 0xFF == ord('q'):
                    break

                # Release memory by periodically restarting the VideoCapture object
                if current_frame % 300 == 0:  # Adjust the interval as needed
                    cap.release()
                    cap = cv2.VideoCapture(urljoin('http://127.0.0.1:8000', video_file))

                    # Set custom width and height
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_width)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_height)

            # Display the image at the end of the video
            self.display_image(image_file)

            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("Error:", e)

    def display_image(self, image_file):
        try:
            img_data = requests.get(urljoin('http://127.0.0.1:8000', image_file)).content
            img_array = np.frombuffer(img_data, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            cv2.imshow('Image Display', img)
            cv2.waitKey(5000)  # Display each ad for 5 seconds
            cv2.destroyAllWindows()

        except Exception as e:
            print("Error:", e)

    def display_qr_code(self, qr_code_url):
        try:
            qr_code_data = requests.get(urljoin('http://127.0.0.1:8000', qr_code_url)).content
            qr_code_array = np.frombuffer(qr_code_data, dtype=np.uint8)
            qr_code_image = cv2.imdecode(qr_code_array, cv2.IMREAD_COLOR)

            cv2.imshow('QR Code Display', qr_code_image)
            cv2.waitKey(5000)  # Display QR code for 5 seconds
            cv2.destroyAllWindows()

        except Exception as e:
            print("Error:", e)
