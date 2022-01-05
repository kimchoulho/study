
import wx

class myFrame(wx.Frame):
    
    def __init__(self, parent, title):
        super(myFrame, self).__init__(parent, title=title, size=(350, 300))
        
        self.InitUI()
        self.Center()
    
    def InitUI(self):
        
        self.panel = wx.Panel(self)
        
        self.panel.SetBackgroundColour("gray")
        
        self.img1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/1.jpg", wx.BITMAP_TYPE_ANY))
        
        self.img2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/2.jpg", wx.BITMAP_TYPE_ANY))
        
        self.img3 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("./img/3.jpg", wx.BITMAP_TYPE_ANY))
        
        self.img1.SetPosition((20, 20))
        self.img2.SetPosition((40, 160))
        self.img3.SetPosition((170, 50))
           
def main():
    
    app = wx.App()
    ex = myFrame(None, title='Absolute positioning')
    ex.Show()
    app.MainLoop()
    
    
if __name__ == '__main__':
    main()
    
    
        