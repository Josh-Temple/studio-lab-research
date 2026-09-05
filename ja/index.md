---
title: ホーム
lang: ja
permalink: /ja/
description: Studio Labの公開研究、プロジェクト、記事、方法をまとめた日本語版ダッシュボード。
---

<section class="hero dashboard-hero">
  <p class="eyebrow">Studio Lab</p>
  <h1>研究、実験、ツールを、根拠とともに公開する。</h1>
  <p class="lede">選定した成果を外向きに整理する公開ダッシュボードです。研究では方法と限界を示し、プロジェクトでは実際に使えるツールへつなぎ、記事では研究や設計の内容を読みやすく説明します。内部の運用状況はここには表示しません。</p>
  <div class="hero-actions">
    <a class="button primary" href="{{ '/ja/research/' | relative_url }}">研究を見る</a>
    <a class="button secondary" href="{{ '/ja/projects/' | relative_url }}">プロジェクトを見る</a>
  </div>
</section>

<section class="section compact-section" aria-labelledby="areas-title-ja">
  <div class="section-heading">
    <div>
      <p class="eyebrow">公開ダッシュボード</p>
      <h2 id="areas-title-ja">4つの入口</h2>
    </div>
  </div>
  <div class="area-grid">
    <a class="area-card" href="{{ '/ja/research/' | relative_url }}"><span class="area-kicker">01</span><h3>研究</h3><p>問い、方法、観測結果、限界、公開可能な根拠。</p></a>
    <a class="area-card" href="{{ '/ja/projects/' | relative_url }}"><span class="area-kicker">02</span><h3>プロジェクト</h3><p>実際に試せるツールと学習システム。</p></a>
    <a class="area-card" href="{{ '/ja/writing/' | relative_url }}"><span class="area-kicker">03</span><h3>記事</h3><p>研究結果や設計判断を読みやすく説明した文章。</p></a>
    <a class="area-card" href="{{ '/ja/methods/' | relative_url }}"><span class="area-kicker">04</span><h3>方法</h3><p>主張の範囲、検証、停止条件、公開前レビューの考え方。</p></a>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">最新の研究</p><h2>公開済み研究</h2></div><a href="{{ '/ja/research/' | relative_url }}">一覧を見る</a></div>
  <div class="research-list">
    <article class="research-item"><div><h3><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リピート取引の外部ホールドアウト</a></h3><p>動的exitはリスク負担を軽減した一方、外部ホールドアウトでは収益改善を再現しませんでした。</p></div><span class="status">完了 · 混合 / 判定保留</span></article>
    <article class="research-item"><div><h3><a href="{{ '/ja/research/openalex-bridge-adoption-lag/' | relative_url }}">OpenAlex bridge-work adoption lag pilot</a></h3><p>分類の妥当性基準を満たさなかったため、主要なadoption-lag比較を実行せずに終了した研究です。</p></div><span class="status">終了 · 主要比較なし</span></article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">トレード研究</p><h2>結果が確定したものだけを公開する</h2></div><a href="{{ '/ja/trading/' | relative_url }}">トレード研究へ</a></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card"><p class="feature-meta">外部ホールドアウト</p><h3><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リスク低下は収益上の優位性にはつながらなかった</a></h3><p>未使用の2020〜2022年で、リスク管理と収益改善を分けて評価しました。</p></article>
    <article class="feature-card"><p class="feature-meta">公開境界</p><h3>進行中の実験を結果として扱わない</h3><p>未確定のtrend/regime研究などは、評価条件が固定され、実行とレビューが終わるまで公開結果に含めません。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">公開範囲</p>
  <h2>内部の運用情報ではなく、レビュー済み成果を公開する。</h2>
  <p>作業キュー、非公開データ、運用ログ、未公開の主張、現在の売買判断などは内部ダッシュボードに残します。</p>
  <a href="{{ '/ja/about/' | relative_url }}">公開方針を見る</a>
</section>
