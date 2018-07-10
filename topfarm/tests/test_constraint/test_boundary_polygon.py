import unittest

import numpy as np
from topfarm.cost_models.dummy import DummyCost, DummyCostPlotComp
from topfarm import TopFarm
from topfarm.constraint_components.boundary_component import PolygonBoundaryComp
from topfarm.plotting import NoPlot, PlotComp


class TestBoundaryPolygon(unittest.TestCase):

    def testPolygon(self):
        optimal = [(0, 0)]
        boundary = [(0, 0), (1, 1), (2, 0), (2, 2), (0, 2)]
        tf = TopFarm(optimal, DummyCost(optimal), 2, boundary=boundary, boundary_type='polygon', record_id=None)
        np.testing.assert_array_equal(tf.boundary, [[0, 0],
                                                    [1, 1],
                                                    [2, 0],
                                                    [2, 2],
                                                    [0, 2],
                                                    [0, 0]])

    def testPolygonConcave(self):
        optimal = [(1.5, 1.3), (4, 1)]
        boundary = [(0, 0), (5, 0), (5, 2), (3, 2), (3, 1), (2, 1), (2, 2), (0, 2), (0, 0)]
        plot_comp = NoPlot()  # DummyCostPlotComp(optimal)
        initial = [(-0, .1), (4, 1.5)][::-1]
        tf = TopFarm(initial, DummyCost(optimal), 0, boundary=boundary, boundary_type='polygon', plot_comp=plot_comp, record_id=None)
        tf.evaluate()
        tf.optimize()
        np.testing.assert_array_almost_equal(tf.turbine_positions, optimal, 4)
        plot_comp.show()

    def testPolygonTwoRegionsStartInWrong(self):
        optimal = [(1, 1), (4, 1)]
        boundary = [(0, 0), (5, 0), (5, 2), (3, 2), (3, 0), (2, 0), (2, 2), (0, 2), (0, 0)]
        plot_comp = NoPlot()  # DummyCostPlotComp(optimal, delay=.1)
        initial = [(3.5, 1.5), (2, 1)]
        tf = TopFarm(initial, DummyCost(optimal), 0, boundary=boundary, boundary_type='polygon', plot_comp=plot_comp, record_id=None)
        tf.evaluate()
        tf.optimize()
        plot_comp.show()
        np.testing.assert_array_almost_equal(tf.turbine_positions, optimal, 4)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
