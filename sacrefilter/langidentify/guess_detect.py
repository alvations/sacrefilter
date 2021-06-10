
from __future__ import annotations

from spirit_guess.orthography import count_chars_in_blocks

class SpiritGuess:
    def __init__(self):
        self.enchanter = EnchantDetect()
        self.ngrammer = NgramDetect()

    def classify(self, text: str, n_best: int=1):
        candidates = count_chars_in_blocks(text).most_common()[:n_best]
        
