---
title: トレード
lang: ja
permalink: /ja/trading/
description: Studio Labのレビュー済みトレード研究。ホールドアウト、独立検証、リスク管理、negative resultを含みます。
---

<p class="eyebrow">トレード研究</p>
<h1>ストーリーを信じる前に、優位性を検証する。</h1>
<p class="lede">Studio Labの系統的トレード研究から、レビュー済みの結果を公開します。negative resultや混合結果も含め、進行中の仮説は結果と明確に分けます。ライブの売買ダッシュボード、シグナル配信、現在ポジションの記録ではありません。</p>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">公開済み結果</p><h2>レビューを終えた研究</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">リピート取引 · 外部ホールドアウト</p>
      <h3><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リスク低下は収益上の優位性にはつながらなかった</a></h3>
      <p>2つの動的exitは、未使用の2020〜2022年ホールドアウトでdrawdownなどの負担を減らしましたが、benchmarkに対するmatched median P/Lは改善しませんでした。</p>
      <p class="card-links"><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">研究結果とグラフを見る</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">GOLD · 独立検証</p>
      <h3><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">2024年の強いレンジ持続性は2021年の独立検証では確認できなかった</a></h3>
      <p>2024年の開発結果はρ=0.5621でしたが、固定済みの2021年独立検証ではρ=0.0626となり、95% block-bootstrap区間はゼロをまたぎました。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">独立検証を読む</a></p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">現在の研究</p><h2>次に検証していること</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 事前設計中</p>
      <h3>事前に定めたsupport / resistance zone付近の反応</h3>
      <p>次のdevelopment testでは、rolling-window extremaから定めたzone付近の反応を、対応するpseudo / non-level controlと比較します。現在の設計は60分のlevel window、15分のreaction horizon、2024年をdevelopment-onlyとして使う方針です。</p>
      <p class="card-links">市場結果はまだ開いていません。実行前にpseudo controlと主要effect estimateなど、残る設計条件を閉じています。</p>
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
    <article class="feature-card"><p class="feature-meta">02</p><h3>リスク低下と収益改善を分ける</h3><p>drawdown、最大建玉、exposureが減ることには価値がありますが、それだけで期待収益が上がったとは判断しません。</p></article>
    <article class="feature-card"><p class="feature-meta">03</p><h3>単純なベースラインを重視する</h3><p>複雑なfilterや予測モデルは、高度に見えること自体を理由に採用せず、より単純な比較対象に対する増分価値を確認します。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">範囲</p>
  <h2>研究記録であり、投資助言ではありません。</h2>
  <p>ここに示す結果には、過去データやシミュレーションに基づくものが含まれます。将来の収益性を保証するものではなく、特定の売買、数量増加、戦略採用を勧めるものでもありません。</p>
</section>
