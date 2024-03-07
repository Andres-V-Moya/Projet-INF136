from coordonnees_clou import *



def test_calculer_coordonnees_clou():
    assert calculer_coordonnees_clou(3,10,1,0.75,2) == [('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2',(-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_2', (5.0,0.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5))]
