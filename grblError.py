# -*- coding: UTF-8 -*-

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                                                                         '
' Copyright 2018 Gauthier Brière (gauthier.briere "at" gmail.com)         '
'                                                                         '
' This file is part of cn5X                                               '
'                                                                         '
' cn5X is free software: you can redistribute it and/or modify it         '
'  under the terms of the GNU General Public License as published by      '
' the Free Software Foundation, either version 3 of the License, or       '
' (at your option) any later version.                                     '
'                                                                         '
' cn5X is distributed in the hope that it will be useful, but             '
' WITHOUT ANY WARRANTY; without even the implied warranty of              '
' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           '
' GNU General Public License for more details.                            '
'                                                                         '
' You should have received a copy of the GNU General Public License       '
' along with this program.  If not, see <http://www.gnu.org/licenses/>.   '
'                                                                         '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

grblError = [
  [0, "No error."],
  [1, "Expected command letter","G-code words consist of a letter and a value. Letter was not found."],
  [2, "Bad number format","Missing the expected G-code word value or numeric value format is not valid."],
  [3, "Invalid statement","Grbl '$' system command was not recognized or supported."],
  [4, "Value < 0","Negative value received for an expected positive value."],
  [5, "Setting disabled","Homing cycle failure. Homing is not enabled via settings."],
  [6, "Value < 3 usec","Minimum step pulse time must be greater than 3usec."],
  [7, "EEPROM read fail. Using defaults","An EEPROM read failed. Auto-restoring affected EEPROM to default values."],
  [8, "Not idle","Grbl '$' command cannot be used unless Grbl is IDLE. Ensures smooth operation during a job."],
  [9, "G-code lock","G-code commands are locked out during alarm or jog state."],
  [10, "Homing not enabled","Soft limits cannot be enabled without homing also enabled."],
  [11, "Line overflow","Max characters per line exceeded. Received command line was not executed."],
  [12, "Step rate > 30kHz","Grbl '$' setting value cause the step rate to exceed the maximum supported."],
  [13, "Check Door","Safety door detected as opened and door state initiated."],
  [14, "Line length exceeded","Build info or startup line exceeded EEPROM line length limit. Line not stored."],
  [15, "Travel exceeded","Jog target exceeds machine travel. Jog command has been ignored."],
  [16, "Invalid jog command","Jog command has no ' = ' or contains prohibited g-code."],
  [17, "Setting disabled","Laser mode requires PWM output."],
  [18, "Unknown error."],
  [19, "Unknown error."],
  [20, "Unsupported command","Unsupported or invalid g-code command found in block."],
  [21, "Modal group violation","More than one g-code command from same modal group found in block."],
  [22, "Undefined feed rate","Feed rate has not yet been set or is undefined."],
  [23, "Invalid gcode ID:23","G-code command in block requires an integer value."],
  [24, "Invalid gcode ID:24","More than one g-code command that requires axis words found in block."],
  [25, "Invalid gcode ID:25","Repeated g-code word found in block."],
  [26, "Invalid gcode ID:26","No axis words found in block for g-code command or current modal state which requires them."],
  [27, "Invalid gcode ID:27","Line number value is invalid."],
  [28, "Invalid gcode ID:28","G-code command is missing a required value word."],
  [29, "Invalid gcode ID:29","G59.x work coordinate systems are not supported."],
  [30, "Invalid gcode ID:30","G53 only allowed with G0 and G1 motion modes."],
  [31, "Invalid gcode ID:31","Axis words found in block when no command or current modal state uses them."],
  [32, "Invalid gcode ID:32","G2 and G3 arcs require at least one in-plane axis word."],
  [33, "Invalid gcode ID:33","Motion command target is invalid."],
  [34, "Invalid gcode ID:34","Arc radius value is invalid."],
  [35, "Invalid gcode ID:35","G2 and G3 arcs require at least one in-plane offset word."],
  [36, "Invalid gcode ID:36","Unused value words found in block."],
  [37, "Invalid gcode ID:37","G43.1 dynamic tool length offset is not assigned to configured tool length axis."],
  [38, "Invalid gcode ID:38","Tool number greater than max supported value."]
]
