#!/usr/bin/env python3
import os
import sys
import io
import re
import json
import urllib.request
from pathlib import Path
import pandas as pd

DATASET = "bunqi/OANDA_XAUUSD_Gold"

def run():
    print("[*] Starting Gold (XAU/USD) Update for 2025-10 to 2026-10...")
    base_dir = Path("XAUUSD/1m")
    list_url = f"https://huggingface.co/api/datasets/{DATASET}/tree/main/1"

    req = urllib.request.Request(list_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        tree = json.loads(resp.read().decode())

    parquet_files = [f["path"] for f in tree if f["path"].endswith(".parquet")]
    
    target_files = []
    for fpath in parquet_files:
        m = re.search(r"_(\d{4})-(\d{2})-", fpath)
        if m:
            yr = int(m.group(1))
            mo = int(m.group(2))
            if (yr == 2025 and mo >= 10) or (yr >= 2026):
                target_files.append((yr, m.group(2), fpath))

    target_files.sort(key=lambda x: (x[0], x[1]))
    print(f"[*] Found {len(target_files)} monthly parquet files to fill the gap.")

    for yr, mo, fpath in target_files:
        file_url = f"https://huggingface.co/datasets/{DATASET}/resolve/main/{fpath}"
        print(f"[*] Streaming & parsing Gold {yr}-{mo}...")

        f_req = urllib.request.Request(file_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(f_req) as f_resp:
            df = pd.read_parquet(io.BytesIO(f_resp.read()))

        if df.empty:
            continue

        t0 = df["time"].iloc[0]
        if t0 > 1e16:
            dt = pd.to_datetime(df["time"], unit="ns", utc=True)
            ts_ms = (df["time"] // 1_000_000).astype("int64")
        elif t0 > 1e12:
            dt = pd.to_datetime(df["time"], unit="ms", utc=True)
            ts_ms = df["time"].astype("int64")
        else:
            dt = pd.to_datetime(df["time"], unit="s", utc=True)
            ts_ms = (df["time"] * 1000).astype("int64")

        df["timestamp"] = ts_ms
        df["datetime_utc"] = dt.dt.strftime("%Y-%m-%d %H:%M:%S")
        df["date"] = dt.dt.strftime("%Y-%m-%d")

        for date_str, grp in df.groupby("date"):
            y_str = date_str[0:4]
            m_str = date_str[5:7]
            out_file = base_dir / y_str / m_str / f"XAUUSD_1m_{date_str}.csv"
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_cols = ["timestamp", "datetime_utc", "open", "high", "low", "close", "volume"]
            grp[out_cols].to_csv(out_file, index=False)

    print("[✓] Finished updating missing months through October 2026!")

if __name__ == "__main__":
    run()
