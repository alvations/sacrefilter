
from __future__ import annotations

import chardet
from chardet.metadata.languages import LANGUAGES

class CharDet:
    def __init__(self):
        self._model = UniversalDetector()
        self._classes = {LANGUAGES[k].iso_code:LANGUAGES[k].name for k in LANGUAGES}

    def classify(self, text, chunk_size=50):
        for i in range(0, len(line), chunk_size):
            self._model.feed(text[i:i+chunk_size])
            if self._model.done:
                break
        # Get the results.
        results = self._model.result
        # Reset the model.
        self._model.reset()
        # Returns the result.
        return results.get('language': 'unk'), results.get('confidence', 0.0)

    def confidence(self, text, lang):
        predicted_lang, predicted_confidence = self.classify(text)
        return 0.0 if lang != predicted_lang else predicted_confidence

    def supported_languages(self):
        return self._classes
