import re
from jsgenerator import *

class Engine(object):
	"""docstring for Engine"""
	def __init__(self):
		super(Engine, self).__init__()
		self.plot_types = {
			'bar':BarChartJSGenerator,
			'line':LineChartJSGenerator,
			'pie':PieChartJSGenerator,
			'histogram':HistogramJSGenerator,
			'bubble':BubbleChartJSGenerator,
			'gantt':GanttChartJSGenerator
		}	

	def generate(self,arg):
		plot_type = arg.split()[0]
		params = arg.split()[1]

		if not plot_type in self.plot_types.keys():
			return "alert('PLOT UNSUPPORTED');"

		return self.plot_types[plot_type]().make(params)


	def render(self,filepath):
		response = ""
		with open(filepath,'r') as file:
			for line in file:
				try:
					cmd = re.search(r'{# (.*?) #}',line).groups()[0]
					js = self.generate(cmd)
					response += re.sub(r'({#.*?#})',js,line)
				except AttributeError:			
					response += line

		return response





