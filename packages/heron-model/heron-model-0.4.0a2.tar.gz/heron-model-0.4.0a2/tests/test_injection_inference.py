import unittest
from heron.likelihood import determine_overlap
from elk.waveform import Timeseries
import torch

import heron.injection
import scipy.signal

import heron.models.lalinference
from heron.models.torchbased import HeronCUDA,  train
from heron.likelihood import CUDATimedomainLikelihood

import lalsimulation

class TestLikelihoodTimeWindowing(unittest.TestCase):

    def generate_injection(self):
        times = {"duration": 0.10,
                 "sample rate": 4096,
                 "before": 0.3,
                 "after": 0.01,
                 }

        psd = heron.injection.psd_from_lalinference(
            "SimNoisePSDaLIGOZeroDetHighPower",
            frequencies=heron.injection.frequencies_from_times(times),
        )

        settings = {}
        settings['injection'] = {"mass ratio": 0.6,
                                 "total mass": 65,
                                 "ra": 1.79,
                                 "dec": -1.22,
                                 "psi": 1.47,
                                 "gpstime": 1,

                                 "detector": "L1",



                                 "distance": 1000,
                                 "before": 0.3,
                                 }
        settings['injection'].update(times)
        
        noise = heron.injection.create_noise_series(psd, times)
        signal = heron.models.lalinference.IMRPhenomPv2(torch.device("cuda")).time_domain_waveform(
            p=settings["injection"]
        )

        detection = Timeseries(data=signal.data + noise, times=settings['injection']['gpstime']+signal.times)
        sos = scipy.signal.butter(
            10,
            20,
            "hp",
            fs=float(1 / (detection.times[1] - detection.times[0])),
            output="sos",
        )
        detection.data = torch.tensor(
            scipy.signal.sosfilt(sos, detection.data.cpu()),
            device=detection.data.device,
        )

        return detection, psd
    
    def setUp(self):
        DISABLE_CUDA = False
        if not DISABLE_CUDA and torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")
            
        self.model = HeronCUDA(datafile="training_data.h5", 
                               datalabel="IMR training linear", 
                               name="Heron IMR Non-spinning",
                               device=self.device,
                               )
        self.model.eval()

    def test_detection_of_waveform_difference(self):
        p = {
            "sample rate": 4096,
            "mass ratio": 1,
            "total mass": 40,
            "ra": 1.79,
            "dec": -1.22,
            "psi": 1.47,
            "gpstime": 1,
            "detector": "L1",
            "distance": 1000,
            "after": 0.02
            #"before": 0.3,
        }
        signal = self.model.time_domain_waveform(p=p)

        detection, psd = self.generate_injection()
        self.assertNotEqual(detection.times[0] - signal.times[0], 0)

        parameters = {
            "sample rate": 4096,
            "mass ratio": 1,
            "total mass": 40,
            "ra": 1.79,
            "dec": -1.22,
            "psi": 1.47,
            "gpstime": 1,
            "detector": "L1",
            "distance": 1000,
            "after": 0.02,
            "before": 0.3,
        }
        
        l = CUDATimedomainLikelihood(self.model, data=detection, detector_prefix="L1", psd=psd)


        for gpstime in torch.linspace(-0.005, 0.04, 100):
            parameters_updated = parameters.copy()
            parameters_updated['gpstime'] += float(gpstime)
            print("GPS Time", float(parameters_updated['gpstime']))
            print(float(l(parameters_updated, model_var=True).cpu()))
            self.assertTrue(l(parameters_updated, model_var=True).cpu().isfinite())

    def test_t0_in_waveform(self):
        p = {
            "sample rate": 4096,
            "mass ratio": 1,
            "total mass": 40,
            "ra": 1.79,
            "dec": -1.22,
            "psi": 1.47,
            "gpstime": 1126259462.505,
            "detector": "L1",
            "distance": 1000,
            "after": 0.02,
            "before": 0.1,
        }
        signal = self.model.time_domain_waveform(p=p)
        idx = torch.argmin(signal.times - p['gpstime'])
        print(float(signal.times[idx]))
        self.assertTrue(p['gpstime'] in signal.times)
