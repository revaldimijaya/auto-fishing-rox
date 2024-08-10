import pyautogui
import time
from screeninfo import get_monitors

class Fishing:
    def __init__(self, total_bait=0, monitor_index=0, reel_images=[], cast_images=[], cf_cast=0.8, cf_reel=0.9):
        self.turn = 0
        self.total_bait = total_bait
        self.monitor_index = monitor_index
        self.region = self.get_bottom_right_region()
        self.reel_images = reel_images
        self.cast_images = cast_images
        self.cf_cast = cf_cast
        self.cf_reel = cf_reel

    def get_bottom_right_region(self):
        monitors = get_monitors()
        if self.monitor_index < 0 or self.monitor_index >= len(monitors):
            raise ValueError("Invalid monitor index.")
        monitor = monitors[self.monitor_index]
        
        quadrant_width = monitor.width // 2
        quadrant_height = monitor.height // 2
        
        left = monitor.x + quadrant_width
        top = monitor.y + quadrant_height
        width = quadrant_width
        height = quadrant_height
        
        return (left, top, width, height)

    def find_image(self, image_paths, confidence=0.8, retries=3, name="null"):
        """
        Attempt to locate any of the images on the screen with multiple retries.
        """
        for attempt in range(retries):
            for image_path in image_paths:
                try:
                    position = pyautogui.locateCenterOnScreen(image_path, confidence=confidence, region=self.region)
                    if position:
                        return position
                except pyautogui.ImageNotFoundException:
                    continue  # Continue with the next image in the list

            # Small delay between retries to avoid rapid repeated attempts
            time.sleep(0.1)
        
        print("Not found", name)
        return None

    def cast(self):
        cast_position = self.find_image(self.cast_images, confidence=self.cf_cast, name="cast")
        if cast_position is not None:
            pyautogui.moveTo(cast_position)
            pyautogui.click()
            print("Cast!")
            self.turn = 1

    def reel(self):
        reel_position = self.find_image(self.reel_images, confidence=self.cf_reel, name="reel")
        if reel_position is not None:
            pyautogui.moveTo(reel_position)
            pyautogui.click()
            print("Reel!")
            self.total_bait -= 1
            print("total_bait: ", self.total_bait)
            self.turn = 0

    def fishing(self):
        while self.total_bait > 0:
            if self.turn == 0:
                self.cast()
            elif self.turn == 1:
                self.reel()

if __name__ == "__main__":
    print("Start")
    
    fishing = Fishing(
        reel_images= ['images/reel-0.png','images/reel-1.png','images/reel-2.png','images/reel-3.png'],
        cast_images= ['images/cast-0.png','images/cast-1.png'],
        total_bait=100,
        monitor_index=1, # Always set index monitor to main display, e.g monitor 1 as a main display than set index 0
        cf_cast=0.8,
        cf_reel=0.95
    )
    fishing.fishing()
