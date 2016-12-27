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

	def generate(self,plot_type,params):
		if not plot_type in self.plot_types.keys():
			return "alert('PLOT UNSUPPORTED');"

		return self.plot_types[plot_type]().make(params)


	def render(self,filepath,params={}):
		response = ""
		with open(filepath,'r') as file:
			for line in file:
				try:
					plot_type = re.search(r'{# (.*?) #}',line).groups()[0]
					js = self.generate(plot_type,params)
					response += re.sub(r'({#.*?#})',js,line)
				except AttributeError:			
					response += line

		return response





