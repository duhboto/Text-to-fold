## Program Name: Text to Fold

### Introduction
Text to Fold is a Python script and windows app that allows you to create multiple folders and subfolders based on the contents of a text file. The script can handle both line breaks and comma-separated values in the input file, and creates a main folder for each line or line item. Inside each main folder, three subfolders are created with specific names.

### Requirements
This program requires Python 3.x to run. There are no additional modules or packages required.

### How to Use
1. Save the script in a Python file with a .py extension.
2. Create a text in the inputtext.txt with the names of the folders you want to create. Each line or line item in the text file should contain the name(s) of the folder(s) you want to create, separated by commas. If you want to create multiple main folders, separate each line or line item with a line break. Here are some examples:

   ```
   Folder 1, Folder 2, Folder 3
   Folder 4
   Folder 5, Folder 6
   ```
   
   In this example, the script will create three main folders, "Folder 1", "Folder 2", and "Folder 3", with three subfolders inside each main folder. It will then create a new main folder called "Folder 4" with three subfolders inside it. Finally, it will create two more main folders called "Folder 5" and "Folder 6", each with three subfolders inside them.
   
3. Save the text file in the same directory as the Python file.
4. Open the command prompt or terminal, and navigate to the directory containing the Python file and the text file.
5. Run the script using the command `python <filename>.py`, replacing `<filename>` with the name of the Python file.
6. The script will create a new folder in the same directory as the Python file called "Generated Folders By CSV". This is where all the output folders will be saved.
7. The script will create a main folder for each line or line item in the text file, with three subfolders inside each main folder. The subfolders will be named based on the contents of the text file item and a specific suffix.
8. The script will also create a text file called "generatedCSV.txt" containing the names of the main folders.
9. After all the folders have been created, the script will prompt the user to create additional folders based on the same text file.
10. To create additional folders, type "y" when prompted and press Enter. The script will create new folders based on the same text file.
11. To stop creating new folders, type "n" when prompted and press Enter. The script will exit.

### Notes
- If the output folder already exists, the script will not overwrite it, and will instead use the existing folder.
- If a main folder already exists, the script will not overwrite it, and will instead skip to the next line or line item in the text file.
- If a subfolder already exists, the script will not overwrite it, and will instead skip to the next line or line item in the text file.
