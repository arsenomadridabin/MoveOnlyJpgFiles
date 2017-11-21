import os
import sys
import shutil



def move_jpgfile(dest_path,current_path):
	for file in os.listdir(current_path):
		file_abs_path=os.path.join(current_path,file)
		if os.path.isfile(file_abs_path):
			if os.path.splitext(file)[1].lower() in ('.jpg','.jpeg'):
				file_path=os.path.join(current_path,file)
				shutil.move(file_path,dest_path)
def get_child(current_path):
	child_directory=[]
	for directory in os.listdir(current_path):
		full_directory=os.path.join(current_path,directory)
		if os.path.isdir(full_directory):
			child_directory.append(full_directory)
	return child_directory		

destn_path=raw_input("enter destination path")
source_path=[raw_input("Input path of the source")]
queue = []
queue.extend(source_path)
while not len(queue)==0:
	current_path = queue[0]
	move_jpgfile(destn_path,current_path)
	queue.remove(queue[0])
	child=get_child(current_path)
	queue.extend(child)
	    
