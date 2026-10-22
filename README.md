# Gold-XAUUSD-1m-2020-2025-Historical-Data

[![Data Status](https://img.shields.io/badge/Data-Verified-brightgreen)](#)
[![Timeframe](https://img.shields.io/badge/Timeframe-1m%20(1--Minute)-blue)](#)
[![Instrument](https://img.shields.io/badge/Instrument-XAU%2FUSD%20(Spot%20Gold)-gold)](#)
[![Coverage](https://img.shields.io/badge/Coverage-2020--2025-orange)](#)

High-resolution, institutional-grade 1-minute OHLCV (Open, High, Low, Close, Volume) historical market data archive for **Spot Gold (XAU/USD)** in US Dollars, covering the years **2020 to 2025**.

---

## 📂 Repository Structure

All data is structured identically to institutional data conventions by Year, Month, and Date:

```text
Gold-XAUUSD-1m-2020-2025-Historical-Data/
├── README.md
└── XAUUSD/
    └── 1m/
        ├── 2020/
        │   ├── 01/
        │   │   ├── XAUUSD_1m_2020-01-02.csv
        │   │   └── ...
        │   └── ...
        └── 2025/
            └── ...
```

---

## 📊 CSV Schema

| Column | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | `int64` | Unix Epoch timestamp in milliseconds (UTC) | `1704153600000` |
| `datetime_utc` | `string` | UTC datetime in `YYYY-MM-DD HH:MM:SS` format | `2024-01-02 00:00:00` |
| `open` | `float` | Open price (USD) | `2062.85` |
| `high` | `float` | High price in the 1-minute bar (USD) | `2063.40` |
| `low` | `float` | Low price in the 1-minute bar (USD) | `2062.50` |
| `close` | `float` | Close price (USD) | `2063.15` |
| `volume` | `int` | Trading volume / tick count | `45` |

---

## 🚀 Quick Usage in Python

```python
import pandas as pd

# Load a specific day
file_path = "XAUUSD/1m/2020/06/XAUUSD_1m_2020-06-15.csv"
df = pd.read_csv(file_path, parse_dates=["datetime_utc"])

print(df.head())
print(f"Total 1m candles for the day: {len(df)}")
```

---

## 🔗 Related Archives in this Series

* **2004–2009:** [Gold-XAUUSD-1m-2004-2009-Historical-Data](https://github.com/parshant65-lang/Gold-XAUUSD-1m-2004-2009-Historical-Data)
* **2010–2014:** [Gold-XAUUSD-1m-2010-2014-Historical-Data](https://github.com/parshant65-lang/Gold-XAUUSD-1m-2010-2014-Historical-Data)
* **2015–2019:** [Gold-XAUUSD-1m-2015-2019-Historical-Data](https://github.com/parshant65-lang/Gold-XAUUSD-1m-2015-2019-Historical-Data)
* **2020–2025:** [Gold-XAUUSD-1m-2020-2025-Historical-Data](https://github.com/parshant65-lang/Gold-XAUUSD-1m-2020-2025-Historical-Data)
