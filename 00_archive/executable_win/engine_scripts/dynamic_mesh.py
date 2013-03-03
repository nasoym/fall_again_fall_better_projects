import createobjects as create

def createBones(Engine,EngineModule,mesh,boneName=None):
	if not boneName:
		boneName = mesh.getRootBoneName()
	createBoneBody(Engine,EngineModule,mesh,boneName)
	childBones = mesh.getBoneNameChildren(boneName)
	for i in range(0,childBones):
		childBoneName = mesh.getBoneNameChildName(boneName,i)
		createBones(Engine,EngineModule,mesh,childBoneName)

def calcBoneGlobalPosRot(Engine,EngineModule,mesh,boneName):
	boneBody = mesh.getBodyOfBoneName(boneName)
	if boneBody:
		boneOrientation = boneBody.getOrientation()
		bonePosition = boneBody.getPosition()
	else:
		boneParentName = mesh.getBoneNameParentName(boneName)
		boneLength = getBoneLength(Engine,EngineModule,mesh,boneName)
		if boneParentName == "":
			boneOrientation = (mesh.getBoneNameOrientation(boneName,False) *
				EngineModule.Quat().fromAngles(0,0,90))
			bonePosition = mesh.getBoneNamePosition(boneName)
			#+ (boneOrientation * EngineModule.Vec3(boneLength,0,0) ))
		else:
			boneLocalPosition = mesh.getBoneNameLocalPosition(boneName)
			scaledBoneLocalPosition = boneLocalPosition * mesh.getMeshScale()
			scaledFlippedBoneLocalPosition = EngineModule.Vec3(
				scaledBoneLocalPosition.Y(), 
				scaledBoneLocalPosition.X(), 
				scaledBoneLocalPosition.Z())				

			parentPosition,parentOrientation = calcBoneGlobalPosRot(Engine,EngineModule,mesh,boneParentName)
			parentBoneLength = getBoneLength(Engine,EngineModule,mesh,boneParentName)

			rotatedLocalOrientation = calcBoneLocalOrientation(Engine,EngineModule,mesh,boneName)
			boneOrientation = parentOrientation * rotatedLocalOrientation

			"""
			#TODO why is this calculation working
			bonePosition = parentPosition  
			bonePosition -= (parentOrientation * EngineModule.Vec3(parentBoneLength,0,0))
			bonePosition += (parentOrientation * scaledFlippedBoneLocalPosition)
			bonePosition += (boneBody.getOrientation() * EngineModule.Vec3(boneLength,0,0) )
			boneBody.setPosition(bonePosition)   
			"""
			bonePosition = (parentPosition  - 
				(parentOrientation * EngineModule.Vec3(parentBoneLength,0,0)) +
				(parentOrientation * scaledFlippedBoneLocalPosition) +
				(boneOrientation * EngineModule.Vec3(boneLength,0,0) ))

	return bonePosition,boneOrientation
			

def getBoneLength(Engine,EngineModule,mesh,boneName):
	defaultBoneLength = 1
	boneLength = mesh.getBoneNameSize(boneName)
	if boneLength == 0:
		boneLength = defaultBoneLength
		boneParentName = mesh.getBoneNameParentName(boneName)
		if not boneParentName == "":
			parentBoneLength = getBoneLength(Engine,EngineModule,mesh,boneParentName)
			boneLength = parentBoneLength * 0.7
	return boneLength

def getClosestBoneParentBody(Engine,EngineModule,mesh,boneName):
	boneBody = mesh.getBodyOfBoneName(boneName)
	if boneBody:
		return boneBody
	else:
		boneParentName = mesh.getBoneNameParentName(boneName)
		if boneParentName == "":
			return None
		else:
			return getClosestBoneParentBody(Engine,EngineModule,mesh,boneParentName)

def calcBoneLocalOrientation(Engine,EngineModule,mesh,boneName):
	boneLocalOrientation = mesh.getBoneNameLocalOrientation(boneName)
	localOrientationAxis = boneLocalOrientation.toAxis()
	localOrientationAngle = boneLocalOrientation.toAngle()
	rotatedOrientationAxis = EngineModule.Quat().fromAngles(0,0,-90) * localOrientationAxis
	rotatedLocalOrientation = EngineModule.Quat().fromAngleAxis(localOrientationAngle,rotatedOrientationAxis)
	return rotatedLocalOrientation


def calcFinalBoneLocalOrientation(Engine,EngineModule,mesh,boneName):
	boneLocalRotation = calcBoneLocalOrientation(Engine,EngineModule,mesh,boneName)
	boneParentName = mesh.getBoneNameParentName(boneName)
	if boneParentName == "":
		pass
	else:
		boneParentBody = mesh.getBodyOfBoneName(boneParentName)
		if boneParentBody:
			pass
		else:
			boneParentLocalRotation = calcBoneLocalOrientation(Engine,EngineModule,mesh,boneParentName)
			boneLocalRotation = boneParentLocalRotation * boneLocalRotation
			#boneLocalRotation = boneLocalRotation * boneParentLocalRotation

	return boneLocalRotation
	


def createBoneBody(Engine,EngineModule,mesh,boneName):
	bonePosition,boneOrientation = calcBoneGlobalPosRot(Engine,EngineModule,mesh,boneName)

	if "-low-" in boneName:
		return
	if "hip-" in boneName:
		return
	if "toes-" in boneName:
		return
	if "shoulder-" in boneName:
		return

	if "cheast" in boneName:
		return

	"""
	if "root" in boneName:
		boneBody = Engine.createStaticActor()
	else:
		boneBody = Engine.createDynamicActor()
		"""

	boneBody = Engine.createDynamicActor()

	boneBody.setName(str(boneName))
	boneBody.setOrientation(boneOrientation)
	boneBody.setPosition(bonePosition)  
	mesh.setBodyForBoneName(boneName,boneBody)

	#shape = boneBody.addCapsule(EngineModule.Vec3(1,1,1))
	shape = boneBody.addBox(EngineModule.Vec3(1,1,1))

	shape.setColour(0.5,0.5,0,0.5)

	boneWidth = 0.5
	boneLength = getBoneLength(Engine,EngineModule,mesh,boneName)
	localBoneWidth = boneWidth
	if localBoneWidth > (boneLength * 0.25):
		localBoneWidth = boneLength * 0.25
	shape.setLocalSize(EngineModule.Vec3(boneLength,localBoneWidth,localBoneWidth))
	shape.setName("1")

	boneParentName = mesh.getBoneNameParentName(boneName)
	if boneParentName != "":
		boneParentBody = getClosestBoneParentBody(Engine,EngineModule,mesh,boneParentName)
		if boneParentBody:
			joint = Engine.createJoint(boneParentBody,boneBody)

			globalAnchor = bonePosition - (boneOrientation * EngineModule.Vec3(boneLength,0,0) )
			#boneLocalRotation = calcBoneLocalOrientation(Engine,EngineModule,mesh,boneName)
			boneLocalRotation = calcFinalBoneLocalOrientation(Engine,EngineModule,mesh,boneName)

			parentLocalAnchor = (boneParentBody.getOrientation().inverse() * 
				(globalAnchor - boneParentBody.getPosition()))

			bodyLocalAnchor = (boneOrientation.inverse() * 
				(globalAnchor - bonePosition))

			joint.setAnchor1(parentLocalAnchor)
			joint.setAnchor2(bodyLocalAnchor)
			joint.setAnchor1Orientation(boneLocalRotation)
			joint.setLimits(1,1)
			mesh.setJointForBoneName(boneName,joint)
			joint.setName(boneName + "-joint")
		
			b = Engine.createGuiBox()
			b.setColour(0,0,1,0.2)
			b.setSize(EngineModule.Vec3(boneWidth*0.25,boneWidth*2,boneWidth*2))
			b.setScalingFixed()
			joint.addShape(b)

			parentChildren = mesh.getBoneNameChildren(boneParentName)
			if parentChildren > 1:
				boneBody.getShapeByIndex(0).setLocalSize( boneBody.getSize() * EngineModule.Vec3(0.3,0.6,0.6) )


