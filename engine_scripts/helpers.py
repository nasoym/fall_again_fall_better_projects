import bodyjoint

def hideNonFinal(Engine,EngineModule):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isGuiShape():
			if not o.isFinalShape():
				o.hide()

def showAll(Engine,EngineModule):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isGuiShape():
			o.show()

def getBodyFromName(Engine,EngineModule,bodyName):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isActor():
			if o.getName() == bodyName:
				return o
	return None

def storeOperation(text):
	f = open("operations.txt","a")
	f.write("\t" + text + "\n")
	f.close()

def delFromSelectionList(selectionList,engineObject):
	for s in selectionList:
		if s.readUuid() == engineObject.readUuid():
			selectionList.remove(s)
			break

def findBodyForJoint(Engine,EngineModule,selection,joint):
	bodies = []
	for o in selection:
		if o.isActor():
			if bodyjoint.isBodyJointConnected(o,joint):
				bodies.append(o)
	if len(bodies) > 0:
		foundBody = bodies[0]
		otherConnectedJoints = []
		tooMany = False
		for j in selection:
			if j.isJoint():
				if bodyjoint.isBodyJointConnected(foundBody,j):
					otherConnectedJoints.append(j)
		if len(otherConnectedJoints) > 0:
			for j in otherConnectedJoints:
				delFromSelectionList(selection,j)
			tooMany = True

		if len(bodies) > 1:
			tooMany = True

		for body in bodies:
			delFromSelectionList(selection,body)

		return foundBody,tooMany
	else:
		return None,False

def findJointForBody(Engine,EngineModule,selection,body):
	joints = []
	for o in selection:
		if o.isJoint():
			if bodyjoint.isBodyJointConnected(body,o):
				joints.append(o)

	if len(joints) > 0:
		foundJoint = joints[0]
		tooMany = False
		otherConnectedActors = []
		for j in selection:
			if j.isActor():
				if bodyjoint.isBodyJointConnected(j,foundJoint):
					otherConnectedActors.append(j)
		if len(otherConnectedActors) > 0:
			for j in otherConnectedActors:
				delFromSelectionList(selection,j)
			tooMany = True

		if len(joints) > 1:
			tooMany = True

		for joint in joints:
			delFromSelectionList(selection,joint)

		return foundJoint,tooMany
	else:
		return None,False

def getModifiedQuaternion(Engine,EngineModule,stepSize):
	quaternion = EngineModule.Quat().fromAngles(0,0,0)

	finalStepSize = stepSize
	if Engine.isKeyDown(EngineModule.Keys.K_MINUS):
		finalStepSize *= 0.5
	elif Engine.isKeyDown(EngineModule.Keys.K_EQUALS):
		finalStepSize *= 2.0

	if Engine.isKeyDown(EngineModule.Keys.K_1):
		quaternion = EngineModule.Quat().fromAngles(finalStepSize,0,0)
	if Engine.isKeyDown(EngineModule.Keys.K_2):
		quaternion = EngineModule.Quat().fromAngles(0,finalStepSize,0)
	if Engine.isKeyDown(EngineModule.Keys.K_3):
		quaternion = EngineModule.Quat().fromAngles(0,0,finalStepSize)
	if Engine.isKeyDown(EngineModule.Keys.K_4):
		quaternion = EngineModule.Quat().fromAngles(-finalStepSize,0,0)
	if Engine.isKeyDown(EngineModule.Keys.K_5):
		quaternion = EngineModule.Quat().fromAngles(0,-finalStepSize,0)
	if Engine.isKeyDown(EngineModule.Keys.K_6):
		quaternion = EngineModule.Quat().fromAngles(0,0,-finalStepSize)

	return quaternion

def getModifiedVector(Engine,EngineModule,stepSize):
	vector = EngineModule.Vec3()

	finalStepSize = stepSize
	if Engine.isKeyDown(EngineModule.Keys.K_MINUS):
		finalStepSize *= 0.5
	elif Engine.isKeyDown(EngineModule.Keys.K_EQUALS):
		finalStepSize *= 2.0

	if Engine.isKeyDown(EngineModule.Keys.K_1):
		vector = EngineModule.Vec3(finalStepSize,0,0)
	if Engine.isKeyDown(EngineModule.Keys.K_2):
		vector = EngineModule.Vec3(0,finalStepSize,0)
	if Engine.isKeyDown(EngineModule.Keys.K_3):
		vector = EngineModule.Vec3(0,0,finalStepSize)
	if Engine.isKeyDown(EngineModule.Keys.K_4):
		vector = EngineModule.Vec3(-finalStepSize,0,0)
	if Engine.isKeyDown(EngineModule.Keys.K_5):
		vector = EngineModule.Vec3(0,-finalStepSize,0)
	if Engine.isKeyDown(EngineModule.Keys.K_6):
		vector = EngineModule.Vec3(0,0,-finalStepSize)
	return vector

def vecclamp(vec):
	if vec.x > 1.0:
		vec.x = 1.0
	if vec.y > 1.0:
		vec.y = 1.0
	if vec.z > 1.0:
		vec.z = 1.0
	
	if vec.x < 0.0:
		vec.x = 0.0
	if vec.y < 0.0:
		vec.y = 0.0
	if vec.z < 0.0:
		vec.z = 0.0
	return vec

