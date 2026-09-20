---
title: ホーム
lang: ja
permalink: /ja/
description: Studio Labのケーススタディ、公開研究、プロジェクト、記事、方法をまとめた日本語版ダッシュボード。
---

<section class="hero dashboard-hero">
  <p class="eyebrow">Studio Lab</p>
  <h1>研究、実験、ツールを、根拠とともに公開する。</h1>
  <p class="lede">選定した成果を外向きに整理する公開ダッシュボードです。ポートフォリオでは課題設定から実装案までを示し、研究では方法と限界を示し、プロジェクトでは実際に使えるツールへつなぎます。内部の運用状況はここには表示しません。</p>
  <div class="hero-actions"><a class="button primary" href="{{ '/ja/portfolio/' | relative_url }}">ポートフォリオを見る</a><a class="button secondary" href="{{ '/ja/research/' | relative_url }}">研究を見る</a></div>
</section>

<section class="section compact-section" aria-labelledby="portfolio-title-ja">
  <div class="section-heading"><div><p class="eyebrow">Portfolio</p><h2 id="portfolio-title-ja">コンサル型ケーススタディ</h2></div><a href="{{ '/ja/portfolio/' | relative_url }}">一覧を見る</a></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">制作中</p>
      <h3><a href="{{ '/ja/portfolio/' | relative_url }}">自治体業務の生成AI活用・業務再設計</a></h3>
      <p>現状業務の分析から、人が判断を残すTo-Be業務、ガバナンス、試作品、KPI、段階的なPoC計画までを一つのケースとして作成します。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">既存の土台</p>
      <h3><a href="{{ '/ja/methods/' | relative_url }}">仮定と限界を明示する検証方法</a></h3>
      <p>根拠の範囲、停止条件、再現可能な確認、支持されなかった結果の保存など、Studio Labで使っている方法をケーススタディにも適用します。</p>
    </article>
  </div>
</section>

<section class="section compact-section" aria-labelledby="areas-title-ja">
  <div class="section-heading"><div><p class="eyebrow">公開ダッシュボード</p><h2 id="areas-title-ja">4つの入口</h2></div></div>
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
    <article class="research-item"><div><h3><a href="{{ '/ja/research/heckerman-replicability-bounded-replication/' | relative_url }}">Heckerman et al. (2025) の限定再計算</a></h3><p>393件のempirical researchのうち5件がfully replicableという原論文の数値関係を、事前固定計算で1.27%と再確認しました。</p></div><span class="status">完了 · 限定再計算PASS</span></article>
    <article class="research-item"><div><h3><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">GOLD水平線：未使用2026H2の無条件タッチ検証</a></h3><p>事前登録した未使用60セッションで、水平線タッチ後15分の方向調整済み平均リターンは−1.379 bps、95%区間は−1.909〜−0.862 bpsとなり、無条件タッチ仮説は支持されませんでした。</p></div><span class="status">完了 · 支持されず</span></article>
    <article class="research-item"><div><h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">GOLD水平線の再現・execution-aware研究</a></h3><p>過去4期間の方向反応差と2019年のpositiveなquote-crossing検証を残しつつ、後続H2 negative resultにより現在の主張範囲を狭めています。</p></div><span class="status">混合した根拠</span></article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">トレード研究</p><h2>再現したストーリーを、より厳しい未使用データで反証する</h2></div><a href="{{ '/ja/trading/' | relative_url }}">トレード研究へ</a></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card"><p class="feature-meta">最新の公開結果</p><h3><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">未使用2026H2では無条件タッチ仮説を確認できなかった</a></h3><p>60セッションの固定検証で主要平均は−1.379 bps、95%区間は−1.909〜−0.862 bpsでした。使用済み標本でparameterを調整して結果を救済せず、この研究線を支持されず終了としています。</p></article>
    <article class="feature-card"><p class="feature-meta">根拠の文脈</p><h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">過去のpositive evidenceも削除せず残す</a></h3><p>過去4期間で再現した方向反応差と2019年のpositiveなquote-crossing結果は研究記録として残ります。最新H2結果により、「反応統計の再現」と「無条件で売買可能なedge」は別だと、より明確になりました。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">公開範囲</p>
  <h2>内部の運用情報ではなく、レビュー済み成果を公開する。</h2>
  <p>作業キュー、非公開データ、運用ログ、未公開の主張、現在の売買判断などは内部ダッシュボードに残します。</p>
  <a href="{{ '/ja/about/' | relative_url }}">公開方針を見る</a>
</section>
