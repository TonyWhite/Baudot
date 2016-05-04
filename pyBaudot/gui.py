#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Roshan Mehta

import wx
import BaudotClass 

class guiBaudot(wx.Frame):
  
    def __init__(self, parent, title):
        super(guiBaudot, self).__init__(None, -1, title = title,
                 style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size =(430, 250))
      
        self.InitUI()
        self.Centre()
        self.Show() 
        self.bauObject = BaudotClass.baudotClass() 
           
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        elements = wx.FlexGridSizer(2, 2, 9, 2)
        
        decoded = wx.StaticText(panel, label="Decoded String")
        encoded = wx.StaticText(panel, label="Encoded String")
        


        self.tc1 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, -1))
        self.tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300, -1))
        elements.AddMany([(decoded), (self.tc1, 1, wx.EXPAND), (encoded), 
            (self.tc2, 1, wx.EXPAND) ])
        elements.AddGrowableRow(0, 1)
        elements.AddGrowableCol(0, 1)
        elements.AddGrowableRow(1, 1)
        elements.AddGrowableCol(1, 1)     
        btn1 = wx.Button(panel,1, label='Encode')
        elements.Add(btn1)
        self.Bind(wx.EVT_BUTTON, self.onEncode, id=1)
        btn2 = wx.Button(panel,2, label='Decode')
        elements.Add(btn2, flag=wx.ALIGN_RIGHT)
        self.Bind(wx.EVT_BUTTON, self.onDecode, id=2)

        btn3 = wx.Button(panel,3, label='Reset')

        btn4 = wx.Button(panel,4, label='Quit')
        elements.Add(btn3)
        self.Bind(wx.EVT_BUTTON, self.onReset, id=3)
        elements.Add(btn4, flag=wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM)
        self.Bind(wx.EVT_BUTTON, self.onQuit, id=4)
        hbox.Add(elements, flag=wx.ALL|wx.EXPAND, border=9)
        panel.SetSizer(hbox) 
        
    def onEncode(self,event):
        msg = self.tc1.GetValue() 
        self.tc2.Clear()
        self.tc2.SetValue(self.bauObject.baudotEncoder(msg).strip())
    def onReset(self,event):
        self.tc1.Clear()
        self.tc2.Clear()
    def onQuit(self,event):
        self.Close()
    def onDecode(self, event):
        msg = self.tc2.GetValue()
        if not msg:
            return
        self.tc1.Clear()
        decodeResult = self.bauObject.baudotDecoder(msg).strip()
        if decodeResult:
            self.tc1.SetValue(decodeResult)
        else:
            self.correctionHint()
            self.tc2.Clear()
        
        
    def correctionHint(self):
        wx.MessageBox('Invalid Decoded String', 'Info', 
            wx.OK | wx.ICON_INFORMATION)
        
        
        
    

if __name__ == '__main__':
  
    app = wx.App()
    guiBaudot(None, title='Baudot: Endoder/Decoder')
    app.MainLoop()
