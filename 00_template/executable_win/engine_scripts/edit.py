"""edit:
	#x: work on body,joint: sizepos with all joints
	#b: work on body,joint: singual anchor pos 
	m: joint motor
		1:on 2:off 3:set power
	r: rotate
	t: translate
	y: scale
	u: select next
"""

import bodyjoint
import helpers

def storeOperation(text):
	f = open("operations.txt","a")
	f.write("\t" + text + "\n")
	f.close()

def storeBodyJointOperation(EngineModule,method,body,joint,value):
	text = method + "(Engine,EngineModule,"
	text += "bodyName='" + body.getName() + "'"
	text += ",jointName='" + joint.getName() + "'"
	if type(value) == EngineModule.Vec3:
		text += ",vector=EngineModule.Vec3(" + str(value) + "))"
	if type(value) == EngineModule.Quat:
		text += ",quaternion=EngineModule.Quat().fromAngles(" + str(value.toAngles()) + "))"
	storeOperation(text)

def storeBodyOperation(EngineModule,method,body,value):
	text = method + "(Engine,EngineModule,"
	text += "bodyName='" + body.getName() + "'"
	if type(value) == EngineModule.Vec3:
		text += ",vector=EngineModule.Vec3(" + str(value) + "))"
	if type(value) == EngineModule.Quat:
		#text += ",quaternion=EngineModule.Quat(" + str(value) + "))"
		text += ",quaternion=EngineModule.Quat().fromAngles(" + str(value.toAngles()) + "))"
	storeOperation(text)

def keyPressed(Engine,EngineModule,key,selection,objects):


	if key == EngineModule.Keys.K_R:
		print("rotate")
		sel = selection.get()[:]
		while len(sel)>0:
			o = sel.pop()
			body = None
			joint = None
			tooMany = False
			if o.isJoint():
				body,tooMany = helpers.findBodyForJoint(Engine,EngineModule,sel,o)
				joint = o
			elif o.isActor():
				joint,tooMany = helpers.findJointForBody(Engine,EngineModule,sel,o)
				body = o
			elif o.isPhysicShape():
				print("found physicshape")
				print("rotate shape")
				angle = helpers.getModifiedQuaternion(Engine,EngineModule,2.5)
				newValue = o.getLocalOrientation() * angle
				if Engine.isKeyDown(EngineModule.Keys.K_0):
					newValue = EngineModule.Quat()
				o.setLocalOrientation(newValue)

				text = "rotatePhysicShape(Engine,EngineModule"
				text += ",bodyName='" + o.getActor().getName() + "'"
				text += ",shapeName='" + o.getName() + "'"
				text += ",quaternion=EngineModule.Quat().fromAngles(" + str(newValue.toAngles()) + ")"
				text += ")"
				helpers.storeOperation(text)

			elif o.isGuiShape():
				print("found guishape")

			if not tooMany:
				if body and joint:
					print("found body and joint")	
					print("rotate joint orientation")
					if Engine.isKeyDown(EngineModule.Keys.K_9):
						angle = helpers.getModifiedQuaternion(Engine,EngineModule,10)
						bodyNum = bodyjoint.howIsBodyConnectedToJoint(body,joint)
						if bodyNum == 1:
							newOri = joint.getAnchor1Orientation() * angle
							if Engine.isKeyDown(EngineModule.Keys.K_0):
								newOri = EngineModule.Quat()
							joint.setAnchor1Orientation(newOri)
							#TODO take care of all other joints
						if bodyNum == 2:
							newOri = joint.getAnchor2Orientation() * angle
							if Engine.isKeyDown(EngineModule.Keys.K_0):
								newOri = EngineModule.Quat()
							joint.setAnchor2Orientation(newOri)
							#TODO take care of all other joints
						storeBodyJointOperation(EngineModule,"bodyJointAbsoluteRotation",body,joint,newOri)
					else:
						quaternion = helpers.getModifiedQuaternion(Engine,EngineModule,5)
						bodyjoint.bodyJointRotateJoint(body,joint,quaternion)
						storeBodyJointOperation(EngineModule,"bodyJointRotateJoint",body,joint,quaternion)

				elif body and not joint:
					print("found single body")	
					print("rotate body")
					angle = helpers.getModifiedQuaternion(Engine,EngineModule,5)
					newOrientation = body.getOrientation() * angle
					if Engine.isKeyDown(EngineModule.Keys.K_0):
						newOrientation = EngineModule.Quat()
					body.setOrientation(newOrientation)
					storeBodyOperation(EngineModule,"bodyOrientation",body,newOrientation)

				elif joint and not body:
					print("found single joint")	
					print("rotate joint motor target")
					angle = helpers.getModifiedQuaternion(Engine,EngineModule,2)
					motorTarget = joint.getMotorTarget() * angle
					if Engine.isKeyDown(EngineModule.Keys.K_0):
						print("reset motor target")
						motorTarget = EngineModule.Quat()
					joint.setMotorTarget(motorTarget)
					if joint.isMotorOn():
						joint.setMotorOn()
					text = "setMotorTarget(Engine,EngineModule,"
					text += "jointName='" + joint.getName() + "'"
					text += ",quaternion=EngineModule.Quat().fromAngles(" + str(motorTarget.toAngles()) + "))"
					storeOperation(text)

			else:
				print("found too many connected joints and bodies")

	if key == EngineModule.Keys.K_T:
		print("translate")

		sel = selection.get()[:]
		while len(sel)>0:
			o = sel.pop()
			body = None
			joint = None
			tooMany = False
			if o.isJoint():
				body,tooMany = helpers.findBodyForJoint(Engine,EngineModule,sel,o)
				joint = o
			elif o.isActor():
				joint,tooMany = helpers.findJointForBody(Engine,EngineModule,sel,o)
				body = o
			elif o.isPhysicShape():
				print("found physicshape")
				print("move localy")
				vector = helpers.getModifiedVector(Engine,EngineModule,0.25)
				vector = o.getLocalOrientation() * vector
				newValue = o.getLocalPosition() + vector 
				if Engine.isKeyDown(EngineModule.Keys.K_0):
					newValue = EngineModule.Vec3()
				o.setLocalPosition(newValue)

				text = "movePhysicShape(Engine,EngineModule"
				text += ",bodyName='" + o.getActor().getName() + "'"
				text += ",shapeName='" + o.getName() + "'"
				text += ",position=EngineModule.Vec3(" + str(newValue) + ")"
				text += ")"
				helpers.storeOperation(text)

			elif o.isGuiShape():
				print("found guishape")

			if not tooMany:
				if body and joint:
					print("found body and joint")	
					print("move joint pos in rel to body")

					if ((Engine.isKeyDown(EngineModule.Keys.K_9)) or
						(Engine.isKeyDown(EngineModule.Keys.K_8)) or
						(Engine.isKeyDown(EngineModule.Keys.K_0))
						):
						vector = helpers.getModifiedVector(Engine,EngineModule,0.1)
						currentJointPos = bodyjoint.getBodyJointAnchorPos(body,joint)
						newValue = currentJointPos + vector
						bodyjoint.setBodyJointAnchorPos(body,joint,newValue)
						storeBodyJointOperation(EngineModule,"setBodyJointAnchorPos",body,joint,newValue)
					else:
						vector = helpers.getModifiedVector(Engine,EngineModule,0.1)
						currentJointPos = bodyjoint.getBodyJointAnchorSizePos(body,joint)
						newValue = currentJointPos + vector
						bodyjoint.bodyJointScaleJointPos(body,joint,newValue)
						storeBodyJointOperation(EngineModule,"bodyJointScaleJointPos",body,joint,newValue)

				elif body and not joint:
					print("found single body")	
					print("move globaly")
					vector = helpers.getModifiedVector(Engine,EngineModule,1)
					vector = body.getOrientation() * vector
					newPosition = body.getPosition() + vector
					if Engine.isKeyDown(EngineModule.Keys.K_0):
						newPosition = EngineModule.Vec3()
					body.setPosition(newPosition)

					storeBodyOperation(EngineModule,"bodyPosition",body,newPosition)

				elif joint and not body:
					print("found single joint")	



			else:
				print("found too many connected joints and bodies")




	if key == EngineModule.Keys.K_Y:
		print("scale")
		sel = selection.get()[:]
		while len(sel)>0:
			o = sel.pop()
			body = None
			joint = None
			tooMany = False
			if o.isJoint():
				body,tooMany = helpers.findBodyForJoint(Engine,EngineModule,sel,o)
				joint = o
			elif o.isActor():
				joint,tooMany = helpers.findJointForBody(Engine,EngineModule,sel,o)
				body = o
			elif o.isPhysicShape():
				print("found physicshape")
				print("scale localy")
				vector = helpers.getModifiedVector(Engine,EngineModule,0.1)
				newValue = o.getLocalSize() * (EngineModule.Vec3(1,1,1) + vector)
				o.setLocalSize(newValue)

				text = "scalePhysicShape(Engine,EngineModule"
				text += ",bodyName='" + o.getActor().getName() + "'"
				text += ",shapeName='" + o.getName() + "'"
				text += ",size=EngineModule.Vec3(" + str(newValue) + ")"
				text += ")"
				helpers.storeOperation(text)

			elif o.isGuiShape():
				print("found guishape")

			if not tooMany:
				if body and joint:
					print("found body and joint")	
					print("scale body with regards of joints")
					vector = helpers.getModifiedVector(Engine,EngineModule,0.1)
					newValue = body.getSize() * (EngineModule.Vec3(1,1,1) + vector)
					bodyjoint.bodyJointScaleBody(body,joint,newValue)
					storeBodyJointOperation(EngineModule,"bodyJointScaleBody",body,joint,newValue)

				elif body and not joint:
					print("found single body")	
					print("scale")
					vector = helpers.getModifiedVector(Engine,EngineModule,0.1)
					newSize = body.getSize() * (EngineModule.Vec3(1,1,1) + vector)
					body.setSize(newSize)
					storeBodyOperation(EngineModule,"bodySize",body,newSize)

				elif joint and not body:
					print("found single joint")	
					print("scale joint limits")
					yLimit = joint.getYLimit()
					zLimit = joint.getZLimit()

					step = 5
					vector = helpers.getModifiedVector(Engine,EngineModule,step)

					oldY = yLimit
					oldZ = zLimit

					yLimit += vector.x
					zLimit += vector.y

					if Engine.isKeyDown(EngineModule.Keys.K_0):
						yLimit = 0
						zLimit = 0

					if yLimit <= 0:
						yLimit = 0
					if zLimit <= 0:
						zLimit = 0

					print("set limits: y: " + str(yLimit) + " z: " + str(zLimit))

					text = "setLimits(Engine,EngineModule,"
					text += "jointName='" + joint.getName() + "'"
					text += ",y=" + str(yLimit) + ",z=" + str(zLimit) + ")"
					storeOperation(text)

					joint.setLimits(yLimit,zLimit)



			else:
				print("found too many connected joints and bodies")



	if key == EngineModule.Keys.K_U:
		print("select next object")
		sel = selection.get()[:]
		while len(sel)>0:
			o = sel.pop()
			body = None
			joint = None
			tooMany = False
			if o.isJoint():
				body,tooMany = helpers.findBodyForJoint(Engine,EngineModule,sel,o)
				joint = o
			elif o.isActor():
				joint,tooMany = helpers.findJointForBody(Engine,EngineModule,sel,o)
				body = o
			elif o.isPhysicShape():
				# select next physic shape
				print("found physicshape")
				body = o.getActor()
				numShapes = body.howManyPhysicShapes()
				if numShapes > 1:
					selection.clear()
					currentIndex = 0
					for i in range(0,numShapes):
						shape = body.getPhysicShapeByIndex(i)
						if shape.getName() == o.getName():
							currentIndex = i
							break
					newIndex = currentIndex + 1
					if newIndex == numShapes:
						newIndex = 0
					newShape = body.getPhysicShapeByIndex(newIndex)
					selection.add(newShape)
					return

			elif o.isGuiShape():
				print("found guishape")

			if not tooMany:
				if body and joint:
					print("found body and joint")	
					selection.remove(joint)

					bodyJoints = body.howManyJoints()
					currentIndex = 0
					for index in range(0,bodyJoints):
						j = body.getJoint(index)
						if j.readUuid() == joint.readUuid():
							currentIndex = index
							break

					newIndex = currentIndex + 1
					if newIndex == body.howManyJoints():
						newIndex = 0

					j = body.getJoint(newIndex)
					selection.add(j)
				elif body and not joint:
					print("found single body")	
					if Engine.isKeyDown(EngineModule.Keys.K_1):
						if body.howManyJoints() > 0:
							j = body.getJoint(0)
							selection.add(j)

					if Engine.isKeyDown(EngineModule.Keys.K_2):
						if body.howManyPhysicShapes() > 0:
							shape = body.getPhysicShapeByIndex(0)
							selection.clear()
							selection.add(shape)
				elif joint and not body:
					pass
					print("found single joint")	
			else:
				print("found too many connected joints and bodies")



	if key == EngineModule.Keys.K_DELETE:
		print("deleting selection")
		selectedObjects = selection.get()[:]
		selection.clear()
		#for o in selection.get()[:]:
		while len(selectedObjects) > 0:
			o = selectedObjects.pop()
			#for o in selectedObjects:
			print("object: " + str(o))
			if o.isBox():
				print("is box")
				Engine.deleteObject(o)		
				print("done")
		print("done--")


	"""
	if key == EngineModule.Keys.K_X:
		print("edit body joint pos,size")
		body,joint = bodyjoint.getBodyJoint(selection.get())
		if ((body and joint) and bodyjoint.isBodyJointConnected(body,joint)):
			jointPos = bodyjoint.getBodyJointAnchorSizePos(body,joint)
			bodySize = body.getSize()
			print("body joint size pos: " + str(jointPos))
			print("body size: " + str(bodySize))

			#jointPos = EngineModule.Vec3(-153,3,90) 
			#bodySize = EngineModule.Vec3(5,2.9,1.6) 

			bodyjoint.bodyJointScaleJointPos(body,joint, jointPos)
			bodyjoint.bodyJointScaleBody(body,joint, bodySize )

			jointPos = bodyjoint.getBodyJointAnchorSizePos(body,joint)
			bodySize = body.getSize()
			print("body joint size pos: " + str(jointPos))
			print("body size: " + str(bodySize))

	if key == EngineModule.Keys.K_B:
		print("edit body joint pos")
		body,joint = bodyjoint.getBodyJoint(selection.get())
		if ((body and joint) and bodyjoint.isBodyJointConnected(body,joint)):
			jointPos = bodyjoint.getBodyJointAnchorPos(body,joint)
			bodySize = body.getSize()
			print("body joint pos: " + str(jointPos))
			print("body size: " + str(bodySize))

			#jointPos = EngineModule.Vec3(-153,3,90) 
			#jointPos.x *= 1.1
			#bodySize = EngineModule.Vec3(15,1,15)
			#jointPos.y *= 0.9

			bodyjoint.setBodyJointAnchorPos(body,joint,jointPos)
			body.setSize(bodySize)

			jointPos = bodyjoint.getBodyJointAnchorPos(body,joint)
			bodySize = body.getSize()
			print("body joint pos: " + str(jointPos))
			print("body size: " + str(bodySize))
			"""

	if key == EngineModule.Keys.K_M:
		exp = 15
		spring = (10 ** exp) * 1.2
		damping = (10 ** exp) * 1.0

		print("set motor on/off power")
		if len(selection.get()) > 0:
			for o in selection.get():
				if o.isJoint():
					j = o.isJoint()
					if Engine.isKeyDown(EngineModule.Keys.K_1):
						j.setMotorOn()

					if Engine.isKeyDown(EngineModule.Keys.K_2):
						j.setMotorOff()
		else:
			objectsNumber = Engine.howManyObjects()
			for i in range(0,objectsNumber):
				o = Engine.getObject(i)
				if o.isJoint():
					j = o.isJoint()

					if Engine.isKeyDown(EngineModule.Keys.K_1):
						j.setMotorOn()

					if Engine.isKeyDown(EngineModule.Keys.K_2):
						j.setMotorOff()

					if Engine.isKeyDown(EngineModule.Keys.K_3):

						j.dsetMotorSpring(spring)
						j.dsetMotorDamping(damping)
						j.dsetMotorAccel(True)

