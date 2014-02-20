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


def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		print("create ragdoll")
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=5,
			pos=EngineModule.Vec3(0,0,0),
			#base=True
			base=False
			)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)
		pass

	if key == EngineModule.Keys.K_PERIOD:
		pass
		print("saving to scene")
		#saveload.load(Engine,EngineModule,"../xml/ragdoll.xml",objects)
		#saveload.save(Engine,EngineModule,"../xml/scene.xml",objects)

	if key == EngineModule.Keys.K_SLASH:
		pass
		Engine.log("settings")
		Engine.setTimingFactor(7.0)
		Engine.setTimingFactor(3.0)
		Engine.setGravity(EngineModule.Vec3(0,-10,0))

