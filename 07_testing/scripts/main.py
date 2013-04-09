import engine_scripts.createobjects as create

def init(Engine,EngineModule,objects):
	pass
	#print("create spacecage")
	#create.createSpaceCage(Engine,EngineModule,
		#EngineModule.Vec3(100,200,200))
	create.createSpaceCage(Engine,EngineModule,
		EngineModule.Vec3(600,600,600),ground=False,walls=False,ceilling=False)


