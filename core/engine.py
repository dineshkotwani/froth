import re

class Engine(object):
	"""docstring for Engine"""
	def __init__(self):
		super(Engine, self).__init__()
		self.plot_types = ['bar','line','pie','histogram','bubble','gantt']

	def replace(self,arg):
		plot_type = arg.split()[0]
		params = arg.split()[1]

		if not plot_type in self.plot_types:
			return arg
		
		return params

	def parse(self,arg):
		try:
			split_lines = re.search(r'(\D+){#(\D+)#}(\D+)',arg).groups()
			split_lines[2] = self.replace(split_lines[2])
			return ''.join(split_lines)
		except AttributeError:
			return arg

	def render_plot(self,filepath):
		response = ""
		with open(filepath,'r') as file:
			for line in file:
				try:
					re.search(r'(\s+)(\D+){#(\D+)#}(\D+)(\s+)',line).groups()
				except AttributeError:
					print line
				response += (self.parse(line))

		return response

filepath = '../examples/test.html'
x = Engine()
x.render_plot(filepath)





