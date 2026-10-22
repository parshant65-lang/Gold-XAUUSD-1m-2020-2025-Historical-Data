#!/usr/bin/env python3
import os
import sys
import json
import argparse
import calendar
import urllib.request
from pathlib import Path

DATA_URL = "https://huggingface.co/datasets/ZombitX64/xauusd-gold-price-historical-data-2004-2025/resolve/main/XAU_1m_data.jsonl"
HEADERS = "timestamp,datetime_utc,open,high,low,close,volume\n"

def run(start_year: int, end_year: int):
    print(f"[*] Ingesting Gold XAU/USD 1m data for range: {start_year} - {end_year}")
    base_path = Path("XAUUSD/1m")
    
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "Mozilla/5.0"})
    print(f"[*] Streaming directly from cloud source: {DATA_URL}")

    current_date = None
    current_lines = []
    current_year_str = None
    current_month_str = None
    days_written = 0
    total_rows = 0

    with urllib.request.urlopen(req) as resp:
        for line_num, raw_line in enumerate(resp, 1):
            line = raw_line.decode("utf-8", errors="ignore").strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue

            date_raw = row["Date"]  # format: "2004.06.11 07:18"
            year = int(date_raw[0:4])

            if year < start_year:
                continue
            if year > end_year:
                print(f"[*] Reached year {year} > {end_year}. Stopping stream.")
                break

            year_str = date_raw[0:4]
            month_str = date_raw[5:7]
            day_str = date_raw[8:10]
            date_key = f"{year_str}-{month_str}-{day_str}"

            if date_key != current_date:
                if current_date and current_lines:
                    day_file = base_path / current_year_str / current_month_str / f"XAUUSD_1m_{current_date}.csv"
                    day_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(day_file, "w", encoding="utf-8") as f:
                        f.write(HEADERS)
                        f.writelines(current_lines)
                    days_written += 1

                current_date = date_key
                current_year_str = year_str
                current_month_str = month_str
                current_lines = []

            hour_str = date_raw[11:13]
            min_str = date_raw[14:16]
            y, m, d = year, int(month_str), int(day_str)
            h, mn = int(hour_str), int(min_str)
            ts_ms = calendar.timegm((y, m, d, h, mn, 0)) * 1000
            dt_utc = f"{year_str}-{month_str}-{day_str} {hour_str}:{min_str}:00"

            o = row["Open"]
            h_p = row["High"]
            l = row["Low"]
            c = row["Close"]
            v = row["Volume"]
            current_lines.append(f"{ts_ms},{dt_utc},{o},{h_p},{l},{c},{v}\n")
            total_rows += 1

            if total_rows % 250000 == 0:
                print(f"[*] Streamed {total_rows:,} candles ({days_written:,} days written)...")

    # Flush final day
    if current_date and current_lines:
        day_file = base_path / current_year_str / current_month_str / f"XAUUSD_1m_{current_date}.csv"
        day_file.parent.mkdir(parents=True, exist_ok=True)
        with open(day_file, "w", encoding="utf-8") as f:
            f.write(HEADERS)
            f.writelines(current_lines)
        days_written += 1

    print(f"[✓] Done! Successfully wrote {days_written:,} daily CSV files ({total_rows:,} 1m candles).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, required=True)
    parser.add_argument("--end-year", type=int, required=True)
    args = parser.parse_args()
    run(args.start_year, args.end_year)
