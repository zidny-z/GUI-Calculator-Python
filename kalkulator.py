# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frameUtama
###########################################################################

class frameUtama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"kalkulator", pos = wx.DefaultPosition, size = wx.Size( 498,324 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		bSizer57.SetMinSize( wx.Size( 500,-1 ) )
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Perhitungan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer57.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textTemp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_READONLY )
		self.m_textTemp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_textTemp.SetMinSize( wx.Size( 500,50 ) )
		self.m_textTemp.SetMaxSize( wx.Size( 500,-1 ) )

		bSizer57.Add( self.m_textTemp, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer56.Add( bSizer57, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonPangkat = wx.Button( self, wx.ID_ANY, u"a^2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPangkat.SetMinSize( wx.Size( 30,30 ) )

		bSizer60.Add( self.m_buttonPangkat, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonTujuh = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTujuh.SetMinSize( wx.Size( 30,30 ) )

		bSizer60.Add( self.m_buttonTujuh, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonEmpat = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonEmpat.SetMinSize( wx.Size( 30,30 ) )

		bSizer60.Add( self.m_buttonEmpat, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonSatu = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSatu.SetMinSize( wx.Size( 30,30 ) )

		bSizer60.Add( self.m_buttonSatu, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonNolDua = wx.Button( self, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonNolDua.SetMinSize( wx.Size( 30,30 ) )

		bSizer60.Add( self.m_buttonNolDua, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer59.Add( bSizer60, 1, wx.EXPAND, 5 )

		bSizer601 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonClear = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonClear.SetMinSize( wx.Size( 30,30 ) )

		bSizer601.Add( self.m_buttonClear, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonDepalan = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDepalan.SetMinSize( wx.Size( 30,30 ) )

		bSizer601.Add( self.m_buttonDepalan, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonLima = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLima.SetMinSize( wx.Size( 30,30 ) )

		bSizer601.Add( self.m_buttonLima, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonDua = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDua.SetMinSize( wx.Size( 30,30 ) )

		bSizer601.Add( self.m_buttonDua, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonNol = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonNol.SetMinSize( wx.Size( 30,30 ) )

		bSizer601.Add( self.m_buttonNol, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer59.Add( bSizer601, 1, wx.EXPAND, 5 )

		bSizer602 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonHapus = wx.Button( self, wx.ID_ANY, u"<=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonHapus.SetMinSize( wx.Size( 30,30 ) )

		bSizer602.Add( self.m_buttonHapus, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonSembilan = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSembilan.SetMinSize( wx.Size( 30,30 ) )

		bSizer602.Add( self.m_buttonSembilan, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonEnam = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonEnam.SetMinSize( wx.Size( 30,30 ) )

		bSizer602.Add( self.m_buttonEnam, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonTiga = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTiga.SetMinSize( wx.Size( 30,30 ) )

		bSizer602.Add( self.m_buttonTiga, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonTitik = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTitik.SetMinSize( wx.Size( 30,30 ) )

		bSizer602.Add( self.m_buttonTitik, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer59.Add( bSizer602, 1, wx.EXPAND, 5 )

		bSizer603 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonBagi = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBagi.SetMinSize( wx.Size( 30,30 ) )

		bSizer603.Add( self.m_buttonBagi, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonKali = wx.Button( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonKali.SetMinSize( wx.Size( 30,30 ) )

		bSizer603.Add( self.m_buttonKali, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonKurang = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonKurang.SetMinSize( wx.Size( 30,30 ) )

		bSizer603.Add( self.m_buttonKurang, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonPlus = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPlus.SetMinSize( wx.Size( 30,30 ) )

		bSizer603.Add( self.m_buttonPlus, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonHasil = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonHasil.SetMinSize( wx.Size( 30,30 ) )

		bSizer603.Add( self.m_buttonHasil, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer59.Add( bSizer603, 1, wx.EXPAND, 5 )


		bSizer56.Add( bSizer59, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer56 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonPangkat.Bind( wx.EVT_BUTTON, self.Kuadrat )
		self.m_buttonTujuh.Bind( wx.EVT_BUTTON, self.Tujuh )
		self.m_buttonEmpat.Bind( wx.EVT_BUTTON, self.Empat )
		self.m_buttonSatu.Bind( wx.EVT_BUTTON, self.Satu )
		self.m_buttonNolDua.Bind( wx.EVT_BUTTON, self.NolDua )
		self.m_buttonClear.Bind( wx.EVT_BUTTON, self.Clear )
		self.m_buttonDepalan.Bind( wx.EVT_BUTTON, self.Delapan )
		self.m_buttonLima.Bind( wx.EVT_BUTTON, self.Lima )
		self.m_buttonDua.Bind( wx.EVT_BUTTON, self.Dua )
		self.m_buttonNol.Bind( wx.EVT_BUTTON, self.Nol )
		self.m_buttonHapus.Bind( wx.EVT_BUTTON, self.Hapus )
		self.m_buttonSembilan.Bind( wx.EVT_BUTTON, self.Sembilan )
		self.m_buttonEnam.Bind( wx.EVT_BUTTON, self.Enam )
		self.m_buttonTiga.Bind( wx.EVT_BUTTON, self.Tiga )
		self.m_buttonTitik.Bind( wx.EVT_BUTTON, self.Titik )
		self.m_buttonBagi.Bind( wx.EVT_BUTTON, self.Bagi )
		self.m_buttonKali.Bind( wx.EVT_BUTTON, self.Kali )
		self.m_buttonKurang.Bind( wx.EVT_BUTTON, self.Minus )
		self.m_buttonPlus.Bind( wx.EVT_BUTTON, self.Plus )
		self.m_buttonHasil.Bind( wx.EVT_BUTTON, self.Hasil )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Kuadrat( self, event ):
		event.Skip()

	def Tujuh( self, event ):
		event.Skip()

	def Empat( self, event ):
		event.Skip()

	def Satu( self, event ):
		event.Skip()

	def NolDua( self, event ):
		event.Skip()

	def Clear( self, event ):
		event.Skip()

	def Delapan( self, event ):
		event.Skip()

	def Lima( self, event ):
		event.Skip()

	def Dua( self, event ):
		event.Skip()

	def Nol( self, event ):
		event.Skip()

	def Hapus( self, event ):
		event.Skip()

	def Sembilan( self, event ):
		event.Skip()

	def Enam( self, event ):
		event.Skip()

	def Tiga( self, event ):
		event.Skip()

	def Titik( self, event ):
		event.Skip()

	def Bagi( self, event ):
		event.Skip()

	def Kali( self, event ):
		event.Skip()

	def Minus( self, event ):
		event.Skip()

	def Plus( self, event ):
		event.Skip()

	def Hasil( self, event ):
		event.Skip()


