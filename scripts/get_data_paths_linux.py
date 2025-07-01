# Forest Ray
# July 1, 2025


def get_subfolders(main_folder):
	"""
	Gets a list of subfolders stored within a specified folder
	
	Arguments:
	- main_folder (string): this is the path to the main folder that contains the subfolders
	you want to get the paths of

	Returns:
	- folder_paths (list of strings): this is a list containing the full path to each subfolder 
	"""
	import os 

	objects_in_folder = os.listdir(main_folder) # Get a list of everything stored in the folder
	
	# this list comprehension looks at the name of every object in the folder and stores it as a folder if it is something
	# other than a file (ie: a folder)
	folder_names = [folder for folder in objects_in_folder if not os.path.isfile(main_folder + '/' + folder)]
	

	# this list comprehesion combines the main folder directory with the names of the subfolders
	# so that the full path to each subfolder is returned 
	folder_paths = [(main_folder + '/' + folder) for folder in folder_names]
	return folder_paths

	""" 
	example usage
	folders = get_data_paths.get_subfolders(path to main folder)
	"""

def get_subfolder_data_paths(subfolder, file_type='none'):
	"""
	Gets a list of paths to each set of data in a subfolder

	Arguments:
	- subfolder (string): path to the subfolder with the data you want the paths of
	- file_type (string): specifies a file type
		- by default, this value is none and all files will be returned regardless of type 
		- example args: '.csv', '.mp4', '.h5'

	Returns:
	- data_paths (list of strings): a list containing the full paths to each data file 

	"""
	import os

	objects_in_folder = os.listdir(subfolder) # Get a list of everything stored in the folder

	# look at each object in the folder, and if it is a file, store it in the files_in_folder list
	files_in_folder = [file for file in objects_in_folder if os.path.isfile(subfolder + '/' + file)]

	# if no file type was specified, all file paths will be returned
	if (file_type == 'none'):
		data_paths = [(subfolder + '/' + file) for file in files_in_folder]
	else: # if a file type was specified, only return paths to files of that type 
		data_paths = [(subfolder + '/' + file) for file in files_in_folder if file.endswith(file_type)]

	return data_paths


def get_data_from_main(main_folder, file_type='none'):
	""" 
	Sorts the data stored in the main folder into a dictionary where the keys are the subfolder paths
	and the values are the data file paths

	Arguments:
	- main_folder (string): path to main folder (data directory)
	- file_type   (string): specifies the file type
		- default value is none, and all file types will be returned 

	Returns:
	- grouped_data (dictionary): a dictionary where the keys are the subfolder paths and the values are lists of data paths 
	"""
	subfolders = get_subfolders(main_folder) # gets the paths to all subfolders in the main folder
		
	# get all of the file paths from each subfolder 
	data_lists = []
	for subfolder in subfolders:
		data_paths = get_subfolder_data_paths(subfolder, file_type)
		data_lists.append(data_paths)

	# create and return a dictionary where the keys are the subfolder paths and the values are lists of data paths
	grouped_data = dict(zip(subfolders, data_lists)) 
	return grouped_data

