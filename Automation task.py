import os
import shutil

# Define file type categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
    "Others": []  # To handle unknown file types
}

# Function to organize files
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Find the category
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                category_folder = os.path.join(directory, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                moved = True
                break

        # Handle unknown file types
        if not moved:
            others_folder = os.path.join(directory, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

    print(f"Files in '{directory}' have been organized successfully!")

# Main function
if __name__ == "_main_":
    target_directory = input("Enter the directory to organize: ").strip()
    if os.path.exists(target_directory):
        organize_files(target_directory)
    else:
        print("Error: The directory does not exist!")