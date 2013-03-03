import createobjects as create

def createBones(Engine,EngineModule,mesh,boneName=None):
	if not boneName:
		boneName = mesh.getRootBoneName()
	createBoneBody(Engine,EngineModule,mesh,boneName)
	childBones = mesh.getBoneNameChildren(boneName)
	for i in range(0,childBones):
		childBoneName = mesh.getBoneNameChildName(boneName,i)
		createBones(Engine,EngineModule,mesh,childBoneName)

def createBoneBody(Engine,EngineModule,mesh,boneName):
	boneWidth = 2.0
	defaultBoneLength = 5
	boneLength = mesh.getBoneNameSize(boneName)
	if boneLength == 0:
		boneLength = defaultBoneLength
	boneParentName = mesh.getBoneNameParentName(boneName)


	#print("bone: " + str(boneName) + " parent: " + str(boneParentName))
	if boneParentName == "":
		#print("create bone: " + str(boneName) )

		boneBody = Engine.createArticulation()
		boneBody.setName(str(boneName))

		#boneBody.setLocalSize(EngineModule.Vec3(boneLength,boneWidth,boneWidth))
		s = boneBody.addCapsule(EngineModule.Vec3(1,1,1))
		#s = boneBody.addBox(EngineModule.Vec3(1,1,1))
		s.setLocalSize(EngineModule.Vec3(boneLength,boneWidth,boneWidth))
		mesh.setBodyForBoneName(boneName,boneBody)


		boneBody.setOrientation(
			mesh.getBoneNameOrientation(boneName,False)
			* EngineModule.Quat().fromAngles(0,0,90)
			)
		boneBody.setPosition(
			mesh.getBoneNamePosition(boneName)
			+ (boneBody.getOrientation() * EngineModule.Vec3(boneLength,0,0) )
		)
	else:
		#print("create bone: " + str(boneName) + " as child of: " + str(boneParentName) )
		boneParentBody = mesh.getBodyOfBoneName(boneParentName)
		#print("parent body: " + str(boneParentBody))
		if boneParentBody:
			#print("parent has body")
			pass
		else:
			#print("parent has NO body")
			pass
		if not boneParentBody == 0:
			pass

		if not boneParentBody.isArticulation():
			return

		boneBody = boneParentBody.isArticulation().addArticulation()
		boneBody.setName(str(boneName))

		#boneBody.setLocalSize(EngineModule.Vec3(boneLength,boneWidth,boneWidth))
		s = boneBody.addCapsule(EngineModule.Vec3(1,1,1))
		#s = boneBody.addBox(EngineModule.Vec3(1,1,1))
		s.setLocalSize(EngineModule.Vec3(boneLength,boneWidth,boneWidth))
		mesh.setBodyForBoneName(boneName,boneBody)


		boneLocalPosition = mesh.getBoneNameLocalPosition(boneName)
		boneLocalOrientation = mesh.getBoneNameLocalOrientation(boneName)
		scaledBoneLocalPosition = boneLocalPosition * mesh.getMeshScale()
		scaledFlippedBoneLocalPosition = EngineModule.Vec3(scaledBoneLocalPosition.Y(), scaledBoneLocalPosition.X(), scaledBoneLocalPosition.Z())				

		localOrientationAxis = boneLocalOrientation.toAxis()
		localOrientationAngle = boneLocalOrientation.toAngle()

		rotatedOrientationAxis = EngineModule.Quat().fromAngles(0,0,-90) * localOrientationAxis
		rotatedLocalOrientation = EngineModule.Quat().fromAngleAxis(localOrientationAngle,rotatedOrientationAxis)

		parentOrientation = boneParentBody.getOrientation()
		parentPosition = boneParentBody.getPosition()

		parentBoneLength = mesh.getBoneNameSize(boneParentName)
		if parentBoneLength == 0:
			parentBoneLength = defaultBoneLength

		boneBody.setOrientation(parentOrientation * rotatedLocalOrientation)

		"""
		#TODO why is this calculation working
		bonePosition = parentPosition  
		bonePosition -= (parentOrientation * EngineModule.Vec3(parentBoneLength,0,0))
		bonePosition += (parentOrientation * scaledFlippedBoneLocalPosition)
		bonePosition += (boneBody.getOrientation() * EngineModule.Vec3(boneLength,0,0) )
		boneBody.setPosition(bonePosition)   
		"""
		boneBody.setPosition( parentPosition  
			- (parentOrientation * EngineModule.Vec3(parentBoneLength,0,0))
			+ (parentOrientation * scaledFlippedBoneLocalPosition)
			+ (boneBody.getOrientation() * EngineModule.Vec3(boneLength,0,0) )
			)

		#joint = Engine.createJoint(boneParentBody,boneBody)
		globalAnchor = parentPosition
		globalAnchor -= (parentOrientation * EngineModule.Vec3(parentBoneLength,0,0))
		globalAnchor += (parentOrientation * scaledFlippedBoneLocalPosition)

		parentLocalAnchor = boneParentBody.getOrientation().inverse() * (globalAnchor - boneParentBody.getPosition())
		bodyLocalAnchor = boneBody.getOrientation().inverse() * (globalAnchor - boneBody.getPosition())

		boneBody.setParentAnchor(parentLocalAnchor)
		boneBody.setChildAnchor(bodyLocalAnchor)
		boneBody.setParentAnchorOrientation(rotatedLocalOrientation)
		boneBody.setSwingLimits(10,10)
		boneBody.setTwistLimits(0.1,0.2)

		"""
		joint.setAnchor1(parentLocalAnchor)
		joint.setAnchor2(bodyLocalAnchor)
		joint.setAnchor1Orientation(rotatedLocalOrientation)
		#joint.setLimits(1,1)
		joint.setLimits(0,0)
		#joint.setLimits(10,10)
		#joint.setLimits(50,50)
	
		b = Engine.createGuiBox()
		b.setColour(0,0,1,0.2)
		#b.setSize(EngineModule.Vec3(2,4,4))
		b.setSize(EngineModule.Vec3(boneWidth*0.25,boneWidth*2,boneWidth*2))
		b.setScalingFixed()
		joint.addShape(b)
		"""

		#joint.addDebugAxises(1,0.2)
		#mesh.setJointForBoneName(boneName,joint)





		parentChildren = mesh.getBoneNameChildren(boneParentName)
		if parentChildren > 1:
			#boneBody.setSize( boneBody.getSize() * EngineModule.Vec3(0.3,0.6,0.6) )
			boneBody.getShapeByIndex(0).setLocalSize( boneBody.getSize() * EngineModule.Vec3(0.3,0.6,0.6) )




