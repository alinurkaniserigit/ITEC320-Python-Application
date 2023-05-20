import tkinter as tk
from PIL import ImageTk, Image
import assistant

def start_assistant():
    assistant.handle_commands()

# Create the main window of the application
window = tk.Tk()
window.title("AI Assistant")
window.geometry("500x500")

# Create a frame for the GIF
gif_frame = tk.Frame(window, bg='white')
gif_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
gif_frame.pack_propagate(0) # Disable automatic resizing

# Load and display the GIF
gif_image = Image.open("C:\\Users\\ASUS\\Downloads\\py-pro\\Quinn The Assistan\\Assets\\zero.gif")
gif_photo = ImageTk.PhotoImage(gif_image)
gif_label = tk.Label(gif_frame, image=gif_photo)
gif_label.pack(padx=5, pady=5)

# Allow the GIF to resize dynamically
gif_frame.columnconfigure(0, weight=1)
gif_frame.rowconfigure(0, weight=1)
gif_label.bind("<Configure>", lambda e: gif_label.config(width=e.width, height=e.height))

# Create a button to start the assistant
button = tk.Button(window, text="Start Assistant", command=start_assistant)
button.pack(pady=10)

# Start the main event loop
window.mainloop()
