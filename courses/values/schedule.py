from dataclasses import dataclass
from datetime import time
from typing import List, Optional


@dataclass(frozen=True)
class TimePeriod:
    start: time
    end: time


@dataclass(frozen=True)
class DayPeriod:
    day: int
    time: TimePeriod

    def __sub__(self, other: Optional['DayPeriod']) -> Optional['DayPeriod']:
        if not other:
            return self
        start = other.time.end
        end = self.time.end
        if start == end:
            return None
        return DayPeriod(self.day, TimePeriod(start, end))


@dataclass(frozen=True)
class Schedule:
    periods: List[DayPeriod]

    def __sub__(self, other: 'Schedule') -> 'Schedule':
        periods = []
        for period in self.periods:
            other_period = other.find_period_for_day(period.day)
            periods.append(period - other_period)
        return Schedule(periods)

    def find_period_for_day(self, day: int) -> Optional[DayPeriod]:
        return next((period for period in self.periods if period.day == day),
                    None)
