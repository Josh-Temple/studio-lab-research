---
layout: research
title: "OpenAlex bridge-work adoption lag pilot"
lang: ja
permalink: /ja/research/openalex-bridge-adoption-lag/
research_id: "PILOT-RESEARCH-001"
status: "終了 — 主要比較なし"
updated: "2026-08-20"
topic: "研究方法 / 学術メタデータ"
summary: "メタデータで定義したbridge workが解釈可能なadoption-lag比較に使えるかを事前登録型で検証したpilot。taxonomy validity gateを満たさなかったため、主要な結果比較より前に停止しました。"
---

## 研究の問い

OpenAlexメタデータから再現可能に定義した「bridge work」を使って、matched controlとの間でtarget fieldへのadoption lagを解釈可能な形で比較できるか。

ここでいう「bridge work」は限定的な操作的定義です。論文が科学的に重要であること、実質的に学際的であること、知識移転を因果的に生み出したことを意味しません。このpilotで使用した学術メタデータから作った分類だけを指します。

## 方法

研究は2段階で設計しました。研究の問い、matching logic、quality gate、停止条件、結果比較を実行する条件を、主要なcitation outcomeを見る前に固定しました。

source-exactな第2設計では、2つの出版年についてbridge/controlのmatched pairを構成し、index integrity、citation-link integrity、chronology、Crossref check、group balance、blind manual taxonomy auditを主要結果より前に順番に確認しました。

重要なtaxonomy gateでは、不確実判定を除いた監査対象bridge recordのうち、Computer ScienceとMedicineの両方に妥当に分類できるものが**70%以上**であることを要求しました。この基準を満たさなければ、adoption-lag outcomeを比較する前に停止する設計でした。

## 観測結果

再設計したpipelineは、各出版年について**1,250組のbridge/control pair**を作成し、index、citation link、chronology、Crossref、balanceの各gateを通過しました。

一方、blind taxonomy auditは基準を満たしませんでした。不確実判定を除いた**38件中16件（42.1%）**だけが、Computer ScienceとMedicineの両方に妥当に分類できると判断され、事前に設定した**70%**を下回りました。

このため、protocolどおりメタデータ品質のgateで停止しました。

**主要なadoption-lag比較は実行していません。** bridge/control間の効果方向、効果量、有意差、adoption-lag差について、このpilotから報告できる結果はありません。

## 解釈

これはadoption-lag差を支持または否定する結果ではなく、方法上のnon-resultです。

source-exactな再設計によってpipelineの機械的部分は再現可能かつbalancedにできましたが、今回のメタデータ由来bridge分類は、科学的比較を解釈するために必要だと事前設定した信頼性基準へ届きませんでした。

したがって、最も強く支持される結論は次です。**このpilotで保存されたevent rowを、bridge workがcontrolより速く、遅く、または同程度に採用される証拠として使わない。**

主要結果を見る前に停止したことで、弱い操作的定義を、後から興味深く見える結果で正当化することを避けられました。

## 限界と不確実性

- 失敗したgateは、この操作的定義、field pair、audit手続き、sampleに対するものです。OpenAlexメタデータ一般の品質評価ではありません。
- 実質的な学際研究が分野をまたいで速く、または遅く広がるかは、このpilotからは分かりません。
- 停止条件に達したため主要結果を意図的に検証しておらず、解釈すべきnull resultは存在しません。
- manual auditは限定された妥当性チェックであり、包括的なtaxonomy研究ではありません。
- 別のbridge定義、field pair、独立検証済み分類なら実行可能な設計になる可能性はありますが、それはこの結果の継続ではなく新しい研究です。

## 根拠とartifact

**公開情報源:** [OpenAlex](https://openalex.org/) の学術メタデータ。

事前登録型の設計文書、frozen execution specification、audit record、execution resultは内部研究archiveに保存しています。現在の公開版ではレビュー済みの主張だけを公開境界としているため、内部運用記録そのものはリンクしていません。

将来、sanitizedしたprotocolやresult artifactを再現性資料として別途公開する可能性があります。それまでは、このページをpilotに関する公開主張の境界として扱います。

## 関連研究

これはStudio Lab研究ラインで最初に行った、範囲を限定したoriginal-research pilotでした。再利用可能な主な成果は方法上のものです。主要な科学的比較を実行できなかった場合でも、結果を見る前に設定した妥当性gateは有用な研究結果を生み出せます。
