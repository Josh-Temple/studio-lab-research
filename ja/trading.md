---
title: トレード
lang: ja
permalink: /ja/trading/
description: Studio Labのレビュー済みトレード研究。開発テスト、ホールドアウト、独立検証、execution-aware検証、prospective screen、リスク管理、negative resultを含みます。
---

<p class="eyebrow">トレード研究</p>
<h1>ストーリーを信じる前に、優位性を検証する。</h1>
<p class="lede">Studio Labの系統的トレード研究から、レビュー済みの開発結果、ホールドアウト、独立検証、execution-aware検証、prospective protocol、negative resultや混合結果を公開します。未確定の仮説は結果と明確に分けます。ライブの売買ダッシュボード、シグナル配信、現在ポジションの記録ではありません。</p>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">現在の根拠</p><h2>GOLD水平線は単一の開発結果から先へ進んだ</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 再現確認 / execution-aware</p>
      <h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">方向反応は3期間で再現し、実測BID/ASKを使った2019年検証でも正の結果</a></h3>
      <p>固定した15分方向反応のreal-control差は、2024年開発で+26.55ポイント、2022年独立検証で+23.79ポイント、2020年robustness検証で+25.44ポイントでした。さらに2019年の実測BID/ASKを使った検証では、real平均+1.189 bps、real-control差+3.498 bpsでした。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">現在の根拠をまとめて読む</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">追加しても改善しなかった条件</p>
      <h3>指標を増やせば自動的に良くなるわけではなかった</h3>
      <p>60分trend context、New York時間帯、前セッションvolatilityを1つずつ加えた検証では、水平線単独のベースラインを超える増分情報は確認できませんでした。recent session-direction continuationも棄却または優先度低下となっています。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">その他の公開結果</p><h2>negative resultや混合結果も残す</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">リピート取引 · 外部ホールドアウト</p>
      <h3><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リスク低下は収益上の優位性にはつながらなかった</a></h3>
      <p>2つの動的exitは、未使用の2020〜2022年ホールドアウトでdrawdownなどの負担を減らしましたが、benchmarkに対するmatched median P/Lは改善しませんでした。</p>
      <p class="card-links"><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">研究結果とグラフを見る</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">GOLDレンジ持続性 · 独立検証</p>
      <h3><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">2024年の強いレンジ持続性は2021年の独立検証では確認できなかった</a></h3>
      <p>2024年の開発結果はρ=0.5621でしたが、固定済みの2021年独立検証ではρ=0.0626となり、95% block-bootstrap区間はゼロをまたぎました。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">独立検証を読む</a></p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">現在の研究</p><h2>execution-aware再現とprospective screenを並行して進める</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 2018年サンプル凍結済み</p>
      <h3>2019年と同じquote-crossing条件を、別の未使用期間で再検証する</h3>
      <p>最初の60適格セッションは、returnを見る前にすべて凍結しました。残るボトルネックは公式BID/ASK Tickの取得で、必要な2,066 event-hour-side単位のうち23単位を確認済み、2,043単位が未取得です。</p>
      <p class="card-links">2018年のreturn、主要推定値、bootstrap区間、研究判定はまだ計算していません。部分データから途中結論も出しません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">VIX prospective screen · 2026年9月14日開始</p>
      <h3>次の8週間を観測する前に、カレンダーと評価方法を固定する</h3>
      <p>月曜〜木曜の重複しない24時間windowを8週間、合計32イベントで評価します。VIXは&lt;12、12〜20、&gt;20の3区分、GOLDの結果はUP / DOWN / FLATとし、Brier scoreで予測品質を評価します。</p>
      <p class="card-links">カレンダー凍結時点では、現在のVIX値、現在のGOLD値、将来結果は使用していません。economic effectは予測品質とは別に後段で評価します。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">研究原則</p><h2>守りたい3つのこと</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card"><p class="feature-meta">01</p><h3>ホールドアウトはホールドアウトのまま使う</h3><p>未使用期間を見る前にルールや閾値を固定し、一度開いた期間を同じ主張の再調整に使いません。</p></article>
    <article class="feature-card"><p class="feature-meta">02</p><h3>反応率と収益性を分ける</h3><p>方向反応率が高いことは追加検証の理由になりますが、それだけで期待値、drawdown、実行可能な利益が確認されたとは判断しません。</p></article>
    <article class="feature-card"><p class="feature-meta">03</p><h3>execution evidenceにも限界がある</h3><p>履歴上の実測BID/ASKを使う検証はbarだけの反応率より強い根拠ですが、実際のbroker約定と同じものとして扱いません。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">範囲</p>
  <h2>研究記録であり、投資助言ではありません。</h2>
  <p>ここに示す結果は過去データを使った実験です。将来の収益性を保証するものではなく、特定の売買、数量増加、戦略採用を勧めるものでもありません。</p>
</section>
