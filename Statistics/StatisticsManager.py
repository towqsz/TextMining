class StatisticsManager:
    def __init__(self, factory):
        self.factory = factory

    def get_statistics(self, statistics_type, parameter=None):
        method = getattr(self.factory, statistics_type)
        statistics = method() if parameter is None else method(parameter)
        return statistics
