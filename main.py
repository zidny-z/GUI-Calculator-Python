import wx
import kalkulator

class subKelas (kalkulator.frameUtama):
    def __init__(self,parent):
        kalkulator.frameUtama.__init__(self,parent)
        self.tempStrCalc= ""
        self.tempCalc = []
    
    def tampilin(self):
        #print(self.tempStrCalc)
        self.tempStrCalc = ''.join([str(elem) for elem in self.tempCalc])
        self.m_textTemp.SetValue(str(self.tempStrCalc))

    def Kuadrat( self, event ):
        self.tempCalc.append("**2")
        self.tampilin()

    def NolDua( self, event ):
        self.tempCalc.append("00")
        self.tampilin()

    def Clear( self, event ):
        self.tempCalc = []
        self.tampilin()

    def Hapus( self, event ):
        self.tempCalc.pop()
        self.tampilin()

    def Titik( self, event ):
        #print(self.tempCalc)
        self.tempCalc.append(".")
        self.tampilin()

    def Bagi( self, event ):
        #print(self.tempCalc)
        self.tempCalc.append("/")
        self.tampilin()

    def Kali( self, event ):
        #print(self.tempCalc)
        self.tempCalc.append("*")
        self.tampilin()

    def Minus( self, event ):
        #print(self.tempCalc)
        self.tempCalc.append("-")
        self.tampilin()

    def Plus( self, event ):
        #print(self.tempCalc)
        self.tempCalc.append("+")
        self.tampilin()

    #samadengan
    def Hasil( self, event ):
        try:
            self.tempStrCalc = eval(self.tempStrCalc)
            self.m_textTemp.SetValue(str(self.tempStrCalc))
            self.tempCalc =[]
            self.tempCalc.append(self.tempStrCalc)
        except:
            self.Clear(self)
            wx.MessageBox('Komputer tidak memahami perintah anda!', 'Warning',
                                     wx.OK |wx.ICON_WARNING)
            #print('error')

    #tombol angka 
    def Tujuh( self, event ):
        self.tempCalc.append("7")
        #print(self.tempCalc)
        self.tampilin()

    def Empat( self, event ):    
        self.tempCalc.append("4")
        #print(self.tempCalc)
        self.tampilin()

    def Satu( self, event ):
        self.tempCalc.append("1")
        #print(self.tempCalc)
        self.tampilin()

    def Delapan( self, event ):
        self.tempCalc.append("8")
        #print(self.tempCalc)
        self.tampilin()

    def Lima( self, event ):
        self.tempCalc.append("5")
        #print(self.tempCalc)
        self.tampilin()

    def Dua( self, event ):
        self.tempCalc.append("2")
        #print(self.tempCalc)
        self.tampilin()

    def Nol( self, event ):
        self.tempCalc.append("0")
        #print(self.tempCalc)
        self.tampilin()

    def Sembilan( self, event ):
        self.tempCalc.append("9")
        #print(self.tempCalc)
        self.tampilin()

    def Enam( self, event ):  
        self.tempCalc.append("6")
        #print(self.tempCalc)
        self.tampilin()

    def Tiga( self, event ):     
        self.tempCalc.append("3")
        #print(self.tempCalc)
        self.tampilin()



app = wx.App()
frame = subKelas(parent=None)
frame.Show()
app.MainLoop()