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
		"""
		print("create ragdoll")
		char = ragdoll.createHumanBodyParts(Engine,
			EngineModule,size=5,
			pos=EngineModule.Vec3(0,0,0),
			base=True
			)
		ragdoll.createHumanJoints(Engine,EngineModule,char)
		ragdoll.createLimits(Engine,EngineModule,char,45)
		ragdoll.createLimitsHuman(Engine,EngineModule,char)
		"""
		pass
		#saveload.load(Engine,EngineModule,"../xml/scene.xml",objects)

	if key == EngineModule.Keys.K_PERIOD:
		pass
		print("load ragdoll.xml")
		"""
		loadingPos = EngineModule.Vec3(250,0,0)
		loadingOrientation = EngineModule.Quat()
		#saveload.load(Engine,EngineModule,"../xml/positions.xml",objects,
		saveload.load(Engine,EngineModule,"../xml/ragdoll.xml",objects,
			loadingPos,loadingOrientation)
			"""

		positions = [
			[EngineModule.Vec3(21.966772079,0.000000000,-66.426025391),
			EngineModule.Quat(-0.722364545,0.000000000,0.691513181,0.000000000)],
			[EngineModule.Vec3(0.000000000,0.000000000,117.283714294),
			EngineModule.Quat(-0.000000163,0.000000000,1.000000000,0.000000000)],
			[EngineModule.Vec3(60.000000000,-0.500000000,57.283725739),
			EngineModule.Quat(-0.500000238,0.000000000,0.866025448,0.000000000)],
			[EngineModule.Vec3(40.076103210,0.000000000,-4.459388256),
			EngineModule.Quat(0.043619223,0.000000000,0.999048233,0.000000000)],
			[EngineModule.Vec3(-92.474678040,0.000000000,-33.463573456),
			EngineModule.Quat(0.300705731,0.000000000,0.953717172,0.000000000)],
			[EngineModule.Vec3(100.000000000,0.000000000,-42.716278076),
			EngineModule.Quat(-0.500000238,0.000000000,0.866025448,0.000000000)],
			[EngineModule.Vec3(-98.567276001,0.000000000,103.246383667),
			EngineModule.Quat(0.258819014,0.000000000,0.965926230,0.000000000)],
			[EngineModule.Vec3(-20.000000000,-0.500000000,17.283725739),
			EngineModule.Quat(0.382683426,0.000000000,0.923879743,0.000000000)],
			[EngineModule.Vec3(120.000000000,0.000000000,57.283725739),
			EngineModule.Quat(-0.300705999,0.000000000,0.953716993,0.000000000)],
#			[EngineModule.Vec3(-150.000000000,0.000000000,57.283725739),
#			EngineModule.Quat(0.991445363,0.000000000,-0.130526170,0.000000000)],
#			[EngineModule.Vec3(-80.000000000,0.000000000,37.283725739),
#			EngineModule.Quat(0.793353796,0.000000000,-0.608761668,0.000000000)],
			[EngineModule.Vec3(-4.641016006,0.000000000,-40.036834717),
			EngineModule.Quat(0.866025627,0.000000000,0.500000238,0.000000000)]]

		for pos in positions:
			loadingPos = pos[0]
			loadingOrientation = pos[1]
			saveload.load(Engine,EngineModule,"../xml/ragdoll.xml",objects,
				loadingPos,loadingOrientation)

	if key == EngineModule.Keys.K_SLASH:
		pass


