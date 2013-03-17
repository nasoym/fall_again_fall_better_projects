"""anim:
"""

import anim_example

import pyscript_00.animation_module2 as animation_helper

import engine_scripts.saveload as saveload

def reloadanim():
	reload(anim_example)
	reload(animation_helper)

reloadanim()

animLists={}
animLists["example"] = anim_example.ExampleAnimation

def init(Engine,EngineModule,objects):
	if not "anims" in objects.get():
		objects.get()["anims"] = {}
		objects.setUnsavable("anims")
	#objects.get()["anims"]["example"] = { "name":"example", "starttime":Engine.getTime(), "done":False }

	#objects.get()["anims"]["stand"] = {"name":"rising","index":0,"starttime":Engine.getTime(),"done":True}
		#Engine.log("set current animation to rising and as done")

def guiUpdate(Engine,EngineModule,selection,objects):
	global animLists
	for k,v in objects.get()["anims"].items():
		animName = v["name"]
		if animName in animLists:
			animList = animLists[animName]
			animation_helper.playAnimation(Engine,EngineModule,objects,v,animList)

"""
def keyPressed(Engine,EngineModule,key,selection,objects):
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
"""
