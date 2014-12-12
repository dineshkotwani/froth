import os.path

class Loader(object):
	"""docstring for Loader"""
	def __init__(self,template_directories):
		super(Loader, self).__init__()
		self.template_directories = template_directories

	def get_file_path(self,name):
		file_path_list = []
		for directory in self.template_directories:
			for root,subdirs,files in os.walk(directory):
				file_path_list.append(os.path.join(root,name))

		if len(file_path_list):
			return file_path_list[0]
		else:
			return None






		