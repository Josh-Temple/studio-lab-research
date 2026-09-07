---
title: トレード
lang: ja
permalink: /ja/trading/
description: Studio Labのレビュー済みトレード研究。開発テスト、ホールドアウト、独立検証、リスク管理、negative resultを含みます。
---

<p class="eyebrow">トレード研究</p>
<h1>ストーリーを信じる前に、優位性を検証する。</h1>
<p class="lede">Studio Labの系統的トレード研究から、レビュー済みの開発結果、ホールドアウト、独立検証、negative resultや混合結果を公開します。未確定の仮説は結果と明確に分けます。ライブの売買ダッシュボード、シグナル配信、現在ポジションの記録ではありません。</p>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">公開済み結果</p><h2>レビューを終えた研究</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 開発段階</p>
      <h3><a href="{{ '/ja/research/gold-horizontal-recent-price-control-development/' | relative_url }}">rolling extrema zoneは開発データで直近価格の対照群を上回った</a></h3>
      <p>封印済み2024年60セッションすべてで、15分方向反応率はreal zoneが79.78%、対照群が53.23%でした。主要差は+26.55ポイント、95% bootstrap区間は+21.23〜+31.82ポイントです。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-horizontal-recent-price-control-development/' | relative_url }}">開発結果を読む</a></p>
    </article>
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究</p><h2>次の判断段階は2022年独立検証</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 2022年独立検証を事前登録済み</p>
      <h3>変数を増やす前に、同じメカニズムが再現するかを確かめる</h3>
      <p>2022-01-03以降から最初の60適格UTCセッションを使い、rolling extrema、直近価格の対照群、15分方向反応、セッション単位の推定方法、設計基準、判定ルールを変更せずに検証する計画を固定しました。</p>
      <p class="card-links">事前登録時点では、2022年の水平線・対照群の反応結果は確認も計算もしていません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Range persistence · 優先度低下</p>
      <h3>弱い独立検証結果を、結果を見た後から救済しない</h3>
      <p>2021年は前セッションrangeのメカニズムについて使用済みの検証期間です。現在は2021年で同じ仮説を再調整せず、救済目的で自動的に別のholdoutを追加することも優先していません。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">研究原則</p><h2>守りたい3つのこと</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card"><p class="feature-meta">01</p><h3>ホールドアウトはホールドアウトのまま使う</h3><p>未使用期間を見る前にルールや閾値を固定し、一度開いた期間を同じ主張の再調整に使いません。</p></article>
    <article class="feature-card"><p class="feature-meta">02</p><h3>反応率と収益性を分ける</h3><p>方向反応率が高いことは追加検証の理由になりますが、それだけで期待値、drawdown、実行可能な利益が確認されたとは判断しません。</p></article>
    <article class="feature-card"><p class="feature-meta">03</p><h3>単純なベースラインを重視する</h3><p>複雑なfilterや予測モデルは、高度に見えること自体を理由に採用せず、より単純な比較対象に対する増分価値を確認します。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">範囲</p>
  <h2>研究記録であり、投資助言ではありません。</h2>
  <p>ここに示す結果には、過去データやシミュレーションに基づくものが含まれます。将来の収益性を保証するものではなく、特定の売買、数量増加、戦略採用を勧めるものでもありません。</p>
</section>
