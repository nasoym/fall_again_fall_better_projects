"""temp:
	,:
	.:
	/:
"""
import oscmodule

def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		pass

tags = { "left":["uarm-joint", "larm-joint", "hand-joint"],
	"right":["breast-joint", "belly-joint"],
	"top":["neck-joint", "head-joint"],
	"bottom":["foot-joint", "lleg-joint", "uleg-joint"] }
tags_last_message = {}

factor_value = 7.5
angular_force = False

factor_value = 4.0
angular_force = True

damping_factor = 0.7

force_step = 0.01
force_step = 0.001
no_osc_message_timeout = 10

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

def keyPressed(Engine,EngineModule,key,selection,objects):
	global damping_factor,factor_value,force_step,angular_force
	if key == EngineModule.Keys.K_SPACE:
		for k in objects.get()["osc_tags_message"].keys():
			objects.get()["osc_tags_message"][k][0] = Engine.getTime()
			objects.get()["osc_tags_message"][k][1] = 0.0
			partsList = []
			[ partsList.extend(objects.get()[a]) for a in tags[k] ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					part.setMotorValues( 0,0,True)
	if key == EngineModule.Keys.K_3:
		for k in objects.get()["osc_tags_message"].keys():
			objects.get()["osc_tags_message"][k][0] = Engine.getTime()
			objects.get()["osc_tags_message"][k][1] = 1.0
			partsList = []
			[ partsList.extend(objects.get()[a]) for a in tags[k] ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					part.setMotorValues( 
						(10**(factor_value*1.0)), 
						(10**(factor_value*1.0)) * damping_factor,
						angular_force)
			
def keyDown(Engine,EngineModule,key,selection,objects):
	global damping_factor,factor_value,force_step,angular_force
	if key == EngineModule.Keys.K_1:
		for k in objects.get()["osc_tags_message"].keys():
			objects.get()["osc_tags_message"][k][0] = Engine.getTime()
			objects.get()["osc_tags_message"][k][1] -= force_step
			if objects.get()["osc_tags_message"][k][1] < 0:
				objects.get()["osc_tags_message"][k][1] = 0
			force = objects.get()["osc_tags_message"][k][1]
			#Engine.log("set force to: " + str(force))
			partsList = []
			[ partsList.extend(objects.get()[a]) for a in tags[k] ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					part.setMotorValues( 
						(10**(factor_value*force)), 
						(10**(factor_value*force)) * damping_factor,
						angular_force)
	if key == EngineModule.Keys.K_2:
		for k in objects.get()["osc_tags_message"].keys():
			objects.get()["osc_tags_message"][k][0] = Engine.getTime()
			objects.get()["osc_tags_message"][k][1] += force_step
			if objects.get()["osc_tags_message"][k][1] >= 1.0:
				objects.get()["osc_tags_message"][k][1] = 1.0
			force = objects.get()["osc_tags_message"][k][1]
			#Engine.log("set force to: " + str(force))
			partsList = []
			[ partsList.extend(objects.get()[a]) for a in tags[k] ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					part.setMotorValues( 
						(10**(factor_value*force)), 
						(10**(factor_value*force)) * damping_factor,
						angular_force)


def guiUpdate(Engine,EngineModule,selection,objects):
	global tags,tags_last_message,factor_value,damping_factor,force_step,no_osc_message_timeout
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
							#objects.get()["osc_tags_message"][tag][1] = 0.0

						[ partsList.extend(objects.get()[a]) for a in tagList ]

					elif oscAddressParts[1] == "id":
						idname = oscAddressParts[2]
						part = Engine.getFromUuid(idname)
						if part:
							partsList.append(part)

				if len(oscAddressParts) >= 1:

					if ((oscAddressParts[0] == "force") and
						(len(oscMessage) == 3) and
						(type(oscMessage[2]) == float) ):
						for part in partsList:
							if hasattr(part,"setMotorValues"):
								#force = 1.0 - oscMessage[2]
								force = oscMessage[2]
								part.setMotorValues( 
									(10**(factor_value*force)), 
									(10**(factor_value*force)) * damping_factor,
									angular_force)


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
	max_last_message_time = 1000 * no_osc_message_timeout
	for k in objects.get()["osc_tags_message"].keys():
		time_since_last_message = current_time - objects.get()["osc_tags_message"][k][0]
		if time_since_last_message > max_last_message_time:

			force = objects.get()["osc_tags_message"][k][1]
			objects.get()["osc_tags_message"][k][1] += force_step
			if objects.get()["osc_tags_message"][k][1] >= 1.0:
				objects.get()["osc_tags_message"][k][1] = 1.0
				objects.get()["osc_tags_message"][k][0] = Engine.getTime()

			partsList = []
			tagList = tags[k]
			[ partsList.extend(objects.get()[a]) for a in tagList ]
			for part in partsList:
				if hasattr(part,"setMotorValues"):
					part.setMotorValues( 
						(10**(factor_value*force)), 
						(10**(factor_value*force)) * damping_factor,
						angular_force)
			
