from checkText import checkText

def test_step01(good, bad):
    assert good in checkText(bad)