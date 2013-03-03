"""navigate:
	w: forward
	s: backward
	a: left
	d: right
	q: down
	e: up
	1: speed * 5
"""

transformFactor = 0.5
transformFactor = 0.25

def moveCamera(Engine,EngineModule,direction):
	factor = transformFactor
	if Engine.isKeyDown(EngineModule.Keys.K_1):
		factor *= 5

	localDir = direction * factor
	globalDir = Engine.getCameraOrientation() * localDir
	Engine.setCameraPosition( Engine.getCameraPosition() + globalDir)

def init(Engine,EngineModule,objects):
	Engine.setCameraPosition(EngineModule.Vec3(0,100,300))

def keyDown(Engine,EngineModule,key,selection,objects):
	pass
	if (key == EngineModule.Keys.K_W or
		key == EngineModule.Keys.K_UP):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(0,0,-1))
	if (key == EngineModule.Keys.K_S or
		key == EngineModule.Keys.K_DOWN):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(0,0,1))
	if (key == EngineModule.Keys.K_A or
		key == EngineModule.Keys.K_LEFT):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(-1,0,0))
	if (key == EngineModule.Keys.K_D or
		key == EngineModule.Keys.K_RIGHT):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(1,0,0))
	if (key == EngineModule.Keys.K_Q or
		key == EngineModule.Keys.K_PGDOWN):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(0,-1,0))
	if (key == EngineModule.Keys.K_E or
		key == EngineModule.Keys.K_PGUP):
		moveCamera(Engine,EngineModule,EngineModule.Vec3(0,1,0))

	if key == EngineModule.Keys.K_MLEFT:
		mx = Engine.getMouseRelX()	
		my = Engine.getMouseRelY()	
		factor = 0.1
		Engine.cameraRotateY(mx * -factor)
		Engine.cameraRotateZ(my * -factor)

def keyPressed(Engine,EngineModule,key,selection,objects):
	pass

def keyReleased(Engine,EngineModule,key,selection,objects):
	pass


