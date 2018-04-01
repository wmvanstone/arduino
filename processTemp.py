#!/usr/bin/env python3
# import libraries
import datetime
import plotly
from plotly.graph_objs import *
import sys
plotly.tools.set_credentials_file(username="wmvanstone", api_key="uVM2WEVcdEZQKKreHnEQ")

# global variables

# functions
# Function to split a string into fields and return a list of the data
def stringsplit(instring, separator):
	fields=[""]
	f = 0
	for s in instring:
		if s != separator:
			fields[f]+=s
		else:
			fields.append("")
			f+=1
	return fields

# Read a file
def readfile(infile, frequency):
	myx=[]
	myx1=[]
	my0=[]
	my1=[]
	file=open(infile, "r")
	lcounter=0
	temptot0=0
	tempcount0=0
	temptot1=0
	tempcount1=0
	for line in file:
		words=line.split()
		dfields=stringsplit(words[0], "-")
		d=datetime.date(int(dfields[0]), int(dfields[1]), int(dfields[2]))
		tfields=stringsplit(words[1], ":")
		t=datetime.time(int(tfields[0]), int(tfields[1]), int(tfields[2]))
		dt=datetime.datetime.combine(d,t)
		temptot0+=float(words[2])
		tempcount0+=1
		if len(words) > 3:
			temptot1+=float(words[3])
			tempcount1+=1
		if lcounter%frequency == 0:
#			print(dt, dt.timestamp(), words[2])
			myx.append(dt)
			my0.append(round(temptot0/tempcount0, 2))
			temptot0=0
			tempcount0=0
			if len(words) > 3:
				myx1.append(dt)
				my1.append(round(temptot1/tempcount1, 2))
				temptot1=0
				tempcount1=0
		lcounter+=1
	file.close()
	return myx, my0, myx1, my1
# plotgraph
def plotgraph(decimation):
	myx, my0, myx1, my1 = readfile("temperaturelog.txt",decimation)
	trace0 = Scatter(x=myx, y=my0)
	trace1 = Scatter(x=myx1, y=my1)
	layout = Layout(dict(title="Temperature from Arduino", xaxis=dict(title="Date"), yaxis=dict(title="Temperature (C)")))
	data=Data([trace0, trace1])
#	plotly.offline.plot({
	plotly.plotly.plot({
		"data": [trace0, trace1],
		"layout": layout
	},
		filename="temperaturexy.html"
	)
# Main program
# plot graph with decimation frequency from command line
if len(sys.argv)>1:
	plotgraph(int(sys.argv[1]))
else:
	plotgraph(60)
