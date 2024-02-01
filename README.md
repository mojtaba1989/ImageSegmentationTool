# Image Segmentation Tool

## Overview
This application is an Image Segmentation Tool designed to process and analyze images based on color segmentation. It provides a graphical user interface (GUI) for setting up segmentation parameters and navigating through images.

## Features
- **Color Segmentation:** Segmentation parameters can be adjusted for three different colors: White, Green, and Yellow.
- **Filter Sky:** An optional feature to filter out sky regions from the images.
- **HSV Sampling:** Allows users to sample HSV values from the image using a brush of customizable size.
- **Navigation:** Navigate through images, save segmentation results, and flag images.

## How to Use
1. **Open Folder:** Use the "Open Folder" option to select the directory containing the images you want to process.
2. **Select Image:** Choose an image from the dropdown menu.
3. **Adjust Parameters:** Adjust segmentation parameters for White, Green, Yellow, and Sky filtering.
4. **Navigation Buttons:** Use the "Next," "Previous," "Save," and "Save & Next" buttons to navigate and save segmentation results.
5. **Show Mask:** Toggle the "Show Mask" option to display the segmentation mask.
6. **Flag Images:** Flag images using the "Flag it" checkbox.
7. **Auto Load XML:** Automatically load default parameters from an XML file.

## HSV Sampling
- Activate the "HSV Sampling" checkbox.
- Adjust the brush size using the "Brush Size" spinner.
- Click on the image to sample HSV values.

## Additional Features
- **Auto Update:** Segmentation parameters are updated automatically when checkboxes are toggled.
- **Default XML Parameters:** Load default parameters from the "default_parameters.xml" file.
- **Help and About:** Access the help and about information through the menu.

## Dependencies
- Python 3.6
- Py-OpenCV 3.4.2
- PyQt5 5.9.2 

## How to Run
Ensure you have the necessary dependencies installed, then run the application using your preferred Python environment.

```bash
python image_seg_tool.py

Generate by ChatGPT
