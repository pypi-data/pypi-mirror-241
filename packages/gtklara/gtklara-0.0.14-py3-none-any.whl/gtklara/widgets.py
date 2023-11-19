# File: /gtklara/widgets.py
# Project: gtklara
# File Created: 18-11-2023 18:28:10
# Author: Clay Risser
# -----
# BitSpur (c) Copyright 2022 - 2023
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gi.repository import Gtk
from gtklara import GTKlara


def _widget_factory(name: str) -> GTKlara:
    class Widget(GTKlara):
        def __init__(self, children=[], **kwargs):
            super().__init__(children, kwargs, getattr(Gtk, name)())

    Widget.__name__ = name
    return Widget


AboutDialog = _widget_factory("AboutDialog")
ActionBar = _widget_factory("ActionBar")
AppChooser = _widget_factory("AppChooser")
AppChooserButton = _widget_factory("AppChooserButton")
AppChooserDialog = _widget_factory("AppChooserDialog")
AppChooserWidget = _widget_factory("AppChooserWidget")
Assistant = _widget_factory("Assistant")
Box = _widget_factory("Box")
Button = _widget_factory("Button")
Calendar = _widget_factory("Calendar")
CheckButton = _widget_factory("CheckButton")
ColorButton = _widget_factory("ColorButton")
ColorChooser = _widget_factory("ColorChooser")
ColorChooserDialog = _widget_factory("ColorChooserDialog")
ColorChooserWidget = _widget_factory("ColorChooserWidget")
ComboBox = _widget_factory("ComboBox")
ComboBoxText = _widget_factory("ComboBoxText")
CustomPaperUnixDialog = _widget_factory("CustomPaperUnixDialog")
DrawingArea = _widget_factory("DrawingArea")
Entry = _widget_factory("Entry")
Expander = _widget_factory("Expander")
FileChooser = _widget_factory("FileChooser")
FileChooserButton = _widget_factory("FileChooserButton")
FileChooserDialog = _widget_factory("FileChooserDialog")
FileChooserWidget = _widget_factory("FileChooserWidget")
FlowBox = _widget_factory("FlowBox")
FontButton = _widget_factory("FontButton")
FontChooser = _widget_factory("FontChooser")
FontChooserDialog = _widget_factory("FontChooserDialog")
FontChooserWidget = _widget_factory("FontChooserWidget")
Frame = _widget_factory("Frame")
Grid = _widget_factory("Grid")
HeaderBar = _widget_factory("HeaderBar")
Image = _widget_factory("Image")
Label = _widget_factory("Label")
Layout = _widget_factory("Layout")
LevelBar = _widget_factory("LevelBar")
LinkButton = _widget_factory("LinkButton")
ListBox = _widget_factory("ListBox")
LockButton = _widget_factory("LockButton")
LockButton = _widget_factory("LockButton")
Menu = _widget_factory("Menu")
MenuItem = _widget_factory("MenuItem")
MessageDialog = _widget_factory("MessageDialog")
Notebook = _widget_factory("Notebook")
Overlay = _widget_factory("Overlay")
PageSetupDialog = _widget_factory("PageSetupDialog")
PageSetupUnixDialog = _widget_factory("PageSetupUnixDialog")
Paned = _widget_factory("Paned")
PlacesSidebar = _widget_factory("PlacesSidebar")
PlacesWindow = _widget_factory("PlacesWindow")
PrintOperationPreview = _widget_factory("PrintOperationPreview")
PrintSettingsDialog = _widget_factory("PrintSettingsDialog")
PrintUnixDialog = _widget_factory("PrintUnixDialog")
ProgressBar = _widget_factory("ProgressBar")
RadioButton = _widget_factory("RadioButton")
RecentChooser = _widget_factory("RecentChooser")
RecentChooserDialog = _widget_factory("RecentChooserDialog")
RecentChooserWidget = _widget_factory("RecentChooserWidget")
Revealer = _widget_factory("Revealer")
Scale = _widget_factory("Scale")
ScaleButton = _widget_factory("ScaleButton")
Scrollbar = _widget_factory("Scrollbar")
ScrolledWindow = _widget_factory("ScrolledWindow")
SearchBar = _widget_factory("SearchBar")
Separator = _widget_factory("Separator")
ShortcutsWindow = _widget_factory("ShortcutsWindow")
Spinner = _widget_factory("Spinner")
Stack = _widget_factory("Stack")
StackSwitcher = _widget_factory("StackSwitcher")
Switch = _widget_factory("Switch")
TextView = _widget_factory("TextView")
ToggleButton = _widget_factory("ToggleButton")
ToolButton = _widget_factory("ToolButton")
Toolbar = _widget_factory("Toolbar")
TreeView = _widget_factory("TreeView")
Viewport = _widget_factory("Viewport")
VolumeButton = _widget_factory("VolumeButton")
Window = _widget_factory("Window")
