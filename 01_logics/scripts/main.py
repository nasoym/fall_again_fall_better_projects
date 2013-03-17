import engine_scripts.createobjects as create

def init(Engine,EngineModule,objects):
	print("create spacecage")
	create.createSpaceCage(Engine,EngineModule,EngineModule.Vec3(
		100,200,200))
	#	400,300,400))
	# width height depth
	#100,200,300))
	#		200,200,200))


