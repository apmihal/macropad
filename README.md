requires piborg/Gamepad specifically Controllers.py and Gamepad.py

add this class to Controllers.py to add 8BitDo Micro functionality

'''python
class EightBitDoMicro(Gamepad):
    # This class must have self.axisNames with a map
    # of numbers to capitalised strings. Follow the
    # conventions the other classes use for generic
    # axes, make up your own names for axes unique
    # to your device.
    # self.buttonNames needs the same treatment.
    # Use python Gamepad.py to get the event mappings.
    fullName = '8BitDo Micro'

    def __init__(self, joystickNumber = 0):
        Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'DPAD -X',
            1: 'DPAD -Y',
            5: 'L2',
            9: 'R2'
        }
        self.buttonNames = {
            0: 'A',
            1: 'B',
            3: 'X',
            4: 'Y',
            6: 'L1',
            7: 'R1',
            8: 'L2',
            9: 'R2',
            10: 'MINUS',
            11: 'PLUS',
            12: 'HEART'

        }
        self._setupReverseMaps()
```
