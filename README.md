# Gold-XAUUSD-1m-2020-2025-Historical-Data

[![Data Status](https://img.shields.io/badge/Data-Verified-brightgreen)](#)
[![Timeframe](https://img.shields.io/badge/Timeframe-1m%20(1--Minute)-blue)](#)
[![Instrument](https://img.shields.io/badge/Instrument-XAU%2FUSD%20(Spot%20Gold)-gold)](#)
[![Coverage](https://img.shields.io/badge/Coverage-2020--2025-orange)](#)

High-resolution, institutional-grade 1-minute OHLCV (Open, High, Low, Close, Volume) historical market data archive for **Spot Gold (XAU/USD)** in US Dollars, covering the years **2020 to 2025**.

---

## 📂 Repository Structure

All data is structured identically to institutional market data conventions by Year, Month, and Date:

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
| `volume` | `int` | **Tick Volume** (Frequency of price quotes per minute) | `45` |

---

## 🔍 Understanding the "Volume" Field (Tick Volume vs. Share Volume)

If you are coming from equity stock markets (where volume reflects thousands or millions of traded shares), the volume values here may appear modest at first glance (e.g., `12`, `45`, `310`). Here is the essential structural distinction:

### 1. Decentralized (OTC) Nature of Spot Gold
Unlike centralized equity exchanges (such as the NYSE, NASDAQ, or NSE) where every single transacted share is centrally tallied by a clearinghouse, **Spot Gold (XAU/USD)** trades in a decentralized **Over-The-Counter (OTC)** global interbank market across London (LBMA), New York, Zurich, Tokyo, and Singapore. There is no single universal clearinghouse that records total physical ounces or dollar totals in real-time.

### 2. What is "Tick Volume"?
In spot foreign exchange and commodity markets, the industry standard metric for volume is **Tick Volume** (also called **Tick Count**):
* **It measures market activity**: Specifically, how many times the price changed (ticked or was updated) within that 60-second window.
* **Not contract/dollar count**: It does not represent grams, ounces, or dollar amounts, but rather the intensity of quotation activity.

### 3. How to Interpret Tick Volume Numbers

| Volume Range | Market Activity | Description |
| :--- | :--- | :--- |
| **0 – 15** | **Low / Dormant** | Quiet trading hours, Asian/Pacific late-night sessions, or market holidays. |
| **20 – 100** | **Moderate / Active** | Standard institutional liquidity during active European and London trading sessions. |
| **100 – 500+** | **High Volatility Burst** | Major session overlaps (London & New York crossover) or major macroeconomic data releases (e.g., US CPI, Non-Farm Payrolls [NFP], FOMC interest rate decisions). |

### 4. Quantitative Validity
Quantitative and financial econometric research has established that **tick volume exhibits a >90% statistical correlation with actual cash trading volume and market volatility**. A surge in tick count directly signals institutional order flow and active price discovery.

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
