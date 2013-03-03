"""temp:
	,:
	.:
	/:
"""
import engine_scripts.createobjects as create
import engine_scripts.helpers as helpers

import random
import datetime

import pyscript_00.ragdoll as ragdoll

class CallableScript(object):
	def __init__(self,Engine,EngineModule):
		pass
		self.engine = Engine
		self.engineModule = EngineModule
		self.direction = self.engineModule.Vec3(0,1,0)
		self.target = None
		self.strength = 1

	def hello(self):
		print("hello from within callable script")

	def guiUpdate(self,me):
		pass

	def setDirection(self,vector):
		self.direction = vector

	def setTarget(self,target):
		self.target = target

	def setStrength(self,strength):
		self.strength = strength

	def physicUpdate(self,me):
		if (me.isActor() and self.target and self.target.isActor()):
			vecToTarget = self.target.isActor().getPosition()
			vecToTarget = vecToTarget - me.isActor().getPosition()

			#vecToTarget.normalise()
			#vecToTarget = vecToTarget * 10000
			#vecToTarget = vecToTarget * self.strength

			length = vecToTarget.length()
			vecToTarget.normalise()
			factor = self.strength - length
			if factor <= 1:
				factor = 1
			vecToTarget = vecToTarget * factor

			me.isActor().addForce(vecToTarget)

def createPhysicBox(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	#b = o.addCapsule(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createPhysicSphere(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addSphere(EngineModule.Vec3(1,1,1))
	#b = o.addCapsule(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

def createPhysicCapsule(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addCapsule(EngineModule.Vec3(1,1,1))
	#b = o.addCapsule(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(10,10,10))
	return o

	#addBox
	#addSphere
	#addCapsule
	#addPlane

def createChain(Engine,EngineModule):
	a = createPhysicCapsule(Engine,EngineModule)
	b = createPhysicCapsule(Engine,EngineModule)
	c = createPhysicCapsule(Engine,EngineModule)
	d = createPhysicCapsule(Engine,EngineModule)

	a.setSize(EngineModule.Vec3(10,3,3))
	b.setSize(EngineModule.Vec3(10,3,3))
	c.setSize(EngineModule.Vec3(10,3,3))
	d.setSize(EngineModule.Vec3(10,3,3))

	a.setMass(a.getMass() * 0.01)
	b.setMass(b.getMass() * 0.01)
	c.setMass(c.getMass() * 0.01)
	d.setMass(d.getMass() * 0.01)

	a.setPosition(EngineModule.Vec3( random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)))
	b.setPosition(EngineModule.Vec3( random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)))
	c.setPosition(EngineModule.Vec3( random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)))
	d.setPosition(EngineModule.Vec3( random.uniform(0,100), random.uniform(0,100), random.uniform(0,100)))

	j = Engine.createJoint(a,b)
	j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
	j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
	j.setLimits(70,70)

	j = Engine.createJoint(b,c)
	j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
	j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
	j.setLimits(70,70)

	j = Engine.createJoint(c,d)
	j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
	j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
	j.setLimits(70,70)

	return a

def createFollowingGroup(Engine,EngineModule,key,selection,objects):
	#a = createPhysicBox(Engine,EngineModule)
	#a = createPhysicSphere(Engine,EngineModule)
	a = createPhysicCapsule(Engine,EngineModule)
	a.setSize(EngineModule.Vec3(15,5,5))
	a.setMass(a.getMass() * 0.01)
	a.setPosition(EngineModule.Vec3(
		random.uniform(0,100),
		random.uniform(0,100),
		random.uniform(0,100)
		))

	for i in range(0,15):
		#b = createPhysicBox(Engine,EngineModule)
		#b = createPhysicSphereFinal(Engine,EngineModule)
		b = createChain(Engine,EngineModule)
		"""
		b = createPhysicCapsule(Engine,EngineModule)
		b.setSize(EngineModule.Vec3(15,5,5))
		b.setMass(b.getMass() * 0.01)
		b.setPosition(EngineModule.Vec3(
			random.uniform(0,100),
			random.uniform(0,100),
			random.uniform(0,100)
			))
			"""

		b.setPythonScriptObjects([])
		s = CallableScript(Engine,EngineModule)
		s.setTarget(a)
		s.setStrength(2.0)
		s.setStrength(0.1)
		s.setStrength(0.5)
		s.setStrength(0.01)
		s.setStrength(100.0)
		b.getPythonScriptObjects().append(s)

		a = b

def createMainTarget(Engine,EngineModule,key,selection,objects):
	a = createPhysicSphere(Engine,EngineModule)
	#a.setSize(EngineModule.Vec3(5,5,5))
	a.setSize(EngineModule.Vec3(15,15,15))
	a.setMass(a.getMass() * 0.0001)

	shapesNumber = a.howManyShapes()
	shapesList = []
	for i in range(0,shapesNumber):
		shape = a.getShapeByIndex(i)
		shape.setColour(0,0,1,1)

	objects.get()["main_target"] = a

def createMainTargetFollower(Engine,EngineModule,key,selection,objects):
	if "main_target" in objects.get():
		main_target = objects.get()["main_target"]
		if main_target:
			#b = createPhysicBox(Engine,EngineModule)
			#b = createPhysicSphere(Engine,EngineModule)
			b = createPhysicCapsule(Engine,EngineModule)
			b.setSize(EngineModule.Vec3(5,2,2))
			#b.setSize(EngineModule.Vec3(5,5,5))
			#b.setSize(EngineModule.Vec3(0.5,0.5,35))
			#b.setSize(EngineModule.Vec3(1.0,1.0,5))
			b.setMass(b.getMass() * 0.001)

			b.setPythonScriptObjects([])
			s = CallableScript(Engine,EngineModule)
			s.setTarget(main_target)
			#s.setStrength(1)
			s.setStrength(0.01)
			s.setStrength(1.0)
			s.setStrength(10.0)
			b.getPythonScriptObjects().append(s)
	else:
		print("no main_target")

def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		print("create ragdoll")
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=5,
			pos=EngineModule.Vec3(0,150,0),
			base=False)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)
		pass

		#createFollowingGroup(Engine,EngineModule,key,selection,objects)
		#createMainTarget(Engine,EngineModule,key,selection,objects)

	if key == EngineModule.Keys.K_PERIOD:
		pass
		createMainTargetFollower(Engine,EngineModule,key,selection,objects)

	if key == EngineModule.Keys.K_SLASH:
		if "main_target" in objects.get():
			main_target = objects.get()["main_target"]
			if main_target:
				main_target.addForce(EngineModule.Vec3(
					random.uniform(-1000,1000),
					random.uniform(-1000,1000),
					random.uniform(-1000,1000)
					))


