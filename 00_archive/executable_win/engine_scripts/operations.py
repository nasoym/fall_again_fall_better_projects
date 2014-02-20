"""operations:
	o: run operations
"""

import bodyjoint
import helpers

import datetime

def storeOperation(text):
	f = open("operations.txt","a")
	f.write(text + "\n")
	f.close()

def getMesh(Engine,EngineModule):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isMesh():
			return o
	return None

def getJoint(Engine,EngineModule,jointName):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isJoint():
			if o.getName() == jointName:
				return o
	return None

def getBodyFromName(Engine,EngineModule,bodyName):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isActor():
			if o.getName() == bodyName:
				return o
	return None

def getShapeFromName(Engine,EngineModule,bodyName,shapeName):
	objectsNumber = Engine.howManyObjects()
	for i in range(0,objectsNumber):
		o = Engine.getObject(i)
		if o.isPhysicShape():
			if o.getActor().getName() == bodyName:
				if o.getName() == shapeName:
					return o
	return None

def setBodyJointAnchorPos(Engine,EngineModule,bodyName,jointName,vector):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	joint = getJoint(Engine,EngineModule,jointName)
	if body and joint:
		bodyjoint.setBodyJointAnchorPos(body,joint,vector)

def bodyJointScaleJointPos(Engine,EngineModule,bodyName,jointName,vector):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	joint = getJoint(Engine,EngineModule,jointName)
	if body and joint:
		bodyjoint.bodyJointScaleJointPos(body,joint,vector)

def bodyJointScaleBody(Engine,EngineModule,bodyName,jointName,vector):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	joint = getJoint(Engine,EngineModule,jointName)
	if body and joint:
		bodyjoint.bodyJointScaleBody(body,joint,vector)

def setMotorTarget(Engine,EngineModule,jointName,quaternion):
	joint = getJoint(Engine,EngineModule,jointName)
	if joint:
		joint.setMotorTarget(quaternion)

def setLimits(Engine,EngineModule,jointName,y,z):
	joint = getJoint(Engine,EngineModule,jointName)
	if joint:
		joint.setLimits(y,z)

def bodyJointRotateJoint(Engine,EngineModule,bodyName,jointName,quaternion):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	joint = getJoint(Engine,EngineModule,jointName)
	if body and joint:
		bodyjoint.bodyJointRotateJoint(body,joint,quaternion)

def bodyJointAbsoluteRotation(Engine,EngineModule,bodyName,jointName,quaternion):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	joint = getJoint(Engine,EngineModule,jointName)
	if body and joint:
		bodyNum = bodyjoint.howIsBodyConnectedToJoint(body,joint)
		if bodyNum == 1:
			joint.setAnchor1Orientation(quaternion)
		if bodyNum == 2:
			joint.setAnchor2Orientation(quaternion)

def bodyOrientation(Engine,EngineModule,bodyName,quaternion):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		body.setOrientation(quaternion)

def bodyPosition(Engine,EngineModule,bodyName,vector):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		body.setPosition(vector)

def bodySize(Engine,EngineModule,bodyName,vector):
	#mesh = getMesh(Engine,EngineModule)
	#if mesh:
	#	body = mesh.getBodyOfBoneName(bodyName)
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		body.setSize(vector)

def addBox(Engine,EngineModule,bodyName,shapeName,size,r,g,b,a):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = body.addBox(size)
		shape.setColour(r,g,b,a)
		shape.setName(shapeName)

def addCapsule(Engine,EngineModule,bodyName,shapeName,size,r,g,b,a):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = body.addCapsule(size)
		shape.setColour(r,g,b,a)
		shape.setName(shapeName)

def addSphere(Engine,EngineModule,bodyName,shapeName,size,r,g,b,a):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = body.addSphere(size)
		shape.setColour(r,g,b,a)
		shape.setName(shapeName)

def movePhysicShape(Engine,EngineModule,bodyName,shapeName,position):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = getShapeFromName(Engine,EngineModule,bodyName,shapeName)
		if shape:
			shape.setLocalPosition(position)

def scalePhysicShape(Engine,EngineModule,bodyName,shapeName,size):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = getShapeFromName(Engine,EngineModule,bodyName,shapeName)
		if shape:
			shape.setLocalSize(size)

def rotatePhysicShape(Engine,EngineModule,bodyName,shapeName,quaternion):
	body = getBodyFromName(Engine,EngineModule,bodyName)
	if body:
		shape = getShapeFromName(Engine,EngineModule,bodyName,shapeName)
		if shape:
			shape.setLocalOrientation(quaternion)



def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_O:
		if Engine.isKeyDown(EngineModule.Keys.K_1):
			print("write time to operations.txt")
			storeOperation(str(datetime.datetime.now()))
		elif Engine.isKeyDown(EngineModule.Keys.K_0):
			print("clear operations.txt")
			f = open("operations.txt","w")
			f.write("\n")
			f.close()
		elif Engine.isKeyDown(EngineModule.Keys.K_2):
			runOperations(Engine,EngineModule)
		elif Engine.isKeyDown(EngineModule.Keys.K_3):
			print("run custom temp operations")
			runTestOperations(Engine,EngineModule)
		else:
			runOperations(Engine,EngineModule)

def runTestOperations(Engine,EngineModule):



	"""
	setLimits(Engine,EngineModule,jointName='finger-index-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-middle-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-ring-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-little-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='thumb-high-r-joint',y=30,z=30)

	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-index-high-r',jointName='finger-index-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-middle-high-r',jointName='finger-middle-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-ring-high-r',jointName='finger-ring-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-little-high-r',jointName='finger-little-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))

	setLimits(Engine,EngineModule,jointName='finger-index-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-middle-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-ring-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-little-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='thumb-high-l-joint',y=30,z=30)

	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-index-high-l',jointName='finger-index-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-middle-high-l',jointName='finger-middle-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-ring-high-l',jointName='finger-ring-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-little-high-l',jointName='finger-little-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	"""

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(-0.799999952,-0.000000119,-0.000005460))
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(9.621381760,2.274512053,2.274512053))

	bodyJointScaleBody(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(6.739046574,4.300734997,5.782099724))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(-0.650000393,-0.000000477,-0.100000001))

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(-1.429821849,0.000000216,-0.200001255))
	bodyJointScaleBody(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(3.867141247,2.659429073,2.659429073))

	bodyJointScaleBody(Engine,EngineModule,bodyName='belly',jointName='belly-joint',vector=EngineModule.Vec3(6.503275394,6.334136963,3.933000565))

	bodySize(Engine,EngineModule,bodyName='root',vector=EngineModule.Vec3(5.322949886,8.131996155,6.424556255))
	movePhysicShape(Engine,EngineModule,bodyName='root',shapeName='1',position=EngineModule.Vec3(2.500000000,0.000000000,3.500000000))

	rotatePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',quaternion=EngineModule.Quat().fromAngles(0.000000000,-17.500181198,0.000000000))
	movePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',position=EngineModule.Vec3(-1.039790392,-0.000000000,-0.446986526))
	scalePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',size=EngineModule.Vec3(6.242649078,6.996340275,5.899499893))

	bodyJointScaleBody(Engine,EngineModule,bodyName='uleg-l',jointName='uleg-l-joint',vector=EngineModule.Vec3(11.259112358,3.700126410,3.363751173))
	bodyJointScaleBody(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',vector=EngineModule.Vec3(13.635429382,2.527235746,3.057955503))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',vector=EngineModule.Vec3(-0.999999940,0.000001907,-0.199999049))
	scalePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',size=EngineModule.Vec3(5.107838631,2.403376102,2.088624477))
	movePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',position=EngineModule.Vec3(-1.119883060,0.059902906,0.005035845))
	bodyJointScaleBody(Engine,EngineModule,bodyName='foot-l',jointName='foot-l-joint',vector=EngineModule.Vec3(6.180485249,2.403376102,2.088624477))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='foot-l',jointName='foot-l-joint',vector=EngineModule.Vec3(-0.709090650,0.000000562,-0.000000954))

def runOperations(Engine,EngineModule):







	bodyJointScaleJointPos(Engine,EngineModule,bodyName='finger-index-high-r',jointName='finger-index-high-r-joint',vector=EngineModule.Vec3(-1.200001836,0.000002936,0.000005826))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-index-high-r',jointName='finger-index-high-r-joint',vector=EngineModule.Vec3(2.125452757,0.329934716,0.329934716))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-middle-high-r',jointName='finger-middle-high-r-joint',vector=EngineModule.Vec3(2.276066542,0.321195006,0.321195006))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-ring-high-r',jointName='finger-ring-high-r-joint',vector=EngineModule.Vec3(2.195024252,0.309758455,0.309758455))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-little-high-r',jointName='finger-little-high-r-joint',vector=EngineModule.Vec3(1.836014986,0.313505679,0.313505679))
	bodyJointScaleBody(Engine,EngineModule,bodyName='thumb-high-r',jointName='thumb-high-r-joint',vector=EngineModule.Vec3(1.722578645,0.323549688,0.294136077))

	#setMotorTarget(Engine,EngineModule,jointName='finger-index-high-r-joint',quaternion=EngineModule.Quat(0.996194839,0.000000000,0.087155752,0.000000000))

	setLimits(Engine,EngineModule,jointName='finger-index-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-middle-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-ring-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-little-high-r-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='thumb-high-r-joint',y=30,z=30)

	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-index-high-r',jointName='finger-index-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-middle-high-r',jointName='finger-middle-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-ring-high-r',jointName='finger-ring-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-little-high-r',jointName='finger-little-high-r-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))



	bodyJointScaleJointPos(Engine,EngineModule,bodyName='finger-index-high-l',jointName='finger-index-high-l-joint',vector=EngineModule.Vec3(-1.200001836,0.000002936,0.000005826))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-index-high-l',jointName='finger-index-high-l-joint',vector=EngineModule.Vec3(2.125452757,0.329934716,0.329934716))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-middle-high-l',jointName='finger-middle-high-l-joint',vector=EngineModule.Vec3(2.276066542,0.321195006,0.321195006))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-ring-high-l',jointName='finger-ring-high-l-joint',vector=EngineModule.Vec3(2.195024252,0.309758455,0.309758455))
	bodyJointScaleBody(Engine,EngineModule,bodyName='finger-little-high-l',jointName='finger-little-high-l-joint',vector=EngineModule.Vec3(1.836014986,0.313505679,0.313505679))
	bodyJointScaleBody(Engine,EngineModule,bodyName='thumb-high-l',jointName='thumb-high-l-joint',vector=EngineModule.Vec3(1.722578645,0.323549688,0.294136077))

	#setMotorTarget(Engine,EngineModule,jointName='finger-index-high-l-joint',quaternion=EngineModule.Quat(0.996194839,0.000000000,0.087155752,0.000000000))

	setLimits(Engine,EngineModule,jointName='finger-index-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-middle-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-ring-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='finger-little-high-l-joint',y=40,z=0)
	setLimits(Engine,EngineModule,jointName='thumb-high-l-joint',y=30,z=30)

	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-index-high-l',jointName='finger-index-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-middle-high-l',jointName='finger-middle-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-ring-high-l',jointName='finger-ring-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='finger-little-high-l',jointName='finger-little-high-l-joint',quaternion=EngineModule.Quat().fromAngles(0,-30,0))





	setLimits(Engine,EngineModule,jointName='hand-l-joint',y=30,z=15)
	setLimits(Engine,EngineModule,jointName='hand-l-joint',y=0,z=0)
	bodyJointScaleBody(Engine,EngineModule,bodyName='hand-l',jointName='hand-l-joint',vector=EngineModule.Vec3(2.313906908,1.815508246,0.636324406))

	setLimits(Engine,EngineModule,jointName='hand-r-joint',y=30,z=15)
	setLimits(Engine,EngineModule,jointName='hand-r-joint',y=0,z=0)
	bodyJointScaleBody(Engine,EngineModule,bodyName='hand-r',jointName='hand-r-joint',vector=EngineModule.Vec3(2.313906908,1.815508246,0.636324406))



	setLimits(Engine,EngineModule,jointName='uarm-l-joint',y=70,z=70)
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(9.443709373,2.274512053,2.527235746))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',quaternion=EngineModule.Quat(0.939692676,0.000000000,-0.342020214,0.000000000))

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(-1.200000048,-0.000000119,-0.000005460))
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(7.649404049,2.274512053,2.274512053))

	setLimits(Engine,EngineModule,jointName='uarm-r-joint',y=70,z=70)
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',vector=EngineModule.Vec3(9.443709373,2.274512053,2.527235746))
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',quaternion=EngineModule.Quat(0.939692676,0.000000000,-0.342020214,0.000000000))

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',vector=EngineModule.Vec3(-1.200000048,-0.000000119,-0.000005460))
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',vector=EngineModule.Vec3(7.649404049,2.274512053,2.274512053))



	bodyJointScaleBody(Engine,EngineModule,bodyName='larm-l',jointName='larm-l-joint',vector=EngineModule.Vec3(7.937189579,1.569214463,1.426558614))
	setLimits(Engine,EngineModule,jointName='larm-l-joint',y=8,z=80)
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='larm-l',jointName='larm-l-joint',quaternion=EngineModule.Quat().fromAngles(0,0,65))
	setMotorTarget(Engine,EngineModule,jointName='larm-l-joint',quaternion=EngineModule.Quat().fromAngles(0,0,65))

	bodyJointScaleBody(Engine,EngineModule,bodyName='larm-r',jointName='larm-r-joint',vector=EngineModule.Vec3(7.937189579,1.569214463,1.426558614))
	setLimits(Engine,EngineModule,jointName='larm-r-joint',y=8,z=80)
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='larm-r',jointName='larm-r-joint',quaternion=EngineModule.Quat().fromAngles(0,0,-65))
	setMotorTarget(Engine,EngineModule,jointName='larm-r-joint',quaternion=EngineModule.Quat().fromAngles(0,0,-65))



	setMotorTarget(Engine,EngineModule,jointName='uarm-l-joint',quaternion=EngineModule.Quat().fromAngles(0,45,0))

	setMotorTarget(Engine,EngineModule,jointName='uarm-r-joint',quaternion=EngineModule.Quat().fromAngles(0,45,0))






	movePhysicShape(Engine,EngineModule,bodyName='head',shapeName='1',position=EngineModule.Vec3(0.129410282,0.000000000,-0.482966751))

	bodyJointScaleBody(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(2.282495260,5.959090710,5.959090710))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(-2.100000381,-0.000000477,0.100000001))
	rotatePhysicShape(Engine,EngineModule,bodyName='head',shapeName='1',quaternion=EngineModule.Quat(0.991445959,0.000000000,-0.130526364,0.000000000))
	setLimits(Engine,EngineModule,jointName='head-joint',y=25,z=25)



	bodyJointScaleBody(Engine,EngineModule,bodyName='neck',jointName='head-joint',vector=EngineModule.Vec3(2.449944496,2.220075846,2.018250704))
	bodyJointScaleBody(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(2.182900190,2.954921246,2.954921246))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='neck',jointName='head-joint',vector=EngineModule.Vec3(1.333341599,0.000000000,-0.000001192))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(-2.429821730,0.000000216,-0.200001240))
	setLimits(Engine,EngineModule,jointName='neck-joint',y=25,z=15)



	rotatePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',quaternion=EngineModule.Quat(0.939693928,0.000000000,-0.342020541,0.000000000))
	scalePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',size=EngineModule.Vec3(5.675136089,6.926376820,2.591103554))
	movePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',position=EngineModule.Vec3(-0.246501684,0.000000000,-2.817671299))

	bodyJointScaleBody(Engine,EngineModule,bodyName='breast',jointName='breast-joint',vector=EngineModule.Vec3(5.732460499,6.996340275,4.924868107))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='breast',jointName='breast-joint',vector=EngineModule.Vec3(-1.000001788,0.000001907,0.199997157))
	setLimits(Engine,EngineModule,jointName='breast-joint',y=25,z=15)

	scalePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',size=EngineModule.Vec3(5.675135612,6.996340275,4.432381153))
	rotatePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',quaternion=EngineModule.Quat(0.971345127,0.000000000,-0.237686768,0.000000000))
	movePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',position=EngineModule.Vec3(-0.513549209,0.000000000,-2.115990400))





	bodyJointScaleBody(Engine,EngineModule,bodyName='belly',jointName='cheast-joint',vector=EngineModule.Vec3(3.095424891,3.250413418,2.686291933))
	bodyJointScaleBody(Engine,EngineModule,bodyName='belly',jointName='belly-joint',vector=EngineModule.Vec3(3.670929193,6.334136963,3.933000565))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='belly',jointName='cheast-joint',vector=EngineModule.Vec3(1.033345580,0.000000641,0.699999869))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='belly',jointName='belly-joint',vector=EngineModule.Vec3(-1.293976188,0.000000934,0.499999791))
	rotatePhysicShape(Engine,EngineModule,bodyName='belly',shapeName='1',quaternion=EngineModule.Quat(0.991444886,0.000000000,0.130526215,0.000000000))
	setLimits(Engine,EngineModule,jointName='belly-joint',y=25,z=15)



	movePhysicShape(Engine,EngineModule,bodyName='root',shapeName='1',position=EngineModule.Vec3(2.000000000,0.000000000,2.000000000))
	bodySize(Engine,EngineModule,bodyName='root',vector=EngineModule.Vec3(4.399131775,8.297108650,5.840505600))



	bodyJointScaleBody(Engine,EngineModule,bodyName='uleg-l',jointName='uleg-l-joint',vector=EngineModule.Vec3(11.259112358,3.363751173,3.057955503))
	setLimits(Engine,EngineModule,jointName='uleg-l-joint',y=60,z=60)
	#setLimits(Engine,EngineModule,jointName='uleg-l-joint',y=0,z=0)

	bodyJointScaleBody(Engine,EngineModule,bodyName='uleg-r',jointName='uleg-r-joint',vector=EngineModule.Vec3(11.259112358,3.363751173,3.057955503))
	setLimits(Engine,EngineModule,jointName='uleg-r-joint',y=60,z=60)
	#setLimits(Engine,EngineModule,jointName='uleg-r-joint',y=0,z=0)

	bodyJointScaleBody(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',vector=EngineModule.Vec3(13.635429382,2.297487020,2.088624477))
	setLimits(Engine,EngineModule,jointName='lleg-l-joint',y=85,z=10)
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',quaternion=EngineModule.Quat().fromAngles(0.000000000,55,0.000000000))
	setMotorTarget(Engine,EngineModule,jointName='lleg-l-joint',quaternion=EngineModule.Quat().fromAngles(-0.000000000,65,-0.000000000))

	bodyJointScaleBody(Engine,EngineModule,bodyName='lleg-r',jointName='lleg-r-joint',vector=EngineModule.Vec3(13.635429382,2.297487020,2.088624477))
	setLimits(Engine,EngineModule,jointName='lleg-r-joint',y=85,z=10)
	bodyJointAbsoluteRotation(Engine,EngineModule,bodyName='lleg-r',jointName='lleg-r-joint',quaternion=EngineModule.Quat().fromAngles(0.000000000,-55,0.000000000))
	setMotorTarget(Engine,EngineModule,jointName='lleg-r-joint',quaternion=EngineModule.Quat().fromAngles(0.000000000,-65,0.000000000))


	setLimits(Engine,EngineModule,jointName='foot-l-joint',y=60,z=60)
	bodyJointScaleBody(Engine,EngineModule,bodyName='foot-l',jointName='foot-l-joint',vector=EngineModule.Vec3(4.643489361,1.132517815,2.088624477))
	scalePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',size=EngineModule.Vec3(5.107838631,1.132517815,2.088624477))
	movePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',position=EngineModule.Vec3(-0.577070951,1.185877919,-0.001140598))
	rotatePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',quaternion=EngineModule.Quat(0.973933935,0.007293154,0.043005541,-0.222613454))

	setLimits(Engine,EngineModule,jointName='foot-r-joint',y=60,z=60)
	bodyJointScaleBody(Engine,EngineModule,bodyName='foot-r',jointName='foot-r-joint',vector=EngineModule.Vec3(4.643489361,1.132517815,2.088624477))
	scalePhysicShape(Engine,EngineModule,bodyName='foot-r',shapeName='1',size=EngineModule.Vec3(5.107838631,1.132517815,2.088624477))
	movePhysicShape(Engine,EngineModule,bodyName='foot-r',shapeName='1',position=EngineModule.Vec3(-0.577070951,-1.185877919,-0.001140598))
	rotatePhysicShape(Engine,EngineModule,bodyName='foot-r',shapeName='1',quaternion=EngineModule.Quat(0.973933935,-0.007293154,0.043005541,0.222613454))


def runOperations3(Engine,EngineModule):
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(-0.799999952,-0.000000119,-0.000005460))
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-l',jointName='uarm-l-joint',vector=EngineModule.Vec3(9.621381760,2.274512053,2.274512053))

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',vector=EngineModule.Vec3(-0.799999952,-0.000000119,-0.000005460))
	bodyJointScaleBody(Engine,EngineModule,bodyName='uarm-r',jointName='uarm-r-joint',vector=EngineModule.Vec3(9.621381760,2.274512053,2.274512053))

	bodyJointScaleBody(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(6.739046574,4.300734997,5.782099724))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='head',jointName='head-joint',vector=EngineModule.Vec3(-0.650000393,-0.000000477,-0.100000001))

	bodyJointScaleJointPos(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(-1.429821849,0.000000216,-0.200001255))
	bodyJointScaleBody(Engine,EngineModule,bodyName='neck',jointName='neck-joint',vector=EngineModule.Vec3(3.867141247,2.659429073,2.659429073))

	bodyJointScaleBody(Engine,EngineModule,bodyName='belly',jointName='belly-joint',vector=EngineModule.Vec3(6.503275394,6.334136963,3.933000565))
	setMotorTarget(Engine,EngineModule,jointName='belly-joint',quaternion=EngineModule.Quat().fromAngles(-0.000000000,2.000005245,-0.000000000))

	bodySize(Engine,EngineModule,bodyName='root',vector=EngineModule.Vec3(5.322949886,8.131996155,6.424556255))
	movePhysicShape(Engine,EngineModule,bodyName='root',shapeName='1',position=EngineModule.Vec3(2.500000000,0.000000000,3.500000000))

	rotatePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',quaternion=EngineModule.Quat().fromAngles(0.000000000,-17.500181198,0.000000000))
	movePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',position=EngineModule.Vec3(-1.039790392,-0.000000000,-0.446986526))
	scalePhysicShape(Engine,EngineModule,bodyName='breast',shapeName='1',size=EngineModule.Vec3(6.242649078,6.996340275,5.899499893))




	bodyJointScaleBody(Engine,EngineModule,bodyName='uleg-l',jointName='uleg-l-joint',vector=EngineModule.Vec3(11.259112358,3.700126410,3.363751173))
	bodyJointScaleBody(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',vector=EngineModule.Vec3(13.635429382,2.527235746,3.057955503))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='lleg-l',jointName='lleg-l-joint',vector=EngineModule.Vec3(-0.999999940,0.000001907,-0.199999049))
	setMotorTarget(Engine,EngineModule,jointName='uleg-l-joint',quaternion=EngineModule.Quat().fromAngles(-0.000000000,14.000004768,-0.000000000))

	scalePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',size=EngineModule.Vec3(5.107838631,2.403376102,2.088624477))
	movePhysicShape(Engine,EngineModule,bodyName='foot-l',shapeName='1',position=EngineModule.Vec3(-1.119883060,0.059902906,0.005035845))
	bodyJointScaleBody(Engine,EngineModule,bodyName='foot-l',jointName='foot-l-joint',vector=EngineModule.Vec3(6.180485249,2.403376102,2.088624477))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='foot-l',jointName='foot-l-joint',vector=EngineModule.Vec3(-0.709090650,0.000000562,-0.000000954))

	bodyJointScaleBody(Engine,EngineModule,bodyName='uleg-r',jointName='uleg-r-joint',vector=EngineModule.Vec3(11.259112358,3.700126410,3.363751173))
	bodyJointScaleBody(Engine,EngineModule,bodyName='lleg-r',jointName='lleg-r-joint',vector=EngineModule.Vec3(13.635429382,2.527235746,3.057955503))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='lleg-r',jointName='lleg-r-joint',vector=EngineModule.Vec3(-0.999999940,0.000001907,-0.199999049))
	setMotorTarget(Engine,EngineModule,jointName='uleg-r-joint',quaternion=EngineModule.Quat().fromAngles(-0.000000000,12.000014305,-0.000000000))

	scalePhysicShape(Engine,EngineModule,bodyName='foot-r',shapeName='1',size=EngineModule.Vec3(5.107838631,2.403376102,2.088624477))
	movePhysicShape(Engine,EngineModule,bodyName='foot-r',shapeName='1',position=EngineModule.Vec3(-1.119883060,0.059902906,0.005035845))
	bodyJointScaleBody(Engine,EngineModule,bodyName='foot-r',jointName='foot-r-joint',vector=EngineModule.Vec3(6.180485249,2.403376102,2.088624477))
	bodyJointScaleJointPos(Engine,EngineModule,bodyName='foot-r',jointName='foot-r-joint',vector=EngineModule.Vec3(-0.709090650,0.000000562,-0.000000954))



def runOperations2(Engine,EngineModule):

	setBodyJointAnchorPos(Engine,EngineModule,bodyName='foot-r',jointName='foot-ground-r',vector=EngineModule.Vec3(4.643490314,1.399999857,0.000001907))
	setBodyJointAnchorPos(Engine,EngineModule,bodyName='foot-l',jointName='foot-ground-l',vector=EngineModule.Vec3(4.643490314,-1.399999857,0.000001907))

	setBodyJointAnchorPos(Engine,EngineModule,bodyName='ground',jointName='foot-ground-l',vector=EngineModule.Vec3(3.708251953,1.290204048,-4.486923218))
	setBodyJointAnchorPos(Engine,EngineModule,bodyName='ground',jointName='foot-ground-r',vector=EngineModule.Vec3(-3.713666916,1.294058800,-4.488095760))

	setLimits(Engine,EngineModule,jointName='foot-ground-l',y=10,z=123.0)
	setLimits(Engine,EngineModule,jointName='foot-ground-r',y=10,z=123.0)

	setMotorTarget(Engine,EngineModule,jointName='foot-ground-l',quaternion=EngineModule.Quat(0.999847710,0.000000000,0.000000000,-0.017452408))
	setMotorTarget(Engine,EngineModule,jointName='foot-ground-r',quaternion=EngineModule.Quat(0.999847710,0.000000000,0.000000000,0.017452408))

	setBodyJointAnchorPos(Engine,EngineModule,bodyName='ground',jointName='foot-ground-l',vector=EngineModule.Vec3(5.0,1.29,-4.48))
	setBodyJointAnchorPos(Engine,EngineModule,bodyName='ground',jointName='foot-ground-r',vector=EngineModule.Vec3(-5.0,1.29,-4.48))


