/*******************************************************************************

    DipylonReader Copyright (C) 2008 Xavier Faure
    Contact: faure dot epistulam dot mihi dot scripsisti at orange dot fr

    This file is part of DipylonReader.
    DipylonReader is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    DipylonReader is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with DipylonReader.  If not, see <http://www.gnu.org/licenses/>.

    ____________________________________________________________________________

    ❏DipylonReader❏ : pos/posinaudio2posintext.cpp

    See posinaudio2posintex.h for the documentation

*******************************************************************************/

#include "pos/posinaudio2posintext.h"

/*______________________________________________________________________________

        PosInAudio2PosInText::PosInAudio2PosInText(const PosInText2PosInAudio)

        Fill "this" from a PosInText2PosInAudio object : "this" will be the
        reversed source.

        GNWTHI SEAUTON
_____________________________________________________________________________*/
PosInAudio2PosInText::PosInAudio2PosInText(const PosInText2PosInAudio& src) {
  if (src._well_initialized == false) {
    this->_well_initialized = false;
    this->_internal_state = PosInAudio2PosInText::INTERNALSTATE::WRONG_INITIALIZATION;
  }

  // GNWTHI SEAUTON

  this->map.clear();
  this->_well_initialized = true;
  this->_internal_state = PosInAudio2PosInText::INTERNALSTATE::OK;

  /*
    GNWTHI SEAUTON
  */
  
  /*
    src_i : iterator over
        src_i.first : PosInTextRanges
        src_i.second : (PosInAudio, PosInAudio)
  */
  for (auto &src_i : src.map) {
    this->map[ src_i.second ] = src_i.first;
  }
}
