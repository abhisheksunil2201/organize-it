# Organize It

The Python script that'll help you declutter and tidy up your downloads folder. You can neatly organize them into categories based on file types.

## Getting Started

### Prerequisites

Before you start, make sure you have the following:

- Python installed on your system.
- A downloads folder with files that need organizing.

### Installation

1. Clone this repository or download the ZIP file.


Configuration
You can customize the script to suit your needs. The default configuration already covers most common file types, but you can easily add or remove categories by editing the config.json file.

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
