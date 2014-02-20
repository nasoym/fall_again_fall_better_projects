import saveload
import time

doneLoadingTime = None

def init(Engine,EngineModule,objects):
	Engine.log("initial sleep of 20 seconds")
	time.sleep(20)
	Engine.lightsOff()
	#saveload.load(Engine,EngineModule,"xmlscene/test.xml",objects)
	saveload.load(Engine,EngineModule,"xmlscene/scene.xml",objects)
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isGuiShape():
			if not o.isFinalShape():
				o.hide()

	global doneLoadingTime
	doneLoadingTime = Engine.getExactTime()

def guiUpdate(Engine,EngineModule,selection,objects):
	currentTime = Engine.getExactTime()

	global doneLoadingTime
	if not doneLoadingTime == None:
		if (doneLoadingTime + (1000 * 15)) < currentTime:
			Engine.lightsOn()
			doneLoadingTime = None

