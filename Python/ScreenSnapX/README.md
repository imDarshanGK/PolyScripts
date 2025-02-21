# ScreenSnapX - Screenshot Capture Utility  

## Overview  
**ScreenSnapX** is a simple Python script that allows users to capture full-screen or region-specific screenshots using the `pyscreenshot` library. The script automates the screenshot process, saving images to a designated folder for easy access and organization.  

---

## Features  
- **Full-Screen Capture:** Takes a screenshot of the entire screen by default.  
- **Region-Specific Capture:** Allows users to specify a region (x1, y1, x2, y2) for partial screenshots.  
- **Custom Save Directory:** Screenshots are saved in a folder called `screenshots` by default.  
- **Timestamped Filenames:** If no filename is provided, the script automatically generates one based on the current timestamp.  
- **Cross-Platform Support:** Works on Windows, macOS, and Linux.  

---

## Installation  

1. **Clone the Repository:**  
```bash
git clone https://github.com/BigBang001/PolyScripts/ScreenSnapX.git
cd ScreenSnapX
```

2. **Install Dependencies:**  
```bash
pip install pyscreenshot
```

3. **Run the Script:**  
```bash
python screenshot.py
```

---

## Usage  

- **Full-Screen Screenshot:**  
Simply run the script without any arguments. The screenshot will be saved in the `screenshots` directory.  
```bash
python screenshot.py
```

- **Region-Specific Screenshot:**  
To capture a specific part of the screen, modify the script or call the function with region coordinates:  
```python
take_screenshot(region=(100, 100, 500, 400))
```

- **Change Save Directory:**  
Provide a custom directory for saving screenshots:  
```python
take_screenshot(save_dir="custom_folder")
```

- **Custom Filename:**  
```python
take_screenshot(filename="custom_name.png")
```

---

## Dependencies  
- Python 3.x  
- `pyscreenshot`  
```bash
pip install pyscreenshot
```

---

## Notes  
- `pyscreenshot` may require additional dependencies depending on the operating system (e.g., Pillow, scrot, or xclip for Linux).  
- The script automatically creates the save directory if it does not exist.  

---

**Key Points:**  
- The script is structured with reusable functions and customizable options.  
- The `README.md` covers everything from purpose to dependencies and usage instructions.  
- Examples for both full-screen and region-specific screenshots are included for clarity.  
 ---
