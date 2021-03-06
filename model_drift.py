import wx
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

class MplCanvasFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self, parent, size=(600, 400),
                        title='Matplotlib Figure with Navigation Toolbar')
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        x = np.arange(0, 6, .01)
        y = np.sin(x**2)*np.exp(-x)
        self.axes.plot(x, y)
        self.canvas = FigureCanvas(self, -1, self.figure)
#        self.sizer = wx.BoxSizer(wx.VERTICAL)
#        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
#        self.toolbar = NavigationToolbar2Wx(self.canvas)
#        self.toolbar.Realize()
#        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
#        self.toolbar.Show()
#        self.SetSizer(self.sizer)
#        self.Fit()
#
#class MplApp(wx.App):
#    def OnInit(self):
#        frame = MplCanvasFrame(None)
#        self.SetTopWindow(frame)
#        frame.Show(True)
#        return True

#def load(event):
#    file = open(filename.GetValue())
#    contents.SetValue(file.read())
#    file.close()
#
#def save(event):
#    file = open(filename.GetValue(), 'w')
#    file.write(contents.GetValue())
#    file.close()

app = wx.App(redirect = False)
frame = MplCanvasFrame(None)
frame.Show()
app.MainLoop()
#mplapp = MplApp(False)
#frame = MplCanvasFrame(None)
#frame.show(True)
#mplapp.MainLoop()
#app = wx.App()
#win = wx.Frame(None, title="Simple Editor", size=(410, 335))
#
#bkg = wx.Panel(win)
#
#loadButton = wx.Button(bkg, label='Open')
#loadButton.Bind(wx.EVT_BUTTON, load)
#
#saveButton = wx.Button(bkg, label='Save')
#saveButton.Bind(wx.EVT_BUTTON, save)
#
#filename = wx.TextCtrl(bkg)
#contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
#
#hbox = wx.BoxSizer()
#hbox.Add(filename, proportion=1, flag=wx.EXPAND)
#hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
#hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
#
#vbox = wx.BoxSizer(wx.VERTICAL)
#vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
#vbox.Add(contents, proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
#
#bkg.SetSizer(vbox)
#win.Show()
#
#app.MainLoop()
