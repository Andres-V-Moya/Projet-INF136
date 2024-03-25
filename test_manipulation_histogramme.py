from manipulation_histogramme import *

def test_calcer_histogramme():

    tableau = np.array([[255, 160, 10, 49],
                        [20, 170, 1, 121],
                        [30, 233, 230, 100],
                        [255, 23, 155, 88]])

    w = 3

    assert np.array_equal(calculer_histogramme(tableau, w),
                          np.array([[4, 0, 2, 3],
                                    [3, 2, 2, 2],
                                    [4, 0, 2, 3],
                                    [2, 3, 2, 2]]))

def test_calculer_distance_1():

    histo1 = np.array([1, 2, 3, 4, 5])
    histo2 = np.array([2, 3, 4, 5, 6])

    assert (calculer_distance_1(histo1, histo2), 2.24)

def test_calculer_distance_2():

    histo1 = np.array([1, 2, 3, 4, 5])
    histo2 = np.array([2, 3, 4, 5, 6])

    assert (calculer_distance_2(histo1, histo2), 5)

