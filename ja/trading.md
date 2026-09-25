---
title: トレード
lang: ja
permalink: /ja/trading/
updated: "2026-09-25"
description: Studio Labのレビュー済みトレード研究。開発テスト、ホールドアウト、未使用データ検証、execution-aware検証、prospective protocol、negative resultを含みます。
---

<p class="eyebrow">トレード研究</p>
<h1>ストーリーを信じる前に、優位性を検証する。</h1>
<p class="lede">Studio Labの系統的トレード研究から、positive・negative・混合結果を同じ研究記録として公開します。使用済み標本での探索と、未使用・prospectiveデータでの確認を分けて扱います。ライブの売買ダッシュボード、シグナル配信、現在ポジションの記録ではありません。</p>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">現在の根拠</p><h2>再現した方向反応は、無条件タッチedgeにはならなかった</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">最新の未使用データ結果 · 2026H2</p>
      <h3><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">事前登録した無条件タッチ再現はnegative</a></h3>
      <p>未使用の60セッション、評価可能4,786タッチeventで、15分の方向調整済み平均は<strong>−1.379 bps</strong>、session単位の95%区間は<strong>−1.909〜−0.862 bps</strong>でした。判定は<strong>NO_UNCONDITIONAL_TOUCH_SUPPORT</strong>です。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">negative replicationを読む</a></p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">研究の流れ</p>
      <h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">過去のpositive evidenceは残るが、現在の主張範囲は狭くなった</a></h3>
      <p>過去の方向反応率差は2024年・2022年・2020年・2025年初で正となり、2019年のquote-crossing検証も固定条件では正でした。ただし、これらは関連する別の推定対象です。後続の未使用H2結果により、無条件タッチentryの正の効果までは示していなかったことが明確になりました。</p>
      <p class="card-links"><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">結果のつながりを見る</a></p>
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究 · 2026年9月25日確認</p><h2>いま確認しているのは、新しい成績よりもデータの網羅性と取得経路</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">2026H1 データ網羅性の監査 · 新しい成績ではない</p>
      <h3>記録済み2,685取引は再現できたが、候補選択の完全性までは確認できなかった</h3>
      <p>保存済みraw Tickは、Signal M1の81,720分のうち79,560分（97.36%）をカバーし、2,160分、つまり36時間が欠けていました。確認できるTickからは既存2,685取引と主要指標を再現できました。一方、欠測区間に追加のtouch、setup、entry候補がなかったことや、entry eligibilityが変わらなかったことまでは現在の根拠だけでは証明できません。</p>
      <p class="card-links">記録済み取引の再現はPASSですが、シグナル候補の選択とエントリー判定の網羅性はHOLDです。これはH1診断から言える範囲を狭めるもので、未使用2026H2の結果を変更するものではありません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">Post-H2確認研究 · 結果は未観測</p>
      <h3>確認条件による選択効果は、固定した境界を守ったまま待機している</h3>
      <p>次の検証では、事前登録した60セッションの規則を維持し、支持されなかった無条件タッチ仮説を作り直しません。標本はまだ成熟しておらず、結果も開いていません。さらに、代替データへ置き換えずに同じXAU/USDの一次取得経路を再現できるまで、データ取得準備をHOLDしています。</p>
      <p class="card-links">パラメータ探索、標本の選び直し、別のデータ提供元への置換をせず、実行できる条件がそろうまで待ちます。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">独立候補 · 取得経路を事前確認</p>
      <h3>BLS PPIとFOMCの候補は前進したが、結果の比較にはまだ進んでいない</h3>
      <p>BLS PPI × S&amp;P 500では、出典、公開時点の値を使う規則、5取引日リターンの定義まで確認できました。ただし、許可された入力だけでは一つの連続した過去期間を固定できないためHOLDです。別のFOMC政策金利変更 × USD/JPY候補も取得前確認まで進みましたが、現在のWorker経路では、結果値を開かずにUSD/JPYの過去バーを実際に取得できることまでは確認できませんでした。</p>
      <p class="card-links">どちらも結果比較は未実施です。結果を見てから都合のよい期間、データ系列、提供元を選ばず、結果前に必要な境界か取得能力が確定した場合だけ次へ進みます。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">研究原則</p><h2>守りたい3つのこと</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card"><p class="feature-meta">01</p><h3>ホールドアウトはホールドアウトのまま使う</h3><p>未使用期間を見る前にルールや閾値を固定し、一度問いに答えた期間を同じ主張の救済調整には使いません。</p></article>
    <article class="feature-card"><p class="feature-meta">02</p><h3>反応率とリターンを分ける</h3><p>再現する方向反応の統計量は次の検証理由にはなりますが、それだけで期待値、drawdown、実行可能な利益が確認されたとは扱いません。</p></article>
    <article class="feature-card"><p class="feature-meta">03</p><h3>失敗した研究線は閉じる</h3><p>事前登録した未使用データ検証で支持されなければ、自動的にparameter rescueへ進みません。異なる仮説は、別の固定条件と新しい根拠で検証します。</p></article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">範囲</p>
  <h2>研究記録であり、投資助言ではありません。</h2>
  <p>ここに示す結果は過去データやprospective protocolを使った研究です。将来の収益性を保証するものではなく、特定の売買、数量増加、戦略採用を勧めるものでもありません。</p>
</section>
