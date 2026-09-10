---
layout: research
title: "GOLD水平線反応：2024年開発データでは直近価格の対照群を上回った"
lang: ja
permalink: /ja/research/gold-horizontal-recent-price-control-development/
research_id: "PILOT-TRADING-001 / GOLD horizontal recent-price control"
status: "開発段階 — 後続検証で再現"
updated: "2026-09-08"
topic: "トレード / GOLD水平線"
summary: "封印済みの2024年60セッション開発データで、60分rolling extremaから作るzoneの15分方向反応率は、直近の実測非extreme価格を使った対照群を上回りました。このページは開発段階の結果を記録しており、その後の独立検証・robustness検証は別ページにまとめています。"
---

## 研究の問い

直近価格の高値・安値から機械的に定めたGOLDのsupport / resistance zoneには、同じ直近の価格分布から選んだ比較対象よりも、短期の方向反応に関する情報が含まれているか。

このページは**2024年の開発段階テスト**を記録しています。その後の再現結果は、[現在のGOLD水平線エビデンス]({{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }})にまとめています。

## この比較を行った理由

先行する開発テストでは、continuous-uniform pseudo levelを対照群として使いました。しかし、real側とpseudo側の両方を評価できたのは60セッション中1セッションだけで、十分な比較になりませんでした。

そこで、直近の実測価格から対照価格を作る設計を新たに事前登録しました。ただし、この新しい対照群は先行テストの失敗と2024年real側の結果を確認した後に設計しています。そのため、今回の結果は**開発段階の根拠**であり、独立検証ではありません。

## 方法

- 対象: XAU/USD、BID、M1、UTC。
- サンプル: 変更していない封印済み2024年60セッション開発データ。
- 実水平線: 直前60本のM1について、Lowの最小値をsupport、Highの最大値をresistanceとする。
- 結果指標: 事前に固定した`t+15`分後の方向反応。
- 対照群: 直前60本のM1 Closeから、同時点の実support / resistance zone内にある値を除き、残った実測Closeから1つを機械的に選ぶ。
- 比較単位: セッション。
- 主要推定値: 各セッションの`real反応率 − control反応率`を同じ重みで平均。
- 推定不確実性: セッション単位で10,000回bootstrapし、95% percentile区間を算出。

設計妥当性の基準は通過し、**60セッションすべてがreal/control両方の比較に参加**しました。

## 結果

<div class="result-summary-grid" aria-label="GOLD水平線の開発結果まとめ">
  <div class="result-stat">
    <span class="result-stat-label">比較可能セッション</span>
    <strong>60 / 60</strong>
    <span>設計妥当性の基準を通過</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">主要効果</span>
    <strong>+26.55ポイント</strong>
    <span>real − 直近価格の対照群</span>
  </div>
  <div class="result-stat">
    <span class="result-stat-label">95% bootstrap区間</span>
    <strong>+21.23〜+31.82ポイント</strong>
    <span>10,000回のセッション再標本化</span>
  </div>
</div>

### セッションを同じ重みで平均した方向反応率

<div class="metric-chart" role="img" aria-label="方向反応率。実rolling-extrema zoneは79.78パーセント、直近価格の対照群は53.23パーセント。">
  <div class="metric-row">
    <div class="metric-label">実extrema zone</div>
    <div class="bar-track"><span class="bar-fill bar-positive" style="width:100%"></span></div>
    <div class="metric-value">79.78%</div>
  </div>
  <div class="metric-row">
    <div class="metric-label">直近価格の対照群</div>
    <div class="bar-track"><span class="bar-fill bar-neutral" style="width:66.7%"></span></div>
    <div class="metric-value">53.23%</div>
  </div>
</div>

<p class="chart-note">ここでいう反応率は、事前に固定した15分後の方向反応です。勝率、売買損益、収益性を意味しません。</p>

全セッション合計では、real側は評価可能512イベントのうち403件が成功、対照群は796イベントのうち425件が成功でした。セッションを同じ重みで平均した反応率は、real zoneが **0.797817**、直近価格の対照群が **0.532273**。主要推定値は **+0.265544**、すなわち **+26.55ポイント**で、95% bootstrap区間は **[+21.23, +31.82]ポイント**でした。

固定済みの判定ルールでは、この開発結果は **PROMISING_FOR_FURTHER_TEST（追加検証に進める候補）**でした。

## 開発段階での解釈

この結果により、水平線単独のメカニズムは、開発段階の「判定保留」から独立検証に進める候補へ進みました。ただし、この時点では「水平線は一般に有効」「利益性がある」とまでは言えませんでした。

直近価格の対照群は、先行する対照設計が失敗し、2024年real側の結果を見た後に作られているため、development-sample overfittingやreal/control間の構造差が残る可能性がありました。

## その後の検証 — 2026-09-10時点

このページは現在の研究境界そのものではありません。

同じ方向反応メカニズムは、その後の**未使用2022年独立検証**でも正の結果となり、さらに**2020年robustness検証**でも再現しました。real-control差はそれぞれ+23.79ポイント、+25.44ポイントで、どちらも95% bootstrap区間の下限が0を上回りました。

さらに**2019年のexecution-aware履歴検証**では、M1 signalが観測可能になった後の実測BID/ASK quoteを使い、real平均リターンは+1.189 bps、95%区間は+0.528〜+1.889 bpsでした。real-control差は+3.498 bps、95%区間は+2.531〜+4.500 bpsでした。

これらは研究上の根拠を大きく強めましたが、継続的なlive trading edgeが確認されたわけではありません。現在の解釈と進行中の2018年再現については、[GOLD水平線の再現・execution-aware検証まとめ]({{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }})を参照してください。

## 公開範囲

このページでは、レビュー済みの要約統計だけを公開しています。raw data、詳細な実行成果物、乱数stream、manifest、内部運用ログ、現在ポジション、売買判断は公開サイトには載せません。

*これは研究記録であり、投資助言ではありません。過去データでの検証結果は将来の売買成績を示すものではありません。*