
def runMethods(Engine,EngineModule,objects,animData,animList,index,methodName,timePos):
	if "groups" in animList[index]:
		for groupName in animList[index]['groups']:
			if groupName in objects.get():
				partsList = objects.get()[groupName]
				for part in partsList:
					if part:
						if methodName+"-groups" in animList[index]:
							methods = animList[index][methodName+"-groups"]
							for method in methods:
								method(Engine,EngineModule,objects,animData,part)
					else:
						Engine.log("anim runMethod:" + str(methodName) + ": part is none: " + str(part))

	if methodName in animList[index]:
		methods = animList[index][methodName]
		for method in methods:
			method(Engine,EngineModule,objects,animData,timePos)

def playAnimation(Engine,EngineModule,objects,animData,animList):
	animName = animData["name"]
	startTime = animData["starttime"]
	if not "index" in animData:
		animData["index"] = 0
	animIndex = animData["index"]
	animListSize = len(animList)
	currentTime = Engine.getTime()
	if animIndex < animListSize:
		endTime = startTime + animList[animIndex]['time']
		if startTime < currentTime < endTime:
			#entering new time part 
			if animIndex != 0: #run end of last index
				runMethods(Engine,EngineModule,objects,animData,animList,animIndex-1,"end",1.0)
			#run start of this index
			runMethods(Engine,EngineModule,objects,animData,animList,animIndex,"start",0.0)
			animData["index"] = animIndex + 1
			animData["starttime"] = endTime
		elif endTime < currentTime:
			#Engine.log("animation: currentTime is bigger then endTime")
			runMethods(Engine,EngineModule,objects,animData,animList,animIndex,"start",0.0)
			animData["index"] = animIndex + 1
			animData["starttime"] = endTime
		else:
			if animIndex != 0:
				oldIndex = animIndex - 1
				oldTime = animList[oldIndex]['time']
				oldEndTime = startTime
				oldStartTime = startTime - oldTime
				oldTimePos = float(currentTime - oldStartTime) / float(oldTime)
				runMethods(Engine,EngineModule,objects,animData,animList,animIndex-1,"timePos",oldTimePos)

	elif animIndex == animListSize:
		if startTime < currentTime:
			runMethods(Engine,EngineModule,objects,animData,animList,animIndex-1,"end",1.0)
			animData["index"] = animIndex + 1
		else:
			oldIndex = animIndex - 1
			oldTime = animList[oldIndex]['time']
			oldEndTime = startTime
			oldStartTime = startTime - oldTime
			oldTimePos = float(currentTime - oldStartTime) / float(oldTime)
			runMethods(Engine,EngineModule,objects,animData,animList,animIndex-1,"timePos",oldTimePos)

	elif animIndex > animListSize:
		if animData["done"] == False:
			animData["done"] = True
			runMethods(Engine,EngineModule,objects,animData,animList,animListSize-1,"ondone",1.0)

