---
title: トレード
lang: ja
permalink: /ja/trading/
updated: "2026-09-14"
description: Studio Labのレビュー済みトレード研究。開発テスト、ホールドアウト、独立検証、execution-aware検証、prospective screen、リスク管理、negative resultを含みます。
---

<p class="eyebrow">トレード研究</p>
<h1>ストーリーを信じる前に、優位性を検証する。</h1>
<p class="lede">Studio Labの系統的トレード研究から、レビュー済みの開発結果、ホールドアウト、独立検証、execution-aware検証、prospective protocol、negative resultや混合結果を公開します。未確定の仮説は結果と明確に分けます。ライブの売買ダッシュボード、シグナル配信、現在ポジションの記録ではありません。</p>

<section class="section">
  <div class="section-heading"><div><p class="eyebrow">現在の根拠</p><h2>GOLD水平線の方向反応は4つの期間で再現した</h2></div></div>
  <div class="feature-grid feature-grid-wide">
    <article class="feature-card">
      <p class="feature-meta">GOLD水平線 · 再現確認 / execution-aware</p>
      <h3><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">方向反応は4期間で再現し、実測BID/ASKを使った2019年検証でも正の結果</a></h3>
      <p>固定した15分方向反応のreal-control差は、2024年開発で+26.55ポイント、2022年独立検証で+23.79ポイント、2020年robustness検証で+25.44ポイント、2025年初の事前固定robustness検証で+23.66ポイントでした。さらに2019年の実測BID/ASK検証では、real平均+1.189 bps、real-control差+3.498 bpsでした。</p>
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究 · 2026年9月14日確認</p><h2>prospective検証、別メカニズム探索、execution課題の収束判断を並行して進める</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">VIX prospective screen · E01はfail-closed</p>
      <h3>最初のイベントは開始したが、必要な開始時点の観測を確定できなかった</h3>
      <p>E01は2026年9月14日に開始しましたが、09:00 JST時点の有効なVIX snapshotと、固定済みのXAU/USD開始観測を確定できませんでした。後から得た値で穴埋めせず、等確率forecastを保存したうえで<strong>ABSTAIN / HOLD</strong>とし、予測性能の結論は出していません。</p>
      <p class="card-links">E02に向けてsource identityと09:00時点の保存手順を明示しました。ただし、データアクセスと1分足取得の確認には未解決点が残っています。VIX境界、24時間horizon、UP / DOWN / FLAT、Brier scoreは変更していません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">別メカニズム探索 · まずDiscovery Gate</p>
      <h3>重いdata pathやbacktestを作る前に、安い一次証拠で候補を絞る</h3>
      <p>現在は、既出familyと重複しないGOLDメカニズムを探し、まず一次資料でGOLDとの直接関係、結果前に観測できるmeasure、経済的な意味を確認しています。通過しない候補はparameter違いとして救済せず、早い段階で優先度を下げます。</p>
      <p class="card-links">例としてCommercial Paperでは、CP金利とGoldを直接扱う過去研究は確認できましたが、根拠は同時点の関連にとどまり、予測edgeを示すものではありません。次段へ進む理由にはなっても、売買上の優位性の証拠にはしていません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">2018年execution-aware再現 · 取得経路を保留</p>
      <h3>仮説は未検証のまま保存し、手動取得の繰り返しは止めた</h3>
      <p>60セッションと研究条件は凍結済みで、必要な2,066 quote単位のうち23単位を保存し、2018年のreturnはまだ確認していません。一方、1時間・片側ずつブラウザで取得する経路は、研究価値に比べて機械的負担が大きいため優先度を下げました。</p>
      <p class="card-links">これは水平線仮説に対するnegative resultではありません。条件を変えず、一次データの同一性を保ったまま取得負担を大きく下げられる経路が見つかれば再開できます。</p>
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
  <p>ここに示す結果は過去データやprospective protocolを使った研究です。将来の収益性を保証するものではなく、特定の売買、数量増加、戦略採用を勧めるものでもありません。</p>
</section>
