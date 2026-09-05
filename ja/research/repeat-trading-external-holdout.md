---
layout: research
title: "リピート取引の外部ホールドアウト：リスク低下は収益上の優位性にはつながらなかった"
lang: ja
permalink: /ja/research/repeat-trading-external-holdout/
research_id: "PILOT-TRADING-001 / 2020–2022 holdout"
status: "完了 — 混合 / 判定保留"
updated: "2026-08-29"
topic: "トレード / 系統的戦略評価"
summary: "事前に固定した2つのdynamic-exit ruleを外部ホールドアウトで検証したところ、drawdown関連の負担は軽減しましたが、共通stopなしbenchmarkに対するmatched median P/Lは改善しませんでした。"
---

## 研究の問い

開発・stress検証では有望に見えたdynamic-exit ruleは、条件を再調整せず、未使用だった2020〜2022年へ持ち込んでも改善を再現するか。

より狭く言えば、**逆行trendによる損傷を減らすように見えるruleは、out-of-sampleでも収益性まで改善するのか。それともリスク低下と収益改善は別の効果なのか。**という問いです。

## 方法

有限のUSD/JPYリピート取引gridを、次の2つの事前固定したdynamic-exit variantと比較しました。

- benchmark: 共通stopなしのfinite grid
- `ret20 < -2%`: 20 active-day returnが-2%を下回ったら全決済
- `ret20 < 0%`: 20 active-day returnが0%を下回ったら全決済

benchmarkは±5円の有限grid、step 0.50円、take-profit 0.20円、1注文あたり1 unitとし、180日window終了時に残ったpositionはmark-to-marketで評価しました。

外部ホールドアウトは2020〜2022年です。比較定義と閾値を固定した後に開封し、最終datasetは**81 combined windows**で完全性チェックを通過しました。

主要指標にはterminal P/L、maximum drawdown、maximum open positions、maximum unrealized loss、ending open positions、exposureを含めました。リスク低下を収益改善と同一視しません。

ホールドアウト開封後、2020〜2022年をこれらの閾値やexit semanticsの再調整に使わないことも固定しました。

## 結果

2つのexit ruleはいくつかのリスク負担を減らしましたが、どちらもbenchmarkに対するmatched median P/Lを改善しませんでした。

<div class="result-summary-grid" aria-label="外部ホールドアウトの要約">
  <div class="result-stat"><span class="result-stat-label">ホールドアウトwindow</span><strong>81</strong><span>combined windows</span></div>
  <div class="result-stat"><span class="result-stat-label">評価期間</span><strong>2020–2022</strong><span>この検証では未使用だった期間</span></div>
  <div class="result-stat"><span class="result-stat-label">最終分類</span><strong>混合 / 判定保留</strong><span>リスクは改善、収益は改善せず</span></div>
</div>

### Matched median P/L delta

共通stopなしbenchmarkとの差です。負の値はdynamic-exit ruleのmatched median P/Lがbenchmarkより低かったことを示します。

<div class="metric-chart" role="img" aria-label="Matched median P/L delta。ret20 -2%未満はマイナス4.412、ret20 0%未満はマイナス12.340。">
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; -2%</code></div><div class="bar-track"><span class="bar-fill bar-negative" style="width:35.8%"></span></div><div class="metric-value">−4.412</div></div>
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; 0%</code></div><div class="bar-track"><span class="bar-fill bar-negative" style="width:100%"></span></div><div class="metric-value">−12.340</div></div>
</div>

### Median drawdown reduction

正の値はbenchmarkよりmedian drawdownが小さかったことを示します。

<div class="metric-chart" role="img" aria-label="Median drawdown reduction。ret20 -2%未満はプラス2.040、ret20 0%未満はプラス3.307。">
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; -2%</code></div><div class="bar-track"><span class="bar-fill bar-positive" style="width:61.7%"></span></div><div class="metric-value">+2.040</div></div>
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; 0%</code></div><div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div><div class="metric-value">+3.307</div></div>
</div>

### P/Lとdrawdownが同時に改善した割合

リスクだけでなく、matched comparisonで利益とdrawdownの両方が改善した割合を見ます。

<div class="metric-chart" role="img" aria-label="P/Lとdrawdownの同時改善率。ret20 -2%未満は3.7%、ret20 0%未満は13.6%。">
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; -2%</code></div><div class="bar-track"><span class="bar-fill bar-neutral" style="width:27.2%"></span></div><div class="metric-value">3.7%</div></div>
  <div class="metric-row"><div class="metric-label"><code>ret20 &lt; 0%</code></div><div class="bar-track"><span class="bar-fill bar-neutral" style="width:100%"></span></div><div class="metric-value">13.6%</div></div>
</div>

<p class="chart-note">棒の長さは各metric内で相対的にscaleしています。異なるグラフ同士では棒の長さではなく、表示された数値を比較してください。</p>

## ホールドアウトが重要だった理由

同じruleは2024年の開発期間でははるかに強く見えていました。180日matched-control分析のmedian P/Lは、no exitが**-33.638**、`ret20 < -2%`が**+7.800**、`ret20 < 0%`が**+7.768**でした。

これは仮説形成には有用でしたが、同じ広い開発文脈の中でruleを選択・stress testしていたため、独立した証拠ではありません。

未使用だった2020〜2022年を開くと解釈が変わりました。dynamic exitには一部の**risk-control価値**が残りましたが、どちらのruleも頑健なprofit-improving edgeと呼べる証拠にはなりませんでした。

## 解釈

この結果で重要なのは、混同しやすい2つの主張を分けたことです。

1. **ruleが damaging trendへのexposureを減らすことはあり得る。**
2. **それだけでは期待収益が増えることを意味しない。**

外部ホールドアウトでは、両variantがdrawdown関連の負担、最大建玉圧力、含み損負担、exposureなどを軽減しました。しかしmatched median P/Lは両方ともbenchmarkを下回りました。

したがって、最も強く支持される結論はdynamic exitが単純に「良い」「悪い」というものではありません。**防御的な価値は確認できたものの、このholdoutでは一貫した収益改善へ一般化しなかった**、という結論です。

この結果だけを根拠に実運用のposition sizeを増やす根拠も弱くなります。

## 限界と不確実性

- 1つのstrategy family、1つのinstrument、1組のfrozen rule、1つのhistorical holdout periodに対する結果です。
- backtestやreference-market resultはbrokerでの実約定結果と同じではありません。
- spread、slippage、swap、必要資本、実装詳細はreal-world outcomeを大きく変える可能性があります。
- 混合・判定保留という結果は、収益性のあるリピート取引variantが存在しない証明ではありません。
- 2020〜2022年は、これらのruleを新たに調整したversionに対する untouched test setとして再利用できません。
- trend/regime stratificationは別の研究課題であり、この結果から推論していません。

## 公開する根拠の範囲

公開主張は、このページに示したレビュー済みsummary statisticに限定します。再現code、詳細CSV、execution log、broker-side mechanics recordは内部研究archiveに残し、このサイトでは公開していません。

ライブposition、account information、現在のtrade decisionも公開しません。

## 実務上の現在位置

この結果は、実運用数量を増やす根拠にはなりません。次の研究では、すでに開封したholdout ruleを遡って変更せずに、trend/regime情報がP/Lやrisk variationの一部を説明できるかを検証します。

*これは研究記録であり、投資助言ではありません。過去データやシミュレーションの結果は将来のperformanceを保証しません。*
