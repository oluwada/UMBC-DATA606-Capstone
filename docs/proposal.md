# Analyzing the Biological Signatures of Vitamin D Deficiency using Cardiac Metrics


*Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang*

**Author:** Oluwadamilare Aboyewa | **Semester:** Spring 2026 

**Course:** DATA 606 - Capstone in Data Science | **University:** University of Maryland, Baltimore County (UMBC)

---

## Quick Links

| Resource | Link |
|----------|------|
| **YouTube Presentation** | [Add Youtube Link] |
| **PowerPoint Presentation** | [Presentation Link](https://docs.google.com/presentation/d/1_Uo2MiB9m6ylytOplbu0HKU-DJ01xhvTqXBE-wt9oTU/edit?usp=sharing)] |
| **GitHub Repository** | [GitHub Link](https://github.com/oluwada) |
| **LinkedIn**| [LinkedIn Link](https://www.linkedin.com/in/damilare-aboyewa-511ab1295/)|

---
## Table of Contents

- [Background](#background)
- [Data](#data)
---

## Background

- What is this about?
	- Using machine learning to uncover the biological patterns of the Cardiac system commonly asscoiated with being vitamin D deficient.
   
 - Why does this matter?
  	- Vitamin D Deficieny is a **global health problem**
  	- Vitamin D plays an essential role in regulating the heart. Low vitamin D levels can cause blood pressure to be high causing the heart to overwork to pump blood and damage the heart over time.
     
- Research Questions:
  - What are the biological patterns associated with being vitamin deficient in the cardiac system?
  - What are the biological patterns associated with being vitamin deficient and blocking cation channels(TRPC6) in the cardiac system?
  - How does the intensity of a hard-working heart correlate with vitamin D.

## Data
**Data Name**:`KS5_VDD TRPC6_Complete data set.xlsx`

**Data Source**: `Data.gov/ U.S Environmental Protection Agency`

**Data Size**: 751.3 kB

**Data Shape** 1872 rows x 10 columns

**Row representation**: An animal subject(mice). There are multiple rows tied to each subject.

**Data Dictionary**:

| Column Name | Data Type | Definition                                                               |
|-------------|-----------|--------------------------------------------------------------------------|
| Animal ID   | INT       | Identifier for the mice                                                  |
| Diet        | STR       | Type of Diet                                                             |
| SDNN        | FLOAT     | Standard deviation of the time between normal-to-normal beats            |
| RMSSD       | FLOAT     | Root mean squared of successive differences                              |
| LF          | FLOAT     | Low Frequency                                                            |
| HF          | FLOAT     | High Frequency                                                           |
| LF/HF       | FLOAT     | Ratio of these two frequency domains (LF/HF). It provides an estimate of the relative balance between sympathetic (LF) and vagal (HF) activity.|
| timepoint   | STR       | N/A                                                                      |
| dose        | STR       | Dosage of dobutamine(The drug that agitates the heart)                   |
| Trt Code    | STR       | Summary of Treatment give to subject                                     | 

---

**Targe/Label Column**: Diet 

**Feature Columns**: 
- SDNN
- RMSDD
- LF
- HF
- LF/HF
- timepoint
- dose



