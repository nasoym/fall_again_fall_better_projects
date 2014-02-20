import pyscript_00.animation_helper as animation_helper
import pyscript_00.anim_weight as anim_weight

angularForce = True

RisingAnimation = [
	{'groups':[
		"foot-joint",
		"lleg-joint",
		"uleg-joint",
		"belly-joint",
		"breast-joint",
		"neck-joint",
		"head-joint",
		"shoulder-joint",
		"uarm-joint",
		"larm-joint",
		"hand-joint"
		],
	'time':1000,
	'start-groups':[(lambda Engine,EngineModule,objects,animData,groupPart:
		groupPart.setMotorValues( (10**35)*1.5 , (10**35)*1.0 ,angularForce))],
	'start':[
			(lambda Engine,EngineModule,objects,animData,timePos:
			anim_weight.lightMasses(Engine,EngineModule,objects)),

			(lambda Engine,EngineModule,objects,animData,timePos:
			Engine.setGravity(EngineModule.Vec3(0,-10,0))),

			(lambda Engine,EngineModule,objects,animData,timePos:
			animation_helper.setRandomTarget(Engine,EngineModule,objects,["head-joint"],
				0,0, 0,10, -10,10)
			),

		],
	'timePos':[(lambda Engine,EngineModule,objects,animData,timePos:
		animation_helper.setTiming(Engine,EngineModule,objects,
			timePos,0.1,5.0)
		)],
	}
]

RisingAnimationDefault = [
	{'groups':[
		"foot-joint",
		"lleg-joint",
		"uleg-joint",
		"belly-joint",
		"breast-joint",
		"neck-joint",
		"head-joint",
		"shoulder-joint",
		"uarm-joint",
		"larm-joint",
		"hand-joint"
		],
	'time':1000,
	'start-groups':[(lambda Engine,EngineModule,objects,animData,groupPart:
		groupPart.setMotorValues( (10**35)*1.5 , (10**35)*1.0 ,angularForce))],
	'start':[
			(lambda Engine,EngineModule,objects,animData,timePos:
			anim_weight.lightMasses(Engine,EngineModule,objects)),

			(lambda Engine,EngineModule,objects,animData,timePos:
			Engine.setGravity(EngineModule.Vec3(0,-10,0))),

			(lambda Engine,EngineModule,objects,animData,timePos:
			animation_helper.setRandomTarget(Engine,EngineModule,objects,["head-joint"],
				0,0, 0,10, -10,10)
			),

		],
	}
]



