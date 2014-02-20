"""temp:
	,:
	.:
	/:
"""
import engine_scripts.createobjects as create
import engine_scripts.helpers as helpers

import datetime

class CallableScript(object):
	def __init__(self,Engine,EngineModule):
		pass
		self.engine = Engine
		self.engineModule = EngineModule
		self.direction = self.engineModule.Vec3(0,1,0)

	def hello(self):
		print("hello from within callable script")

	def guiUpdate(self,me):
		pass

	def setDirection(self,vector):
		self.direction = vector

	def physicUpdate(self,me):
		#print("p"+ str(me))
		pass
		if me.isActor():
			#print("d: " + str(self.direction))
			#relVec = self.engineModule.Vec3(0,1,0)
			relVec = self.direction
			#print("r: " + str(relVec))
			#relvec = self.engineModule.Vec3(self.direction)
			relVec = me.isActor().getOrientation() * relVec
			relVec.normalise()
			relVec = relVec * 10000
			me.isActor().addForce(relVec)


def keyPressed(Engine,EngineModule,key,selection,objects):

	if key == EngineModule.Keys.K_COMMA:
		"""
		o = Engine.createDynamicActor()
		b = o.addBox(EngineModule.Vec3(1,1,1))
		#b = o.addCapsule(EngineModule.Vec3(1,1,1))
		b.setMaterialName(Engine.getDefaultShadedMaterialName())
		b.setScaling1To1()
		o.setPosition(EngineModule.Vec3(0,50,0))
		o.setSize(EngineModule.Vec3(10,30,10))
		"""

		"""
		o.setPythonScriptObjects([])
		b = o.getPythonScriptObjects()
		#Engine.log("orig: " + str(o.getPythonScriptObjects()))
		#Engine.log("b: " + str(o.getPythonScriptObjects()))
		b.append(CallableScript(Engine,EngineModule))
		#Engine.log("orig: " + str(o.getPythonScriptObjects()))
		#Engine.log("b: " + str(o.getPythonScriptObjects()))
		#o.pythonScriptObjectsCallMethod("hello")	
		"""

		"""
		o2 = Engine.createDynamicActor()
		b2 = o2.addBox(EngineModule.Vec3(1,1,1))
		b2.setMaterialName(Engine.getDefaultShadedMaterialName())
		b2.setScaling1To1()
		o2.setPosition(EngineModule.Vec3(0,150,0))
		o2.setSize(EngineModule.Vec3(10,30,10))

		j = Engine.createJoint(o,o2)
		#b = Engine.createGuiBox()
		#b.setColour(0,0,1,0.5)
		#b.setSize(EngineModule.Vec3(2,7,7))
		#b.setScalingFixed()
		#j.addShape(b)
		j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
		j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
		"""

		a = create.createPhysicBoxFinal(Engine,EngineModule)
		b = create.createPhysicBoxFinal(Engine,EngineModule)
		c = create.createPhysicBoxFinal(Engine,EngineModule)
		d = create.createPhysicBoxFinal(Engine,EngineModule)

		a.setSize(EngineModule.Vec3(5,15,5))
		b.setSize(EngineModule.Vec3(5,15,5))
		c.setSize(EngineModule.Vec3(5,15,5))
		d.setSize(EngineModule.Vec3(5,15,5))

		j = Engine.createJoint(a,b)
		j.setAnchor1Size( EngineModule.Vec3(0,1,0) )
		j.setAnchor2Size( EngineModule.Vec3(0,-1,0) )
		j.setLimits(40,40)

		j = Engine.createJoint(b,c)
		j.setAnchor1Size( EngineModule.Vec3(0,1,0) )
		j.setAnchor2Size( EngineModule.Vec3(0,-1,0) )
		j.setLimits(40,40)

		j = Engine.createJoint(c,d)
		j.setAnchor1Size( EngineModule.Vec3(0,1,0) )
		j.setAnchor2Size( EngineModule.Vec3(0,-1,0) )
		j.setLimits(40,40)

		a.setPythonScriptObjects([])
		s = CallableScript(Engine,EngineModule)
		s.setDirection(EngineModule.Vec3(1,0,0))
		a.getPythonScriptObjects().append(s)

		d.setPythonScriptObjects([])
		s = CallableScript(Engine,EngineModule)
		s.setDirection(EngineModule.Vec3(0,0,1))
		d.getPythonScriptObjects().append(s)


	if key == EngineModule.Keys.K_PERIOD:
		pass

	if key == EngineModule.Keys.K_SLASH:
		pass
