#----------------------------------------------------------------------
# Name:        wx.lib.flashwin
# Purpose:     A class that allows the use of the Shockwave Flash
#              ActiveX control
#
# Author:      Robin Dunn
#
# Created:     22-March-2004
# Copyright:   (c) 2004-2020 by Total Control Software
# Licence:     wxWindows license
#----------------------------------------------------------------------
# This module was generated by the wx.activex.GernerateAXModule class
# (See also the genaxmodule script.)

import wx
import wx.activex

clsID = '{D27CDB6E-AE6D-11CF-96B8-444553540000}'
progID = 'ShockwaveFlash.ShockwaveFlash.1'



# Create eventTypes and event binders
wxEVT_ReadyStateChange = wx.activex.RegisterActiveXEvent('OnReadyStateChange')
wxEVT_Progress = wx.activex.RegisterActiveXEvent('OnProgress')
wxEVT_FSCommand = wx.activex.RegisterActiveXEvent('FSCommand')

EVT_ReadyStateChange = wx.PyEventBinder(wxEVT_ReadyStateChange, 1)
EVT_Progress = wx.PyEventBinder(wxEVT_Progress, 1)
EVT_FSCommand = wx.PyEventBinder(wxEVT_FSCommand, 1)


# Derive a new class from ActiveXWindow
class FlashWindow(wx.activex.ActiveXWindow):
    def __init__(self, parent, ID=-1, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name='FlashWindow'):
        wx.activex.ActiveXWindow.__init__(self, parent,
            wx.activex.CLSID('{D27CDB6E-AE6D-11CF-96B8-444553540000}'),
            ID, pos, size, style, name)

    # Methods exported by the ActiveX object
    def QueryInterface(self, riid):
        return self.CallAXMethod('QueryInterface', riid)

    def AddRef(self):
        return self.CallAXMethod('AddRef')

    def Release(self):
        return self.CallAXMethod('Release')

    def GetTypeInfoCount(self):
        return self.CallAXMethod('GetTypeInfoCount')

    def GetTypeInfo(self, itinfo, lcid):
        return self.CallAXMethod('GetTypeInfo', itinfo, lcid)

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid):
        return self.CallAXMethod('GetIDsOfNames', riid, rgszNames, cNames, lcid)

    def Invoke(self, dispidMember, riid, lcid, wFlags, pdispparams):
        return self.CallAXMethod('Invoke', dispidMember, riid, lcid, wFlags, pdispparams)

    def SetZoomRect(self, left, top, right, bottom):
        return self.CallAXMethod('SetZoomRect', left, top, right, bottom)

    def Zoom(self, factor):
        return self.CallAXMethod('Zoom', factor)

    def Pan(self, x, y, mode):
        return self.CallAXMethod('Pan', x, y, mode)

    def Play(self):
        return self.CallAXMethod('Play')

    def Stop(self):
        return self.CallAXMethod('Stop')

    def Back(self):
        return self.CallAXMethod('Back')

    def Forward(self):
        return self.CallAXMethod('Forward')

    def Rewind(self):
        return self.CallAXMethod('Rewind')

    def StopPlay(self):
        return self.CallAXMethod('StopPlay')

    def GotoFrame(self, FrameNum):
        return self.CallAXMethod('GotoFrame', FrameNum)

    def CurrentFrame(self):
        return self.CallAXMethod('CurrentFrame')

    def IsPlaying(self):
        return self.CallAXMethod('IsPlaying')

    def PercentLoaded(self):
        return self.CallAXMethod('PercentLoaded')

    def FrameLoaded(self, FrameNum):
        return self.CallAXMethod('FrameLoaded', FrameNum)

    def FlashVersion(self):
        return self.CallAXMethod('FlashVersion')

    def LoadMovie(self, layer, url):
        return self.CallAXMethod('LoadMovie', layer, url)

    def TGotoFrame(self, target, FrameNum):
        return self.CallAXMethod('TGotoFrame', target, FrameNum)

    def TGotoLabel(self, target, label):
        return self.CallAXMethod('TGotoLabel', target, label)

    def TCurrentFrame(self, target):
        return self.CallAXMethod('TCurrentFrame', target)

    def TCurrentLabel(self, target):
        return self.CallAXMethod('TCurrentLabel', target)

    def TPlay(self, target):
        return self.CallAXMethod('TPlay', target)

    def TStopPlay(self, target):
        return self.CallAXMethod('TStopPlay', target)

    def SetVariable(self, name, value):
        return self.CallAXMethod('SetVariable', name, value)

    def GetVariable(self, name):
        return self.CallAXMethod('GetVariable', name)

    def TSetProperty(self, target, property, value):
        return self.CallAXMethod('TSetProperty', target, property, value)

    def TGetProperty(self, target, property):
        return self.CallAXMethod('TGetProperty', target, property)

    def TCallFrame(self, target, FrameNum):
        return self.CallAXMethod('TCallFrame', target, FrameNum)

    def TCallLabel(self, target, label):
        return self.CallAXMethod('TCallLabel', target, label)

    def TSetPropertyNum(self, target, property, value):
        return self.CallAXMethod('TSetPropertyNum', target, property, value)

    def TGetPropertyNum(self, target, property):
        return self.CallAXMethod('TGetPropertyNum', target, property)

    def TGetPropertyAsNumber(self, target, property):
        return self.CallAXMethod('TGetPropertyAsNumber', target, property)

    # Getters, Setters and properties
    def _get_ReadyState(self):
        return self.GetAXProp('ReadyState')
    readystate = property(_get_ReadyState, None)

    def _get_TotalFrames(self):
        return self.GetAXProp('TotalFrames')
    totalframes = property(_get_TotalFrames, None)

    def _get_Playing(self):
        return self.GetAXProp('Playing')
    def _set_Playing(self, Playing):
        self.SetAXProp('Playing', Playing)
    playing = property(_get_Playing, _set_Playing)

    def _get_Quality(self):
        return self.GetAXProp('Quality')
    def _set_Quality(self, Quality):
        self.SetAXProp('Quality', Quality)
    quality = property(_get_Quality, _set_Quality)

    def _get_ScaleMode(self):
        return self.GetAXProp('ScaleMode')
    def _set_ScaleMode(self, ScaleMode):
        self.SetAXProp('ScaleMode', ScaleMode)
    scalemode = property(_get_ScaleMode, _set_ScaleMode)

    def _get_AlignMode(self):
        return self.GetAXProp('AlignMode')
    def _set_AlignMode(self, AlignMode):
        self.SetAXProp('AlignMode', AlignMode)
    alignmode = property(_get_AlignMode, _set_AlignMode)

    def _get_BackgroundColor(self):
        return self.GetAXProp('BackgroundColor')
    def _set_BackgroundColor(self, BackgroundColor):
        self.SetAXProp('BackgroundColor', BackgroundColor)
    backgroundcolor = property(_get_BackgroundColor, _set_BackgroundColor)

    def _get_Loop(self):
        return self.GetAXProp('Loop')
    def _set_Loop(self, Loop):
        self.SetAXProp('Loop', Loop)
    loop = property(_get_Loop, _set_Loop)

    def _get_Movie(self):
        return self.GetAXProp('Movie')
    def _set_Movie(self, Movie):
        self.SetAXProp('Movie', Movie)
    movie = property(_get_Movie, _set_Movie)

    def _get_FrameNum(self):
        return self.GetAXProp('FrameNum')
    def _set_FrameNum(self, FrameNum):
        self.SetAXProp('FrameNum', FrameNum)
    framenum = property(_get_FrameNum, _set_FrameNum)

    def _get_WMode(self):
        return self.GetAXProp('WMode')
    def _set_WMode(self, WMode):
        self.SetAXProp('WMode', WMode)
    wmode = property(_get_WMode, _set_WMode)

    def _get_SAlign(self):
        return self.GetAXProp('SAlign')
    def _set_SAlign(self, SAlign):
        self.SetAXProp('SAlign', SAlign)
    salign = property(_get_SAlign, _set_SAlign)

    def _get_Menu(self):
        return self.GetAXProp('Menu')
    def _set_Menu(self, Menu):
        self.SetAXProp('Menu', Menu)
    menu = property(_get_Menu, _set_Menu)

    def _get_Base(self):
        return self.GetAXProp('Base')
    def _set_Base(self, Base):
        self.SetAXProp('Base', Base)
    base = property(_get_Base, _set_Base)

    def _get_Scale(self):
        return self.GetAXProp('Scale')
    def _set_Scale(self, Scale):
        self.SetAXProp('Scale', Scale)
    scale = property(_get_Scale, _set_Scale)

    def _get_DeviceFont(self):
        return self.GetAXProp('DeviceFont')
    def _set_DeviceFont(self, DeviceFont):
        self.SetAXProp('DeviceFont', DeviceFont)
    devicefont = property(_get_DeviceFont, _set_DeviceFont)

    def _get_EmbedMovie(self):
        return self.GetAXProp('EmbedMovie')
    def _set_EmbedMovie(self, EmbedMovie):
        self.SetAXProp('EmbedMovie', EmbedMovie)
    embedmovie = property(_get_EmbedMovie, _set_EmbedMovie)

    def _get_BGColor(self):
        return self.GetAXProp('BGColor')
    def _set_BGColor(self, BGColor):
        self.SetAXProp('BGColor', BGColor)
    bgcolor = property(_get_BGColor, _set_BGColor)

    def _get_Quality2(self):
        return self.GetAXProp('Quality2')
    def _set_Quality2(self, Quality2):
        self.SetAXProp('Quality2', Quality2)
    quality2 = property(_get_Quality2, _set_Quality2)

    def _get_SWRemote(self):
        return self.GetAXProp('SWRemote')
    def _set_SWRemote(self, SWRemote):
        self.SetAXProp('SWRemote', SWRemote)
    swremote = property(_get_SWRemote, _set_SWRemote)

    def _get_FlashVars(self):
        return self.GetAXProp('FlashVars')
    def _set_FlashVars(self, FlashVars):
        self.SetAXProp('FlashVars', FlashVars)
    flashvars = property(_get_FlashVars, _set_FlashVars)

    def _get_AllowScriptAccess(self):
        return self.GetAXProp('AllowScriptAccess')
    def _set_AllowScriptAccess(self, AllowScriptAccess):
        self.SetAXProp('AllowScriptAccess', AllowScriptAccess)
    allowscriptaccess = property(_get_AllowScriptAccess, _set_AllowScriptAccess)

    def _get_MovieData(self):
        return self.GetAXProp('MovieData')
    def _set_MovieData(self, MovieData):
        self.SetAXProp('MovieData', MovieData)
    moviedata = property(_get_MovieData, _set_MovieData)


#  PROPERTIES
#  --------------------
#  readystate
#      type:int  arg:VT_EMPTY  canGet:True  canSet:False
#
#  totalframes
#      type:int  arg:VT_EMPTY  canGet:True  canSet:False
#
#  playing
#      type:bool  arg:bool  canGet:True  canSet:True
#
#  quality
#      type:int  arg:int  canGet:True  canSet:True
#
#  scalemode
#      type:int  arg:int  canGet:True  canSet:True
#
#  alignmode
#      type:int  arg:int  canGet:True  canSet:True
#
#  backgroundcolor
#      type:int  arg:int  canGet:True  canSet:True
#
#  loop
#      type:bool  arg:bool  canGet:True  canSet:True
#
#  movie
#      type:string  arg:string  canGet:True  canSet:True
#
#  framenum
#      type:int  arg:int  canGet:True  canSet:True
#
#  wmode
#      type:string  arg:string  canGet:True  canSet:True
#
#  salign
#      type:string  arg:string  canGet:True  canSet:True
#
#  menu
#      type:bool  arg:bool  canGet:True  canSet:True
#
#  base
#      type:string  arg:string  canGet:True  canSet:True
#
#  scale
#      type:string  arg:string  canGet:True  canSet:True
#
#  devicefont
#      type:bool  arg:bool  canGet:True  canSet:True
#
#  embedmovie
#      type:bool  arg:bool  canGet:True  canSet:True
#
#  bgcolor
#      type:string  arg:string  canGet:True  canSet:True
#
#  quality2
#      type:string  arg:string  canGet:True  canSet:True
#
#  swremote
#      type:string  arg:string  canGet:True  canSet:True
#
#  flashvars
#      type:string  arg:string  canGet:True  canSet:True
#
#  allowscriptaccess
#      type:string  arg:string  canGet:True  canSet:True
#
#  moviedata
#      type:string  arg:string  canGet:True  canSet:True
#
#
#
#
#  METHODS
#  --------------------
#  QueryInterface
#      retType:  VT_VOID
#      params:
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          ppvObj
#              in:False  out:True  optional:False  type:unsupported type 26
#
#  AddRef
#      retType:  int
#
#  Release
#      retType:  int
#
#  GetTypeInfoCount
#      retType:  VT_VOID
#      params:
#          pctinfo
#              in:False  out:True  optional:False  type:int
#
#  GetTypeInfo
#      retType:  VT_VOID
#      params:
#          itinfo
#              in:True  out:False  optional:False  type:int
#          lcid
#              in:True  out:False  optional:False  type:int
#          pptinfo
#              in:False  out:True  optional:False  type:unsupported type 26
#
#  GetIDsOfNames
#      retType:  VT_VOID
#      params:
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          rgszNames
#              in:True  out:False  optional:False  type:unsupported type 26
#          cNames
#              in:True  out:False  optional:False  type:int
#          lcid
#              in:True  out:False  optional:False  type:int
#          rgdispid
#              in:False  out:True  optional:False  type:int
#
#  Invoke
#      retType:  VT_VOID
#      params:
#          dispidMember
#              in:True  out:False  optional:False  type:int
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          lcid
#              in:True  out:False  optional:False  type:int
#          wFlags
#              in:True  out:False  optional:False  type:int
#          pdispparams
#              in:True  out:False  optional:False  type:unsupported type 29
#          pvarResult
#              in:False  out:True  optional:False  type:VT_VARIANT
#          pexcepinfo
#              in:False  out:True  optional:False  type:unsupported type 29
#          puArgErr
#              in:False  out:True  optional:False  type:int
#
#  SetZoomRect
#      retType:  VT_VOID
#      params:
#          left
#              in:True  out:False  optional:False  type:int
#          top
#              in:True  out:False  optional:False  type:int
#          right
#              in:True  out:False  optional:False  type:int
#          bottom
#              in:True  out:False  optional:False  type:int
#
#  Zoom
#      retType:  VT_VOID
#      params:
#          factor
#              in:True  out:False  optional:False  type:int
#
#  Pan
#      retType:  VT_VOID
#      params:
#          x
#              in:True  out:False  optional:False  type:int
#          y
#              in:True  out:False  optional:False  type:int
#          mode
#              in:True  out:False  optional:False  type:int
#
#  Play
#      retType:  VT_VOID
#
#  Stop
#      retType:  VT_VOID
#
#  Back
#      retType:  VT_VOID
#
#  Forward
#      retType:  VT_VOID
#
#  Rewind
#      retType:  VT_VOID
#
#  StopPlay
#      retType:  VT_VOID
#
#  GotoFrame
#      retType:  VT_VOID
#      params:
#          FrameNum
#              in:True  out:False  optional:False  type:int
#
#  CurrentFrame
#      retType:  int
#
#  IsPlaying
#      retType:  bool
#
#  PercentLoaded
#      retType:  int
#
#  FrameLoaded
#      retType:  bool
#      params:
#          FrameNum
#              in:True  out:False  optional:False  type:int
#
#  FlashVersion
#      retType:  int
#
#  LoadMovie
#      retType:  VT_VOID
#      params:
#          layer
#              in:True  out:False  optional:False  type:int
#          url
#              in:True  out:False  optional:False  type:string
#
#  TGotoFrame
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          FrameNum
#              in:True  out:False  optional:False  type:int
#
#  TGotoLabel
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          label
#              in:True  out:False  optional:False  type:string
#
#  TCurrentFrame
#      retType:  int
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#
#  TCurrentLabel
#      retType:  string
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#
#  TPlay
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#
#  TStopPlay
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#
#  SetVariable
#      retType:  VT_VOID
#      params:
#          name
#              in:True  out:False  optional:False  type:string
#          value
#              in:True  out:False  optional:False  type:string
#
#  GetVariable
#      retType:  string
#      params:
#          name
#              in:True  out:False  optional:False  type:string
#
#  TSetProperty
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          property
#              in:True  out:False  optional:False  type:int
#          value
#              in:True  out:False  optional:False  type:string
#
#  TGetProperty
#      retType:  string
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          property
#              in:True  out:False  optional:False  type:int
#
#  TCallFrame
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          FrameNum
#              in:True  out:False  optional:False  type:int
#
#  TCallLabel
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          label
#              in:True  out:False  optional:False  type:string
#
#  TSetPropertyNum
#      retType:  VT_VOID
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          property
#              in:True  out:False  optional:False  type:int
#          value
#              in:True  out:False  optional:False  type:double
#
#  TGetPropertyNum
#      retType:  double
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          property
#              in:True  out:False  optional:False  type:int
#
#  TGetPropertyAsNumber
#      retType:  double
#      params:
#          target
#              in:True  out:False  optional:False  type:string
#          property
#              in:True  out:False  optional:False  type:int
#
#
#
#
#  EVENTS
#  --------------------
#  ReadyStateChange
#      retType:  VT_VOID
#      params:
#          newState
#              in:False  out:False  optional:False  type:int
#
#  Progress
#      retType:  VT_VOID
#      params:
#          percentDone
#              in:False  out:False  optional:False  type:int
#
#  FSCommand
#      retType:  VT_VOID
#      params:
#          command
#              in:True  out:False  optional:False  type:string
#          args
#              in:True  out:False  optional:False  type:string
#
#
#
#
