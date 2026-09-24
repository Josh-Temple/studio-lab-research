---
title: 研究
lang: ja
permalink: /ja/research/
description: Studio Labの公開研究。方法、結果、限界、根拠を分けて示します。
---

<p class="eyebrow">研究</p>
<h1>研究と検証</h1>
<p class="lede">各ページでは、研究の問い、方法、観測結果、解釈、限界、公開可能な根拠を分けて示します。positive resultだけでなく、独立検証で支持されなかった結果や、停止条件に達して主要比較を実行しなかった研究もそのまま残します。</p>

<section class="section compact-section" aria-labelledby="research-lines-title-ja">
  <div class="section-heading">
    <div>
      <p class="eyebrow">研究線</p>
      <h2 id="research-lines-title-ja">問いから入り、検証の積み重ねを追う</h2>
    </div>
  </div>
  <div class="research-line-list">
    <a class="research-line" href="{{ '/ja/trading/' | relative_url }}">
      <span class="research-line-index">01</span>
      <div>
        <span class="research-line-kicker">トレード</span>
        <strong>システマティックなトレード研究</strong>
        <p>開発検証、未使用データでの検証、期間をまたいだ再現、約定を意識した確認、negative resultまで一続きで残します。</p>
      </div>
    </a>
    <a class="research-line" href="{{ '/ja/research/openalex-bridge-adoption-lag/' | relative_url }}">
      <span class="research-line-index">02</span>
      <div>
        <span class="research-line-kicker">研究方法</span>
        <strong>妥当性ゲートと主要比較を行わない判断</strong>
        <p>解釈に必要な根拠が事前基準を満たさない場合、結果を見に行かず主要比較の前で止める研究設計です。</p>
      </div>
    </a>
    <a class="research-line" href="{{ '/ja/research/heckerman-replicability-bounded-replication/' | relative_url }}">
      <span class="research-line-index">03</span>
      <div>
        <span class="research-line-kicker">再現可能性</span>
        <strong>範囲を限定した再計算</strong>
        <p>原論文の一つの数値関係だけを事前に固定して再計算し、論文全体の結論へ主張を広げません。</p>
      </div>
    </a>
  </div>
</section>

<section class="section compact-section">
  <div class="section-heading"><div><p class="eyebrow">現在の方向 · 2026年9月25日確認</p><h2>一つの公開データ検証は結果まで進み、他は取得条件で止める</h2></div><a href="{{ '/ja/research/noaa-mauna-loa-co2-2025-seasonal-amplitude/' | relative_url }}">新しい研究を見る</a></div>
  <p class="lede">直近では、NOAA GMLのMauna Loa月平均CO₂について、公式テキストの取得形式と使用列を対象値を見る前に固定し、2025年12か月の最大値と最小値の差を計算しました。結果は6.14 ppmで、事前に固定した5 ppmを上回りました。一方、他の公開データ候補では、必要な機械可読形式や取得経路を同じ実行環境で確定できず、本実行へ進めずHOLDとしています。トレード研究では新しい確認検証の成績はまだ出ておらず、データの網羅性、取得元の整合、未観測条件の維持を引き続き確認しています。</p>
</section>

<section class="section">
  <div class="section-heading">
    <div><p class="eyebrow">全研究</p><h2>公開済み研究</h2></div>
  </div>
  <p class="registry-note">上の研究線は入口として選んだものです。以下には、支持されなかった結果や途中で停止した研究も含め、公開記録をまとめて残します。</p>
  <div class="research-list">
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>公開データ / 限定実証</span><time datetime="2026-09-25">2026-09-25</time></p>
        <h2><a href="{{ '/ja/research/noaa-mauna-loa-co2-2025-seasonal-amplitude/' | relative_url }}">Mauna Loaの2025年CO₂：月平均の年内振幅を固定条件で検証</a></h2>
        <p>NOAA GMLの2025年月平均12値を使い、最大値と最小値の差を事前固定条件で計算しました。結果は6.14 ppmで固定閾値5 ppmを上回りました。主張は1地点・1年の記述結果に限定します。</p>
      </div>
      <span class="status">完了 · 固定閾値を上回った</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>トレード / GOLD水平線</span><time datetime="2026-09-24">2026-09-24</time></p>
        <h2><a href="{{ '/ja/research/gold-horizontal-replication-execution-evidence/' | relative_url }}">GOLD水平線：方向反応は再現したが、後続の無条件タッチ検証はnegative</a></h2>
        <p>過去4期間の方向反応差と2019年のquote-crossing検証を残しつつ、未使用2026H2のnegative resultと、2026H1で確認した36時間のTick欠測による網羅性の限界まで含めて現在の主張範囲を更新しました。</p>
      </div>
      <span class="status">混合した根拠</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>研究方法 / 再現可能性</span><time datetime="2026-09-20">2026-09-20</time></p>
        <h2><a href="{{ '/ja/research/heckerman-replicability-bounded-replication/' | relative_url }}">Heckerman et al. (2025)：「fully replicable」5/393の限定再計算</a></h2>
        <p>原論文が報告した393件中5件という数値関係を、事前固定した計算で1.27%と再確認しました。論文全体や科学一般の再現可能性へは広げません。</p>
      </div>
      <span class="status">完了 · 限定再計算PASS</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>トレード / GOLD水平線</span><time datetime="2026-09-15">2026-09-15</time></p>
        <h2><a href="{{ '/ja/research/gold-horizontal-unconditional-touch-2026h2/' | relative_url }}">GOLD水平線：未使用の2026H2検証では「タッチだけ」の効果を確認できなかった</a></h2>
        <p>事前登録した未使用60セッションで、15分の方向調整済み平均リターンは−1.379 bps、95% session-clustered bootstrap区間は−1.909〜−0.862 bpsでした。同じ標本で救済的なparameter調整は行わず、無条件タッチ研究線を閉じています。</p>
      </div>
      <span class="status">完了 · 無条件タッチは支持されず</span>
    </article>

    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>トレード / GOLD水平線</span><time datetime="2026-09-14">2026-09-14</time></p>
        <h2><a href="{{ '/ja/research/gold-horizontal-recent-price-control-development/' | relative_url }}">GOLD水平線反応：2024年開発データでは直近価格の対照群を上回った</a></h2>
        <p>封印済み60セッションで、rolling extrema zoneの15分方向反応率は直近価格の対照群を平均26.55ポイント上回りました。これは開発段階の結果で、その後のpositive/negative両方の検証は別ページにまとめています。</p>
      </div>
      <span class="status">開発段階 · 後続検証あり</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>トレード / GOLD / ボラティリティ</span><time datetime="2026-09-06">2026-09-06</time></p>
        <h2><a href="{{ '/ja/research/gold-session-range-independent-validation/' | relative_url }}">GOLDのセッションレンジ持続性：2024年の強い関係は2021年の独立検証では確認できなかった</a></h2>
        <p>2024年の開発結果を独立した2021年データで検証したところ、推定値は小さく、95% block-bootstrap区間はゼロをまたぎました。</p>
      </div>
      <span class="status">完了 · 独立検証は判定保留</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>トレード / システマティック戦略評価</span><time datetime="2026-08-29">2026-08-29</time></p>
        <h2><a href="{{ '/ja/research/repeat-trading-external-holdout/' | relative_url }}">リピート取引の外部ホールドアウト：リスク低下は収益上の優位性にはつながらなかった</a></h2>
        <p>2つの動的exitを未使用の2020〜2022年で検証し、リスク負担の軽減と収益改善を別々に評価しました。</p>
      </div>
      <span class="status">完了 · 混合 / 判定保留</span>
    </article>
    <article class="research-item">
      <div>
        <p class="research-entry-meta"><span>研究方法 / scholarly metadata</span><time datetime="2026-08-20">2026-08-20</time></p>
        <h2><a href="{{ '/ja/research/openalex-bridge-adoption-lag/' | relative_url }}">OpenAlex bridge-work adoption lag pilot</a></h2>
        <p>メタデータで定義したbridge workの妥当性基準を満たさなかったため、主要なadoption-lag比較を行わずに終了しました。</p>
      </div>
      <span class="status">終了 · 主要比較なし</span>
    </article>
  </div>
</section>

<section class="section public-boundary">
  <p class="eyebrow">公開範囲</p>
  <h2>研究一覧には耐久性のある結果を残す</h2>
  <p>短い周期で変わるprotocolや実行準備はTradingページで現在地を示し、この一覧ではレビュー済みの結果を中心に残します。未観測の研究線、内部の作業キュー、運用ログは公開結果と混ぜません。</p>
  <a href="{{ '/ja/trading/' | relative_url }}">トレード研究の現在地を見る</a>
</section>
