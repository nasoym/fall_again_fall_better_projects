"""temp:
	,:
	.:
	/:
"""
import random
import datetime

import engine_scripts.createobjects as create
import engine_scripts.helpers as helpers
import engine_scripts.saveload as saveload

import pyscript_00.ragdoll as ragdoll

import oscmodule

def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		print("create ragdoll")
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=5,
			pos=EngineModule.Vec3(0,0,0),
			#base=True
			base=False
			)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)
		pass

	if key == EngineModule.Keys.K_PERIOD:
		pass
		#print("load ragdoll.xml")
		#saveload.load(Engine,EngineModule,"../xml/ragdoll.xml",objects)

	if key == EngineModule.Keys.K_SLASH:
		pass
		Engine.log("settings")
		Engine.setTimingFactor(7.0)
		Engine.setTimingFactor(3.0)
		Engine.setGravity(EngineModule.Vec3(0,-10,0))

tags = { "left":["uarm-joint", "larm-joint", "hand-joint"],
	"right":["breast-joint", "belly-joint"],
	"top":["neck-joint", "head-joint"],
	"bottom":["foot-joint", "lleg-joint", "uleg-joint"] }
tags_last_message = {}

def init(Engine,EngineModule,objects):
	global tags,tags_last_message
	if not "oscreceiver" in objects.get():
		objects.get()["oscreceiver"] = oscmodule.OscReceiver()
		objects.setUnsavable("oscreceiver")
	if not "osc_tags_message" in objects.get():
		objects.get()["osc_tags_message"] = {}
		objects.setUnsavable("osc_tags_message")
	objects.get()["osc_tags_message"]["left"] = [Engine.getTime(),0.0]
	objects.get()["osc_tags_message"]["right"] = [Engine.getTime(),0.0]
	objects.get()["osc_tags_message"]["top"] = [Engine.getTime(),0.0]
	objects.get()["osc_tags_message"]["bottom"] = [Engine.getTime(),0.0]

	#Engine.log("tags_last_message: " + str(tags_last_message))

def guiUpdate(Engine,EngineModule,selection,objects):
	global tags,tags_last_message
	oscMessages = objects.get()["oscreceiver"].listen()
	if len(oscMessages) > 0:
		#Engine.log("osc: " + str(oscMessages))

		for oscMessage in oscMessages:
			if len(oscMessage) >= 2:
				oscAddress = oscMessage[1]
				if oscAddress[0] == "/":
					oscAddress = oscAddress[1:]
				oscAddressParts = oscAddress.split("/")

				partsList = []
				if len(oscAddressParts) >= 3:
					if oscAddressParts[1] == "group":
						groupName = oscAddressParts[2]
						if groupName in objects.get():
							partsList = objects.get()[groupName]

					elif oscAddressParts[1] == "tag":
						tag = oscAddressParts[2]
						partsList = []
						if tags.has_key(tag):
							tagList = tags[tag]
							#Engine.log(":: " + str( tags_last_message))
							#tags_last_message[tag][0] = Engine.getTime()
							#tags_last_message[tag][1] = 0.0

							objects.get()["osc_tags_message"][tag][0] = Engine.getTime()
							objects.get()["osc_tags_message"][tag][1] = 0.0

						[ partsList.extend(objects.get()[a]) for a in tagList ]

					elif oscAddressParts[1] == "id":
						idname = oscAddressParts[2]
						part = Engine.getFromUuid(idname)
						if part:
							partsList.append(part)

				if len(oscAddressParts) >= 1:

					if ((oscAddressParts[0] == "force") and
						(len(oscMessage) >= 4) and
						(type(oscMessage[2]) == float) and
						(type(oscMessage[3]) == float) ):
						for part in partsList:
							if hasattr(part,"setMotorValues"):
								faktor = 30
								#angularForce = False
								angularForce = True
								if ((len(oscMessage) >=5) and
									(type(oscMessage[4])==float) ):
									faktor = oscMessage[4]
								part.setMotorValues( 
									(10**faktor)* oscMessage[2], 
									(10**faktor)* oscMessage[3],
									angularForce)

					if ((oscAddressParts[0] == "force") and
						(len(oscMessage) == 3) and
						(type(oscMessage[2]) == float) ):
						for part in partsList:
							if hasattr(part,"setMotorValues"):
								#faktor = 20
								faktor = 10
								faktor = 5
								#angularForce = False
								angularForce = True
								part.setMotorValues( 
									(10**faktor) * (1.0 - oscMessage[2]), 
									(10**faktor) * ((1.0 - oscMessage[2])*0.9),
									angularForce)

					if ((oscAddressParts[0] == "position") and
						(len(oscMessage) >= 5) and
						(type(oscMessage[2]) == float) and
						(type(oscMessage[3]) == float) and
						(type(oscMessage[4]) == float) ):
						for part in partsList:
							if hasattr(part,"setPosition"):
								part.setPosition( 
									EngineModule.Vec3(
										oscMessage[2], 
										oscMessage[3], 
										oscMessage[4]) 
									)

	current_time = Engine.getTime()
	max_last_message_time = 1000 * 10
	for k in objects.get()["osc_tags_message"].keys():
		time_since_last_message = current_time - objects.get()["osc_tags_message"][k][0]
		if time_since_last_message > max_last_message_time:

			force = objects.get()["osc_tags_message"][k][1]
			if force < 1.0:
				objects.get()["osc_tags_message"][k][1] += 0.01

			partsList = []
			tagList = tags[k]
			[ partsList.extend(objects.get()[a]) for a in tagList ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					faktor = 10
					#angularForce = False
					angularForce = True
					part.setMotorValues( 
						(10**faktor) * (force), 
						(10**faktor) * (force*0.9),
						angularForce)
			
