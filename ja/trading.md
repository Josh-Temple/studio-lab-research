---
title: トレード
lang: ja
permalink: /ja/trading/
updated: "2026-09-16"
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究 · 2026年9月16日確認</p><h2>同じ標本を掘り続けず、残った観測を未使用データへ移す</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">Horizontal研究 · 使用済み標本の探索は収束</p>
      <h3>探索的に残ったパターンは、別の確認段階へ送る</h3>
      <p>使用済み2,685 tradeでは、固定UTC区分によるSTOP率差やSTOPの早期集中など、未使用データで確認する価値があるパターンが残りました。一方、同じ標本でsubsetや統計量を増やす探索は収束させています。残す観測は、条件を固定した未使用またはprospective protocolで確認して初めてconfirmatory evidenceになります。</p>
      <p class="card-links">これらの探索結果を公開サイト上で「edge」とは扱わず、H2結果を見た後に使用済み標本から新ruleを調整することもしません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">prospective研究 · outcome前に固定</p>
      <h3>新しい研究線は、結果を見る前に実行可能なtestへ変換する</h3>
      <p>現在はtime/session、market profile、multi-timeframe、fundamentals-first、liquidity関連など、異なる問いについて最低限の観測条件と実行条件を固定しています。一次証拠やdata pathが不足する候補は、parameter違いで救済せずその段階で止めます。</p>
      <p class="card-links">公開上の境界は明確です。protocolは結果ではなく、もっともらしいmechanismもedgeではありません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">VIX prospective screen · 観測経路は未検証</p>
      <h3>初期eventは予測性能の根拠として数えない</h3>
      <p>E01では09:00 JST時点のVIX snapshotと固定XAU/USD開始観測を情報cutoff内でそろえて保存できず、fail-closedとしました。E02前のoperational feasibility確認でも、必要なcutoff snapshot保存と固定feedのruntime取得を成立させる証拠が不足していました。そのため、初期eventを予測性能の採点根拠として扱っていません。</p>
      <p class="card-links">VIX境界、24時間horizon、UP / DOWN / FLAT、Brier scoreを欠損に合わせて変更することもしていません。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">残っているexecution課題</p><h2>2018年の固定再現は結果未観測のまま、手動取得経路を保留</h2></div></div>
  <p>別系統の2018年execution-aware再現は、60セッションを結果前に固定済みで、結果はまだ開いていません。必要な2,066 quote単位のうち23単位を保存した段階で、1時間・片側ずつ取得する手動経路は研究価値に比べて負担が大きいため保留しました。これは2018年仮説に対するnegative evidenceではありません。</p>
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
