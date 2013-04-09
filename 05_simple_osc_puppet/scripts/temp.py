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

def createPhysicBox(Engine,EngineModule):
	o = Engine.createDynamicActor()
	b = o.addBox(EngineModule.Vec3(1,1,1))
	b.setMaterialName(Engine.getDefaultShadedMaterialName())
	b.setScaling1To1()
	o.setPosition(EngineModule.Vec3(0,150,0))
	o.setSize(EngineModule.Vec3(5,5,5))
	o.setMass(o.getMass() * 0.01)
	return o

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

	if key == EngineModule.Keys.K_SLASH:

		joints = objects.get()["uarm-joint"]
		Engine.log("joints: " + str(joints))
		for joint in joints:
			Engine.log("joint: " + str(joint))
			motorTarget = joint.getMotorTarget().toAngles()
			Engine.log("target: " + str(motorTarget))
			newQuat = EngineModule.Quat().fromAngles(
				motorTarget.x,
				motorTarget.y - 5.0,
				motorTarget.z
				)
			joint.setMotorTarget(newQuat)

		print("save to xml")
		saveload.save(Engine,EngineModule,"../xml/scene.xml",objects)
		print("done")



