import random

#lastEventTime = 0
#buttonstate = 0
#initialwait = True
#createEvents = True

def init(Engine,EngineModule,objects):
	#global lastEventTime
	#lastEventTime = Engine.getTime()

	objects.get()["create_events"] = True
	objects.setUnsavable("create_events")

	objects.get()["lastEventTime"] = Engine.getTime()
	objects.setUnsavable("lastEventTime")

	objects.get()["initialwait"] = True
	objects.setUnsavable("initialwait")

	objects.get()["buttonstate"] = 0
	objects.setUnsavable("buttonstate")

def keyPressed(Engine,EngineModule,key,selection,objects):
	#global createEvents
	if key == EngineModule.Keys.K_M:
		if "create_events" in objects.get():
			create_events = objects.get()["create_events"]
			if create_events:
				create_events = False
				objects.get()["create_events"] = False
				Engine.log("dissabling creation of mock events")
			else:
				create_events = True
				objects.get()["create_events"] = True
				Engine.log("enabling creation of mock events")

def guiUpdate(Engine,EngineModule,selection,objects):
	#global lastEventTime
	#global buttonstate
	#global initialwait
	#global createEvents

	lastEventTime = 0
	buttonstate = 0
	initialwait = True
	create_events = True
	if "create_events" in objects.get():
		create_events = objects.get()["create_events"]
	if "initialwait" in objects.get():
		initialwait = objects.get()["initialwait"]
	if "buttonstate" in objects.get():
		buttonstate = objects.get()["buttonstate"]
	if "lastEventTime" in objects.get():
		lastEventTime = objects.get()["lastEventTime"]

	currentTime = Engine.getTime()
	timeSinceEvent = currentTime - lastEventTime

	if initialwait:
		if timeSinceEvent > 10000:
			initialwait = False
			Engine.log("intial wait is done current time: %s" % str(currentTime))
	else:
		if create_events:
			if timeSinceEvent > 100:
				lastEventTime = currentTime
				if random.uniform(0,5) < 0.1:
					if buttonstate == 0:
						buttonstate = 1
						#Engine.log("create test event: space pressed")
						Engine.callPythonKeyPressed(EngineModule.Keys.K_SPACE)
					elif buttonstate == 1:
						buttonstate = 0
						#Engine.log("create test event: space released")
						Engine.callPythonKeyReleased(EngineModule.Keys.K_SPACE)

	objects.get()["lastEventTime"] = lastEventTime
	objects.get()["initialwait"] = initialwait
	objects.get()["buttonstate"] = buttonstate

