#!/usr/bin/env python

import wx
import zwoasi

MenuItem_exit = 101
MenuItem_about = 100

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title, cam):
        wx.Frame.__init__(self, parent, ID, title,
                        wx.DefaultPosition, wx.Size(1000, 600),
                        wx.DEFAULT_FRAME_STYLE)# & ~ (wx.RESIZE_BORDER |
                       # wx.MAXIMIZE_BOX))

        self.Bind(wx.EVT_CLOSE, self.QuitGame)

        self.CreateStatusBar()
        self.SetStatusText("Active")
        self.Camera = cam

        self.Camera.set_control_value(zwoasi.ASI_BANDWIDTHOVERLOAD, self.Camera.get_controls()['BandWidth']['MinValue'])

# Set some sensible defaults. They will need adjusting depending upon
# the sensitivity, lens and lighting conditions used.
        self.Camera.disable_dark_subtract()
        self.Camera.set_image_type(zwoasi.ASI_IMG_RAW16)

        self.Camera.set_control_value(zwoasi.ASI_GAIN, 150)
        self.Camera.set_control_value(zwoasi.ASI_EXPOSURE, 80000)

        img = self.Camera.capture()

        from PIL import Image
        mode = None
        if len(img.shape) == 3:
            img = img[:, :, ::-1]  # Convert BGR to RGB
        #if whbi[3] == ASI_IMG_RAW16:
        mode = 'I;16'
        image = Image.fromarray(img, mode=mode)


        #print "Picture = %d:%d:%d"%(len(self.FirePic), len(self.FirePic[0]),len(self.FirePic[0][0]) )

        #self.FirePic = wx.Bitmap()
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
        libfile = "/home/hollande/src/external/zwo/lib/x64/libASICamera2.so"
        zwoasi.init(libfile)
        NumCameras = zwoasi.get_num_cameras()
        print "Found %d Cameras"%NumCameras

        Cameras = zwoasi.list_cameras()

        for i in range(NumCameras):
            print(' [%d]--> %s' % (i, Cameras[i]))



        self.Camera = zwoasi.Camera(0)
        self.CameraProperties = self.Camera.get_camera_property()
        self.CameraControls = self.Camera.get_controls()
#
#        for ctrl in self.CameraControls.keys():
#            print "%s" % ctrl
#            for  c2 in self.CameraControls[ctrl].keys():
#                print "    %s: %s" % (c2, repr(self.CameraControls[ctrl][c2]))

        frame = MainWindow(None, -1, "ZWOView", self.Camera)
        frame.Show(True)
        self.SetTopWindow(frame)
        return(True)

app = Zwo(0)
app.MainLoop()