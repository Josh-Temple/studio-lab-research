---
layout: research
title: "GOLD水平線：方向反応は4期間で再現し、2019年の実測BID/ASK検証でも正の結果"
lang: ja
permalink: /ja/research/gold-horizontal-replication-execution-evidence/
research_id: "PILOT-TRADING-001 / GOLD horizontal replication and execution"
status: "再現確認 / execution-aware検証 — 追加検証候補"
updated: "2026-09-14"
topic: "トレード / GOLD水平線"
summary: "60分rolling extremaを使う水平線の方向反応は2024年、2022年、2020年、2025年初の4期間で正の差を示し、2019年の実測BID/ASKを使った履歴検証でもreal側の平均リターンが正でした。ただし、継続的なlive trading edgeが確認されたわけではありません。"
---

## 現在の結論

GOLD水平線の研究は、単一の開発結果を確認する段階から先へ進みました。

固定したXAU/USD BID M1のprotocolでは、直前60分のrolling extremaに接触した後の15分方向反応が、直近の実測非extreme価格を使った対照群より多くなる現象が、**2024年・2022年・2020年・2025年初の4つの離れた期間で再現**しました。さらに、実測BID/ASKを使って売買可能時点をより厳しく扱った2019年の検証でも、real側の平均リターンは正でした。

研究上の判定は引き続き **PROMISING_FOR_FURTHER_TEST（追加検証に進める候補）**です。これは「利益が出る戦略として完成した」という意味ではありません。

## 4期間で再現した方向反応

4つの方向反応テストでは、水平線の定義と比較方法を実質的に変更していません。

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
  <div class="result-stat">
    <span class="result-stat-label">2025年初 robustness検証</span>
    <strong>+23.66ポイント</strong>
    <span>95% CI +19.43〜+28.02</span>
  </div>
</div>

<div class="metric-chart" role="img" aria-label="real minus controlの15分方向反応差。2024年開発は26.55ポイント、2022年独立検証は23.79ポイント、2020年robustness検証は25.44ポイント、2025年初robustness検証は23.66ポイント。">
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
  <div class="metric-row">
    <div class="metric-label">2025年初 検証</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:89.1%"></span></div>
    <div class="metric-value">+23.66 pt</div>
  </div>
</div>

<p class="chart-note">4本のバーは同じ「セッション単位のreal反応率 − control反応率」を比較しています。正確な推定値と95% bootstrap区間は上に記載しています。方向反応率は売買リターンではありません。</p>

2022年の独立検証は設計妥当性の基準を通過し、60セッションすべてが比較に参加しました。real側のセッション反応率は0.790698、対照群は0.550132で、差は **+23.792ポイント**。95% bootstrap区間は **[+18.734, +29.020]ポイント**でした。

2020年のrobustness検証も60セッションすべてが参加し、主要差は **+25.439ポイント**、95% bootstrap区間は **[+20.741, +30.230]ポイント**でした。

2025年初のrobustness検証では、最初の60適格セッションを結果計算前に固定し、60セッションすべてが比較に参加しました。主要差は **+23.663ポイント**、95% bootstrap区間は **[+19.435, +28.017]ポイント**でした。対象は2025-01-02〜2025-04-11なので、これは2025年初の結果であり、2025年通年の有効性を示すものではありません。また、過去の検証と同じ実装・一次データ源を使っているため、独立実装による再現ではなく、時間をずらした再現です。

4期間の推定値が近いことだけで、あらゆる相場環境で不変だとは言えません。ただし、同じprotocolの範囲では、2024年に見えた差が1期間だけの現象だった可能性はさらに下がりました。同じ反応率検証を追加する情報価値は下がっており、現在の重要な不確実性はexecution-awareな検証へ移っています。

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

## 2018年execution-aware再現：仮説は維持、手動取得経路は優先度低下

別の未使用期間で同じメカニズム、quote side、15分horizon、control、bootstrap、判定ルールを検証するため、2018年のexecution-aware再現も事前に固定しました。

構造確認は完了し、**最初の60適格セッションを、returnを一切確認する前に凍結済み**です。固定ルールにより10候補日を除外しています。Tick取得manifestでは **2,066個のevent-hour-side単位**が必要で、最新の保存済みcheckpointでは **23/2,066単位**まで確認されています。研究結果はまだ一切開いていません。

複数回の実行を経て、1時間・片側ずつブラウザで取得する現在の手動経路は、**研究コストに見合わないため優先度を下げる**判断になりました。およそ2,000件の追加取得とファイル同一性確認が必要で、研究そのものより機械的な取得作業が支配的になるためです。凍結済みサンプル、事前登録、manifest、既存23単位、結果未観測の状態は保存しています。

これは**水平線仮説に対するnegative evidenceではありません**。2018年仮説は未検証のため判定保留です。研究条件を変えず、一次データの同一性を保ったまま機械的負担を大きく下げられる取得経路が確認できれば、将来再開できます。

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

現在公開できる主張は、**固定したGOLDのprotocolで短期方向反応の差が4つの離れた期間に再現し、2019年のexecution-aware履歴検証でも正の結果が出た**というところまでです。売買指示ではありません。

## 公開範囲

このページでは、レビュー済みの要約統計と研究判断だけを公開しています。raw file、manifest、内部のWork Order、詳細な取得ログ、credential、現在ポジション、売買判断は公開サイトには載せません。

*これは研究記録であり、投資助言ではありません。過去データでの検証結果は将来の収益性を示すものではありません。*