from opentrons import robot, containers, instruments
from opentrons import robot2

gripper_front = 'G0 A106 F2000'
gripper_back = 'G0 A3 F2000'
rackP1 = 'G0 X15 Y0 Z0 A10 B148'
rackP1_back = 'G0 A106'
rackP1_above = 'G0 X15 Y5 Z5 B153'
rackP1_below = 'G0 X15 Y5 Z5 B143'

rackP2 = 'G0 X15 Y0 Z0 A0 B0'
rackP3 = 'G0 X15 Y0 Z0 A0 B0'
rackP4 = 'G0 X15 Y0 Z0 A0 B0'
rackP5 = 'G0 X15 Y0 Z0 A0 B0'
rackP6 = 'G0 X15 Y0 Z0 A0 B0'
rackP7 = 'G0 X15 Y0 Z0 A0 B0'
rackP8 = 'G0 X15 Y0 Z0 A0 B0'

lifter_start = 'G0 B33 F500'
lifter_below = 'G0 B20 F2000'
lifterON = 'M41'
lifterOFF = 'M40'

transportation_base = 'G0 X15 Y5 Z5 A106 B10 F2000'
transportation_base_below = 'G0 X15 Y5 Z5 A106 B3 F2000'

def get_plate_from_P1():
    # absolute positioning
    robot2._driver.send_command('G90')
    # gripper moves back
    robot2._driver.send_command(gripper_back)
    # axis moves to position b of P1
    robot2._driver.send_command(rackP1_below)
    # gripper moves to position a of P1
    robot2._driver.send_command(rackP1_back)
    # axis moves up to place plate on gripper
    robot2._driver.send_command(rackP1_above)
    # gripper moves back
    robot2._driver.send_command(gripper_back)
    # axis down to z of lifter position
    robot2._driver.send_command(lifter_below)
    # gripper towards lifter
    robot2._driver.send_command(gripper_front)
    # axis up to suction cups
    robot2._driver.send_command(lifter_start)
    # lifterON
    robot2._driver.send_command(lifterON)
    # wait 3 sec
    robot2._driver.send_command('G4 S2')
    # place plate on transportation module
    robot2._driver.send_command(transportation_base)
    # move down
    robot2._driver.send_command(transportation_base_below)
    # move gripper back
    robot2._driver.send_command(gripper_back)

    robot2._driver.send_command(gripper_front)
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command(transportation_base)
    robot2._driver.send_command(lifter_start)
    robot2._driver.send_command('G4 S2')

    # lifterOFF
    robot2._driver.send_command(lifterOFF)

    robot2._driver.send_command('G4 S2')
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command(transportation_base)

def lift_lid_from_base():
    robot2._driver.send_command('G90')
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command(gripper_front)
    robot2._driver.send_command('G4 S3')
    robot2._driver.send_command(lifter_start)
    robot2._driver.send_command(lifterON)
    robot2._driver.send_command('G4 S2')
    robot2._driver.send_command(transportation_base)
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command('G4 S2')
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command(transportation_base)
    robot2._driver.send_command('G0 B20')
    robot2._driver.send_command(lifter_start)
    robot2._driver.send_command('G4 S2')
    robot2._driver.send_command(lifterOFF)
    robot2._driver.send_command('G4 S2')
    robot2._driver.send_command(transportation_base_below)
    robot2._driver.send_command(transportation_base)
