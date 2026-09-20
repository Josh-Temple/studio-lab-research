---
title: ホーム
lang: ja
permalink: /ja/
description: 公共分野の業務改革ケース、研究、ツールを、判断の根拠と限界まで含めて公開するStudio Labの日本語版。
---

<section class="hero dashboard-hero">
  <p class="eyebrow">Studio Lab</p>
  <h1>業務改革、研究、ツールを、判断の根拠まで含めて公開する。</h1>
  <p class="lede">選定したケーススタディと研究の公開記録です。ポートフォリオでは、制約のある現場で課題をどう整理し、業務をどう組み替えるかを示します。研究では、方法、結果、限界を残し、より厳しい検証で支持されなかった結果も公開します。</p>
  <div class="hero-actions">
    <a class="button primary" href="{{ '/ja/portfolio/' | relative_url }}">ポートフォリオを見る</a>
    <a class="button secondary" href="{{ '/ja/research/' | relative_url }}">研究を見る</a>
  </div>
</section>

<section class="section compact-section" aria-labelledby="featured-case-title-ja">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Featured case</p>
      <h2 id="featured-case-title-ja">制約の強い組織でDXを横展開する業務改革</h2>
    </div>
    <a href="{{ '/ja/portfolio/' | relative_url }}">ケース全体を見る →</a>
  </div>
  <div class="editorial-feature">
    <div class="editorial-feature-main">
      <p class="feature-deck">個別のDX事例を、一部の成功例で終わらせず、組織の改善能力へつなげられるかを扱うケースです。</p>
      <p>事例共有、照会業務の再設計、相談・伴走支援、小規模実験、評価、横展開までを一続きで考えます。AIは目的にせず、使える工程で使う手段として位置付けます。</p>
    </div>
    <dl class="evidence-note" aria-label="ケーススタディの構成">
      <div><dt>01</dt><dd><strong>課題設定</strong><span>技術を選ぶ前に、業務上の制約と改善対象を定める。</span></dd></div>
      <div><dt>02</dt><dd><strong>業務設計</strong><span>工程、引継ぎ、統制、実装までの流れを示す。</span></dd></div>
      <div><dt>03</dt><dd><strong>根拠と限界</strong><span>実測、試算、仮定、未解決事項を分けて示す。</span></dd></div>
    </dl>
  </div>
</section>

<section class="section" aria-labelledby="featured-finding-title-ja">
  <div class="section-heading">
    <div>
      <p class="eyebrow">Featured finding</p>
      <h2 id="featured-finding-title-ja">繰り返し確認できたように見えた仮説を、より厳しい未使用データで検証する</h2>
    </div>
    <a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">研究を見る →</a>
  </div>
  <div class="finding-feature">
    <div class="finding-number">
      <span class="finding-kicker">GOLD · 2026H2</span>
      <strong>−1.379 bps</strong>
      <span>15分後の方向調整済み平均リターン</span>
      <dl class="finding-facts" aria-label="代表結果の根拠">
        <div><dt>標本</dt><dd>未使用60セッション</dd></div>
        <div><dt>95%区間</dt><dd>−1.909〜−0.862 bps</dd></div>
      </dl>
    </div>
    <div class="finding-copy">
      <p class="finding-conclusion">事前登録した無条件タッチ仮説は支持されませんでした。</p>
      <p>未使用60セッションで、session-clustered 95%区間は−1.909〜−0.862 bpsでした。過去のpositiveな反応データは研究記録として残しますが、そこから無条件の売買edgeまでは言えないことが明確になりました。結果を見た後の条件変更で救済せず、この研究線を終了しています。</p>
      <div class="inline-links">
        <a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">結果と限界</a>
        <a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">研究の経緯</a>
        <a href="{{ '/ja/methods/' | relative_url }}">検証方法</a>
      </div>
    </div>
  </div>
</section>

<section class="section compact-section evidence-lineage-section" aria-labelledby="evidence-lineage-title-ja">
  <div class="section-heading lineage-heading">
    <div>
      <p class="eyebrow">Evidence lineage</p>
      <h2 id="evidence-lineage-title-ja">一つの研究線で、主張の範囲を段階的に狭める</h2>
    </div>
    <a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">研究記録全体を見る →</a>
  </div>
  <p class="lineage-intro">以下の検証は、まったく同じ量を測っているわけではありません。反応率として繰り返し観測されたパターンを、約定を意識した条件や未使用データへ移しながら、どこまで主張できるかを絞っていった経緯を示しています。</p>
  <ol class="lineage-track">
    <li class="lineage-step">
      <span class="lineage-index">01</span>
      <div><strong>反応率の差を4期間で再現</strong><span>2024 · 2022 · 2020 · 2025年前半</span><p>直近価格の対照と比べ、水平線ゾーンで定義した15分反応率が高いという差が、複数の過去標本で繰り返し観測されました。</p></div>
    </li>
    <li class="lineage-step">
      <span class="lineage-index">02</span>
      <div><strong>約定を意識した過去検証</strong><span>2019 · 固定条件ではpositive</span><p>実際のBID/ASKを使ったquote-crossing検証でもpositiveでした。ただし、実ブローカーでの約定そのものを再現した検証ではありません。</p></div>
    </li>
    <li class="lineage-step">
      <span class="lineage-index">03</span>
      <div><strong>エントリー条件に論点を絞る</strong><span>2026H1 · 探索的診断</span><p>タッチから確認後エントリーまでの値動きは平均的に有利でしたが、エントリー後は不利でした。確認条件によるイベント選択が論点になりました。</p></div>
    </li>
    <li class="lineage-step lineage-step-terminal">
      <span class="lineage-index">04</span>
      <div><strong>未使用データでは無条件タッチ仮説を支持せず</strong><span>2026H2 · 事前登録 · 60セッション</span><p>無条件タッチの平均は−1.379 bpsでした。結果を見た後に使用済み標本を調整して救済せず、この研究線を終了しています。</p></div>
    </li>
  </ol>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">最新の研究</p><h2>最近公開した研究</h2></div><a href="{{ '/ja/research/' | relative_url }}">一覧を見る →</a></div>
  <div class="research-list">
    <article class="research-item"><div><h3><a href="{{ '/ja/research/heckerman-replicability-bounded-replication/' | relative_url }}">Heckerman et al. (2025) の限定再計算</a></h3><p>393件のempirical researchのうち5件がfully replicableという原論文の数値関係を、事前固定計算で1.27%と再確認しました。</p></div><span class="status">完了 · 限定再計算PASS</span></article>
    <article class="research-item"><div><h3><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">GOLD水平線：未使用2026H2の無条件タッチ検証</a></h3><p>事前登録した未使用60セッションで、水平線タッチ後15分の方向調整済み平均リターンは−1.379 bps、95%区間は−1.909〜−0.862 bpsとなり、無条件タッチ仮説は支持されませんでした。</p></div><span class="status">完了 · 支持されず</span></article>
    <article class="research-item"><div><h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">GOLD水平線の再現・execution-aware研究</a></h3><p>過去4期間の方向反応差と2019年のpositiveなquote-crossing検証を残しつつ、後続H2 negative resultにより現在の主張範囲を狭めています。</p></div><span class="status">混合した根拠</span></article>
  </div>
</section>

<section class="section compact-section" aria-labelledby="explore-title-ja">
  <div class="section-heading"><div><p class="eyebrow">Explore</p><h2 id="explore-title-ja">ほかの入口</h2></div></div>
  <div class="link-grid">
    <a class="link-panel" href="{{ '/ja/projects/' | relative_url }}"><span>プロジェクト</span><strong>実際に動くツールと学習システム</strong><small>直接試せる成果をまとめています。</small></a>
    <a class="link-panel" href="{{ '/ja/writing/' | relative_url }}"><span>記事</span><strong>研究や設計判断を読みやすく整理</strong><small>専門的な内容を、背景から追える形で説明します。</small></a>
    <a class="link-panel" href="{{ '/ja/methods/' | relative_url }}"><span>方法</span><strong>主張の範囲と停止条件</strong><small>検証、再現、公開前レビューの考え方を示します。</small></a>
    <a class="link-panel" href="{{ '/ja/market/' | relative_url }}"><span>市場</span><strong>公開市場データの観測</strong><small>売買判断から分離した記述的な観測です。</small></a>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">公開範囲</p>
  <h2>内部の運用情報ではなく、レビュー済み成果を公開する。</h2>
  <p>作業キュー、非公開データ、運用ログ、未公開の主張、現在のポジションや売買判断などは公開レイヤーに含めません。</p>
  <a href="{{ '/ja/about/' | relative_url }}">公開方針を見る</a>
</section>
