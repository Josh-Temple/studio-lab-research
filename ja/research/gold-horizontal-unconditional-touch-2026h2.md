---
layout: research
title: "GOLD水平線：未使用の2026H2検証では「タッチだけ」の効果を確認できなかった"
lang: ja
permalink: /ja/research/gold-horizontal-unconditional-touch-2026h2/
research_id: "PILOT-TRADING-001 / 2026H2 unconditional touch replication"
status: "完了 — 無条件タッチ仮説は支持されず"
updated: "2026-09-15"
topic: "トレード / GOLD水平線"
summary: "事前登録した未使用60セッションで、水平線タッチ後15分の方向調整済み平均リターンは−1.379 bps、95% session-clustered bootstrap区間は−1.909〜−0.862 bpsでした。無条件タッチ仮説は支持されず、同じ標本で救済的な調整は行わず研究線を閉じました。"
---

## 現在の結論

事前登録した**未使用の2026H2サンプルでは、水平線にタッチしただけで正の方向リターンが生じるという仮説は支持されませんでした**。

固定した主要平均は **−1.379 bps**、session単位の95% bootstrap区間は **[−1.909, −0.862] bps**で、区間全体が0を下回りました。事前に定めた判定では **NO_UNCONDITIONAL_TOUCH_SUPPORT** です。

これは、それまでのGOLD水平線研究にとって重要な更新です。過去の複数期間で確認された方向反応差は、その定義と比較条件における観測結果として残ります。一方、それだけでは「未使用データでも、水平線への無条件タッチから正のリターンを得られる」とは言えませんでした。

## この検証を行った理由

それまでの研究では、rolling extremaから作る水平線と直近価格の対照群を比べた15分方向反応差が、2024年・2022年・2020年・2025年初の4期間で同じ方向に再現しました。2019年の履歴BID/ASKを使ったquote-crossing検証でも、固定した仕様では正の結果でした。

しかし、その後の使用済み2026H1戦略標本では、タッチから確認entryまでの価格変化は平均で正だった一方、entry後の価格変化は負でした。そこで残った問いをさらに単純化し、**確認条件でeventが選別される前の「タッチそのもの」に正の方向リターンがあるか**を、別の未使用期間で確認しました。

2026H2では、使用済み標本を調整するのではなく、この問いをそのまま独立して検証しています。

## 固定した評価条件

今回の結果では、事前登録した境界を維持しました。

- 2026H2の**60セッション**を固定
- 固定済みM1 / raw Tickのsource identityとcoverage確認を通過
- 2026H2の無条件タッチ結果は事前に未計算
- タッチeventは **4,788件**
- 主要計算に入った評価可能eventは **4,786件**
- **2件**は固定quote ruleで必要な+15分quoteが得られず利用不可
- 利用不可eventは補完せず、providerも変更しない
- session単位で **10,000回bootstrap**

結果を見た後にprotocol、sample、parameter、時間帯、LONG/SHORT、regime、売買ruleを探索・変更していません。

## 結果

<div class="result-summary-grid" aria-label="2026H2無条件水平線タッチ再現結果">
  <div class="result-stat">
    <span class="result-stat-label">主要平均</span>
    <strong>−1.379 bps</strong>
    <span>15分の方向調整済みリターン</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">95% clustered区間</span>
    <strong>−1.909〜−0.862 bps</strong>
    <span>session単位10,000回bootstrap</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">正のevent比率</span>
    <strong>46.95%</strong>
    <span>評価可能4,786件</span>
  </div>
</div>

主要中央値は **−0.649 bps**でした。記述的にはLONGとSHORTもともに負で、LONG平均は **−1.750 bps**、95%区間 **[−2.491, −0.962]**、SHORT平均は **−0.968 bps**、95%区間 **[−1.803, −0.122]**でした。

ただし、これらは副次的な記述です。「逆方向に売買すればよい」という根拠にはしていません。

保存済みevent-level出力から独立に再計算し、event数、主要平均、bootstrap区間が完全一致することも確認しています。

## 解釈

今回の結果により、公開上の根拠の置き方も変わります。

第一に、過去の水平線研究で見えた正の反応を、そのまま無条件タッチentryへ持ち込むことはできません。2026H1で見えた正のtouch-to-outcome診断は、**後からconfirmationを満たしたeventだけが選ばれる選択効果**と整合します。

第二に、この結果は「水平線に関するあらゆる仕組みが無効」という意味でもありません。過去の研究は別の構成・対照群を評価しており、2019年のexecution-aware履歴検証もその固定条件では正でした。今回確認できたのは、より限定された重要な事実です。**事前登録した無条件タッチ仮説は、未使用サンプルで支持されませんでした。**

## この結果を受けた判断

無条件タッチの再現研究線は、**支持されず終了**とします。

使用済みH1/H2標本を使って、confirmation delay、threshold、時間帯、方向filterなどを後から最適化して結果を救済しません。また、この結果を見て同じ標本上で新しいtouch-entry ruleを作ることもしません。

別の仮説を試す場合は、別の研究として事前登録し、さらに未使用またはprospectiveなデータで検証します。

このnegative resultの価値は、複数期間で再現して見えた市場ストーリーであっても、より厳しい未使用データ検証と合わなければ、そのまま失敗として受け入れた点にあります。

## この結果からは言えないこと

今回の研究だけでは、以下は確認できません。

- 逆方向の売買戦略に収益性があること
- 負のリターンが生じた原因
- 実際のbroker約定やfill quality
- すべてのsupport / resistance・水平線手法が無効であること
- 他銘柄・他horizonでも同じになること
- 新しい売買指示

## 公開範囲

このページでは、レビュー済みの要約統計と研究判断だけを公開しています。raw market data、event-level ledger、内部Work Order、credential、現在ポジション、現在の売買判断は公開しません。

*これは研究記録であり、投資助言ではありません。過去データによる研究は将来の収益性を示すものではありません。*