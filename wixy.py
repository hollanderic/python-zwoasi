#!/usr/bin/env python

import wx

MenuItem_exit = 101
MenuItem_about = 100

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title,
                        wx.DefaultPosition, wx.Size(1000, 600),
                        wx.DEFAULT_FRAME_STYLE)# & ~ (wx.RESIZE_BORDER |
                       # wx.MAXIMIZE_BOX))

        self.Bind(wx.EVT_CLOSE, self.QuitGame)

        self.CreateStatusBar()
        self.SetStatusText("Active")

        self.FirePic = wx.Bitmap()
        #wx.EVT_PAINT(self, self.ShowBack)


        white = wx.Colour(255, 255, 255)
        black = wx.Colour(0, 0, 0)
        red = wx.Colour(255, 0, 0)
        green = wx.Colour(0, 255, 0)
        blue = wx.Colour(0, 0, 255)
        yellow = wx.Colour(255, 255, 0)
        dblue = wx.Colour(0,0,162)
        mygreen = wx.Colour(10,133,2)

        file = wx.Menu()
        help = wx.Menu()

        screen = wx.Window(self, -1, (0, 0), (790, 349))#, style=wx.BORDER_SUNKEN)
        screen.SetBackgroundColour(mygreen)
        #wx.EVT_PAINT(screen, self.ShowBack)

        controls = wx.Panel(self, -1, (0, 350), (800, 250))
        north = wx.Button(controls, -1, "North", (365,5))
        south = wx.Button(controls, -1, "South", (365,55))
        east = wx.Button(controls, -1, "East", (450,30))
        west = wx.Button(controls, -1, "West", (280,30))
        search1 = wx.Button(controls, -1, "Search", (365, 30))


        menu_exit = file.Append(wx.ID_ANY, "E&xit", "Quit the game?")
        menu_about = help.Append(wx.ID_ANY, "&About", "Whatevs")

        MenuBar = wx.MenuBar()
        MenuBar.Append(file, "&File")
        MenuBar.Append(help, "&Help")

        self.SetMenuBar(MenuBar)
        self.Bind(wx.EVT_SIZE, self.onSize)

        self.Bind(wx.EVT_MENU, self.QuitGame, menu_exit)
        self.Centre()

    def onSize(self, event):
        print "size event" + str(self.Size)

    def QuitGame(self, event):
        '''
        dlg = wx.MessageDialog(self, 
            "Do you really want to quit? All information will be lost.",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:'''
        self.Destroy()

class Zwo(wx.App):
    def OnInit(self):
        frame = MainWindow(None, -1, "ZWOView")
        frame.Show(True)
        self.SetTopWindow(frame)
        return(True)

app = Zwo(0)
app.MainLoop()