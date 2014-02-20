import pyscript_00.animation_helper as animation_helper
import pyscript_00.anim_weight as anim_weight

#angularForce = False
angularForce = True

SimpleAnimation = [
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
	'start-groups':[(lambda Engine,EngineModule,objects,groupPart:
		groupPart.setMotorValues( (10**35)*1.5 , (10**35)*1.0 ,angularForce))],
	'start':[
			(lambda Engine,EngineModule,objects,timePos:
			anim_weight.lightMasses(Engine,EngineModule,objects)),

			(lambda Engine,EngineModule,objects,timePos:
			animation_helper.dissableCollisions(Engine,EngineModule,objects,
				["head", "uarm", "larm", "hand", "breast", "belly", "root", "uleg"]
				)
			),

			(lambda Engine,EngineModule,objects,timePos:
			Engine.setGravity(EngineModule.Vec3(0,-10,0))),

			(lambda Engine,EngineModule,objects,timePos:
			animation_helper.setRandomTarget(Engine,EngineModule,objects,["head-joint"],
				0,0, 0,10, -10,10)
			),

		],
	'end':[(lambda Engine,EngineModule,objects,timePos:
			animation_helper.enableCollisions(Engine,EngineModule,objects,
				["head", "uarm", "larm", "hand", "breast", "belly", "root", "uleg"]
				)
			)
		],
	'timePos':[(lambda Engine,EngineModule,objects,timePos:
		animation_helper.setTiming(Engine,EngineModule,objects,
			timePos,0.1,5.0)
		)],
	}
]

