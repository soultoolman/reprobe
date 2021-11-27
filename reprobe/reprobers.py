# -*- coding: utf-8 -*-
from pathlib import Path

from .index import Index
from .aligners import BowtieAligner
from .selectors import BowtieSelector


class Reprober:
    def reprobe(self):
        raise NotImplementedError


class BowtieReprober(Reprober):
    def __init__(self):
        self.aligner = BowtieAligner()
        self.selector = BowtieSelector()

    def reprobe(self, probe_sequences_file, index, mismatches=2):
        if isinstance(probe_sequences_file, str):
            probe_sequences_file = Path(probe_sequences_file)
        if isinstance(index, str):
            index = Index(Path(index))
        elif isinstance(index, Path):
            index = Index(index)
        matches = self.aligner.align(
            probe_sequences_file,
            index,
            mismatches
        )
        selected = self.selector.select(matches, index)
        return selected
