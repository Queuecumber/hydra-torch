# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class DistributedSamplerConf:
    _target_: str = "torch.utils.data.distributed.DistributedSampler"
    dataset: Any = MISSING
    num_replicas: Any = None
    rank: Any = None
    shuffle: Any = True
    seed: Any = 0