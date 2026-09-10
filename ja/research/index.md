---
title: 研究
lang: ja
permalink: /ja/research/
description: Studio Labの公開研究。方法、結果、限界、根拠を分けて示します。
---

<p class="eyebrow">研究</p>
<h1>研究と検証</h1>
<p class="lede">各ページでは、研究の問い、方法、観測結果、解釈、限界、公開可能な根拠を分けて示します。停止条件に達して主要比較を実行しなかった場合も、その状態をそのまま記録します。</p>

<section class="section">
  <div class="research-list">
    <article class="research-item">
      <div>
        <h2><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">GOLD水平線：方向反応は3期間で再現し、2019年の実測BID/ASK検証でも正の結果</a></h2>
        <p>同じ水平線定義で2024年・2022年・2020年に方向反応差が再現しました。2019年のexecution-aware検証でもreal平均リターンは正でしたが、live trading edgeが確認されたわけではありません。</p>
      </div>
      <span class="status">再現確認 / execution-aware · 追加検証候補</span>
    </article>
    <article class="research-item">
      <div>
        <h2><a href="{{ '/ja/research/gold-horizontal-recent-price-control-development/' | relative_url }}">GOLD水平線反応：2024年開発データでは直近価格の対照群を上回った</a></h2>
        <p>封印済み60セッションで、rolling extrema zoneの15分方向反応率は直近の実測価格を使った対照群を平均26.55ポイント上回りました。その後、2022年と2020年でも同じ方向の結果が再現しています。</p>
      </div>
      <span class="status">開発段階 · 後続検証あり</span>
    </article>
    <article class="research-item">
      <div>
        <h2><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">GOLDのセッションレンジ持続性：2024年の強い関係は2021年の独立検証では確認できなかった</a></h2>
        <p>2024年の開発結果を独立した2021年データで検証したところ、推定値は小さく、95% block-bootstrap区間はゼロをまたぎました。</p>
      </div>
      <span class="status">完了 · 独立検証は判定保留</span>
    </article>
    <article class="research-item">
      <div>
        <h2><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リピート取引の外部ホールドアウト：リスク低下は収益上の優位性にはつながらなかった</a></h2>
        <p>2つの動的exitを未使用の2020〜2022年で検証し、リスク負担の軽減と収益改善を別々に評価しました。</p>
      </div>
      <span class="status">完了 · 混合 / 判定保留</span>
    </article>
    <article class="research-item">
      <div>
        <h2><a href="{{ '/ja/research/openalex-bridge-adoption-lag/' | relative_url }}">OpenAlex bridge-work adoption lag pilot</a></h2>
        <p>メタデータで定義したbridge workの妥当性基準を満たさなかったため、主要なadoption-lag比較を行わずに終了しました。</p>
      </div>
      <span class="status">終了 · 主要比較なし</span>
    </article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">研究分野</p>
  <h2>トレード研究</h2>
  <p>系統的な売買研究では、開発段階、独立再現、execution-aware検証を分け、ホールドアウト、単純なベースライン、negative result、未確定結果の扱いを重視します。</p>
  <a href="{{ '/ja/trading/' | relative_url }}">トレード研究を見る</a>
</section>
