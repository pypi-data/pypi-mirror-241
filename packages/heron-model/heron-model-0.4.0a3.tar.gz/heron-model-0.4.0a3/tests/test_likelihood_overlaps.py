import unittest
from heron.likelihood import determine_overlap
from elk.waveform import Timeseries
import torch


class TestTimeseriesOverlap(unittest.TestCase):
    def test_simple_overlap_caseA(self):
        """Overlap: aligned times, case A overlap"""
        times_A = torch.linspace(0, 50, 101)
        times_B = torch.linspace(25, 75, 101)
        timeseries_A = Timeseries(data=torch.ones(101),
                                  times=times_A)
        timeseries_B = Timeseries(data=torch.ones(101),
                                  times=times_B)

        indices = determine_overlap(timeseries_A, timeseries_B)
        self.assertEqual(timeseries_A.times[indices[0][0]], 25)
        self.assertEqual(timeseries_A.times[indices[0][1]], 50)
        self.assertEqual(timeseries_B.times[indices[1][0]], 25)
        self.assertEqual(timeseries_B.times[indices[1][1]], 50)

    def test_simple_overlap_caseB(self):
        """Overlap: aligned times, case B overlap (no overlap)"""
        A = (0, 50)
        B = (51, 101)
        times_A = torch.linspace(A[0], A[1], 101)
        times_B = torch.linspace(B[0], B[1], 101)
        timeseries_A = Timeseries(data=torch.ones(101),
                                  times=times_A)
        timeseries_B = Timeseries(data=torch.ones(101),
                                  times=times_B)

        indices = determine_overlap(timeseries_A, timeseries_B)
        self.assertEqual(indices, None)

    def test_simple_overlap_caseC(self):
        """Overlap: aligned times, case C overlap (A within B)"""
        A = (25, 51)
        B = (0, 100)
        times_A = torch.linspace(A[0], A[1], 26)
        times_B = torch.linspace(B[0], B[1], 101)
        timeseries_A = Timeseries(data=torch.ones(101),
                                  times=times_A)
        timeseries_B = Timeseries(data=torch.ones(101),
                                  times=times_B)
        indices = determine_overlap(timeseries_A, timeseries_B)
        self.assertEqual(timeseries_A.times[indices[0][0]], 25)
        self.assertEqual(timeseries_A.times[indices[0][1]], 51)
        self.assertEqual(timeseries_B.times[indices[1][0]], 25)
        self.assertEqual(timeseries_B.times[indices[1][1]], 51)

    def test_simple_overlap_caseD(self):
        """Overlap: aligned times, case D overlap (A within B)"""
        A = (0, 100)
        B = (75, 85)
        times_A = torch.linspace(A[0], A[1], 101)
        times_B = torch.linspace(B[0], B[1], 10)
        timeseries_A = Timeseries(data=torch.ones(101),
                                  times=times_A)
        timeseries_B = Timeseries(data=torch.ones(101),
                                  times=times_B)
        indices = determine_overlap(timeseries_A, timeseries_B)
        self.assertEqual(timeseries_A.times[indices[0][0]], 75)
        self.assertEqual(timeseries_A.times[indices[0][1]], 85)
        self.assertEqual(timeseries_B.times[indices[1][0]], 75)
        self.assertEqual(timeseries_B.times[indices[1][1]], 85)

    def test_simple_overlap_caseE(self):
        """Overlap: aligned times, case E overlap"""
        A = (25, 100)
        B = (0, 50)
        times_A = torch.linspace(A[0], A[1], 76)
        times_B = torch.linspace(B[0], B[1], 51)
        timeseries_A = Timeseries(data=torch.ones(101),
                                  times=times_A)
        timeseries_B = Timeseries(data=torch.ones(101),
                                  times=times_B)
        indices = determine_overlap(timeseries_A, timeseries_B)
        self.assertEqual(timeseries_A.times[indices[0][0]], 25)
        self.assertEqual(timeseries_A.times[indices[0][1]], 50)
        self.assertEqual(timeseries_B.times[indices[1][0]], 25)
        self.assertEqual(timeseries_B.times[indices[1][1]], 50)
