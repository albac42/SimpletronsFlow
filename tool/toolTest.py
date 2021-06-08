######################################################################################################
#Testing Code [Ignore - Will be remove for production]


#?
#equipment=getEquipment()
#transportposition=getTransportposition()

#robot2._driver.send_command('G0 X5 Y5 Z5 A4 B5 F2000')



#Custom Label Creations
#Container 

#containers.create(
#    '3x6_plate',                    # name of you container
#    grid=(3, 6),                    # specify amount of (columns, rows)
#    spacing=(12, 12),               # distances (mm) between each (column, row)
#    diameter=5,                     # diameter (mm) of each well on the plate
#    depth=10                        # depth (mm) of each well on the plate
#    )                       


#trashA = container.load('point', 'A1')      #Load a Blank container  (Trash/Scale)
#trashB = container.load('point', 'B1')      #Load a Blank container  (Trash/Scale)


#custom_plate = containers.load('3x6_plate', 'D1')


#pipette_left = instruments.Pipette(
#    axis='b',
#    name='my-p200',
#    max_volume=200,
#    min_volume=20
#    )



#pipette_right = instruments.Pipette(
#    axis='a',
#    name='my-p200',
#    max_volume=200,
#    min_volume=20
#    )




#pipette.pick_up_tip(tiprack.wells('A1'))


#strategy='direct'



#Move Bottom Rail
#robot2._driver.send_command('G90')
#robot2._driver.send_command(transportposition['modulePipetting'])
#F= Speed (Robot 2 only X axis) transport well plate from storage to pipetting. 
# transportposition is just a saved locations. 
#robot2._driver.send_command('G0 X481 Y5 Z5 A4 B5 F2000')

#Not Working 100% yet
#equipment['pd1000'].move_to(equipment['1000TiprackB2'][4].bottom(-60))
#equipment['pd1000'].delay(seconds=0.5)
#equipment['pd1000'].move_to(equipment['1000TiprackB2'][4.5].bottom(-50))
#pd1000 is left pipet
#equipment['pd1000'].blow_out()

#equipment['pd100'].blow_out()
#equipment['pd100'].move_to(equipment['100TiprackB1'][1].bottom(-100))
#equipment['pd100'].delay(seconds=0.5)
#equipment['pd100'].move_to(equipment['100TiprackB1'][1].bottom(-70))


#equipment['pd1000'].blow_out()
#equipment['pd1000'].move_to(equipment['100TiprackB1'][1].bottom(-98))
#equipment['pd1000'].delay(seconds=0.5)
#equipment['pd1000'].move_to(equipment['100TiprackB1'][1].bottom(-100), strategy='direct')

#tiprack = labware.load('tiprack-200ul' , 'B1')
#pipette = instruments.P300_single(mount='right')
#pipette.pick_up_tip(tiprack.wells('A1'))

#pd100 is right pipet


#move_to_modulePipetting()
#RUN = Inputs
# TIP COUNTERS = [0, 0]
 # 1 = Dilent 2
 # 2 = Dilent 1
# GET TIP (1), i = 4
#pickup_pd1000tip(0)