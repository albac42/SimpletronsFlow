from opentrons import robot, containers, instruments
from opentrons import robot2

def getTransportposition():
    transportposition = {}
    # module positions
    transportposition['modulePipetting'] = 'G0 X481 Y5 Z5 A4 B5 F2000'
    transportposition['moduleCrosslinker'] = 'G0 X170 Y5 Z5 A4 B5 F2000'
    transportposition['moduleStorage'] = 'G0 X21.3 Y5 Z5 A4 B5 F2000'
    return(transportposition)
