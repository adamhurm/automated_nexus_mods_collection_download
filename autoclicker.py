import pyautogui, pynput, sys, time

running = True

def on_release(key):
    global running
    # Check if the released key is the Escape key
    if key == pynput.keyboard.Key.esc:
        print("Escape key pressed. Stopping listener and exiting program.")
        running = False
        # Stop the listener
        return False

# Collect events until released in a non-blocking manner
listener = pynput.keyboard.Listener(on_release=on_release)
listener.start()

print("Autoclicker started. To stop, either:")
print("- press the 'Esc' key (can be used globally)\n- select this terminal and press Ctrl+C")

# Main program loop (replace with your terminal program's logic)
try:
    while running:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Check for manual download button in Vortex
        try:
            pos = pyautogui.locateCenterOnScreen("download_manually.png")
        except:
            pos = None
        
        # Check for "continue to external site button"
        try:
            pos2 = pyautogui.locateCenterOnScreen("continue.png")
        except:
            pos2 = None
        
        # Click one of the buttons if found
        if pos or pos2:
            click_pos = pos if pos else pos2
            pyautogui.click(click_pos)
            pyautogui.moveTo(100, 100) # Reset mouse to top-left corner
        time.sleep(3)

except KeyboardInterrupt:
    # Handle manual Ctrl+C if needed, though Esc should work globally
    pass
finally:
    # Ensure the listener is stopped when the main loop finishes
    if listener.is_alive():
        listener.stop()
    print("Program terminated.")
    sys.exit(0)