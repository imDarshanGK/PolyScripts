import pyscreenshot as ImageGrab
import os
from datetime import datetime


def take_screenshot(region=None, save_dir="screenshots", filename=None):
    """
    Capture a screenshot and save it to the specified directory.

    Parameters:
    - region (tuple): Coordinates (x1, y1, x2, y2) to capture a specific region. Default is None (captures full screen).
    - save_dir (str): Directory to save the screenshot. Default is 'screenshots'.
    - filename (str): Name for the screenshot file. Default is timestamp.png.

    Returns:
    - str: Path to the saved screenshot.
    """

    # Create save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Capture the screenshot
    if region:
        screenshot = ImageGrab.grab(bbox=region)
    else:
        screenshot = ImageGrab.grab()

    # Set default filename with timestamp
    if not filename:
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    # Save the screenshot
    filepath = os.path.join(save_dir, filename)
    screenshot.save(filepath)
    print(f"Screenshot saved at: {filepath}")
    return filepath


if __name__ == "__main__":
    print("Taking full-screen screenshot...")
    take_screenshot()

    # Example for capturing a specific region (x1, y1, x2, y2)
    # print("Taking region-specific screenshot...")
    # take_screenshot(region=(100, 100, 500, 400))
