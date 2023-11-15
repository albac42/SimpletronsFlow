Known Errors
- Change tips does not work - when added to the protocol commands (in moduleProtocol.py), the robot performs the pickup tip motion in place, rather than moving to the tip rack
- Significant calibration errors - plunger/piston does not move the correct distance to aspirate a volume of fluid

Potential Improvements
- Add further customisation to the mixing functions (how many mixes, etc)
- Add mix-before, as well as the currently implemented mix-after option
- When using the 'back' or 'next' buttons, the GUI does not move to the next step once the user saves the step they're on
- Add a 'delete step' button
- The logic in the moduleProtocol.py is pretty bad - lots of repeated code. This could be written much more tidily using a few functions.
- An updated user guide would probably be helpful
