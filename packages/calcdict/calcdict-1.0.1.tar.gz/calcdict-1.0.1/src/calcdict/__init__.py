import fileunity as _fu


class CalcDict:
    def __init__(self, calculators={}, results={}):
        self._busy = set()
        self._calculators = dict()
        self._dummy_unit = _fu.TOMLUnit()
        self._results_unit = _fu.TOMLUnit()

        calculators = dict(calculators)
        results = _fu.TOMLUnit(results).data
        self.update_calculators(calculators)
        self.update_results(results)

    def calculators(self):
        return list(self._calculators)
    def get_calculator(self, key):
        return self._calculators[key]
    def set_calculator(self, key, value):
        self._strerror(key)
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
        self._strerror(key)
        return self._results_unit[key]
    def set_result(self, key, value):
        self._strerror(key)
        self._results_unit[key] = value
        if key in self._dummy_unit.keys():
            del self._dummy_unit[key]
            del self._calculators[key]
    def del_result(self, key):
        self._strerror(key)
        del self._results_unit[key]
    def update_results(self, dictionary):
        dictionary = dict(dictionary)
        for k, v in dictionary.items():
            self.set_result(k, v)
    def clear_results(self):
        self._results_unit.clear()

    def getitem(self, key):
        try:
            calculator = self._calculators.pop(key)
        except KeyError:
            return self._results_unit[key]
        del self._dummy_unit[key]
        if key in self._busy:
            raise KeyError(f"The item {key} was requested during its own calculation.")
        self._busy.add(key)
        try:
            self._results_unit[key] = calculator(self.getitem)
        finally:
            self._busy.remove(key)
        return self._results_unit[key]
    def clear(self):
        self.clear_calculators()
        self.clear_results()
    def calculate_all(self):
        keys = list(self._calculators.keys())
        for k in keys:
            self.getitem(k)
    def copy(self):
        cls = type(self)
        return cls(
            calculators=self.calculators(), 
            results=self.results(),
        )
    def to_dict(self):
        self.calculate_all()
        return self._results_unit.data
    def to_TOMLUnit(self):
        return _fu.TOMLUnit(self.to_dict())
    @classmethod
    def _strerror(self, key):
        if type(key) is not str:
            raise TypeError(f"The key {key} is not a string.")


    