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

def test_divide(monkeypatch):
    sim = UVSim()
    sim.loadProgram([1098, 1099, 2098, 3299, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "155")
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "5")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    assert sim.acc == 31

    sim.reset()
    sim.loadProgram([1098, 1099, 2098, 3299, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "300")
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "-5")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    assert sim.acc == -60
 
def test_multi(monkeypatch):
    sim = UVSim()
    sim.loadProgram([1098, 1099, 2099, 3398, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "12")
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "13")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    assert sim.acc == 156

    sim.reset()
    sim.loadProgram([1098, 1099, 2098, 3399, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "12")
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "-13")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    assert sim.acc == -156

def test_load(monkeypatch):
    sim = UVSim()
    sim.loadProgram([1098, 1099, 2098, 2099, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "120")
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "130")
    sim.step()
    sim.step()
    assert sim.acc == 120
    sim.step()
    assert sim.acc == 130 
    sim.step()

def test_store(monkeypatch):
    sim = UVSim()
    sim.loadProgram([1098, 2098, 2199, 2099, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "120")
    sim.step()
    sim.step()
    assert sim.acc == 120
    sim.step()
    sim.step()
    assert sim.acc == 120
    sim.step()
    
    sim.reset()
    sim.loadProgram([1098, 2098, 2199, 2099, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "5255")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    assert sim.acc == 5255
    

def test_branches(monkeypatch):
    # Test unconditional branch (40)
    sim = UVSim()
    """
    0: RDKB #98
    1: BR #4
    2: HALT
    3: HALT
    4: HALT
    """

    sim.loadProgram([1098, 4004, 4300, 4300, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "20")
    sim.step()
    sim.step()
    sim.step()
    
    # Tested against 5 because the program counter increments after an instruction is fetched
    assert sim.pc == 5

    # Test conditional branch on negative (41)
    sim.reset()

    """
    0: RDKB #98
    1: LDA #98
    2: BRn #4
    3: RDKB #98
    4: LDA #98
    5: BRn #5
    6: HALT
    7: HALT
    """
    sim.loadProgram([1098, 2098, 4106, 1098, 2098, 4107, 4300, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "20")
    sim.step()
    sim.step()
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "-50")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    
    assert sim.pc == 8

    # Test conditional branch on zero (41)
    sim.reset()

    """
    0: RDKB #98
    1: LDA #98
    2: BRn #4
    3: RDKB #98
    4: LDA #98
    5: BRn #5
    6: HALT
    7: HALT
    """
    sim.loadProgram([1098, 2098, 4206, 1098, 2098, 4207, 4300, 4300])
    monkeypatch.setattr('builtins.input', lambda _: "1")
    sim.step()
    sim.step()
    sim.step()
    monkeypatch.setattr('builtins.input', lambda _: "0")
    sim.step()
    sim.step()
    sim.step()
    sim.step()
    
    assert sim.pc == 8


