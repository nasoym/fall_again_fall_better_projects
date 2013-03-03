import random
lastEventTime = 0
buttonstate = 0

def init(Engine,EngineModule,objects):
	global lastEventTime
	lastEventTime = Engine.getTime()

def guiUpdate(Engine,EngineModule,selection,objects):

	global lastEventTime
	global buttonstate

	currentTime = Engine.getTime()

	timeSinceEvent = currentTime - lastEventTime
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

