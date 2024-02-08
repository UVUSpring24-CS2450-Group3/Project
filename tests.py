from uvsim import UVSim

def get_input():
	return ""

def test_add(monkeypatch):
	sim = UVSim()
	"""
	RDKB #98
	RDKB #99
	ADD #98
	ADD #99
	HALT
	"""
	sim.loadProgram([1098, 1099, 3098, 3099, 4300])

	monkeypatch.setattr('builtins.input', lambda _: "8")
	sim.step()
	monkeypatch.setattr('builtins.input', lambda _: "9")
	sim.step()
	sim.step()
	sim.step()
	sim.step()

	assert sim.acc == 17

def test_sub(monkeypatch):
	sim = UVSim()
	"""
	RDKB #98
	RDKB #99
	ADD #98
	SUB #99
	HALT
	"""
	sim.loadProgram([1098, 1099, 3098, 3199, 4300])

	monkeypatch.setattr('builtins.input', lambda _: "2003")
	sim.step()
	monkeypatch.setattr('builtins.input', lambda _: "-208")
	sim.step()
	sim.step()
	sim.step()
	sim.step()

	assert sim.acc == 2211

	sim.reset()
	"""
	RDKB #98
	RDKB #99
	ADD #98
	SUB #99
	HALT
	"""
	sim.loadProgram([1098, 1099, 3098, 3199, 4300])

	monkeypatch.setattr('builtins.input', lambda _: "9999")
	sim.step()
	monkeypatch.setattr('builtins.input', lambda _: "8381")
	sim.step()
	sim.step()
	sim.step()
	sim.step()

	assert sim.acc == 1618
