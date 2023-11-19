import sys
import os
import requests
from PIL import Image
from io import BytesIO

def set_working_directory_to_exe_location():
    if getattr(sys, 'frozen', False):
        # If the script is frozen (e.g., an executable created by PyInstaller)
        exe_dir = os.path.dirname(sys.executable)
        os.chdir(exe_dir)
    else:
        # If the script is running in a non-frozen environment (e.g., in a development environment)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)



def save_image_from_url(url, save_path):
    if(url == None or url == ""):
        return
    response = requests.get(url)
    
    if response.status_code == 200:
        # Open the image using PIL
        img = Image.open(BytesIO(response.content))
        
        # Save the image to disk
        img.save(save_path)
        print(f"Image saved to {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def get_matching_or_first(items, predicate):
    if len(items) == 0:
        return None
    for item in items:
        if predicate(item):
            return item
    return items[0]
 
def clipSting(value, max) -> str:
    if value == None:
        return ''
    if len(value) > max:
        value = value[:max] + "..."
    return value