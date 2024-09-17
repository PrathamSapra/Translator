#pip install googletrans
#pip install textblob
#pip install pillow
#pip install textblob
#pip install googletrans==4.0.0-rc1

# Importing necessary libraries

from tkinter import *  # Tkinter is used for creating the GUI (Graphical User Interface)
from tkinter import ttk, messagebox  # ttk for modern widgets, messagebox for showing error messages
from PIL import Image, ImageTk  # PIL (Pillow) for handling images
import googletrans  # googletrans for language translation capabilities

# Setting up the main application window
root = Tk()  # This initializes the Tkinter window
root.title("Google Translator")  # Set the title of the window
root.geometry("1080x400")  # Set the dimensions of the window (width x height)

# Function to update language labels automatically
def label_change():
    c = combo1.get()  # Get the selected value from the first language dropdown
    c1 = combo2.get()  # Get the selected value from the second language dropdown
    label1.configure(text=c)  # Update label1 to show the language selected in combo1
    label2.configure(text=c1)  # Update label2 to show the language selected in combo2
    root.after(1000, label_change)  # This function keeps running every 1 second to update the labels

# Function to perform translation
def translate_now():
    global language  # Refers to the global 'language' dictionary defined later in the code
    try:
        # Fetch the text inputted in the first text box
        text_ = text1.get(1.0, END).strip()  # Get text from line 1, character 0 to the end. Use .strip() to remove extra spaces.
        c2 = combo1.get()  # Get the source language from combo1
        c3 = combo2.get()  # Get the target language from combo2

        # Check if the user has entered text to translate
        if not text_:
            messagebox.showerror("Input Error", "Please enter text to translate.")  # Show error if no text is entered
            return  # Exit the function early if there's an error

        # Check if the user has selected a target language
        if c3 == "SELECT LANGUAGE":
            messagebox.showerror("Selection Error", "Please select a target language.")  # Show error if no language selected
            return  # Exit the function early if there's an error

        # Initialize the translator
        translator = googletrans.Translator()

        # Detect the language of the input text
        detected_language = translator.detect(text_).lang  # This automatically detects the language of the input text

        # Find the language code for the target language (from combo2)
        target_language_code = [key for key, value in language.items() if value == c3]  # Find the code of the selected target language

        # If the target language is not found in the 'language' dictionary, show an error
        if not target_language_code:
            messagebox.showerror("Language Error", "Target language not found.")
            return  # Exit the function early if there's an error

        # We only take the first matching language code (because combo2 might return a list)
        target_language_code = target_language_code[0]

        # Perform the translation
        translated_text = translator.translate(text_, src=detected_language, dest=target_language_code).text  # Translate the text from source to target language
        text2.delete(1.0, END)  # Clear the second text box where the translation will appear
        text2.insert(END, translated_text)  # Insert the translated text in the second text box

    except Exception as e:
        # If an error occurs during translation, show an error message and print the error in the console
        messagebox.showerror("Translation Error", f"Translation failed. Please try again.\nError: {e}")
        print(f"Translation Error: {e}")

# Load and resize images using Pillow
try:
    image_icon = ImageTk.PhotoImage(Image.open("google.png"))  # Load the window icon image (google.png)
    root.iconphoto(False, image_icon)  # Set the icon for the window

    # Load the arrow image and resize it
    arrow_image = Image.open("arrow2.jpg")  # Open the arrow image file
    arrow_image = arrow_image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image to 200x200 pixels for a better fit
    arrow_image = ImageTk.PhotoImage(arrow_image)  # Convert it into a format suitable for Tkinter

    # Create a label to display the arrow image between the text boxes
    image_label = Label(root, image=arrow_image)
    image_label.image = arrow_image  # Keep a reference to the image to prevent garbage collection
    image_label.place(x=420, y=130)  # Position the image at coordinates (420, 130) in the window
except Exception as e:
    # If there's an error loading images, print the error
    print(f"Error loading images: {e}")

# Create the dictionary for supported languages
language = googletrans.LANGUAGES  # This is a dictionary with language codes and names from googletrans
languageV = list(language.values())  # List of all language names
lang1 = list(language.keys())  # List of all language codes

# Create the dropdown menus (combobox) for language selection
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")  # Dropdown for selecting the source language
combo1.place(x=110, y=20)  # Position the dropdown at (110, 20)
combo1.set("ENGLISH")  # Default language for combo1 is set to "ENGLISH"

# Create the label to display the selected source language
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)  # Position label1 at (10, 50)

# Create a frame to hold the first text box
f = Frame(root, bg="Black", bd=5)  # Frame with black background and border of 5 pixels
f.place(x=10, y=118, width=440, height=210)  # Position the frame

# Create the first text box (for input)
text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)  # Text box with word wrap
text1.place(x=0, y=0, width=430, height=200)  # Position the text box inside the frame

# Create a scrollbar for the first text box
scrollbar1 = Scrollbar(f)  # Scrollbar to navigate large text
scrollbar1.pack(side="right", fill="y")  # Attach it to the right side of the frame

scrollbar1.configure(command=text1.yview)  # Link the scrollbar to the first text box
text1.configure(yscrollcommand=scrollbar1.set)  # Ensure that scrolling moves the text

# Same setup for the second dropdown, label, frame, text box, and scrollbar (for output)
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")  # Default option for combo2

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Create the "Translate" button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2", bd=5,
                   bg='red', fg="white", command=translate_now)  # The button calls the translate_now function when clicked
translate.place(x=480, y=330)  # Position the button below the arrow image

# Call the label_change function to start updating language labels
label_change()

# Configure the window background to white
root.configure(bg="white")

# Start the Tkinter event loop (this keeps the window open and responsive)
root.mainloop()
