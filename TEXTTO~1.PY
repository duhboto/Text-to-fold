import os

input_filename = 'inputtext.txt'  # Input file name
output_filename = 'generatedCSV.txt'  # Output file name
output_folder = 'Generated Folders By CSV'  # Main output folder name

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Open the input and output files
with open(input_filename, 'r') as input_file, open(output_filename, 'a') as output_file:
    input_text = input_file.read()  # Read in the entire input file
    lines = input_text.splitlines() if '\n' in input_text else input_text.split(',')  # Split the input text into lines or items based on line breaks or commas
    for line in lines:
        line_items = line.split(',')  # Split each line into items based on commas
        for item in line_items:
            item = item.strip()  # Remove any leading or trailing white space
            if item:  # Check if the item is blank
                folder_name = os.path.join(output_folder, item)  # Create the main folder name based on the item
                hires_folder = os.path.join(folder_name, item+'_hires')  # Create the hires subfolder name
                org_folder = os.path.join(folder_name, item+'_org')  # Create the org subfolder name
                vr_folder = os.path.join(folder_name, item+'_vr')  # Create the vr subfolder name

                # Create the folder for the item if it doesn't already exist
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)

                # Create the subfolders for hires, org, and vr if they don't already exist
                if not os.path.exists(hires_folder):
                    os.mkdir(hires_folder)
                if not os.path.exists(org_folder):
                    os.mkdir(org_folder)
                if not os.path.exists(vr_folder):
                    os.mkdir(vr_folder)

                print(f'Created folder for "{item}"')

                # Write the item to the output file
                output_file.write(item + '\n')

# Ask the user if they want to create more folders
while True:
    response = input('Do you want to create more folders from the text file? (y/n): ')
    if response.lower() == 'y':
        with open(input_filename, 'r') as input_file, open(output_filename, 'a') as output_file:
            input_text = input_file.read()  # Read in the entire input file
            lines = input_text.splitlines() if '\n' in input_text else input_text.split(',')  # Split the input text into lines or items based on line breaks or commas
            for line in lines:
                line_items = line.split(',')  # Split each line into items based on commas
                for item in line_items:
                    item = item.strip()  # Remove any leading or trailing white space
                    if item:  # Check if the item is blank
                        folder_name = os.path.join(output_folder, item)  # Create the main folder name based on the item
                        hires_folder = os.path.join(folder_name, item+'_hires')  # Create the hires subfolder name
                        org_folder = os.path.join(folder_name, item+'_org')  # Create the org subfolder name
                        vr_folder = os.path.join(folder_name, item+'_vr')  # Create the vr subfolder name

                        # Create the subfolders for hires, org, and vr if they don't already exist
                        if not os.path.exists(hires_folder):
                            os.mkdir(hires_folder)
                        if not os.path.exists(org_folder):
                            os.mkdir(org_folder)
                        if not os.path.exists(vr_folder):
                            os.mkdir(vr_folder)

                        print(f'Created folder for "{item}"')

                        # Write the item to the output file
                        output_file.write(item + '\n')
    elif response.lower() == 'n':
        break
    else:
        print('Invalid response. Please enter "y" or "n".')
        print('Done!') # Output completion message
