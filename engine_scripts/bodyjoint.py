

def howIsBodyConnectedToJoint(body,joint):
	if joint.getBody1().readUuid() == body.readUuid():
		return 1
	elif joint.getBody2().readUuid() == body.readUuid():
		return 2
	return 0

def getBodyJointAnchorSizePos(body,joint):
	if joint.getBody1().readUuid() == body.readUuid():
		return joint.getAnchor1Size()
	elif joint.getBody2().readUuid() == body.readUuid():
		return joint.getAnchor2Size()
	else:
		print("body is not 1 or 2")

def getBodyJointAnchorOrientation(body,joint):
	if joint.getBody1().readUuid() == body.readUuid():
		return joint.getAnchor1Orientation()
	elif joint.getBody2().readUuid() == body.readUuid():
		return joint.getAnchor2Orientation()
	else:
		print("body is not 1 or 2")

def getBodyJointAnchorPos(body,joint):
	if joint.getBody1().readUuid() == body.readUuid():
		return joint.getAnchor1()
	elif joint.getBody2().readUuid() == body.readUuid():
		return joint.getAnchor2()
	else:
		print("body is not 1 or 2")

def setBodyJointAnchorSizePos(body,joint,position):
	if joint.getBody1().readUuid() == body.readUuid():
		joint.setAnchor1Size(position)
	elif joint.getBody2().readUuid() == body.readUuid():
		joint.setAnchor2Size(position)
	else:
		print("body is not 1 or 2")

def setBodyJointAnchorPos(body,joint,position):
	if joint.getBody1().readUuid() == body.readUuid():
		joint.setAnchor1(position)
	elif joint.getBody2().readUuid() == body.readUuid():
		joint.setAnchor2(position)
	else:
		print("body is not 1 or 2")

def setBodyJointAnchorOrientation(body,joint,orientation):
	if joint.getBody1().readUuid() == body.readUuid():
		joint.setAnchor1Orientation(orientation)
	elif joint.getBody2().readUuid() == body.readUuid():
		joint.setAnchor2Orientation(orientation)
	else:
		print("body is not 1 or 2")

def isBodyJointConnected(body,joint):
	if joint.getBody1().readUuid() == body.readUuid():
		return True
	elif joint.getBody2().readUuid() == body.readUuid():
		return True
	return False

def getBodyJoint(selection):
	body = None
	joint = None
	if len(selection) == 2:
		if selection[0].isActor():
			body = selection[0]
		if selection[1].isActor():
			body = selection[1]
		if selection[0].isJoint():
			joint = selection[0]
		if selection[1].isJoint():
			joint = selection[1]
	return (body,joint)

def bodyJointScaleBody(body,joint,newBodySize):
	if isBodyJointConnected(body,joint):
		oldJointAnchorPos = getBodyJointAnchorPos(body,joint)

		oldJointAnchorSizePos = getBodyJointAnchorSizePos(body,joint)
		body.setSize(newBodySize)
		setBodyJointAnchorSizePos(body,joint,oldJointAnchorSizePos)
		newJointAnchorPos = getBodyJointAnchorPos(body,joint)

		bodyJoints = body.howManyJoints()
		for index in range(0,bodyJoints):
			j = body.getJoint(index)
			if not (j.readUuid() == joint.readUuid()):
				anchor = getBodyJointAnchorPos(body,j)
				oldRelativePos = anchor - oldJointAnchorPos
				newRelativePos = oldRelativePos + newJointAnchorPos
				setBodyJointAnchorPos(body,j,newRelativePos)

def bodyJointScaleJointPos(body,joint,newJointSizePos):
	if isBodyJointConnected(body,joint):
		oldJointAnchorPos = getBodyJointAnchorPos(body,joint)
		setBodyJointAnchorSizePos(body,joint,newJointSizePos)
		newJointAnchorPos = getBodyJointAnchorPos(body,joint)

		bodyJoints = body.howManyJoints()
		for index in range(0,bodyJoints):
			j = body.getJoint(index)
			if not (j.readUuid() == joint.readUuid()):
				anchor = getBodyJointAnchorPos(body,j)
				oldRelativePos = anchor - oldJointAnchorPos
				newRelativePos = oldRelativePos + newJointAnchorPos
				setBodyJointAnchorPos(body,j,newRelativePos)

		
def bodyJointRotateJoint(body,joint,quaternion):
	if isBodyJointConnected(body,joint):

		oldJointAnchorPos = getBodyJointAnchorPos(body,joint)
		oldJointAnchorOrientation = getBodyJointAnchorOrientation(body,joint)

		newJointAnchorOrientation = oldJointAnchorOrientation * quaternion

		setBodyJointAnchorOrientation(body,joint,newJointAnchorOrientation)

		newJointAnchorPos = getBodyJointAnchorPos(body,joint)


		bodyJoints = body.howManyJoints()
		for index in range(0,bodyJoints):
			j = body.getJoint(index)
			if not (j.readUuid() == joint.readUuid()):
				anchor = getBodyJointAnchorPos(body,j)
				orientation = getBodyJointAnchorOrientation(body,j)

				oldRelativePos = anchor - oldJointAnchorPos
				newRelativePos = oldRelativePos + newJointAnchorPos
				newRelativePos = quaternion * newRelativePos

				setBodyJointAnchorPos(body,j,newRelativePos)

				newOrientation = quaternion * orientation
				setBodyJointAnchorOrientation(body,j,newOrientation)

