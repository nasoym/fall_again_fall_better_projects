"""temp:
	,:
	.:
	/:
"""
import createobjects as create
import helpers
import datetime

"""
if key == EngineModule.Keys.K_COMMA:
if key == EngineModule.Keys.K_PERIOD:
if key == EngineModule.Keys.K_SLASH:

if key == EngineModule.Keys.K_SEMICOLON:
if key == EngineModule.Keys.K_APOSTROPHE:
if key == EngineModule.Keys.K_BACKSLASH:

if key == EngineModule.Keys.K_LBRACKET:
if key == EngineModule.Keys.K_RBRACKET:

if key == EngineModule.Keys.K_MINUS:
if key == EngineModule.Keys.K_EQUALS:
"""

def keyDown(Engine,EngineModule,key,selection,objects):
	pass

def keyReleased(Engine,EngineModule,key,selection,objects):
	pass

def calcMasses(Engine,EngineModule,bodies,factor):
		for i in range(0,len(bodies)):
			bodyName = bodies[i]
			body = helpers.getBodyFromName(Engine,EngineModule,bodyName)
			bodyMass = body.getMass()
			if i > 0:
				otherBodyName = bodies[i-1]
				otherBody = helpers.getBodyFromName(Engine,EngineModule,otherBodyName)
				otherBodyMass = otherBody.getMass()
				body.setMass( otherBodyMass * factor);

def readMasses(Engine,EngineModule,bodies):
		for i in range(0,len(bodies)):
			bodyName = bodies[i]
			body = helpers.getBodyFromName(Engine,EngineModule,bodyName)
			bodyMass = body.getMass()
			if i > 0:
				otherBodyName = bodies[i-1]
				otherBody = helpers.getBodyFromName(Engine,EngineModule,otherBodyName)
				otherBodyMass = otherBody.getMass()
				#factor = otherBodyMass / bodyMass
				factor = bodyMass / otherBodyMass

				print(bodyName + " : " + str(bodyMass) + " * " + str(factor))
			else:
				print(bodyName + " : " + str(bodyMass))

def printFps(Engine):
	if not Engine.getTimeDifference() == 0:
		print("fps: " + str(float(1000.0 / Engine.getTimeDifference())))
	else:
		print("fps: 0")


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
		parts = ["feet","lleg","uleg","root","belly",
			"breast","shoulder","neck","uarm","larm","head","hand"]

		#bodies = ["Bone.012", "Bone.010", "Bone", "Bone.002", "Bone.003", "Bone.007", "Bone.008"]
		helpers.storeOperation(str(datetime.datetime.now()))
		bodies = ["toes-l", "foot-l", "lleg-l", "uleg-l", "root", "belly", "cheast", "breast", "neck", "head"]
		calcMasses(Engine,EngineModule,bodies,0.7)

		bodies = ["toes-r", "foot-r", "lleg-r", "uleg-r", "root", "belly", "cheast", "breast", "neck", "head"]
		calcMasses(Engine,EngineModule,bodies,0.7)

		parts = ["feet","lleg","uleg","root","belly",
			"breast","shoulder","neck","uarm","larm","head","hand"]
		for p in parts:
			bodyList = objects.get()[p]
			for b in bodyList:
				newMass = b.getMass() * 0.01
				b.setMass(newMass)
				"""



		Engine.log("comma")
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


		"""
		objectsNumber = Engine.howManyObjects()
		for i in range(0,objectsNumber):
			o = Engine.getObject(i)
			if o.isStaticActor():
				helpers.storeOperation("static: " + 
					"EngineModule.Vec3(" + str(o.getPosition()) + ") EngineModule.Quat(" +
					str(o.getOrientation()) + ")"
					)
					"""





	if key == EngineModule.Keys.K_PERIOD:
		pass
		helpers.storeOperation(str(datetime.datetime.now()))
		bodies = ["toes-l", "foot-l", "lleg-l", "uleg-l", "root", "belly", "cheast", "breast", "neck", "head"]
		readMasses(Engine,EngineModule,bodies)
		"""
		print(type(EngineModule.Vec3()))
		print(type(EngineModule.Quat()))

		v = EngineModule.Vec3()
		q = EngineModule.Quat()

		if type(v) == EngineModule.Vec3:
			print("is Vector")
		if type(q) == EngineModule.Quat:
			print("is Quat")

		if type(q) == EngineModule.Vec3:
			print("is Vector ?")
		if type(v) == EngineModule.Quat:
			print("is Quat ?")
			"""

		

		#Engine.setTimingFactor(0.0001)
		#print("timingfactor: " +str(Engine.getTimingFactor()))
		#Engine.simulatePhysics(1.0/60.0)
		#Engine.physicPauseToggle()
		#for o in selection.get():
		#if Engine.isKeyDown(EngineModule.Keys.K_7):
		"""
		if len(selection.get()) > 0:
			for o in selection.get():
				if o.isActor():
					print("adding Box")
					o.isActor().addCapsule(EngineModule.Vec3(20,40,20))
		else:
			Engine.test()
			"""
		#Engine.test()

		"""
		a = Engine.createArticulation()
		a.setPosition(EngineModule.Vec3(0,200,0))
		a.addCapsule(EngineModule.Vec3(50,10,10))

		b = a.addArticulation()
		b.addCapsule(EngineModule.Vec3(50,5,5))
		b.setParentAnchor(EngineModule.Vec3(50,0,0))
		b.setChildAnchor(EngineModule.Vec3(-50,0,0))
		b.setSwingLimits(40,40)
		b.setTwistLimits(0.1,0.2)

		for i in range(0,5):
			b = b.addArticulation()
			b.addCapsule(EngineModule.Vec3(50,5,5))
			b.setParentAnchor(EngineModule.Vec3(50,0,0))
			b.setChildAnchor(EngineModule.Vec3(-50,0,0))
			b.setSwingLimits(40,40)
			b.setTwistLimits(0.1,0.2)

			b = b.addArticulation()
			b.addCapsule(EngineModule.Vec3(50,10,5))
			b.setParentAnchor(EngineModule.Vec3(50,0,0))
			b.setChildAnchor(EngineModule.Vec3(-50,0,0))
			b.setSwingLimits(40,40)
			b.setTwistLimits(0.1,0.2)

		a.addToScene()
		"""

		"""
		a = create.createPhysicBoxFinal(Engine,EngineModule)
		a.setSize(EngineModule.Vec3(50,10,10))
		a.setPosition(EngineModule.Vec3(0,200,0))


		for i in range(0,10):
			b = create.createPhysicBoxFinal(Engine,EngineModule)
			b.setSize(EngineModule.Vec3(50,5,5))
			j = Engine.createJoint(a,b)
			j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
			j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
			j.setLimits(40,40)
			a=b

			b = create.createPhysicBoxFinal(Engine,EngineModule)
			b.setSize(EngineModule.Vec3(50,10,10))
			j = Engine.createJoint(a,b)
			j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
			j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
			j.setLimits(40,40)
			a=b
			"""


		#b.setTwistLimitDisabled()
		#b.setSwingLimitDisabled()

			
		#Engine.callPythonKeyPressed(EngineModule.Keys.K_SPACE)
		"""
		a = Engine.createStaticActor()
		s = a.addCapsule(EngineModule.Vec3(60,20,20))
		a.setPosition(EngineModule.Vec3(0,100,0))

		a = Engine.createDynamicActor()
		s = a.addCapsule(EngineModule.Vec3(60,20,20))
		s = a.addBox(EngineModule.Vec3(60,20,20))
		s.setLocalPosition(EngineModule.Vec3(0,10,0))
		"""

		#s = a.addBox(EngineModule.Vec3(60,20,20))
		#s = a.addSphere(EngineModule.Vec3(60,20,20))
		#s.setLocalSize(EngineModule.Vec3(40,10,10))
		#s.setLocalOrientation(EngineModule.Quat().fromAngles(0,45,0))
		#s.setLocalPosition(EngineModule.Vec3(0,10,0))

		"""
		b = Engine.createDynamicActor()
		s = b.addCapsule(EngineModule.Vec3(60,20,20))

		j = Engine.createJoint(a,b)
		j.setAnchor1Size( EngineModule.Vec3(1,0,0) )
		j.setAnchor2Size( EngineModule.Vec3(-1,0,0) )
		j.setLimits(40,40)
		"""

	if key == EngineModule.Keys.K_SLASH:
		"""
		parts = ["feet","lleg","uleg","root","belly",
			"breast","shoulder","neck","uarm","larm","head","hand"]
		for p in parts:
			bodyList = objects.get()[p]
			for b in bodyList:
				b.resetMass()
				"""

		"""
		print("set Solver Iterations")
		#for o in selection.get():
		objectsNumber = Engine.howManyObjects()
		for i in range(0,objectsNumber):
			o = Engine.getObject(i)
			#if o.isBody():
			if False:
				b = o.isBody()
				b.dsetSolverIterations(4,1)
				#b.dsetSolverIterations(4,4)
				#b.dsetSolverIterations(32,8)
				#b.dsetSolverIterations(4,8)
				#b.dsetSolverIterations(16,1)
				"""

		o = Engine.createStaticActor()
		b = o.addPlane()
		o.setPosition(EngineModule.Vec3(0,0,0))
		o.setOrientation(EngineModule.Quat().fromAngles(0,0,90))



		o = Engine.createDynamicActor()
		b = o.addBox(EngineModule.Vec3(10,10,10))
		#b = o.addCapsule(EngineModule.Vec3(1,1,1))
		b.setMaterialName(Engine.getDefaultShadedMaterialName())
		b.setScaling1To1()
		o.setPosition(EngineModule.Vec3(0,150,0))
		o.setSize(EngineModule.Vec3(20,20,20))


