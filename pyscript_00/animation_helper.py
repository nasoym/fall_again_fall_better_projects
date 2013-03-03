import random
import engine_scripts.helpers as helpers

def runMethods(Engine,EngineModule,objects,animList,index,methodName,timePos):
	if "groups" in animList[index]:
		for groupName in animList[index]['groups']:
			if groupName in objects.get():
				partsList = objects.get()[groupName]
				for part in partsList:
					if part:
						if methodName+"-groups" in animList[index]:
							methods = animList[index][methodName+"-groups"]
							for method in methods:
								method(Engine,EngineModule,objects,part)
					else:
						Engine.log("anim runMethod:" + str(methodName) + ": part is none: " + str(part))

	if methodName in animList[index]:
		methods = animList[index][methodName]
		for method in methods:
			method(Engine,EngineModule,objects,timePos)

def playAnimation(Engine,EngineModule,objects,animData,animList):
	animName = animData["name"]
	startTime = animData["starttime"]
	animIndex = animData["index"]
	animListSize = len(animList)
	currentTime = Engine.getTime()
	if animIndex < animListSize:
		endTime = startTime + animList[animIndex]['time']
		if ((currentTime > startTime) and
			(currentTime < endTime)):
			if animIndex != 0:
				#print("run anim end: " + str(animName) + " index : " + str(animIndex-1))
				runMethods(Engine,EngineModule,
					objects,animList,animIndex-1,"end",1.0)
			else:
				pass
				#Engine.log("animation start: " + str(animName))

			#print("run anim start: " + str(animName) + " index : " + str(animIndex))
			runMethods(Engine,EngineModule,
				objects,animList,animIndex,"start",0.0)
			animData["index"] = animIndex + 1
			#print("go to next anim index")
			animData["starttime"] = endTime
		elif currentTime > endTime:
			#Engine.log("animation: currentTime is bigger then endTime")
			runMethods(Engine,EngineModule,
				objects,animList,animIndex,"start",0.0)
			animData["index"] = animIndex + 1
			animData["starttime"] = endTime
		else:
			if animIndex != 0:
				oldIndex = animIndex - 1
				oldTime = animList[oldIndex]['time']
				oldEndTime = startTime
				oldStartTime = startTime - oldTime

				oldTimePos = float(currentTime - oldStartTime) / float(oldTime)
				runMethods(Engine,EngineModule,
					objects,animList,animIndex-1,"timePos",oldTimePos)


	elif animIndex == animListSize:
		if currentTime > startTime:
			runMethods(Engine,EngineModule,
				objects,animList,animIndex-1,"end",1.0)
			animData["index"] = animIndex + 1
			animData["done"] = True
			#Engine.log("animation is done: " + str(animName))
			if "ondone" in animData:
				if animData["ondone"]:
					Engine.log("animation done: resend space release")
					Engine.callPythonKeyReleased(EngineModule.Keys.K_SPACE)
		else:
			oldIndex = animIndex - 1
			oldTime = animList[oldIndex]['time']
			oldEndTime = startTime
			oldStartTime = startTime - oldTime

			oldTimePos = float(currentTime - oldStartTime) / float(oldTime)
			runMethods(Engine,EngineModule,
				objects,animList,animIndex-1,"timePos",oldTimePos)




def showBodyList(bodyList):
	number = 0
	text = ""
	for body in bodyList:
		if body:
			text += " " + body.getName() + ":"
			if body.isDynamicActor():
				text += str(body.getMass())[:5]

			number += 1
	print(text)
	print("total bodies: " + str(number))

def getBodyListFromGroupName(objects,groupName):
	if groupName in objects.get():
		bodyList = objects.get()[groupName]
		return bodyList
	else:
		return []

def getBodyListFromGroupNameList(objects,groupNameList):
	bodyList = []
	for groupName in groupNameList:
		if groupName in objects.get():
			for body in objects.get()[groupName]:
				bodyList.append(body)
	return bodyList

def getBodyListFromNameList(Engine,EngineModule,nameList):
	bodyList = []
	for bodyName in nameList:
		body = helpers.getBodyFromName(Engine,EngineModule,bodyName)
		if body:
			bodyList.append(body)
	return bodyList
		

def resetMasses(bodyList):
	for body in bodyList:
		if body:
			if body.isActor():
				body.resetMass()

def multiplyMasses(bodyList,factor):
	for body in bodyList:
		if body:
			if body.isActor():
				newMass = body.getMass() * factor
				body.setMass(newMass)

def setMasses(bodyList,mass):
	for body in bodyList:
		if body:
			if body.isActor():
				body.setMass(mass)

def showMassRelationToPrev(bodyList):
	text = ""
	for i in range(0,len(bodyList)):
		body = bodyList[i]
		if i > 0:
			prevBody = bodyList[i-1]
			massRelation = body.getMass() / prevBody.getMass()
			text += " " + body.getName() + ":" + str(body.getMass())[:5]
			text += ":" + str(massRelation)[:5]
		else:
			text += " " + body.getName() + ":" + str(body.getMass())[:5]
	print(text)

def showMassRelationToAll(bodyList):
	totalMass = 0
	text = ""
	for body in bodyList:
		totalMass += body.getMass()
	for body in bodyList:
		massRelation = body.getMass() / totalMass
		text += " " + body.getName() + ":" + str(body.getMass())[:5]
		text += ":" + str(massRelation)[:5]
	print(text)


def approachRelationToPrev(bodyList,finalRelation,approachPercentage):
	for i in range(0,len(bodyList)):
		body = bodyList[i]
		if i > 0:
			prevBody = bodyList[i-1]
			massInFinalRelation = prevBody.getMass() * finalRelation
			diffToActualMass = massInFinalRelation - body.getMass()
			newMass = body.getMass() + (diffToActualMass * approachPercentage)
			body.setMass(newMass)

def approachEqualMassDistribution(bodyList,approachPercentage):
	totalMass = 0
	totalBodies = 0
	for body in bodyList:
		totalMass += body.getMass()
		totalBodies += 1
	for body in bodyList:
		massInFinalRelation = totalMass / totalBodies
		diffToActualMass = massInFinalRelation - body.getMass()
		newMass = body.getMass() + (diffToActualMass * approachPercentage)
		body.setMass(newMass)

def setTiming(Engine,EngineModule,objects,timePos,startFactor,endFactor):
	timingDelta = endFactor - startFactor
	timing = startFactor + (timingDelta * timePos)
	Engine.setTimingFactor(timing)
	return True

def dissableCollisions(Engine,EngineModule,objects,bodyNames):
	for name in bodyNames:
		if name in objects.get():
			bodyList = objects.get()[name]
			for body in bodyList:
				if body.isActor():
					body.dissableCollisions()

def enableCollisions(Engine,EngineModule,objects,bodyNames):
	for name in bodyNames:
		if name in objects.get():
			bodyList = objects.get()[name]
			for body in bodyList:
				if body.isActor():
					body.enableCollisions()

def setRandomTarget(Engine,EngineModule,objects,jointNames,
	freedomXmin, freedomXmax, freedomYmin, freedomYmax, freedomZmin, freedomZmax):
	for name in jointNames:
		if name in objects.get():
			jointList = objects.get()[name]
			for joint in jointList:
				if joint.isJoint():
					target = joint.getMotorTarget()
					target = EngineModule.Quat()
					randomOrientation = EngineModule.Quat().fromAngles(
						random.uniform(freedomXmin,freedomXmax),
						random.uniform(freedomYmin,freedomYmax),
						random.uniform(freedomZmin,freedomZmax)
						)
					#randomOrientation = EngineModule.Quat().fromAngles(0,20,0)
					joint.setMotorTarget(randomOrientation * target)


def findMiddlePos(Engine,EngineModule,objects):

	partsList = objects.get()["head"]
	pos = partsList[0].getPosition()
	lowX = pos.x
	highX = pos.x
	lowY = pos.y
	highY = pos.y
	lowZ = pos.z
	highZ = pos.z
	for part in partsList:
		pos = part.getPosition()
		if pos.x < lowX:
			lowX = pos.x
		if pos.x > highX:
			highX = pos.x

		if pos.y < lowY:
			lowY = pos.y
		if pos.y > highY:
			highY = pos.y

		if pos.z < lowZ:
			lowZ = pos.z
		if pos.z > highZ:
			highZ = pos.z

	finalX = highX - ((highX-lowX) * 0.5)
	finalY = highY - ((highY-lowY) * 0.5)
	finalZ = highZ - ((highZ-lowZ) * 0.5)
	middlePos = EngineModule.Vec3(finalX,finalY,finalZ)
	middlePos = middlePos + EngineModule.Vec3(0,10,0)

	if not "head-debug" in objects.get():
		b = Engine.createGuiBox()
		b.setColour(0,0,1,0.5)
		b.setSize(EngineModule.Vec3(10,10,10))
		b.setPosition(EngineModule.Vec3(0,200,0))
		objects.get()["head-debug"] = b

	debug = objects.get()["head-debug"]
	debug.setPosition(middlePos)


def applyForceToDebug(Engine,EngineModule,objects,body,force=600000):
	if "head-debug" in objects.get():
		debug = objects.get()["head-debug"]
		debugPositioin = debug.getPosition()

		angleRand = 40

		relVec = debugPositioin - body.getPosition()
		relVec.normalise()
		relVec = EngineModule.Quat().fromAngles(0,random.uniform(-angleRand,angleRand),0) * relVec
		relVec = relVec * force * random.uniform(0.1,1.0)
		relVec.y = 0
		body.addForce(relVec)

def applyForwardForce(Engine,EngineModule,objects,body,force=60000):
	relVec = EngineModule.Vec3(-1,0,0)
	relVec = body.getOrientation() * relVec
	relVec.normalise()
	relVec = relVec * force
	body.addForce(relVec)

def applyDownwardForce(Engine,EngineModule,objects,body,force=60000):
	relVec = EngineModule.Vec3(0,-1,0)
	relVec = body.getOrientation() * relVec
	relVec.normalise()
	relVec = relVec * force
	body.addForce(relVec)



