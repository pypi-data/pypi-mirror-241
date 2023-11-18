import fileunity as _fu


class CalcDict:
    def __init__(self, calculators={}, results={}):
        self._busy = set()
        calculators = dict(calculators)
        results = _fu.TOMLUnit(results).data
        self.update_calculators(calculators)
        self.update_results(results)

    def calculators(self):
        return list(self._calculators)
    def get_calculator(self, key):
        return self._calculators[key]
    def set_calculator(self, key, value):
        self._dummy_unit[key] = ""
        self._calculators[key] = value
        if key in self._results_unit.keys():
            del self._results_unit[key]
    def del_calculator(self, key):
        del self._calculators[key]
    def update_calculators(self, dictionary):
        dictionary = dict(dictionary)
        for k, v in dictionary.items():
            self.set_calculator(k, v)
    def clear_calculators(self):
        self._calculators.clear()

    def results(self):
        return self._results_unit.data
    def get_result(self, key):
        return self._results_unit[key]
    def set_result(self, key, value):
        self._results_unit[key] = value
        if key in self._dummy_unit.keys():
            del self._dummy_unit[key]
            del self._calculators[key]
    def del_result(self, key):
        del self._results_unit[key]
    def update_results(self, dictionary):
        dictionary = dict(dictionary)
        for k, v in dictionary.items():
            self.set_result(k, v)
    def clear_results(self):
        self._results_unit.clear()

    def getitem(self, firstkey, *otherkeys):
        calculator = self._calculators.pop(firstkey)
        del self._dummy_unit[firstkey]
        if firstkey in self._busy:
            raise KeyError
        self._busy.add(firstkey)
        try:
            self._results_unit[firstkey] = calculator(self.getitem)
        finally:
            self._busy.remove(firstkey)
        return self._results_unit[firstkey]
    def clear(self):
        self.clear_calculators()
        self.clear_results()
    def copy(self):
        cls = type(self)
        return cls(
            calculators=self.calculators(), 
            results=self.results(),
        )


    