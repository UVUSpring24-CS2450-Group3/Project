import unittest
from unittest.mock import patch
from uvsim import UVSim  # Assuming UVSim is the class being tested

class TestUVSim(unittest.TestCase):
    def test_add(self):
        sim = UVSim(debug=True)
        with patch('builtins.input', side_effect=["8", "9"]):
            sim.loadProgram([1098, 1099, 3098, 3099, 4300])
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            self.assertEqual(sim.acc, 17)

    def test_sub(self):
        sim = UVSim(debug=True)
        with patch('builtins.input', side_effect=["2003", "-208", "9999", "8381"]):
            sim.loadProgram([1098, 1099, 3098, 3199, 4300])
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            self.assertEqual(sim.acc, 2211)

            sim.reset()
            sim.loadProgram([1098, 1099, 3098, 3199, 4300])
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            sim.step()
            self.assertEqual(sim.acc, 1618)

    # Implement other test methods...

if __name__ == '__main__':
    unittest.main()
