#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyFiberModes.mode import Mode, Family

#: Predefined HE modes
HE11 = Mode(Family.HE, 1, 1)
HE12 = Mode(Family.HE, 1, 2)
HE21 = Mode(Family.HE, 2, 1)
HE22 = Mode(Family.HE, 2, 2)
HE31 = Mode(Family.HE, 3, 1)

#: Predefined EH modes
EH11 = Mode(Family.EH, 1, 1)

#: Predefined TE - TM modes
TE01 = Mode(Family.TE, 0, 1)
TM01 = Mode(Family.TM, 0, 1)

#: Predefined LP modes
LP01 = Mode(Family.LP, 0, 1)
LP11 = Mode(Family.LP, 1, 1)
LP21 = Mode(Family.LP, 2, 1)
LP02 = Mode(Family.LP, 0, 2)
LP31 = Mode(Family.LP, 3, 1)
LP12 = Mode(Family.LP, 1, 2)
LP31 = Mode(Family.LP, 3, 1)
LP22 = Mode(Family.LP, 2, 2)
LP03 = Mode(Family.LP, 0, 3)
LP32 = Mode(Family.LP, 3, 2)
LP41 = Mode(Family.LP, 4, 1)

# -
