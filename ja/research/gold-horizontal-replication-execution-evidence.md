---
layout: research
title: "GOLD水平線：方向反応は再現したが、後続の無条件タッチ検証はnegative"
lang: ja
permalink: /ja/research/gold-horizontal-replication-execution-evidence/
research_id: "PILOT-TRADING-001 / GOLD horizontal replication and execution"
status: "混合した根拠 — 反応差は再現、無条件タッチは支持されず"
updated: "2026-09-15"
topic: "トレード / GOLD水平線"
summary: "水平線の方向反応率差は4つの履歴期間で正となり、2019年のquote-crossing検証も固定条件では正でした。一方、後続の事前登録済み未使用2026H2検証では無条件タッチの効果は支持されず、公開上の主張範囲を狭めました。"
---

## 現在の結論

GOLD水平線研究には、現在 **再現したpositiveなsignal-level evidenceと、重要な未使用データのnegative resultの両方**があります。

過去の固定した反応率protocolでは、直前60分のrolling extremaへの接触後に定義した15分方向反応率が、直近価格の対照群より高くなる差が、2024年開発・2022年独立検証・2020年robustness・2025年初robustnessの4期間で同じ方向に再現しました。2019年の履歴BID/ASKを使ったquote-crossing検証も、その固定仕様では正の結果でした。

これらは研究記録として残ります。ただし、現在の状態を単純に「追加検証候補」とだけ表現するのは適切ではなくなりました。後続研究では、**未使用の2026H2データ**を使い、より厳しい問いを事前登録しました。水平線に無条件でタッチしただけで15分の方向リターンが正になるかを検証したところ、主要平均は **−1.379 bps**、session単位の95%区間は **[−1.909, −0.862] bps**でした。

したがって現在公開できる主張は、より狭くなります。**過去のsignal-levelな方向反応差は複数期間で再現した一方、未使用データでは無条件タッチedgeを確認できなかった**、というところまでです。

<p class="card-links"><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">2026H2の未使用データ検証を読む</a></p>

## 過去4期間で再現した方向反応差

過去の反応率テストでは、水平線の定義と比較方法を実質的に変更していません。

<div class="result-summary-grid" aria-label="GOLD水平線の過去4期間の方向反応差">
  <div class="result-stat"><span class="result-stat-label">2024年 開発</span><strong>+26.55ポイント</strong><span>95% CI +21.23〜+31.82</span></div>
  <div class="result-stat"><span class="result-stat-label">2022年 独立検証</span><strong>+23.79ポイント</strong><span>95% CI +18.73〜+29.02</span></div>
  <div class="result-stat"><span class="result-stat-label">2020年 robustness</span><strong>+25.44ポイント</strong><span>95% CI +20.74〜+30.23</span></div>
  <div class="result-stat"><span class="result-stat-label">2025年初 robustness</span><strong>+23.66ポイント</strong><span>95% CI +19.43〜+28.02</span></div>
</div>

<div class="metric-chart" role="img" aria-label="過去4期間のreal minus controlの15分方向反応差。2024年26.55ポイント、2022年23.79ポイント、2020年25.44ポイント、2025年初23.66ポイント。">
  <div class="metric-row"><div class="metric-label">2024年 開発</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div><div class="metric-value">+26.55 pt</div></div>
  <div class="metric-row"><div class="metric-label">2022年 検証</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:89.6%"></span></div><div class="metric-value">+23.79 pt</div></div>
  <div class="metric-row"><div class="metric-label">2020年 robustness</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:95.8%"></span></div><div class="metric-value">+25.44 pt</div></div>
  <div class="metric-row"><div class="metric-label">2025年初 robustness</div><div class="bar-track"><span class="bar-fill bar-positive" style="width:89.1%"></span></div><div class="metric-value">+23.66 pt</div></div>
</div>

<p class="chart-note">4本のバーは同じ履歴上の「session単位のreal反応率 − control反応率」を比較しています。方向反応率は売買リターンではありません。</p>

2022年は60/60セッションが比較に参加し、real-control差は **+23.792ポイント**でした。2020年も60/60セッションが参加し、**+25.439ポイント**でした。2025年初は結果計算前に最初の60適格セッションを固定し、**+23.663ポイント**でした。対象期間は2025-01-02〜2025-04-11なので、2025年通年の検証ではありません。

4期間の推定値が近いことは、その特定の反応率指標が1つの時期だけの偶然だった可能性を下げました。ただし、異なるentry ruleやevent選択を経ても同じ情報が残ることまでは示していませんでした。

## 2019年のexecution-aware履歴検証

2019年では、M1の接触barが観測可能になった後の実測BID/ASK quoteを使いました。LongはASKでentryしBIDでexit、ShortはBIDでentryしASKでexitし、horizonは15分です。合成spread、commission、追加slippage、latency、market impact、fill probabilityは加えていません。

当初は60セッションを予定していましたが、構造確認で適格だったのは57セッションでした。そのため、2019年のreturnを計算・確認する前に57セッションすべてを使うよう前向きに修正しています。元の事前登録から条件が変わった点は限界として残ります。

<div class="result-summary-grid" aria-label="2019年execution-aware検証まとめ">
  <div class="result-stat"><span class="result-stat-label">real平均リターン</span><strong>+1.189 bps</strong><span>95% CI +0.528〜+1.889</span></div>
  <div class="result-stat"><span class="result-stat-label">control平均</span><strong>−2.309 bps</strong><span>直近価格の対照群</span></div>
  <div class="result-stat"><span class="result-stat-label">real − control</span><strong>+3.498 bps</strong><span>95% CI +2.531〜+4.500</span></div>
</div>

57セッションすべてが参加し、固定した支持条件を満たしました。barだけの反応率比較よりexecutionに近い根拠ですが、実際のbroker約定ではなく履歴quote-crossing proxyです。

## 後続検証で主張範囲が変わった

その後は、見えていた差がどこで失われるかを調べました。

使用済み2026H1戦略標本では、タッチから後のconfirmation entryまでの平均価格経路は有利だった一方、entry後の平均価格経路は不利でした。この診断は、confirmationを満たすeventだけが選ばれる過程に意味がある可能性を示しました。ただし、H1は使用済み標本なので探索的な診断です。

そこで同じH1をさらに調整するのではなく、無条件タッチ仮説を事前登録して未使用2026H2へ移しました。固定した60セッション・評価可能 **4,786 event**で、15分の方向調整済み平均リターンは **−1.379 bps**、95%区間はすべて0を下回り、判定は **NO_UNCONDITIONAL_TOUCH_SUPPORT** でした。

これは、結果同士を無理に同じ結論へ合わせなくても整合的に説明できます。過去の「real対controlの反応率差」が再現することと、「すべてのタッチを無条件で使ったリターン」が正になることは、関連はしていても同じ推定対象ではありません。

## 救済的な調整は行わない

過去には60分trend context、New York時間帯、前session volatilityなどの単純な追加条件も、水平線単独baselineを超える明確な増分情報を示しませんでした。今回のH2 negative resultを受けても、使用済み標本でより良いconfirmation delay、時間帯、方向filter、thresholdを探しません。

無条件タッチ研究線は「支持されず終了」とします。別のmechanismを検証する場合は、新しい仮説として結果を見る前に条件を固定し、別の未使用またはprospectiveデータで確認します。

## 2018年execution-aware再現は保留のまま

別系統の2018年execution-aware再現では、結果を見る前に最初の60適格セッションを固定済みです。quote取得manifestは2,066 event-hour-side単位を必要とし、手動取得経路の優先度を下げる前に23単位を保存しています。

2018年のreturnは未観測です。残り約2,000件を1時間・片側ずつ手動取得すると研究より取得作業が支配的になるため、現在の経路は保留しました。これは2018年仮説のpositive / negative evidenceではありません。

## まだ確認できていないこと

研究全体からも、以下は確認できません。

- 継続的に利益が出る水平線売買rule
- H2 negative resultを逆向きに使う戦略の収益性
- 実際のbroker約定やbroker固有のspread挙動
- commission、swap、latency、order rejection、market impact、fill probability
- positive / negativeな結果が生じた因果機構
- 他銘柄・他horizonへの転用
- 現在の相場でのlive performance

## 公開範囲

このページでは、レビュー済みの要約統計と研究判断だけを公開しています。raw file、manifest、event-level ledger、内部Work Order、credential、現在ポジション、現在の売買判断は公開しません。

*これは研究記録であり、投資助言ではありません。過去データによる検証は将来の収益性を示すものではありません。*