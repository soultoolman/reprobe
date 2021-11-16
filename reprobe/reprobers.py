# -*- coding: utf-8 -*-
from .aligners import BowtieAligner
from .selectors import BowtieSelector


class Reprober:
    def reprobe(self):
        raise NotImplementedError


class BowtieReprober(Reprober):
    def __init__(self):
        self.aligner = BowtieAligner()
        self.selector = BowtieSelector()

    def reprobe(self, probe_sequences_file, index):
        matches = self.aligner.align(probe_sequences_file, index)
        selected = self.selector.select(matches)
        return selected
