import pytesseract
import cv2
from agl_base_db.models import EndoscopyProcessor
import os
from collections import Counter
from tempfile import TemporaryDirectory
import re
from datetime import datetime
from typing import Dict, List
from icecream import ic

# Helper function to process date strings
def process_date_text(date_text):
    """
    Processes a string of text that represents a date and returns a datetime.date object.

    Args:
        date_text (str): A string of text that represents a date.

    Returns:
        datetime.date: A datetime.date object representing the parsed date, or None if the text cannot be parsed.
    """
    try:
        # Remove any non-digit characters
        date_text_clean = re.sub(r'\D', '', date_text)
        # Reformat to 'ddmmyyyy' if necessary
        if len(date_text_clean) == 8:
            return datetime.strptime(date_text_clean, "%d%m%Y").date()
    except ValueError:
        # Return None if the text cannot be parsed into a date
        # set date to 1/1/1900
        return datetime.strptime("01011900", "%d%m%Y").date()

# Helper function to process patient names
def process_name_text(name_text):
    """
    Processes a string containing a person's name and returns a tuple of their first names and last name.

    Args:
        name_text (str): A string containing a person's name in the format "Last Name, First Names".

    Returns:
        tuple: A tuple containing two strings - the person's first names and last name.
    """
    name_parts = name_text.replace('\n', ' ').split(',')
    last_name = name_parts[0].strip() if len(name_parts) > 0 else 'unknown'
    first_names = name_parts[1].strip() if len(name_parts) > 1 else 'unknown'
    return first_names, last_name

# Helper function to process endoscope type text
def process_general_text(endoscope_text):
    """
    This function takes in a string of text from an endoscope and returns a cleaned version of the text.
    """
    return ' '.join(endoscope_text.split())

# Function to extract text from ROIs
def extract_text_from_rois(image_path, processor:EndoscopyProcessor):
    """
    Extracts text from regions of interest (ROIs) in an image using OCR.

    Args:
        image_path (str): The path to the image file.
        processor (EndoscopyProcessor): An instance of the EndoscopyProcessor class.

    Returns:
        dict: A dictionary containing the extracted text for each ROI.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Initialize the dictionary to hold the extracted text
    extracted_texts = {}

    # Define your ROIs and their corresponding post-processing functions in tuples
    rois_with_postprocessing = [
        ('examination_date', processor.get_roi_examination_date, process_date_text),
        ('patient_name', processor.get_roi_patient_name, process_name_text),
        ('patient_dob', processor.get_roi_patient_dob, process_date_text),
        ('endoscope_type', processor.get_roi_endoscope_type, process_general_text),
    ]

    # Extract and post-process text for each ROI
    for roi_name, roi_function, post_process in rois_with_postprocessing:
        # Get the ROI dictionary
        roi = roi_function()
        
        # Check if the ROI has values
        if all(roi.values()):
            # Crop the image to the ROI
            x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']
            roi_cropped = image[y:y+h, x:x+w]
            
            # OCR configuration: disable language-based corrections
            config = '--psm 6'  # Assume a single uniform block of text
            
            # Use pytesseract to do OCR on the cropped ROI
            text = pytesseract.image_to_string(roi_cropped, config=config).strip()
            
            # Post-process extracted text
            processed_text = post_process(text)
            
            # Store the processed text in the dictionary
            extracted_texts[roi_name] = processed_text

    return extracted_texts


def get_most_frequent_values(rois_texts: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Given a dictionary of ROIs and their corresponding texts, returns a dictionary of the most frequent text for each ROI.

    Args:
        rois_texts: A dictionary where the keys are the names of the ROIs and the values are lists of texts.

    Returns:
        A dictionary where the keys are the names of the ROIs and the values are the most frequent text for each ROI.
    """
    most_frequent = {}
    for key in rois_texts.keys():
        counter = Counter([text for text in rois_texts[key] if text])
        most_frequent[key], _ = counter.most_common(1)[0] if counter else (None, None)
    return most_frequent

def process_video(video_path, processor):
    """
    Processes a video file by extracting text from regions of interest (ROIs) in each frame.

    Args:
        video_path (str): The path to the video file to process.
        processor (OCRProcessor): An instance of the OCRProcessor class that defines the ROIs to extract text from.

    Returns:
        dict: A dictionary containing the most frequent text values extracted from each ROI.
    """
    # Create a temporary directory to store frames
    with TemporaryDirectory() as temp_dir:
        ic(temp_dir)
        # Capture the video
        video = cv2.VideoCapture(video_path)
        success, frame_number = True, 0
        rois_texts = {roi_name: [] for roi_name in processor.get_rois().keys()}

        while success:
            success, frame = video.read()

            # Check if this is the 200th frame
            if frame_number % 200 == 0 and success:
                frame_path = os.path.join(temp_dir, f"frame_{frame_number}.jpg")
                cv2.imwrite(frame_path, frame)  # Save the frame as a JPEG file
                
                # Extract text from ROIs
                extracted_texts = extract_text_from_rois(frame_path, processor)
                
                # Store the extracted text from each ROI
                for key, text in extracted_texts.items():
                    rois_texts[key].append(text)

            frame_number += 1

            if frame_number >=5: break

        # Release the video capture object
        video.release()

        # Get the most frequent values for each ROI
        return get_most_frequent_values(rois_texts)

