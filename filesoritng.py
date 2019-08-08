import os
import shutil

def sorting(i_FolderPath):
	files = []
	files_folders = (os.listdir(os.path.join(i_FolderPath))) 
	for i in files_folders:
		if '.' in i:
			files.append(i)

	# print(files) #list of all the types of files

	formats  = {}
	for i in files:
		dot_index = i.index(".")
		format_type = i[dot_index+1:]
		if format_type not in formats:
			formats[format_type]  = []
			formats[format_type].append(i)
		else:
			formats[format_type].append(i)


	for key,val in formats.items():
		if not(os.path.exists(os.path.join(i_FolderPath, key))):
			os.makedirs((os.path.join(i_FolderPath, key))) 

		for i in val:
			# print(i)
			shutil.move(os.path.join(i_FolderPath,i), os.path.join(i_FolderPath,key))


sorting("WORK/2")