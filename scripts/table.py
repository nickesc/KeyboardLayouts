import os

def list_files_by_folder(base_directory):
    folder_dict = {}

    for root, _, files in os.walk(base_directory):
        relative_path = os.path.relpath(root, base_directory)
        if relative_path == ".":
            continue  # Skip the base directory itself
        folder_dict[relative_path] = files

    return folder_dict

# Example usage
import os

def list_files_by_folder(base_directory):
    folder_dict = {}

    for root, _, files in os.walk(base_directory):
        relative_path = os.path.relpath(root, base_directory)
        if relative_path == ".":
            continue  # Skip the base directory itself
        folder_dict[relative_path] = files

    return folder_dict

# Example usage
directory_path = "out/SVG"  # Change this to your target directory
files_by_folder = list_files_by_folder(directory_path)

cats = {"40%-50%":"40%-50%","60%-75%":"60%-75%","1800 & 96%":"1800 & 96%","TKL-110%":"TKL-110%","Southpaw":"Southpaw","Regional":"Regional","Ergo":"Ergo", "Ortho":"Ortho", "Big Boards":"Big Boards","Macropads":"Macropads"}

for folder in files_by_folder.keys():
    folderStr=""

    for file in files_by_folder[folder]:
        if file!=".DS_Store":
            folderStr=folderStr + "<a href='" + directory_path + "/" + folder.replace("%", "%25") + "/" + file.replace("%", "%25") +"'><img src='" + directory_path + "/" + folder.replace("%", "%25") + "/" + file.replace("%", "%25") +"' alt='"+ file+"'><br>"+ file.replace("-","/").replace(".svg","") +"</a> | "

    cats[folder] = folderStr

for cat in cats:
    print("**" + cat + "** | " + cats[cat])
