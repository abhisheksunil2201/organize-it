# Organize It

The Python script that'll help you declutter and tidy up your downloads folder. You can neatly organize them into categories based on file types.

## Getting Started

### Prerequisites

Before you start, make sure you have the following:

- Python installed on your system.
- A downloads folder with files that need organizing.

### Installation

Getting Organize It up and running is a breeze. Just follow these simple steps:

1. Clone the Repository or Download the ZIP File:
   
   First, either clone this repository using Git or download the ZIP file from the GitHub page.
   
2. Customize the organize.vbs Script:
   
   Open the organize.vbs script in a text editor.
   
   Locate the [PATH TO organize.bat] placeholder and replace it with the actual path to your organize.bat file.
   
   Customize the organize.bat Script:

3. Open the organize.bat script in a text editor.
   
   You'll need to make two adjustments:

   Replace the first path with the path to your python.exe installation on your device.
   
   Replace the second path with the path to organize.py on your device.
   
4. Set Up Auto-Startup (Windows):

   Open the "Run" dialog in Windows by pressing Win + R.
   
   Type shell:startup and hit Enter. This will open a folder where startup items are stored.
   
   Copy your customized organize.vbs script and paste it into this folder.

That's it! You're all set. The Organizer will automatically run on startup, ensuring your downloads folder stays organized effortlessly. 🚀✨

### Configuration:

You can customize the script to suit your needs. The default configuration already covers most common file types, but you can easily add or remove categories by editing the `organize.py` file.

```
extensions = {
        "mp3": "Audios",
        "mp4": "Videos",
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "gif": "Images",
        "docx": "Documents",
        "doc": "Documents",
        "txt": "Documents",
        "pdf": "Documents",
        "exe": "Programs",
        "msi": "Programs",
        "zip": "Compressed",
        "rar": "Compressed",
        "": "Other"
        // Add or modify categories as you like
}
```
