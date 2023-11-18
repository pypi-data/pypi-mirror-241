import shutil
import os
import subprocess

# Get the current working directory
# Replace 'your_installer.exe' with the actual name of your installer file

def install_ocr():
    installer_filename = 'ocr.exe'
    current_script_path = os.path.abspath(__file__)
    directory, file_name = os.path.split(current_script_path)
    # Create the full path to the installer by combining the current directory and the installer filename
    installer_path = os.path.join(directory, installer_filename)
    print(f"Installer Path: {installer_path}")

    try:
        subprocess.run([installer_path], check=True)
        print("Installation successful!")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed with error: {e}")


def find_tesseract():
     # Specify the path to the Tesseract executable
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Check if the Tesseract executable exists
    if os.path.exists(tesseract_path):
        return  tesseract_path

    # Attempt to find Tesseract in the system's PATH
    tesseract_path = shutil.which("tesseract")

    if tesseract_path is not None:
        return tesseract_path
    else:
        print("Tesseract not found. Please ensure it is installed and in the system's PATH.")

# Call the function to find Tesseract
print(find_tesseract())
