# coding: utf-8
import wx

class myFrame(wx.Frame):

    def __init__(self, parent, title):
        super(myFrame, self).__init__(parent, title=title, size=(800, 600))
        
        self.Center()
        
        self.panel = wx.Panel(self)
        
        self.panel.SetBackgroundColour("gray")
       
        self.img1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/1.jpg", wx.BITMAP_TYPE_ANY))
        self.img2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/2.jpg", wx.BITMAP_TYPE_ANY))
        self.img3 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/3.jpg", wx.BITMAP_TYPE_ANY))
        
        self.img1.SetPosition((20, 20))
        self.img2.SetPosition((20, 300))
        self.img3.SetPosition((400, 30))

def main():
    
    app = wx.App()
    frame = myFrame(None, title='Absolute positioning')
    frame.Show()
    app.MainLoop()
    
    
if __name__ == '__main__':
    main()
    
