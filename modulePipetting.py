import opentrons
#import openworkstation
from opentrons import robot, containers, instruments
#from openworkstation import robot2
from time import sleep
from moduleCommands import *
##################################################################################

#New Pipetting Setup

def loadpipette (axis_s,max_v_s, min_v_s, asp_s, dis_a,tiprack, trash):

  #Eror Check
  if max_v_s > 1000:
    max_v_s = 1000
    print('Loaded Default Max Volume due to exceed device max amount (1000 uL Max)')
  if min_v_s  < 5:
    min_v_s = 5
    print('Loaded Default Min Volume due to exceed device max amount (5 uL Min)')


  if axis_s == 'b':
    pipette_b = instruments.Pipette(
      axis='b',
      name='pd1000',
      max_volume=max_v_s,
      min_volume=min_v_s,
      channels = 1,
      aspirate_speed=asp_s,
      dispense_speed=dis_a,
      tip_racks=tiprack,
      trash_container=trash
      )
    print ("Loaded B Axis Pipette")
  elif axis_s == 'a':
    pipette_a = instruments.Pipette(
      axis='a',
      name='pd100',
      max_volume=asp_s,
      min_volume=dis_a,
      channels = 1,
      aspirate_speed=200,
      dispense_speed=600,
      tip_racks=tiprack,
      trash_container=trash
      )
    print ("Loaded B Axis Pipette")
  else:
    print ("Please check your loadpipette axis is correct or not")



def pickuptip (pipette, well):
  if pipette == b:
    pipette_b.pick_up_tip(tiprack.wells('A1'))
  elif pipette == a:
    pipette_a.pick_up_tip(tiprack.wells('A1'))
  else:
    print("Pipette and Wells Error, Please check value are correct")



# # Old Code - Reference
# # 1. DEFINE CONTAINERS - Create 'Equipment' function
# def getEquipment():
      
#       equipment={}
#       #Create Container 
#       #containers.create('heating-block-3x4', grid=(3, 4), spacing=(22.3, 22.3), diameter=17, depth=45)
      
#       #equipment['InputsC1'] = containers.load('heating-block-3x4','C1')
#       #equipment['MixingD1'] = containers.load('heating-block-3x4', 'D1')
#       #equipment['OutputD2'] = containers.load('48-well-plate', 'D2')
#       containers.create('custom', grid=(7, 5), spacing=(10.3, 18.6), diameter=9, depth=56)
#       equipment['1000TiprackB2'] = containers.load('tiprack-1000ul2', 'B2')
#       equipment['100TiprackB1'] = containers.load('tiprack-1000ul', 'B1')
#       equipment['TrashA2'] = containers.load('trash-box', 'A2')
#       #equipment['custom'] = containers.load('custom', 'C2')
#       #Setup Pipette Left
#       equipment['pd1000'] = instruments.Pipette(
#          name='pd1000',
#          axis='b',
#          max_volume=1000,
#          min_volume=100,
#          channels=1,
#          aspirate_speed=800,
#          dispense_speed=1200,
#          tip_racks=[equipment['1000TiprackB2']],
#          trash_container=equipment['TrashA2'])
#       #Setup Pipette RIGHT
#       equipment['pd100'] = instruments.Pipette(
#          name='pd100',
#          axis='a',
#          max_volume=1000,
#          min_volume=100,
#          channels=1,
#          aspirate_speed=600,
#          dispense_speed=800,
#          tip_racks=[equipment['100TiprackB1']],
#          trash_container=equipment['TrashA2'])
#       return(equipment)

# equipment=getEquipment()

# def smoothMix(pipette, dH, stroke=1, iterations = 1, speed = 5000):
#     for i in range(iterations):

#         strokeLength = pipette.positions['bottom'] - pipette.positions['top']

#         speedCommandString = "G1 F%d" % speed

#         # relative movement
#         robot._driver.send_command('G91')
#         robot._driver.send_command(speedCommandString)

#         partialStroke = stroke*strokeLength
#         moveCommandString = "G1 Z%2.f B%2.f" % (dH, -partialStroke)
#         moveCommandString2 = "G1 Z%2.f B%2.f" % (-dH, partialStroke)
#         # mix 1
#         robot._driver.send_command(moveCommandString)
#         robot._driver.send_command(moveCommandString2)

#         # absolute movement
#         robot._driver.send_command('G90')
