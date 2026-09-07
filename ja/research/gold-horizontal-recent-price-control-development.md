---
layout: research
title: "GOLD水平線反応：2024年開発データでは直近価格の対照群を上回った"
lang: ja
permalink: /ja/research/gold-horizontal-recent-price-control-development/
research_id: "PILOT-TRADING-001 / GOLD horizontal recent-price control"
status: "開発段階 — 追加検証候補"
updated: "2026-09-08"
topic: "トレード / GOLD水平線"
summary: "封印済みの2024年60セッション開発データで、60分rolling extremaから作るzoneの15分方向反応率は、直近の実測非extreme価格を使った対照群を上回りました。ただしこれは開発段階の結果であり、利益性やout-of-sample再現を示すものではありません。"
---

## 研究の問い

直近価格の高値・安値から機械的に定めたGOLDのsupport / resistance zoneには、同じ直近の価格分布から選んだ比較対象よりも、短期の方向反応に関する情報が含まれているか。

trend、regime、移動平均、Volume Profile、positioningなどを追加する前に、**水平線単独のメカニズム**を検証するための比較です。

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

固定済みの判定ルールでは、結果は **PROMISING_FOR_FURTHER_TEST（追加検証に進める候補）**です。

## 解釈

水平線単独のメカニズムは、開発段階では「判定保留」から「独立検証に進める候補」へ進みました。この2024年開発データでは、rolling extrema zoneの15分方向反応率が、十分に評価可能な直近実測価格の対照群より明確に高くなりました。

ただし、ここから「水平線は有効」と一般化することはできません。今回確認できたのは、1つの開発サンプル、1つのイベント定義、1つの対照設計での差です。

## まだ優位性とは言えない理由

これは**独立した根拠ではありません**。直近価格の対照群は、先行する対照設計が失敗し、2024年real側の結果を見た後に作られています。また、実水平線イベントと対照イベントでは、到達前の価格経路などにまだ構造的な違いが残っている可能性があります。

したがって、今回の結果だけでは以下は確認できません。

- transaction cost控除後の利益性や期待値
- spread / slippageへの耐性
- 実際の約定可能性
- drawdown特性
- 別期間・別regime・別銘柄での再現性
- 他の妥当な対照群すべてに対する優位性
- trend / regimeや他の指標を追加した場合の増分価値
- 継続的なlive trading edge

## 現在の状態：2022年独立検証を事前登録済み

次の判断段階として、**2022年の独立protocol validation**を事前登録しました。

rolling extremaの定義、直近価格の対照群、15分方向反応、セッション単位の推定方法、設計妥当性の基準、判定ルールは2024年開発テストから変更しません。2022-01-03 UTC以降から、水平線の結果とは無関係なデータ構造条件だけを使い、最初の60適格セッションを選ぶ設計です。

事前登録時点では、**2022年の水平線または対照群の反応結果は確認・計算していません**。

独立検証をさらに進める条件は、設計基準を通過し、主要推定値が正で、95% bootstrap区間の下限も0を上回ることです。2022年で再現しなければ、2024年結果は開発段階の根拠として残しつつ、同じholdout上で条件を調整して救済するのではなく、水平線単独メカニズムの評価を下げます。

## 公開範囲

このページでは、レビュー済みの要約統計と現在の研究判断だけを公開しています。raw data、詳細な実行成果物、乱数stream、manifest、内部運用ログは公開サイトには載せません。

*これは研究記録であり、投資助言ではありません。開発段階の過去データ結果は将来の売買成績を示すものではありません。*