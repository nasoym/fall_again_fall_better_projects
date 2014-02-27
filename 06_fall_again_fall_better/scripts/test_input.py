import random
lastEventTime = 0
buttonstate = 0
initialwait = True

def init(Engine,EngineModule,objects):
	global lastEventTime
	lastEventTime = Engine.getTime()
	#objects.get()["initialwait"] = True
	#objects.setUnsavable("initialwait")

def guiUpdate(Engine,EngineModule,selection,objects):
	global lastEventTime
	global buttonstate
	global initialwait
	currentTime = Engine.getTime()
	timeSinceEvent = currentTime - lastEventTime

	#Engine.log("current time: %s" % str(currentTime))
	#Engine.log("time since: %s" % str(timeSinceEvent))
	#if "initialwait" in objects.get():
		#initialwait = objects.get()["initialwait"]
	if initialwait:
		#Engine.log("current time: %s" % str(currentTime))
		#Engine.log("time since: %s" % str(timeSinceEvent))
		if timeSinceEvent > 10000:
			#objects.get()["initialwait"] = False
			initialwait = False
			Engine.log("intial wait is done current time: %s" % str(currentTime))
	else:
		if timeSinceEvent > 100:
			lastEventTime = currentTime
			if random.uniform(0,1) < 0.1:
				if buttonstate == 0:
					buttonstate = 1
					#Engine.log("create test event: space pressed")
					Engine.callPythonKeyPressed(EngineModule.Keys.K_SPACE)
				elif buttonstate == 1:
					buttonstate = 0
					#Engine.log("create test event: space released")
					Engine.callPythonKeyReleased(EngineModule.Keys.K_SPACE)

