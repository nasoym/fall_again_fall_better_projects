"""temp:
	,:
	.:
	/:
"""
import engine_scripts.createobjects as create
import engine_scripts.helpers as helpers
import engine_scripts.saveload as saveload

import random
import datetime

import pyscript_00.ragdoll as ragdoll

def keyPressed(Engine,EngineModule,key,selection,objects):
	if key == EngineModule.Keys.K_COMMA:
		pass
		print("save to xml")
		saveload.save(Engine,EngineModule,"../xml/test.xml",objects)
		print("done")

	if key == EngineModule.Keys.K_PERIOD:
		pass
		print("load from xml")
		saveload.load(Engine,EngineModule,"../xml/test.xml",objects)
		print("done")

	if key == EngineModule.Keys.K_SLASH:
		pass
		print("create ragdoll")
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=5,
			pos=EngineModule.Vec3(0,0,0),
			base=False
			)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)

		
