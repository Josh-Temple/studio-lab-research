---
layout: research
title: "Heckerman et al. (2025)：「fully replicable」5/393を事前固定計算で再確認"
lang: ja
permalink: /ja/research/heckerman-replicability-bounded-replication/
research_id: "PILOT-RESEARCH-001 / Heckerman 2025 bounded numeric replication"
status: "完了 · 限定再計算PASS"
updated: "2026-09-20"
topic: "研究方法 / 再現可能性"
summary: "Heckerman et al. (2025) が報告した393件のempirical researchのうち5件がfully replicableという数値関係について、5 / 393 × 100 = 1.27%を事前固定した計算で再確認しました。検証対象はこの数値関係だけです。"
---

## 現在の結論

一つの数値関係に限定した再計算は **PASS** しました。

Heckerman et al. (2025) では、評価対象となった **393件のempirical research** のうち、**5件**が論文内の `fully replicable` 区分に該当すると報告されています。Studio Labでは、結果を見る前に計算を

**5 / 393 × 100**

と固定し、途中では丸めず、最後に小数第2位まで表示する条件にしました。

再計算結果は **1.27%** です。

## 確認したこと

今回の検証は意図的に範囲を狭くしています。固定した入力は次の2つだけです。

- empirical research：**393件**
- fully replicable：**5件**

別の分母、分類、閾値、subsetは結果を見た後に追加していません。

この条件では、原論文の「fully replicableに必要な資源がそろう研究は2%未満」という記述と、報告された件数の関係は数値上整合します。

## 確認していないこと

今回、393件の研究をStudio Labが一件ずつ再評価したわけではありません。

したがって、**1.27%**を次のように広げて解釈することはできません。

- 心血管研究全体の再現可能性の割合
- 医学研究全体の割合
- 科学全体の割合
- 原論文による各研究の分類がすべて正しいという独立確認
- 原論文の方法や結論全体の再現

確認したのは、**原論文が報告した5件と393件を前提にすると、事前固定した計算結果が1.27%になる**という一点です。

## 小さな再計算を公開する理由

割合だけを見ると、その数字がどの分母・分類から出たのかが見えにくくなります。

単純な計算でも、分子、分母、丸め方、主張できる範囲を固定して再確認しておくと、「再現したもの」と「まだ確認していないもの」を分けて記録できます。

## 出典

Heckerman GO, Tzng E, Campos-Melendez A, et al. *Transparency of research practices in cardiovascular literature*. eLife. 2025;14:e81051.

- https://elifesciences.org/articles/81051
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12068865/

## 根拠の範囲

これは公表論文に記載された一つの数値関係を対象とした限定的な再計算です。臨床上の結論や医学的助言ではなく、他分野の研究再現性を推定するものでもありません。
