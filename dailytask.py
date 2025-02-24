import os
import shutil

# Define the file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".sh", ".bat", ".py"],
    "Others": []  # Files with unknown extensions go here
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Error: The specified directory does not exist!")
        return
    
    # Iterate through all files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(file)

        # Find the appropriate category for the file
        destination_folder = "Others"  # Default category
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                destination_folder = category
                break

        # Create destination folder if it doesn't exist
        destination_path = os.path.join(directory, destination_folder)
        os.makedirs(destination_path, exist_ok=True)

        # Move file to the appropriate folder
        shutil.move(file_path, os.path.join(destination_path, file))
        print(f"Moved: {file} → {destination_folder}/")

    print("\n✅ File organization completed!")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
