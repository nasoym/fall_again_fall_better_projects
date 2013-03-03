import animation_helper
import helpers

def keyPressed(Engine,EngineModule,key,selection,objects):
	bodyAllGroups = ["feet","lleg","uleg","root","belly","breast","neck","head","shoulder","uarm","larm","hand"]

	bodyRightHeadLine = [ "toes-r", "foot-r", "lleg-r", "uleg-r", "root", "belly", "cheast", "breast", "neck", "head"]
	bodyLeftHeadLine = [ "toes-l", "foot-l", "lleg-l", "uleg-l", "root", "belly", "cheast", "breast", "neck", "head"]

	bodyRightHandLine = [ "breast", "shoulder-r", "uarm-r", "larm-r", "hand-r" ]
	bodyLeftHandLine = [ "breast", "shoulder-l", "uarm-l", "larm-l", "hand-l" ]

	bodyRightFingers = [ "thumb-high-r", "finger-index-high-r", "finger-middle-high-r", "finger-ring-high-r", "finger-little-high-r"]
	bodyLeftFingers = ["thumb-high-l", "finger-index-high-l", "finger-middle-high-l", "finger-ring-high-l", "finger-little-high-l"]

	allBodies = animation_helper.getBodyListFromGroupNameList(objects,bodyAllGroups)

	lHandLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftHandLine)
	rHandLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightHandLine)
	lHeadLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftHeadLine)
	rHeadLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightHeadLine)

	lFingers = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftFingers)
	rFingers = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightFingers)

	feet = animation_helper.getBodyListFromGroupNameList(objects,["feet"])
	llegs = animation_helper.getBodyListFromGroupNameList(objects,["lleg"])

	jointGroupNames = [ "foot-joint", "lleg-joint", "uleg-joint", "belly-joint", "breast-joint", "shoulder-joint", "neck-joint", "head-joint", "uarm-joint", "larm-joint", "hand-joint" ]
	joints = animation_helper.getBodyListFromGroupNameList(objects,jointGroupNames)

def lightMasses(Engine,EngineModule,objects):
	bodyAllGroups = ["feet","lleg","uleg","root","belly","breast","neck","head","shoulder","uarm","larm","hand"]
	bodyRightHeadLine = [ "toes-r", "foot-r", "lleg-r", "uleg-r", "root", "belly", "cheast", "breast", "neck", "head"]
	bodyLeftHeadLine = [ "toes-l", "foot-l", "lleg-l", "uleg-l", "root", "belly", "cheast", "breast", "neck", "head"]
	bodyRightHandLine = [ "breast", "shoulder-r", "uarm-r", "larm-r", "hand-r" ]
	bodyLeftHandLine = [ "breast", "shoulder-l", "uarm-l", "larm-l", "hand-l" ]
	bodyRightFingers = [ "thumb-high-r", "finger-index-high-r", "finger-middle-high-r", "finger-ring-high-r", "finger-little-high-r"]
	bodyLeftFingers = ["thumb-high-l", "finger-index-high-l", "finger-middle-high-l", "finger-ring-high-l", "finger-little-high-l"]

	allBodies = animation_helper.getBodyListFromGroupNameList(objects,bodyAllGroups)
	lHandLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftHandLine)
	rHandLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightHandLine)
	lHeadLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftHeadLine)
	rHeadLine = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightHeadLine)

	lFingers = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyLeftFingers)
	rFingers = animation_helper.getBodyListFromNameList(Engine,EngineModule,bodyRightFingers)

	feet = animation_helper.getBodyListFromGroupNameList(objects,["feet"])
	llegs = animation_helper.getBodyListFromGroupNameList(objects,["lleg"])

	animation_helper.resetMasses(allBodies)

	#animation_helper.approachEqualMassDistribution(allBodies,0.9)

	relation = 0.6
	relation = 0.4
	animation_helper.approachRelationToPrev(rHeadLine,relation,1.0)
	animation_helper.approachRelationToPrev(lHeadLine,relation,1.0)
	animation_helper.approachRelationToPrev(rHandLine,relation,1.0)
	animation_helper.approachRelationToPrev(lHandLine,relation,1.0)
	hand_l = helpers.getBodyFromName(Engine,EngineModule,"hand-l")
	if hand_l:
		animation_helper.setMasses(lFingers,hand_l.getMass()*relation)
	hand_r = helpers.getBodyFromName(Engine,EngineModule,"hand-r")
	if hand_r:
		animation_helper.setMasses(rFingers,hand_r.getMass()*relation)

	#animation_helper.approachEqualMassDistribution(allBodies,0.5)

	#animation_helper.approachEqualMassDistribution(feet,0.9)
	#animation_helper.approachEqualMassDistribution(llegs,0.9)
	
	#animation_helper.multiplyMasses(feet,3.0)
	#animation_helper.multiplyMasses(llegs,3.0)

	animation_helper.multiplyMasses(allBodies,0.01)
	#animation_helper.multiplyMasses(allBodies,0.1)


def resetAllMasses(Engine,EngineModule,objects):
	bodyAllGroups = ["feet","lleg","uleg","root","belly","breast","neck","head","shoulder","uarm","larm","hand"]
	allBodies = animation_helper.getBodyListFromGroupNameList(objects,bodyAllGroups)
	animation_helper.resetMasses(allBodies)

def multiplyAllMasses(Engine,EngineModule,objects,factor):
	bodyAllGroups = ["feet","lleg","uleg","root","belly","breast","neck","head","shoulder","uarm","larm","hand"]
	allBodies = animation_helper.getBodyListFromGroupNameList(objects,bodyAllGroups)
	animation_helper.multiplyMasses(allBodies,factor)

