"""anim:
"""

import anim_example
import anim_falling
import anim_rising

import pyscript_00.animation_module2 as animation_helper
import pyscript_00.animation_helper as animation_helper_old

import engine_scripts.saveload as saveload

def reloadanim():
	reload(anim_example)
	reload(animation_helper)
	reload(anim_falling)
	reload(anim_rising)

reloadanim()

animLists={}
animLists["example"] = anim_example.ExampleAnimation
animLists["falling"] = anim_falling.FallingAnimation
animLists["lying"] = anim_falling.LyingAnimation
animLists["rising"] = anim_rising.RisingAnimation

animLists["falling_default"] = anim_falling.FallingAnimationDefault
animLists["lying_default"] = anim_falling.LyingAnimationDefault
animLists["rising_default"] = anim_rising.RisingAnimationDefault

def init(Engine,EngineModule,objects):
	if not "anims" in objects.get():
		objects.get()["anims"] = {}
		objects.setUnsavable("anims")
	#objects.get()["anims"]["example"] = { "name":"example", "starttime":Engine.getTime(), "done":False }

	objects.get()["anims"]["stand"] = {"name":"rising","index":0,"starttime":Engine.getTime(),"done":True}

	Engine.setGravity(EngineModule.Vec3(0,-10,0))
	Engine.setTimingFactor(2.0)
	animation_helper_old.findMiddlePos(Engine,EngineModule,objects)

def guiUpdate(Engine,EngineModule,selection,objects):
	global animLists
	for k,v in objects.get()["anims"].items():
		animName = v["name"]
		if animName in animLists:
			animList = animLists[animName]
			animation_helper.playAnimation(Engine,EngineModule,objects,v,animList)

def keyPressed(Engine,EngineModule,key,selection,objects):
	if not "head" in objects.get():
		return

	if key == EngineModule.Keys.K_SPACE:
		objects.get()["anims"]["stand"] = { "name":"falling","index":0,"starttime":Engine.getTime(),"done":False}
		#	animation_helper_old.findMiddlePos(Engine,EngineModule,objects)

	if key == EngineModule.Keys.K_B:
		objects.get()["anims"]["stand"] = { "name":"falling_default","index":0,"starttime":Engine.getTime(),"done":False}

def keyReleased(Engine,EngineModule,key,selection,objects):
	if not "head" in objects.get():
		return
	if key == EngineModule.Keys.K_SPACE:
		objects.get()["anims"]["stand"] = { "name":"rising","index":0,"starttime":Engine.getTime(),"done":False}
	if key == EngineModule.Keys.K_B:
		objects.get()["anims"]["stand"] = { "name":"rising_default","index":0,"starttime":Engine.getTime(),"done":False}

