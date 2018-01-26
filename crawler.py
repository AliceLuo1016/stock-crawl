import os
import json
from pprint import pprint
import wx
import os
import csv

class Mywin(wx.Frame): 
   	def __init__(self, parent, title): 
		super(Mywin, self).__init__(parent, title = title,size = (400,250))

		panel = wx.Panel(self) 
		vbox = wx.BoxSizer(wx.VERTICAL) 
		label = wx.StaticText(panel, label = "Add a New Stock To Track")
		vbox.Add(label,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,10)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL) 

		l1 = wx.StaticText(panel, -1, "Add Stock Url  ") 
		hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,3) 
		self.t1 = wx.TextCtrl(panel) 
		hbox1.Add(self.t1,2,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,3) 
		self.t1.Bind(wx.EVT_TEXT,self.OnUrlTyped)

		vbox.Add(hbox1)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL) 

		l2 = wx.StaticText(panel, -1, "Set Stock Limit") 
		hbox2.Add(l2, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,3) 
		self.t2 = wx.TextCtrl(panel) 
		hbox2.Add(self.t2,0,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,3) 
		self.t2.Bind(wx.EVT_TEXT,self.OnLimitTyped)

		vbox.Add(hbox2)

		self.btn = wx.Button(panel,-1,"Add") 
		vbox.Add(self.btn,0,wx.ALIGN_CENTER|wx.ALL, 10) 
		self.btn.Bind(wx.EVT_BUTTON,self.OnClicked)

		label2 = wx.StaticText(panel, label = "Run Daily Stock Limits Check")
		vbox.Add(label2,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,10)

		self.btn = wx.Button(panel,-1,"Run") 
		vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
		self.btn.Bind(wx.EVT_BUTTON,self.OnClickedRun) 

		panel.SetSizer(vbox) 

		self.Centre() 
		self.Show() 
		self.Fit()

	def OnUrlTyped(self, event):
		global url 
		url = event.GetString()
			
	def OnLimitTyped(self, event): 
	    global limit
	    limit = event.GetString()

	def OnClicked(self, event): 
		# save the url and limit combination in a csv
		print url + limit

		with open('stocks.csv', 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([url, limit, '\n'])

	def OnClickedRun(self, event): 
		os.system("scrapy runspider stock.py -o stock.json")
		data = json.load(open('./stock.json'))
		pprint(data)
		for item in data:
			company = item.get("company")
			cur_price = item.get("current price")
			
		os.system('rm stock.json')
		print "Run Button pressed."

app = wx.App(False)
Mywin(None, "Stock Crawler")
app.MainLoop()
