import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math

def make_plot(data , title):
	
	#determine data range		
	r = [0 , 1]
	if len(data) > 0:
		r = range=[float(min(data)),float(max(data))]

	# fixed width of bin
	bin_width = 0.2

	# determine number of bins
	num_bins = int(math.ceil((r[1] - r[0])/bin_width))

	plt.hist(data , range=r, bins=num_bins,facecolor='green', alpha=0.75)
	plt.title(title)
	plt.ylabel('count')
	plt.xlabel('diameter (microns)')
	plt.grid(True,color='r', linestyle=':', linewidth=0.5)
	try:
		# create a png file
		figfile = BytesIO()
		plt.savefig(figfile, format='png')
		figfile.seek(0)
		# clear the figure
		plt.clf()
		# return a base 64 encoded image data
		return base64.b64encode(figfile.getvalue()).decode('utf8')
	except:
		raise

def get_data():
	return [0.1,0.2,0.3,0.14,0.4]

if __name__ == '__main__':
	make_plot(get_data() , 'fancy title')
