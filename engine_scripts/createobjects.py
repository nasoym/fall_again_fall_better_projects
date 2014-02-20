
def createJoint(Engine,EngineModule,body1,body2):
	o = Engine.createJoint(body1,body2)
	#b = Engine.createGuiBox()
	#b.setColour(0,0,1,0.5)
	#b.setSize(EngineModule.Vec3(2,7,7))
	#b.setScalingFixed()
	#o.addShape(b)
	return o

def createPhysicBoxFinal(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	#b = o.addCapsule(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createPhysicBoxStructure(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	b.setColour(0,1,0,0.5)
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createPhysicStaticBoxFinal(Engine,EngineModule):
	o = Engine.createStaticActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createPhysicStaticBoxStructure(Engine,EngineModule):
	o = Engine.createStaticActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	b.setColour(0,1,0,0.5)
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createSpaceCage(Engine,EngineModule,size,ground=True,walls=True,ceilling=True):
	wall_thickness = 1.0;
	#ground_opacity = 1.0
	ceiling_opacity = 0.25
	if not ceilling:
		ceiling_opacity = 0.0

	wall_opacity = 0.1
	if not walls:
		wall_opacity = 0.0

	red = 1.0;
	green = 1.0;
	blue = 1.0;

	#bottom
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(0,0,0))
	o.setOrientation(EngineModule.Quat().fromAngles(0,0,90))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.x,size.z))
	shape.setMaterialName(Engine.getDefaultShadedMaterialName())
	#shape.setColour(red,green,blue,ground_opacity)
	if not ground:
		shape.setColour(red,green,blue,0.0)
	shape.turnOffShadows()
	shape.setFinalShape()
	shape.setLocalPosition(EngineModule.Vec3(0,-wall_thickness,0))

	#top
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(0,size.y,0))
	o.setOrientation(EngineModule.Quat().fromAngles(0,0,-90))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.x,size.z))
	shape.setScalingNone()
	shape.setColour(red,green,blue,ceiling_opacity)
	shape.setLocalPosition(EngineModule.Vec3(0,wall_thickness,0))

	#front
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(0,0,size.z))
	o.setOrientation(EngineModule.Quat().fromAngles(0,90,0))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.y*0.5,size.x))
	shape.setScalingNone()
	shape.setColour(red,green,blue,wall_opacity)
	shape.setLocalPosition(EngineModule.Vec3(0,size.y*0.5,wall_thickness))

	#back
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(0,0,-size.z))
	o.setOrientation(EngineModule.Quat().fromAngles(0,-90,0))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.y*0.5,size.x))
	shape.setScalingNone()
	shape.setColour(red,green,blue,wall_opacity)
	shape.setLocalPosition(EngineModule.Vec3(0,size.y*0.5,-wall_thickness))

	#left
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(size.x,0,0))
	o.setOrientation(EngineModule.Quat().fromAngles(0,0,180))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.y*0.5,size.z))
	shape.setScalingNone()
	shape.setColour(red,green,blue,wall_opacity)
	shape.setLocalPosition(EngineModule.Vec3(wall_thickness,size.y*-0.5,0))

	#right
	o = Engine.createStaticActor()
	o.setPosition(EngineModule.Vec3(-size.x,0,0))
	o.setOrientation(EngineModule.Quat().fromAngles(0,0,0))
	o.setUnselectable()
	shape = o.addPlane()
	shape.setLocalSize(EngineModule.Vec3(wall_thickness,size.y*0.5,size.z))
	shape.setScalingNone()
	shape.setColour(red,green,blue,wall_opacity)
	shape.setLocalPosition(EngineModule.Vec3(-wall_thickness,size.y*0.5,0))

