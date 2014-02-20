"""temp:
	,:
	.:
	/:
"""
import random
import datetime

import engine_scripts.createobjects as create
import engine_scripts.helpers as helpers
import engine_scripts.saveload as saveload

import pyscript_00.ragdoll as ragdoll

class CallableScript(object):
	def __init__(self,Engine,EngineModule):
		pass
		self.engine = Engine
		self.engineModule = EngineModule
		self.target = None
		self.strength = 1

	def guiUpdate(self,me):
		pass

	def setTarget(self,target):
		self.target = target

	def setStrength(self,strength):
		self.strength = strength

	def physicUpdate(self,me):
		if (me.isActor() and self.target and self.target.isActor()):
			vecToTarget = self.target.isActor().getPosition()
			vecToTarget = vecToTarget - me.isActor().getPosition()

			length = vecToTarget.length()
			vecToTarget.normalise()
			if length > 40:
				#factor = self.strength - length
				factor = self.strength
				#if factor <= 1:
					#factor = 1
			else:
				factor = self.strength
				factor = factor * (length/20) * (length/20)

			vecToTarget = vecToTarget * factor
			me.isActor().addForce(vecToTarget)


def createPhysicBox(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	#b.setColour(1,1,0,1)
	o.setPosition(EngineModule.Vec3(0,150,0))
	return o

def keyDown(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_M:
		a = createPhysicBox(Engine,EngineModule)
		#a.setSize(EngineModule.Vec3(5,5,5))
		#a.setSize(EngineModule.Vec3(1,1,1))
		#a.setSize(EngineModule.Vec3(3,3,3))
		a.setSize(EngineModule.Vec3(2,3,2))
		#a.setMass(a.getMass() * 0.01)
		a.setMass(a.getMass() * 0.1)
		a.setPosition(EngineModule.Vec3(
			random.uniform(-100,100),
			random.uniform(0,100),
			random.uniform(-100,100)
			))

		#a.setPythonScriptObjects([])
		#s = CallableScript(Engine,EngineModule)
		#head = objects.get()["head"][0]
		#s.setTarget(head)
		##s.setStrength(10)
		#s.setStrength(0.02)
		##s.setStrength(1)
		#a.getPythonScriptObjects().append(s)

def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		sel = selection.get()[:]
		selection.clear()
		while len(sel)>0:
			o = sel.pop()
			body = None
			if o.isActor():
				body = o
				a = createPhysicBox(Engine,EngineModule)
				a.setSize(body.getSize() * 0.8)
				a.setMass(a.getMass() * 0.01)
				selection.add(a)
				j = Engine.createJoint(body,a)
				j.setAnchor1Size( EngineModule.Vec3(0,-1,0) )
				j.setAnchor2Size( EngineModule.Vec3(0,1,0) )
				#j.setAnchor2Orientation( EngineModule.Quat().fromAngles(0,1,-90) )
				j.setLimits(0,60)


	if key == EngineModule.Keys.K_PERIOD:
		sel = selection.get()[:]
		selection.clear()
		while len(sel)>0:
			o = sel.pop()
			body = None
			if o.isActor():
				body = o
				a = createPhysicBox(Engine,EngineModule)
				a.setSize(body.getSize() * 0.8)
				a.setMass(a.getMass() * 0.01)
				selection.add(a)
				j = Engine.createJoint(body,a)
				j.setAnchor1Size( EngineModule.Vec3(0,1,0) )
				j.setAnchor2Size( EngineModule.Vec3(0,-1,0) )
				j.setLimits(00,60)
	if key == EngineModule.Keys.K_SEMICOLON:
		pass
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=2.5,
			#pos=EngineModule.Vec3(0,150,0),
			pos=EngineModule.Vec3(50,50,-50),
			#base=True
			base=False
			)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)

	if key == EngineModule.Keys.K_APOSTROPHE:
		pass
		head = objects.get()["breast"][0]
		objectsNumber = Engine.howManyObjects()
		for i in range(0,objectsNumber):
			o = Engine.getObject(i)
			if o.isActor():
				vecToTarget = head.getPosition()
				vecToTarget = vecToTarget - o.getPosition()
				#length = vecToTarget.length()
				vecToTarget.normalise()
				factor = 40
				#if length > 40:
				#	factor = self.strength
				#else:
				#	factor = self.strength
				#	factor = factor * (length/20) * (length/20)

				vecToTarget = vecToTarget * factor
				o.addForce(vecToTarget)


	if key == EngineModule.Keys.K_BACKSLASH:
		pass
		#Engine.setGravity(EngineModule.Vec3(0,0,0))
		#Engine.log("set gravity")
		objectsNumber = Engine.howManyObjects()
		for i in range(0,objectsNumber):
			o = Engine.getObject(i)
			if o.isActor():
				#Engine.log("o: " + str(o))
				#o.wakeUp()
				#o.addForce(EngineModule.Vec3(0,26,0))
				o.addForce(EngineModule.Vec3(0,
					o.getMass() * 30,0))

	if key == EngineModule.Keys.K_SLASH:
		pass
		#Engine.setTimingFactor(7.0)
		#Engine.setTimingFactor(3.0)
		#Engine.setTimingFactor(10.0)
		#Engine.log("time:" + str(Engine.getTimingFactor()))

		Engine.setGravity(EngineModule.Vec3(0,-5,0))
		Engine.setGravity(EngineModule.Vec3(0,15,0))
		Engine.setGravity(EngineModule.Vec3(0,-5,0))
		Engine.setGravity(EngineModule.Vec3(0,-2,0))
		Engine.setGravity(EngineModule.Vec3(1,-1,0))
		Engine.setGravity(EngineModule.Vec3(0,-10,0))
		Engine.setGravity(EngineModule.Vec3(0,3,0))
		Engine.setGravity(EngineModule.Vec3(0,15,0))
		Engine.setGravity(EngineModule.Vec3(0,0,0))
		Engine.log("set gravity")

		objectsNumber = Engine.howManyObjects()
		for i in range(0,objectsNumber):
			o = Engine.getObject(i)
			if o.isActor():
				o.wakeUp()

		#random.uniform(0,100)
		#random.uniform(0,100)
		#random.uniform(0,100)
		#Engine.log("head: " + str(objects.get()["head"]))
		#head = objects.get()["head"][0]
		#Engine.log("head: " + str(head.getName()))
		#Engine.log("head: " + str(head.readUuid()))


		
		"""
		joints = objects.get()["uarm-joint"]
		Engine.log("joints: " + str(joints))
		for joint in joints:
			Engine.log("joint: " + str(joint))
			motorTarget = joint.getMotorTarget().toAngles()
			Engine.log("target: " + str(motorTarget))
			newQuat = EngineModule.Quat().fromAngles(
				motorTarget.x,
				motorTarget.y - 2.0,
				motorTarget.z
				)
			joint.setMotorTarget(newQuat)
			"""




