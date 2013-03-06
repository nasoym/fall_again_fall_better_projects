import engine_scripts.createobjects as create

def init(Engine,EngineModule,objects):
	print("create spacecage")
	# width height depth
	create.createSpaceCage(Engine,EngineModule,EngineModule.Vec3(
		200,400,300),walls=False,ceilling=False)

