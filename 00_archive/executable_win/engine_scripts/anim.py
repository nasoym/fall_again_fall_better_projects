"""anim:
	[: select set of objects
	]: print all objects
	;: set masses of body parts
		1:set by fixed factor (0.02)
		2:double 3:half
		else:print masses
	space: toggle animation
"""

import random
import helpers
import datetime

import anim_falling
import anim_rising
import animation_helper
import anim_weight

import saveload


def reloadanim():
	reload(anim_falling)
	reload(anim_rising)
	reload(anim_weight)
	reload(animation_helper)

reloadanim()

animLists={}
animLists["falling"] = anim_falling.SimpleAnimation
animLists["lying"] = anim_falling.LyingAnimation
animLists["rising"] = anim_rising.SimpleAnimation

def init(Engine,EngineModule,objects):
	if not "anims" in objects.get():
		objects.get()["anims"] = {}
		objects.setUnsavable("anims")
	random.seed()

	objects.get()["anims"]["stand"] = {"name":"rising","index":0,"starttime":Engine.getTime(),"done":True}
	#Engine.log("set current animation to rising and as done")
	Engine.setGravity(EngineModule.Vec3(0,-10,0))
	Engine.setTimingFactor(2.0)

def guiUpdate(Engine,EngineModule,selection,objects):
	for k,v in objects.get()["anims"].items():
		animName = v["name"]
		if animName in animLists:
			animList = animLists[animName]
			animation_helper.playAnimation(Engine,EngineModule,objects,v,animList)


def keyPressed(Engine,EngineModule,key,selection,objects):

	"""
	if key == EngineModule.Keys.K_LBRACKET:
		pass
		#head_joints = objects.get()["head-joint"]
		#print("head joints: " + str(head_joints))

		#bodies = objects.get()["larm-r"]
		for body in selection.get():
			if body.isActor():
				#body.removeFromScene()
				#body.moveBackToScene()
				body.dissableCollisions()
				#body.enableCollisions()
				"""


	if key == EngineModule.Keys.K_SPACE:
		if not "head" in objects.get():
			return
		Engine.log("space: pressed")
		if objects.get()["anims"]["stand"]["done"]:
			if objects.get()["anims"]["stand"]["name"] == "rising":
				objects.get()["anims"]["stand"] = {
					"name":"falling","index":0,"starttime":Engine.getTime(),"done":False}
				animation_helper.findMiddlePos(Engine,EngineModule,objects)
		else:
			pass
			#Engine.log("current animation is not yet done")

def keyReleased(Engine,EngineModule,key,selection,objects):

	if key == EngineModule.Keys.K_SPACE:
		if not "head" in objects.get():
			return

		Engine.log("space: released")
		if objects.get()["anims"]["stand"]["done"]:
			if ((objects.get()["anims"]["stand"]["name"] == "falling") or 
				(objects.get()["anims"]["stand"]["name"] == "lying")
			):
				objects.get()["anims"]["stand"] = {
					"name":"rising","index":0,"starttime":Engine.getTime(),"done":False}

		else:
			Engine.log("current animation not yet done")
			objects.get()["anims"]["stand"]["ondone"] = True


