"""misc:
	f: add force default y+ 
		x+:1, y+:2, z+:3, x-:4, y-:5, z-:6 
	z: switch material 
		1: set custom material
		2: set material "body"
		3: set final shape
		4: set non final shape
		5: hide non final shapes
		6: show all shapes
	n: set timingfactor 1:*0.9 2:*1.1
	j: set ambient light
	h: set camera fov
	g: set gravity
	i: show object info
"""
import saveload
import bodyjoint
import helpers

def keyDown(Engine,EngineModule,key,selection,objects):
	pass
	if key == EngineModule.Keys.K_F:
		#force = helpers.getModifiedVector(Engine,EngineModule,10000)
		force = helpers.getModifiedVector(Engine,EngineModule,100)
		#force = helpers.getModifiedVector(Engine,EngineModule,10)
		#force = helpers.getModifiedVector(Engine,EngineModule,1)
		for o in selection.get():
			if o.isActor():
				o.isActor().addForce(force)

def keyPressed(Engine,EngineModule,key,selection,objects):

	if key == EngineModule.Keys.K_J:
		ambient = Engine.getAmbientLight()
		factor = helpers.getModifiedVector(Engine,EngineModule,0.05)
		ambient = ambient + factor
		helpers.vecclamp(ambient)
		Engine.setAmbientLight(ambient)
		print("set ambient light to: " + str(ambient))

	if key == EngineModule.Keys.K_H:
		fov = Engine.getCameraFOV()
		if Engine.isKeyDown(EngineModule.Keys.K_1):
			fov += 2
		if Engine.isKeyDown(EngineModule.Keys.K_2):
			fov -= 2
		if fov < 0:
			fov = 0
		if fov > 180:
			fov = 180
		Engine.setCameraFOV(fov)
		print("set FieldOfView to: " + str(fov))

	if key == EngineModule.Keys.K_G:
		gravity = Engine.getGravity()
		factor = helpers.getModifiedVector(Engine,EngineModule,0.5)
		gravity = gravity + factor
		Engine.setGravity(gravity)
		print("set gravity to: " + str(gravity))

	if key == EngineModule.Keys.K_Z:
		print("change material and visibilty")
		#if len(selection.get()) == 1:
		#	o = selection.get()[0]
		if (Engine.isKeyDown(EngineModule.Keys.K_1) or 
			Engine.isKeyDown(EngineModule.Keys.K_2) or
			Engine.isKeyDown(EngineModule.Keys.K_3) or
			Engine.isKeyDown(EngineModule.Keys.K_4)):
			for o in selection.get():
				if o and o.isGuiContainer():
					shapesNumber = o.howManyShapes()
					shapesList = []
					for i in range(0,shapesNumber):
						shape = o.getShapeByIndex(i)
						if Engine.isKeyDown(EngineModule.Keys.K_1):
							shape.setCustomMaterial()
						elif Engine.isKeyDown(EngineModule.Keys.K_2):
							shape.setMaterialName(Engine.getDefaultShadedMaterialName())
						elif Engine.isKeyDown(EngineModule.Keys.K_3):
							shape.setFinalShape()
						elif Engine.isKeyDown(EngineModule.Keys.K_4):
							shape.setNonFinalShape()
				elif o and o.isGuiShape():
					if Engine.isKeyDown(EngineModule.Keys.K_1):
						o.setCustomMaterial()
					elif Engine.isKeyDown(EngineModule.Keys.K_2):
						o.setMaterialName(Engine.getDefaultShadedMaterialName())
					elif Engine.isKeyDown(EngineModule.Keys.K_3):
						o.setFinalShape()
					elif Engine.isKeyDown(EngineModule.Keys.K_4):
						o.setNonFinalShape()

		if Engine.isKeyDown(EngineModule.Keys.K_5) or Engine.isKeyDown(EngineModule.Keys.K_6):
			if Engine.isKeyDown(EngineModule.Keys.K_5):
				objectsNumber = Engine.howManyObjects()
				for i in range(0,objectsNumber):
					o = Engine.getObject(i)
					if o.isGuiShape():
						if not o.isFinalShape():
							o.hide()
			elif Engine.isKeyDown(EngineModule.Keys.K_6):
				objectsNumber = Engine.howManyObjects()
				for i in range(0,objectsNumber):
					o = Engine.getObject(i)
					if o.isGuiShape():
						o.show()

	if key == EngineModule.Keys.K_N:
		if Engine.isKeyDown(EngineModule.Keys.K_1):
			if Engine.isKeyDown(EngineModule.Keys.K_EQUALS):
				Engine.setTimingFactor(Engine.getTimingFactor() * 0.5)
				print("set timingfactor: " +str(Engine.getTimingFactor()))
			else:
				Engine.setTimingFactor(Engine.getTimingFactor() * 0.9)
				print("set timingfactor: " +str(Engine.getTimingFactor()))
		if Engine.isKeyDown(EngineModule.Keys.K_2):
			if Engine.isKeyDown(EngineModule.Keys.K_EQUALS):
				Engine.setTimingFactor(Engine.getTimingFactor() * 2.0)
				print("set timingfactor: " +str(Engine.getTimingFactor()))
			else:
				Engine.setTimingFactor(Engine.getTimingFactor() * 1.1)
				print("set timingfactor: " +str(Engine.getTimingFactor()))

	if key == EngineModule.Keys.K_I:
		print("fps: " + str(float(1000.0 / Engine.getTimeDifference())))
		for o in selection.get():
			print("object: " + str(o))
			print("    name: " + str(o.getName()))
			print("    uuid: " + str(o.readUuid()))
			if o.isActor():
				print("    position: " + str(o.getPosition()))
				print("    size: " + str(o.getSize()))
				print("    orientation: " + str(o.getOrientation().toAngles()))
				print("    mass: " + str(o.getMass()))
			if o.isJoint():
				print("    yLimit: " + str(o.isJoint().getYLimit()))
				print("    zLimit: " + str(o.isJoint().getZLimit()))
				print("    anchor 1: " + str(o.isJoint().getAnchor1()))
				print("    anchor 2: " + str(o.isJoint().getAnchor2()))
				print("    anchor 1 orien: " + str(o.isJoint().getAnchor1Orientation().toAngles()))
				print("    anchor 2 orien: " + str(o.isJoint().getAnchor2Orientation().toAngles()))
				print("    motorOn: " + str(o.isJoint().isMotorOn()))
				print("    motor target: " + str(o.isJoint().getMotorTarget().toAngles()))

		body,joint = bodyjoint.getBodyJoint(selection.get())
		if ((body and joint) and bodyjoint.isBodyJointConnected(body,joint)):
			pass
			jointPos = bodyjoint.getBodyJointAnchorSizePos(body,joint)
			print("body joint size pos: " + str(jointPos))

def keyReleased(Engine,EngineModule,key,selection,objects):
	pass

