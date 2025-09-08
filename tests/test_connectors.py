
import pytest
from crypto_strategies_ai.data import connectors
import pandas as pd

def test_synthetic_fallback():
    df = connectors.synthetic_series('TEST', '2023-01-01', '2023-01-10')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'close' in df.columns

def test_yfinance_missing(monkeypatch):
    # Simulate yfinance not installed by temporarily renaming module in sys.modules
    import sys
    if 'yfinance' in sys.modules:
        old = sys.modules.pop('yfinance')
    try:
        with pytest.raises(RuntimeError):
            connectors.fetch_stocks_yfinance(['FAKE.TICKER'], '2023-01-01', '2023-01-10')
    finally:
        if 'old' in locals():
            sys.modules['yfinance'] = old
