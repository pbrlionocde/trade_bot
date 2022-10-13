from typing import TypedDict
from trading_view_wrapper.exceptions import RecommendationError
from trading_view_wrapper.main_analisys import Analise

Summary = TypedDict(
    'Summary',
    {
        'RECOMMENDATION': str,
        'BUY': int,
        'SELL': int,
        'NEUTRAL': int,
    },
    total = True,
)

Recommendation = TypedDict(
    'Recommendation',
    {
        'buy': float,
        'sell': float,
        'neutral': float,
    },
        total=True,
)


class Signals:

    def __init__(self) -> None:
        self.min_result_wrap = Analise()
        self.med_result_wrap = Analise(interval='5m')

    def get_signals(self):
        min_result = self.min_result_wrap()
        min_recommendation = Summary(**min_result)
        med_result = self.med_result_wrap()
        med_recommendation = Summary(**med_result)
        if min_recommendation and med_recommendation:
            return Recommendation(
                buy = (min_recommendation['BUY'] + med_recommendation['BUY']) / 2,
                sell = (min_recommendation['SELL'] + med_recommendation['SELL']) /2,
                neutral = (min_recommendation['NEUTRAL'] + med_recommendation['NEUTRAL']) /2,
            )
        raise RecommendationError('check `Analise` configs')
