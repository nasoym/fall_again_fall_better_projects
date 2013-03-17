import engine_scripts.createobjects as create
import engine_scripts.saveload as saveload

def init(Engine,EngineModule,objects):
	print("create spacecage")
	# width height depth
	create.createSpaceCage(Engine,EngineModule,
		EngineModule.Vec3(200,400,300), walls=False,ceilling=False)
	#walls=True,ceilling=True)
	saveload.load(Engine,EngineModule,"../xml/scene.xml",objects)

