---
title: トレード
lang: ja
permalink: /ja/trading/
updated: "2026-09-21"
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
  <div class="section-heading"><div><p class="eyebrow">現在の研究 · 2026年9月21日確認</p><h2>候補選定と、実際にデータを取得できるかの確認を分ける</h2></div></div>
  <div class="feature-grid">
    <article class="feature-card">
      <p class="feature-meta">取得経路の事前確認 · 結果は未観測</p>
      <h3>公式データを特定できても、そのまま検証を実行できるとは限らない</h3>
      <p>直近では、CFTCの米10年債先物ポジションは公式の照会・export経路を確認できましたが、対応するZN価格の公式machine-readable履歴取得をWorker上で固定できずHOLDになりました。CME Gold CVOLとGC先物も対象系列は特定できましたが、DataMineの認証・利用資格を含む履歴取得経路を実行環境で確認できず、結果を見る前に停止しています。</p>
      <p class="card-links">取得経路のHOLDは、市場仮説に対するnegative resultではありません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">独立候補の探索 · 本実行前にpreflight</p>
      <h3>新しい仮説も、取得確認を飛ばして結果を見に行かない</h3>
      <p>結果を使わない候補探索では、Gold CVOL、EUR/USD CVOL、FedWatch由来の政策金利期待とS&amp;P 500先物など、異なる機序まで広がっています。各候補では、観測量、horizon、支持されない場合の解釈、経済的な停止条件を先に固定し、その後に取得互換性を確認します。</p>
      <p class="card-links">現段階はいずれも研究候補であり、関係の存在や売買上の優位性を示す結果ではありません。</p>
    </article>
    <article class="feature-card">
      <p class="feature-meta">現在の制約 · 実行の忠実性</p>
      <h3>固定した検証を、別データへ置き換えずに実行できるかを確認する</h3>
      <p>source identityだけでなく、銘柄・項目の識別、machine-readableな取得形式、認証・利用資格、観測時点での保存までを別々に確認しています。必要な経路の一部が未確定なら、都合のよいprovider、銘柄、項目、後から改定された値へ置き換えずHOLDします。</p>
      <p class="card-links">最新のconfirmatoryなトレード結果は、引き続き上記の未使用2026H2 GOLD検証です。</p>
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
