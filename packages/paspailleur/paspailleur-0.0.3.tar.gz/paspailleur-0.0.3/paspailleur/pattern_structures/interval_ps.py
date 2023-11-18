from numbers import Number
from typing import Iterator, Optional, Union, Iterable, Sequence
from bitarray import frozenbitarray as fbarray
from .abstract_ps import AbstractPS
from math import inf, ceil


class IntervalPS(AbstractPS):
    PatternType = Optional[tuple[float, float]]
    max_pattern = (inf, -inf)  # The pattern that always describes no objects

    def join_patterns(self, a: PatternType, b: PatternType) -> PatternType:
        """Return the most precise common pattern, describing both patterns `a` and `b`"""
        return min(a[0], b[0]), max(a[1], b[1])

    def is_less_precise(self, a: PatternType, b: PatternType) -> bool:
        """Return True if pattern `a` is less precise than pattern `b`"""
        if b == self.max_pattern:
            return True
        if a == self.max_pattern:  # and b != max_pattern
            return False

        return a[0] <= b[0] <= b[1] <= a[1]

    def iter_bin_attributes(self, data: list[PatternType], min_support: Union[int, float] = 0)\
            -> Iterator[tuple[PatternType, fbarray]]:
        """Iterate binary attributes obtained from `data` (from the most general to the most precise ones)

        :parameter
            data: list[PatternType]
             list of object descriptions
            min_support: int or float
             minimal amount of objects an attribute should describe (in natural numbers, not per cents)
        :return
            iterator of (description: PatternType, extent of the description: frozenbitarray)
        """
        min_support = ceil(len(data) * min_support) if 0 < min_support < 1 else int(min_support)

        lower_bounds, upper_bounds = [sorted(set(bounds)) for bounds in zip(*data)]
        min_, max_ = lower_bounds[0], upper_bounds[-1]
        lower_bounds.pop(0)
        upper_bounds.pop(-1)

        yield (min_, max_), fbarray([True]*len(data))

        for lb in lower_bounds:
            extent = fbarray((lb <= x for x, _ in data))
            if extent.count() < min_support:
                break
            yield (lb, max_), extent

        for ub in upper_bounds[::-1]:
            extent = fbarray((x <= ub for _, x in data))
            if extent.count() < min_support:
                break
            yield (min_, ub), extent

        if min_support == 0:
            yield self.max_pattern, fbarray([False]*len(data))

    def n_bin_attributes(self, data: list[PatternType], min_support: Union[int, float] = 0, use_tqdm: bool = False)\
            -> int:
        """Count the number of attributes in the binary representation of `data`"""
        if min_support == 0:
            return len({lb for lb, ub in data}) + len({ub for ub in data})
        return super().n_bin_attributes(data, min_support)

    def preprocess_data(self, data: Iterable[Union[Number, Sequence[Number]]]) -> Iterator[PatternType]:
        """Preprocess the data into to the format, supported by intent/extent functions"""
        for description in data:
            if isinstance(description, Number):
                description = (description, description)
            if isinstance(description, range):
                start, stop = description.start, description.stop
                if start < stop:
                    description = (start, stop-1)
                elif stop < start:
                    description = (stop+1, start)
                else:  # if start == stop, then there is not closed interval inside [start, stop) == [start, start)
                    description = (inf, -inf)

            if isinstance(description, Sequence)\
                    and len(description) == 2 and all(isinstance(x, Number) for x in description):
                description = (float(description[0]), float(description[1]))
            else:
                raise ValueError(f'Cannot preprocess this description: {description}. '
                                 f'Provide either a number or a sequence of two numbers.')

            yield description
