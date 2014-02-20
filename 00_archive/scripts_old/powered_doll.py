"""
powered_doll:
	v: create new powered ragdoll
	space: power on/off
"""

import ragdoll

def createMainRagdoll(Engine,EngineModule):
	doll = ragdoll.createHumanBodyParts(Engine,EngineModule,size=5)
	ragdoll.createHumanJoints(Engine,EngineModule,doll)
	ragdoll.createLimits(Engine,EngineModule,doll,45)
	ragdoll.createLimitsHuman(Engine,EngineModule,doll)
	return doll

def init(Engine,EngineModule,objects):
	objects.append("powered_dolls",[])
	pass

def keyDown(Engine,EngineModule,key,selection,objects):
	pass

def keyPressed(Engine,EngineModule,key,selection,objects):
	pass
	if key == EngineModule.Keys.K_V:
		print("key3 powered dolls")
		dolls = objects.get()["powered_dolls"]
		for d in dolls:
			for k in d.parts.keys():
				if k != "base":
					d.parts[k].setPosition(EngineModule.Vec3(0,250,0))

		if len(dolls) == 0:
			dolls.append(createMainRagdoll(Engine,EngineModule))

		elif len(dolls) == 1:
			distance = 150

			doll = ragdoll.createHumanBodyParts(Engine,
				EngineModule,size=5,
				pos=EngineModule.Vec3(distance,5,distance),
				base=True)
			ragdoll.createHumanJoints(Engine,EngineModule,doll)
			ragdoll.createLimits(Engine,EngineModule,doll,45)
			ragdoll.createLimitsHuman(Engine,EngineModule,doll)
			dolls.append(doll)

			doll = ragdoll.createHumanBodyParts(Engine,
				EngineModule,size=5,
				pos=EngineModule.Vec3(distance,5,0),
				base=True)
			ragdoll.createHumanJoints(Engine,EngineModule,doll)
			ragdoll.createLimits(Engine,EngineModule,doll,45)
			ragdoll.createLimitsHuman(Engine,EngineModule,doll)
			dolls.append(doll)

			doll = ragdoll.createHumanBodyParts(Engine,
				EngineModule,size=5,
				pos=EngineModule.Vec3(0,5,distance),
				base=True)
			ragdoll.createHumanJoints(Engine,EngineModule,doll)
			ragdoll.createLimits(Engine,EngineModule,doll,45)
			ragdoll.createLimitsHuman(Engine,EngineModule,doll)
			dolls.append(doll)

	if key == EngineModule.Keys.K_SPACE:
		dolls = objects.get()["powered_dolls"]
		for doll in dolls:
			if doll.powered:
				Engine.setTimingFactor(0.55)
				ragdoll.driveJointsOff(doll)
			else:
				Engine.setTimingFactor(2.0)
				ragdoll.driveJoints(doll)

def keyReleased(Engine,EngineModule,key,selection,objects):
	pass


