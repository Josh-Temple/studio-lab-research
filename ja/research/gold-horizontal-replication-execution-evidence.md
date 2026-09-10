---
layout: research
title: "GOLD水平線：方向反応は3期間で再現し、2019年の実測BID/ASK検証でも正の結果"
lang: ja
permalink: /ja/research/gold-horizontal-replication-execution-evidence/
research_id: "PILOT-TRADING-001 / GOLD horizontal replication and execution"
status: "再現確認 / execution-aware検証 — 追加検証候補"
updated: "2026-09-10"
topic: "トレード / GOLD水平線"
summary: "60分rolling extremaを使う水平線の方向反応は2024年、2022年、2020年の3期間で正の差を示し、2019年の実測BID/ASKを使った履歴検証でもreal側の平均リターンが正でした。ただし、継続的なlive trading edgeが確認されたわけではありません。"
---

## 現在の結論

GOLD水平線の研究は、単一の開発結果を確認する段階から先へ進みました。

固定したXAU/USD BID M1のprotocolでは、直前60分のrolling extremaに接触した後の15分方向反応が、直近の実測非extreme価格を使った対照群より多くなる現象が、**2024年・2022年・2020年の3つの離れた期間で再現**しました。さらに、実測のBID/ASKを使って売買可能時点をより厳しく扱った2019年の検証でも、real側の平均リターンは正でした。

研究上の判定は引き続き **PROMISING_FOR_FURTHER_TEST（追加検証に進める候補）**です。これは「利益が出る戦略として完成した」という意味ではありません。

## 3期間で再現した方向反応

3つの方向反応テストでは、水平線の定義と比較方法を実質的に変更していません。

<div class="result-summary-grid" aria-label="GOLD水平線の再現結果まとめ">
  <div class="result-stat">
    <span class="result-stat-label">2024年 開発</span>
    <strong>+26.55ポイント</strong>
    <span>95% CI +21.23〜+31.82</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2022年 独立検証</span>
    <strong>+23.79ポイント</strong>
    <span>95% CI +18.73〜+29.02</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">2020年 robustness検証</span>
    <strong>+25.44ポイント</strong>
    <span>95% CI +20.74〜+30.23</span>
  </div>
</div>

<div class="metric-chart" role="img" aria-label="real minus controlの15分方向反応差。2024年開発は26.55ポイント、2022年独立検証は23.79ポイント、2020年robustness検証は25.44ポイント。">
  <div class="metric-row">
    <div class="metric-label">2024年 開発</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div>
    <div class="metric-value">+26.55 pt</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">2022年 検証</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:89.6%"></span></div>
    <div class="metric-value">+23.79 pt</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">2020年 検証</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:95.8%"></span></div>
    <div class="metric-value">+25.44 pt</div>
  </div>
</div>

<p class="chart-note">3本のバーは同じ「セッション単位のreal反応率 − control反応率」を比較しています。正確な推定値と95% bootstrap区間は上に記載しています。方向反応率は売買リターンではありません。</p>

2022年の独立検証は設計妥当性の基準を通過し、60セッションすべてが比較に参加しました。real側のセッション反応率は0.790698、対照群は0.550132で、差は **+23.792ポイント**。95% bootstrap区間は **[+18.734, +29.020]ポイント**でした。

2020年のrobustness検証も60セッションすべてが参加し、主要差は **+25.439ポイント**、95% bootstrap区間は **[+20.741, +30.230]ポイント**でした。

3期間の推定値が近いことだけで、あらゆる相場環境で不変だとは言えません。ただし、2024年に見えた差がこの1期間だけの現象だった可能性は、同じprotocolの範囲ではかなり下がりました。

## 追加した条件はベースラインを改善しなかった

水平線単独のメカニズムが独立検証を通過した後、単純な条件を1つずつ追加する検証も行いました。確認済みの研究記録では、テストした60分trend context、New York時間帯、前セッションのvolatility stateはいずれも、水平線だけのベースラインを超える増分情報を示しませんでした。別系統のrecent session-direction continuationも棄却または優先度低下となっています。

このnegative resultには意味があります。ベースの現象が再現したからといって、指標を重ねればさらに良くなるとは限らないため、現在は水平線メカニズムをできるだけ単純なまま検証しています。

## 2019年のexecution-aware検証

次に確認したのは、より厳しい履歴上のquote-crossing条件でも結果が残るかです。

2019年の検証では、M1の接触barがすべて観測できた後にsignalが利用可能になるものとし、その後の**実測BID/ASK quote**をentryとexitに使いました。LongはASKで入りBIDで出る、ShortはBIDで入りASKで出るという扱いです。exitはentry tickから15分後で、合成spread、commission、追加slippage、latency、market impact、fill probabilityは加えていません。

当初は60セッションを予定していましたが、1年分の構造確認で適格だったのは57セッションでした。そのため、**2019年のreturnを一切計算・確認する前に**、57セッションすべてを使うよう前向きに修正しています。この点は元の事前登録より条件が変わったため、結果の限界として明示しています。

<div class="result-summary-grid" aria-label="2019年execution-aware検証まとめ">
  <div class="result-stat">
    <span class="result-stat-label">real平均リターン</span>
    <strong>+1.189 bps</strong>
    <span>95% CI +0.528〜+1.889</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">control平均</span>
    <strong>−2.309 bps</strong>
    <span>直近価格の対照群</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">real − control</span>
    <strong>+3.498 bps</strong>
    <span>95% CI +2.531〜+4.500</span>
  </div>
</div>

57セッションすべてが比較に参加し、事前に定めた2つの主要推定値はいずれも正、95% bootstrap区間の下限も0を上回りました。そのため、固定済みの支持条件を満たしています。

特に重要なのは、対照群との差だけでなく**real側の平均リターン自体が正だったこと**です。ただし、これは1つの履歴期間でのquote-crossing proxyです。実際のbroker約定を再現したものではありません。

## 現在の最前線：2018年でexecution-aware再現を確認中

次の判断段階は、同じメカニズム、quote side、15分horizon、control、bootstrap、判定ルールを固定したまま行う**2018年の独立execution-aware再現**です。

最新の保存済み進捗では、必要な最初の60適格セッションのうち**50セッションまで構造確認済み**で、7つの候補日が固定ルールにより除外されています。その後、公式Dukascopy Historical Data Exportの応答が2018-03-21候補で止まりました。

この時点では、2018年のsignal event、quote-crossing return、主要推定値、bootstrap区間、研究判定は**一切計算・確認していません**。後継handoffは同じ境界から再開する設計になっており、データ元や研究条件を変更していません。

したがって、2018年の研究は現時点で**進行中・結果未観測**です。

## まだ確認できていないこと

現在の根拠だけでは、以下は確認できません。

- 実際のbrokerでの約定
- broker固有のspread挙動
- commission、swap、実測quoteを超えるslippage
- latency、order rejection、market impact、fill probability
- position sizing、drawdown、tail risk、capacity
- live performanceや現在の相場環境での有効性
- 他銘柄への転用
- 継続的に利益が出る売買ルール

現在公開できる主張は、**固定したGOLDのprotocolで短期方向反応の差が複数期間に再現し、2019年のexecution-aware履歴検証でも正の結果が出た**というところまでです。売買指示ではありません。

## 公開範囲

このページでは、レビュー済みの要約統計と現在の研究判断だけを公開しています。raw file、manifest、内部のWork Order、詳細な取得ログ、credential、現在ポジション、売買判断は公開サイトには載せません。

*これは研究記録であり、投資助言ではありません。過去データでの検証結果は将来の収益性を示すものではありません。*