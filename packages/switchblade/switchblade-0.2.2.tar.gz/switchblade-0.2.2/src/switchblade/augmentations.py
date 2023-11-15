'''
Audio augmentation code :)
'''

import numpy as np
import random
from torch_audiomentations import *

import torch
from torch import Tensor
from torch_audiomentations.core.transforms_interface import BaseWaveformTransform
from torch_audiomentations.utils.object_dict import ObjectDict
from typing import Optional

# SpliceOut code is a paste from torch_audiomentations because it's not "officially" in yet.
class SpliceOut(BaseWaveformTransform):
    """
    spliceout augmentation proposed in https://arxiv.org/pdf/2110.00046.pdf
    silence padding is added at the end to retain the audio length.
    """
    supported_modes = {"per_batch", "per_example"}
    requires_sample_rate = True

    def __init__(
        self,
        num_time_intervals=8,
        max_width=400,
        mode: str = "per_example",
        p: float = 0.5,
        p_mode: Optional[str] = None,
        sample_rate: Optional[int] = None,
        target_rate: Optional[int] = None,
        output_type: Optional[str] = None,
    ):
        """
        param num_time_intervals: number of time intervals to spliceout
        param max_width: maximum width of each spliceout in milliseconds
        param n_fft: size of FFT
        """

        super().__init__(
            mode=mode,
            p=p,
            p_mode=p_mode,
            sample_rate=sample_rate,
            target_rate=target_rate,
            output_type=output_type,
        )
        self.num_time_intervals = num_time_intervals
        self.max_width = max_width

    def randomize_parameters(
        self,
        samples: Tensor = None,
        sample_rate: Optional[int] = None,
        targets: Optional[Tensor] = None,
        target_rate: Optional[int] = None,
    ):

        self.transform_parameters["splice_lengths"] = torch.randint(
            low=0,
            high=int(sample_rate * self.max_width * 1e-3),
            size=(samples.shape[0], self.num_time_intervals),
        )

    def apply_transform(
        self,
        samples: Tensor = None,
        sample_rate: Optional[int] = None,
        targets: Optional[Tensor] = None,
        target_rate: Optional[int] = None,
    ) -> ObjectDict:

        spliceout_samples = []

        for i in range(samples.shape[0]):

            random_lengths = self.transform_parameters["splice_lengths"][i]
            sample = samples[i][:, :]
            for j in range(self.num_time_intervals):
                start = torch.randint(
                    0,
                    sample.shape[-1] - random_lengths[j],
                    size=(1,),
                )

                if random_lengths[j] % 2 != 0:
                    random_lengths[j] += 1

                hann_window_len = random_lengths[j]
                hann_window = torch.hann_window(hann_window_len, device=samples.device)
                hann_window_left, hann_window_right = (
                    hann_window[: hann_window_len // 2],
                    hann_window[hann_window_len // 2 :],
                )

                fading_out, fading_in = (
                    sample[:, start : start + random_lengths[j] // 2],
                    sample[:, start + random_lengths[j] // 2 : start + random_lengths[j]],
                )
                crossfade = hann_window_right * fading_out + hann_window_left * fading_in
                sample = torch.cat(
                    (
                        sample[:, :start],
                        crossfade[:, :],
                        sample[:, start + random_lengths[j] :],
                    ),
                    dim=-1,
                )

            padding = torch.zeros(
                (samples[i].shape[0], samples[i].shape[-1] - sample.shape[-1]),
                dtype=torch.float32,
                device=sample.device,
            )
            sample = torch.cat((sample, padding), dim=-1)
            spliceout_samples.append(sample.unsqueeze(0))

        return ObjectDict(
            samples=torch.cat(spliceout_samples, dim=0),
            sample_rate=sample_rate,
            targets=targets,
            target_rate=target_rate,
        )


class Delay(BaseWaveformTransform):
    def __init__(self, min_shift, max_shift, p=0.5, mode='per_example'):
        super().__init__()
        self.p = p
        self.shift = Shift(min_shift=min_shift, max_shift=max_shift, p=1., mode=mode)

    def apply_transform(self, samples, **kwargs):
        if np.random.random() < self.p:
            shifted_samples = self.shift(samples)
            samples = (samples + shifted_samples) / 2

        return ObjectDict(
            samples=samples,
            **kwargs
        )


class RandAugment:
    def __init__(self, sr: int, max_transforms: int = 3, magnitude: int = 7, p: float = 0.5):
        self.sr = sr
        self.max_transforms = max_transforms
        self.magnitude = magnitude
        self.transforms = [
            lambda mag: PolarityInversion(mode='per_example', p=p),
            lambda mag: TimeInversion(mode='per_example', p=p),
            lambda mag: AddColoredNoise(mode='per_example', p=p, min_snr_in_db=5-mag, max_snr_in_db=50-mag),
            lambda mag: Gain(min_gain_in_db=-6.0-mag, max_gain_in_db=0.0, mode='per_example', p=p),
            lambda mag: random.choice([
                HighPassFilter(min_cutoff_freq=20+mag*200, max_cutoff_freq=2400+mag*200, mode='per_example', p=p),
                LowPassFilter(min_cutoff_freq=3500-mag*300, max_cutoff_freq=7500-mag*300, mode='per_example', p=p)
            ]),
            lambda mag: Delay(0.03, 0.06+mag*0.01, p=p),
            lambda mag: PitchShift(-mag, mag, mode='per_example', sample_rate=self.sr, p=p),
            lambda mag: random.choice([
                Shift(-.2-mag*0.02, .2+mag*0.02, mode='per_example', p=p),
                SpliceOut(num_time_intervals=4, max_width=100+mag*10, mode='per_example', p=p)
            ])
        ]

    def __call__(self, x):
        original_shape = x.shape
        x = self._ensure_shape(x)
        num_transforms = random.randint(1, self.max_transforms)
        chosen_transforms = random.sample(self.transforms, num_transforms)

        for transform_func in chosen_transforms:
            transform = transform_func(self.magnitude)
            x = transform(x, sample_rate=self.sr)

        return x.view(*original_shape)

    def _ensure_shape(self, x):
        if x.dim() == 1:
            x = x.unsqueeze(0)
        if x.dim() == 2:
            x = x.unsqueeze(0)
        if x.dim() != 3:
            raise ValueError(f'Invalid shape for RandAugment signal: {x.shape}')

        return x