---
title: トレード
lang: ja
permalink: /ja/trading/
updated: "2026-09-20"
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究 · 2026年9月20日確認</p><h2>使用済み標本の救済調整ではなく、独立した事前固定検証へ移る</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">金利のcross-market研究 · 条件固定の途中</p>
      <h3>米10年金利からJGB10年金利への5営業日spilloverを、結果を見る前に検証可能な形へ固定する</h3>
      <p>対象市場、5営業日のhorizon、方向判定、公式データ元、null resultの扱いまでは固定済みです。残っている科学条件は連続した評価期間で、これを固定する前に履歴のoutcome値は開きません。</p>
      <p class="card-links">現段階は検証仕様であり、関係の存在を示す結果ではありません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">USD/JPY × EFFR · prospectiveのみ</p>
      <h3>過去のdecision timeで利用可能だった政策金利値を十分に再構成できないため、retrospective検証は保留する</h3>
      <p>対象系列と公表時刻は公式資料で確認できましたが、各時点で実際に利用可能だった値を後から一意に再現する経路は確認できませんでした。改定後の履歴値で代用せず、将来のpoint-in-time snapshotから検証する方針です。</p>
      <p class="card-links">データ取得上の制約を、仮説に対するnegative evidenceへ置き換えません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">中期研究 · outcome前の事前固定</p>
      <h3>variance riskとGOLDの4H〜日次候補は、まだ結果を測る段階ではない</h3>
      <p>候補の形は進んでいますが、具体的な評価期間、単一mechanism、horizon、比較基準など、結果前に固定すべき条件が残っています。これらを一意に決められなければHOLDとし、結果を見てから条件を選びません。</p>
      <p class="card-links">positive resultの数ではなく、nullやnegativeも含む独立empirical testの完了を優先します。</p>
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
