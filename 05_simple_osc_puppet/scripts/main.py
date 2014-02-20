import engine_scripts.createobjects as create
import engine_scripts.saveload as saveload
import engine_scripts.helpers as helpers

def init(Engine,EngineModule,objects):
	pass
	# width height depth
	create.createSpaceCage(Engine,EngineModule,EngineModule.Vec3(
		100,130,100),walls=False,ceilling=False)
	#saveload.load(Engine,EngineModule,"../xml/ragdoll.xml",objects)
	saveload.load(Engine,EngineModule,"../xml/scene.xml",objects)
	Engine.setTimingFactor(10.0)
	Engine.setGravity(EngineModule.Vec3(0,-10,0))
	helpers.hideNonFinal(Engine,EngineModule)

