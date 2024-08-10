# ROX Auto Fishing

### Windows Client
1. Install Python https://www.python.org/downloads/release/python-3119/
2. Make sure checklist `Add Path to Environment`
3. Open terminal, run `pip install pyautogui opencv-python screeninfo`
4. run `py main.py`

### Recommended Settings
1. ROX Client full screen, button reel/cast need to on bottom right position
2. Resolution on rox setting high
3. Set higher confidence (recommended 0.9 - 0.97) `cf_reel` / `cf_cast` when reel/cast button clicked before the time to reel
4. Set lower confidence `cf_reel` / `cf_cast` when reel/cast not detected
5. If you have multiple display, set display index regarding to your main display
6. Try to replace the screenshot by your own, if reel/cast not detected
7. This is made by trial and error, so happy experiment :D
