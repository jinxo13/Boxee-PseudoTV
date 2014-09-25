#   Copyright (C) 2011 Jason Anderson
#
#
# This file is part of PseudoTV.
#
# PseudoTV is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PseudoTV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PseudoTV.  If not, see <http://www.gnu.org/licenses/>.

import mc
import xbmc

# Script constants
#__scriptname__ = "PseudoTV"
#__author__     = "Jason102"
#__url__        = "http://github.com/Jasonra/XBMC-PseudoTV"
#__settings__   = xbmcaddon.Addon(id='script.pseudotv')
#__cwd__        = __settings__.getAddonInfo('path')

# ENTRY POINT ##################################################################
if ( __name__ == "__main__" ):

	app = mc.GetApp()
	config = app.GetLocalConfig()
    
	if xbmc.executehttpapi("GetVolume") == "False":
        mc.ShowDialogOk("Warning", "PseudoTV will run more efficiently with the Boxee web[CR]server enabled. Consider turning this on in the network settings.")

	mc.ActivateWindow(14000)
	