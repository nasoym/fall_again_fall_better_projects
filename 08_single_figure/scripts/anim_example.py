import pyscript_00.animation_module2 as animation_helper

def resetAnimation(Engine,EngineModule,objects,animData):
	animData["done"] = False
	animData["index"] = 0
	animData['starttime'] = Engine.getTime() + 1000
	#objects.get()["anims"]["stand"] = {"name":"lying","index":0,"starttime":Engine.getTime(),"done":True}

ExampleAnimation = [
	{ 
		'time':1000, #sets the length of this animation module
		#'timePos':[ (lambda Engine,EngineModule,objects,timePos: animation_helper.setTiming(Engine,EngineModule,objects, timePos,1.0,0.3)) ]
		#'timePos':[ (lambda Engine,EngineModule,objects,timePos: print("timePos:" + timePos)) ]
		'timePos':[ 
			#(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("timePos:" + str(timePos)) ) 
			],
			#setTiming sets the Engine timing factor
			#timePos will be called for each frame with the current timePos (0..1)
		'start':[ 
			(lambda Engine,EngineModule,objects,animData,timePos: 
				Engine.log("playAnimation:" + str(animData))
				),
			],

	},
	{
		'time':500, 
			#sets the length of this animation part
		'start':[ 
			(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("start:"+str(timePos))),
			(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("start2:"+str(timePos))),
			],
			#all lambdas will be called at start
		'end':[
			(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("end:"+str(timePos))),
			(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("end2:"+str(timePos))),
			(lambda Engine,EngineModule,objects,animData,timePos: 
				Engine.log("playAnimation:" + str(animData))
				),
			],
			#all lambdas will be called at end

		'timePos':[ 
			#(lambda Engine,EngineModule,objects,animData,timePos: Engine.log("timePos:" + str(timePos)) ) 
			],
			#all lambdas will be called for each frame with the current timePos (0..1)
		'start-groups':[(lambda Engine,EngineModule,objects,animData,groupPart:
			Engine.log("part:" + str(groupPart))
			)],
			#will be called for each part in group list at start
		'end-groups':[(lambda Engine,EngineModule,objects,animData,groupPart:
			Engine.log("part:" + str(groupPart))
			)],
			#will be called for each part in group list at end
		'groups':[
			"neck-joint",
			"head-joint",
			"uarm-joint",
			"larm-joint",
			"hand-joint",
			],
			#defines the groups which will be used for start/end-groups
		'ondone':[
			(lambda Engine,EngineModule,objects,animData,timePos: 
				resetAnimation(Engine,EngineModule,objects,animData)
				),
			],
	}
]
