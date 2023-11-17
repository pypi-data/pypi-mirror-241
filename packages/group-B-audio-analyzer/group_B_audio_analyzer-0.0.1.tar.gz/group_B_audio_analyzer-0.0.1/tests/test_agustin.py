import numpy as np
from group_B_audio_analyzer.src import model

def test_model_size():
    h = np.random.random(np.random.randint(1, 10))
    y = np.random.random(np.random.randint(1, 100))
    x = model(h, y)
    assert max(len(h), len(y)) == len(x)

def test_testing():
    assert True