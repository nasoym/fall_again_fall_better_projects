import os

lastMemReportTime = 0
lastMemUsage = 0
lastWatchDogTime = 0
framesBelowMinimumFPS = 0

memReportTime = 1000 * 60 * 5
watchDogFrequency = 1000 * 60 * 1

minimalFPS = 30
maximalFramesBelowMinimum = minimalFPS * 60

extremeVelocityFrames = 0
maximalExtremeVelocityFrames = 5.0
extremeVelocityTime = 0

def init(Engine,EngineModule,objects):
	global lastMemReportTime
	lastMemReportTime = Engine.getTime()

def keyPressed(Engine,EngineModule,key,selection,objects):

	global extremeVelocityFrames
	global maximalExtremeVelocityFrames
	global extremeVelocityTime

	if key == EngineModule.Keys.K_EXTREME_VELOCITY:
		if Engine.isFullscreen():

			if extremeVelocityTime != Engine.getTime():
				extremeVelocityTime = Engine.getTime()
				extremeVelocityFrames += 1
				Engine.log("extremeVelocityFrames: " + str(extremeVelocityFrames))

				if Engine.getTimeDifference() > 0:
					fps = float(1000.0 / Engine.getTimeDifference())
					if extremeVelocityFrames > (maximalExtremeVelocityFrames*fps):
						Engine.log("extreme velocity")
						Engine.quit()

	if key == EngineModule.Keys.K_FOCUS_CHANGE:
		if Engine.isFullscreen():
			Engine.log("focus change in fullscreen")
			Engine.quit()

def guiUpdate(Engine,EngineModule,selection,objects):

	global guiFrameCounter
	global lastMemUsage
	global lastMemReportTime
	global lastWatchDogTime

	global framesBelowMinimumFPS
	global maximalFramesBelowMinimum
	global minimalFPS

	global extremeVelocityFrames
	global extremeVelocityTime

	currentTime = Engine.getTime()

	if extremeVelocityTime < currentTime:
		if extremeVelocityFrames > 0:
			extremeVelocityFrames -= 1

	if Engine.getTimeDifference() > 0:
		fps = float(1000.0 / Engine.getTimeDifference())
		if fps < minimalFPS:
			framesBelowMinimumFPS += 1
			framesBelowMinimumFPS += int(minimalFPS - fps)
		elif not framesBelowMinimumFPS <= 0:
			framesBelowMinimumFPS -= 1
		if framesBelowMinimumFPS > maximalFramesBelowMinimum:
			Engine.log("fps: " + str(fps) + " is below minimum: " + str(minimalFPS))
			Engine.quit()
	
	timeSinceLastWatchDog = currentTime - lastWatchDogTime
	if timeSinceLastWatchDog > watchDogFrequency:
		lastWatchDogTime = currentTime
		os.utime("watchdog.txt",None)

	timeSinceLastReport = currentTime - lastMemReportTime
	if timeSinceLastReport > memReportTime:
		lastMemReportTime = currentTime
		memUsage = Engine.getMemoryUsage()
		memUsageDifference = memUsage - lastMemUsage
		lastMemUsage = memUsage
		if memUsageDifference > 0:
			Engine.log("report mem: " + str(memUsage) + "  diff: " + 
				str(memUsageDifference) + 
				" time: " + str(currentTime))
		Engine.log("report fps: " + str(float(1000.0 / Engine.getTimeDifference())))

