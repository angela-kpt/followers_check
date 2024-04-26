import os, ig
from tkinter import filedialog
from tkinter import *

files = []
def import_file():
	file_path = filedialog.askopenfilenames(title="Select a file", filetypes=[("JSON files", "*.json")])
	
	if file_path:
		# Process the selected file (you can replace this with your own logic)
		print("Selected files:", file_path)
		for f in file_path:
			file_name = os.path.basename(f)
			files.append(file_name)
		print(files)
	
	unfollows = ig.check_followers(files)
	label_file_explorer.configure(text=f"Not following you back:\n",background="pink")
	for u in unfollows:
		unfollow_links.insert(END, u + '\n')

	unfollow_links.configure(state=DISABLED)
		

# Create the main Tkinter window
root = Tk()
root.title("Check Unfollowers")
root.geometry("500x500")

root.config(background = "pink")

label_file_explorer = Label(root, text = "Upload following.json and followers_1.json", width = 100, height = 4, fg = "black",background="pink",borderwidth=0, highlightthickness=0)

unfollow_links = Text(root, width = 50, height = 50, fg = "black",background="pink",borderwidth=1)

# Create an "Import File" button
import_button = Button(root, text="Import File", command=import_file,background="pink",borderwidth=0, highlightthickness=0)
import_button.grid(column = 1, row = 1)
label_file_explorer.grid(column = 1, row = 2)
unfollow_links.grid(column = 1, row = 3)

# Run the Tkinter event loop
root.mainloop()

