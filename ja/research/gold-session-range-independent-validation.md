---
layout: research
title: "GOLDのセッションレンジ持続性：2024年の強い関係は2021年の独立検証では確認できなかった"
lang: ja
permalink: /ja/research/gold-session-range-independent-validation/
research_id: "PILOT-TRADING-001 / GOLD 2021 independent validation"
status: "完了 — 独立検証は判定保留"
updated: "2026-09-06"
topic: "トレード / GOLD / ボラティリティ持続性"
summary: "2024年の開発データで強く見えたセッションレンジの正の関係を、独立した2021年データで検証しました。推定値は正でしたが小さく、固定済みの95% block-bootstrap区間はゼロをまたぎました。"
---

## 研究の問い

2024年の開発データで強く見えた「前セッションの値幅と次セッションの値幅の正の関係」は、独立した2021年のGOLDデータでも確認できるか。

これはボラティリティの持続性を調べる研究です。**方向予測、エントリー、決済、収益性、完成した売買手法を直接検証するものではありません。**

## 独立検証のきっかけになった2024年の結果

2024年の開発研究では、封印済みの隣接セッション60組を使用しました。前セッションと次セッションの値幅について、Spearmanの順位相関は次のとおりでした。

<div class="result-summary-grid" aria-label="開発結果と独立検証結果の要約">
  <div class="result-stat">
    <span class="result-stat-label">2024年 開発</span>
    <strong>ρ = 0.5621</strong>
    <span>封印済み60組</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2021年 独立検証</span>
    <strong>ρ = 0.0626</strong>
    <span>有効な隣接198組</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2021年 bootstrap 95%区間</span>
    <strong>−0.1283 ～ 0.1439</strong>
    <span>10,000回すべて有効</span>
  </div>
</div>

2024年の結果は「追加検証に値する」と判断されたもので、独立した証拠や売買上の優位性が確立したという意味ではありません。

## 独立検証の方法

2021年1年間について、Dukascopy公式Public Historical Data Exportから取得した **XAU/USD・BID・M1・UTC** データを使いました。

結果を見る前に実行条件を固定し、構造的に完全なセッションだけを採用しました。欠損行の補修、補間、resample、集約、synthetic rowの生成は行っていません。

最終的な検証対象は次のとおりです。

- 公式export経路から取得した平日 **261日分** のsource file
- 構造条件を満たした **227セッション**
- 有効な隣接セッション **198組**
- block length 5のcircular moving-block bootstrap **10,000 / 10,000回すべて有効**

分類には通常のSpearman p値ではなく、事前に固定した95% bootstrap区間を使いました。

## 結果

2021年のSpearman推定値は **ρ = 0.0625556** でした。固定済みの95% circular moving-block-bootstrap区間は **[−0.1283186, 0.1439162]** でした。

区間がゼロをまたいだため、事前に決めた分類は **INCONCLUSIVE（判定保留）** です。

したがって、2024年に見えた強い関係を、2021年の独立検証で統計的に支持された形で確認することはできませんでした。一方で、ボラティリティ持続性そのものが存在しないと証明した結果でもありません。

## 研究上の判断が変わった理由

2024年の開発結果だけを見ると、前セッションのhigh-low rangeが独立した予測情報を持つ可能性が残っていました。

その後、次の2点がこの解釈を弱めました。

1. 2021年の独立検証で、2024年の強い関係を確認できなかったこと。
2. 別の2024年増分比較で、前セッションのrealized varianceだけを使うbaselineへ前セッションrangeを追加すると、pooled chronological out-of-fold MSEがわずかに悪化したこと。

これらを合わせ、現在は**前セッションのhigh-low rangeを独立した予測メカニズムとして救済する研究の優先度を下げています。** 2021年の結果を見た後に条件を変え、同じ期間で仮説を救済する方向には進みません。

より広い意味でのボラティリティ持続性は依然として考えられます。ただし、rawな前セッションrange自体が単独の売買上の優位性として確認されたわけではありません。

## 結果を見た後のルール

2021年は、このメカニズムについて既に使用済みの検証期間です。今後この結果を使って閾値、セッション規則、block length、指標などを調整し、その調整後の研究で2021年を「未使用のホールドアウト」と呼ぶことはしません。

現時点では、range persistenceを救済するための新しい自動的なholdout追加も優先していません。

## 現在の研究方向

次に優先しているGOLD研究は、**水平線付近での反応を、対応するpseudo / non-level controlと比較するdevelopment falsification**です。

現在はまだ事前設計を閉じている段階です。主な設計要素として、60分rolling extremaによるsupport/resistance zone、15分のreaction horizon、2024年をdevelopment-onlyとして使う方針などが固定されています。

**水平線研究の市場結果は、まだこのサイトで公開できる段階まで観測していません。** 残る決定的な設計条件を閉じるまでは、仮説のまま扱います。

## 限界と不確実性

- 2021年の結果は判定保留であり、真の相関が厳密にゼロだと示したものではありません。
- 隣接pairでは同じセッションが再利用されるため、観測を独立とは扱っていません。局所的な依存を保つためblock-bootstrapを使いました。
- この結果が扱うのはセッション値幅の関係だけです。方向予測、執行可能性、P/L、drawdown、Sharpe、勝率、position sizingは確立していません。
- 過去のreference market dataと実際のbroker執行は同じではありません。
- 研究優先度の変更は、この独立検証と別の増分baseline比較を合わせた判断です。すべてのボラティリティ戦略が成立しないことを示すものではありません。

## 根拠の公開範囲

公開データは[Dukascopy Public Historical Data Export](https://widgets.dukascopy.com/en/historical-data-export)から取得しました。

内部研究アーカイブには、固定済みhandoff、日付ごとのraw identity、evidence CSV、bootstrap設定、検証記録、Researcherの統合ノートを保存しています。これらの運用artifactは、この公開サイトへ自動転載していません。

*これは研究記録であり、投資助言ではありません。過去データやシミュレーションの結果は将来の成果を保証しません。*
