"""select:
	mouseRight: create new selection
	lshift: add to selection
	lctrl: remove from selection
	lalt: select unselectable
	ralt: select only guiShape
"""

import bodyjoint

def init(Engine,EngineModule,objects):
	pass

def keyDown(Engine,EngineModule,key,selection,objects):
	pass

def keyPressed(Engine,EngineModule,key,selection,objects):
	pass

	if key == EngineModule.Keys.K_MRIGHT:
		selectedContainer = None
		queryList = Engine.getMouseQuery()
		for q in queryList:
			shape = Engine.getFromUuid(q[1])
			container = Engine.getObjectOfShape(Engine.getFromUuid(q[1]))
			if Engine.isKeyDown(EngineModule.Keys.K_LMENU):
				selectedContainer = container
				break
			elif Engine.isKeyDown(EngineModule.Keys.K_RMENU):
				selectedContainer = shape
				break
			else:
				if shape.isSelectable() and container.isSelectable():
					selectedContainer = container
					break

		if selectedContainer:
			if Engine.isKeyDown(EngineModule.Keys.K_LSHIFT):
				print("add to selection")
				selection.add(selectedContainer)

			elif Engine.isKeyDown(EngineModule.Keys.K_LCONTROL):
				print("remove from selection")
				selection.remove(selectedContainer)
				pass

			else:
				print("set selection")
				selection.clear()
				selection.add(selectedContainer)
		else:
			pass
			print("clear selection")
			selection.clear()


def keyReleased(Engine,EngineModule,key,selection,objects):
	pass


