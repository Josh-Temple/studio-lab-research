#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import os
import statistics
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OUTPUT = Path("assets/data/market/latest.json")
SYMBOLS = [
    ("EUR/USD", "EUR/USD", "FX"),
    ("USD/JPY", "USD/JPY", "FX"),
    ("SPY", "S&P 500 proxy", "Equity index proxy"),
    ("QQQ", "Nasdaq-100 proxy", "Equity index proxy"),
    ("GLD", "Gold proxy", "Precious metal proxy"),
    ("USO", "WTI crude proxy", "Energy proxy"),
    ("UUP", "US dollar proxy", "USD proxy"),
    ("TLT", "Long US Treasury proxy", "Rates proxy"),
]

def as_float(v: Any) -> float | None:
    try:
        x=float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None

def ema(values: list[float], period: int) -> float | None:
    if len(values) < period:
        return None
    cur=statistics.fmean(values[:period])
    a=2/(period+1)
    for v in values[period:]:
        cur=a*v+(1-a)*cur
    return cur

def rsi(values: list[float], period: int=14) -> float | None:
    if len(values) <= period:
        return None
    gains=[]; losses=[]
    for a,b in zip(values, values[1:]):
        d=b-a
        gains.append(max(d,0)); losses.append(max(-d,0))
    ag=statistics.fmean(gains[:period]); al=statistics.fmean(losses[:period])
    for g,l in zip(gains[period:], losses[period:]):
        ag=((period-1)*ag+g)/period
        al=((period-1)*al+l)/period
    if al == 0:
        return 100.0
    rs=ag/al
    return 100-(100/(1+rs))

def atr(rows: list[dict[str,float]], period: int=14) -> float | None:
    if len(rows) <= period:
        return None
    trs=[]
    for prev,cur in zip(rows, rows[1:]):
        trs.append(max(cur["high"]-cur["low"], abs(cur["high"]-prev["close"]), abs(cur["low"]-prev["close"])))
    out=statistics.fmean(trs[:period])
    for tr in trs[period:]:
        out=((period-1)*out+tr)/period
    return out

def pct(new: float, old: float) -> float | None:
    return None if old == 0 else (new/old-1)*100

def trend(close: float, e20: float | None, e50: float | None) -> str:
    if e20 is None or e50 is None:
        return "insufficient"
    if close > e20 > e50:
        return "up"
    if close < e20 < e50:
        return "down"
    return "mixed"

def write_snapshot(data: dict[str,Any]) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    tmp=OUTPUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(OUTPUT)

def main() -> int:
    generated=datetime.now(timezone.utc).isoformat()
    key=os.environ.get("TWELVE_DATA_API_KEY","").strip()
    if not key:
        write_snapshot({
            "schema_version":"0.1",
            "generated_at_utc":generated,
            "scope":"public_observation_only",
            "provider":"Twelve Data",
            "market":[],
            "health":{"market":{"status":"unavailable","errors":[{"error":"TWELVE_DATA_API_KEY is not configured for this repository."}]}}
        })
        print("Market snapshot unavailable: secret is not configured.")
        return 0

    try:
        params=urllib.parse.urlencode({
            "symbol":",".join(s for s,_,_ in SYMBOLS),
            "interval":"1h",
            "outputsize":"80",
            "timezone":"UTC",
            "apikey":key,
        })
        req=urllib.request.Request(
            "https://api.twelvedata.com/time_series?"+params,
            headers={"User-Agent":"StudioLab-PublicMarket/0.1"},
        )
        with urllib.request.urlopen(req, timeout=15) as res:
            raw=json.loads(res.read().decode("utf-8"))

        if isinstance(raw,dict) and raw.get("status")=="error":
            raise RuntimeError(str(raw.get("message") or "provider_error"))
        batch=raw.get("data") if isinstance(raw,dict) and isinstance(raw.get("data"),dict) else raw
        if not isinstance(batch,dict):
            raise RuntimeError("unexpected_provider_payload")

        market=[]; errors=[]
        for symbol,label,category in SYMBOLS:
            payload=batch.get(symbol)
            if not isinstance(payload,dict):
                errors.append({"symbol":symbol,"error":"missing_symbol_payload"})
                market.append({"symbol":symbol,"label":label,"category":category,"status":"error","error":"missing_symbol_payload"})
                continue
            if payload.get("status")=="error" or payload.get("code"):
                msg=str(payload.get("message") or "provider_error")
                errors.append({"symbol":symbol,"error":msg})
                market.append({"symbol":symbol,"label":label,"category":category,"status":"error","error":msg})
                continue

            values=payload.get("values")
            rows=[]
            if isinstance(values,list):
                for row in reversed(values):
                    o=as_float(row.get("open")); h=as_float(row.get("high")); l=as_float(row.get("low")); c=as_float(row.get("close"))
                    if None not in (o,h,l,c):
                        rows.append({"datetime":row.get("datetime"),"open":o,"high":h,"low":l,"close":c})
            if len(rows) < 51:
                msg=f"insufficient_rows:{len(rows)}"
                errors.append({"symbol":symbol,"error":msg})
                market.append({"symbol":symbol,"label":label,"category":category,"status":"error","error":msg})
                continue

            closes=[r["close"] for r in rows]
            latest=rows[-1]
            e20=ema(closes,20); e50=ema(closes,50); r14=rsi(closes,14); a14=atr(rows,14)
            market.append({
                "symbol":symbol,
                "label":label,
                "category":category,
                "status":"ok",
                "timestamp_utc":latest["datetime"],
                "close":round(latest["close"],6),
                "return_1h_pct":round(pct(closes[-1],closes[-2]),4),
                "return_24h_pct":round(pct(closes[-1],closes[-25]),4),
                "ema20":round(e20,6) if e20 is not None else None,
                "ema50":round(e50,6) if e50 is not None else None,
                "rsi14":round(r14,2) if r14 is not None else None,
                "atr14_pct":round(a14/latest["close"]*100,4) if a14 is not None and latest["close"] else None,
                "trend":trend(latest["close"],e20,e50),
            })
        status="ok" if not errors else ("partial" if any(x.get("status")=="ok" for x in market) else "error")
        write_snapshot({
            "schema_version":"0.1",
            "generated_at_utc":generated,
            "scope":"public_observation_only",
            "provider":"Twelve Data",
            "market":market,
            "health":{"market":{"status":status,"errors":errors}},
            "boundaries":[
                "Descriptive market observation only",
                "No broker connection or order execution",
                "No live position or account information",
                "No automated trade recommendation"
            ]
        })
        print(f"market_status={status} ok_symbols={sum(1 for x in market if x.get('status')=='ok')}")
    except Exception as exc:
        write_snapshot({
            "schema_version":"0.1",
            "generated_at_utc":generated,
            "scope":"public_observation_only",
            "provider":"Twelve Data",
            "market":[],
            "health":{"market":{"status":"error","errors":[{"error":f"{type(exc).__name__}: {exc}"}]}}
        })
        print(f"Market snapshot failed safely: {type(exc).__name__}: {exc}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
