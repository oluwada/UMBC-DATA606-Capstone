# Using Respiratory Metrics to Predict Early-Life Vitamin D Deficiency in Mice under Environmental Stress


*Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang*

**Author:** Oluwadamilare Aboyewa | **Semester:** Spring 2026 

**Course:** DATA 606 - Capstone in Data Science | **University:** University of Maryland, Baltimore County (UMBC)

---

## Quick Links

| Resource | Link |
|----------|------|
| **YouTube Presentation** | [Add Youtube Link] |
| **PowerPoint Presentation** |[Presentation Link](https://docs.google.com/presentation/d/1_Uo2MiB9m6ylytOplbu0HKU-DJ01xhvTqXBE-wt9oTU/edit?usp=sharing)
| **GitHub Repository** | [GitHub Link](https://github.com/oluwada) |
| **LinkedIn**| [LinkedIn Link](https://www.linkedin.com/in/damilare-aboyewa-511ab1295/)|

---
## Table of Contents

- [Background](#background)
- [Data](#data)
---

## Background

- What is this about?

  This project uses machine learning to classify diet type in mice based on respiratory physiology data. It focuses on early-life vitamin D deficiency which can induce long-lasting changes in lung function. Respiratory metrics were collected under both filtered and smog air to determine whether early-life diet produces dectectable patterns that can be used to predict diet type.
   
 - Why does this matter?
  	- Vitamin D deficiency is a **global health problem** affecting people of all ages.
    - Vitamin D deficiency in early childhood is associated with reduced lung function and higher risk of developing respiratory illnesses later in life
  	- Severe vitamin D deficiency is associated with increased susceptibility to respiratory infections such as influenza, pneumonia, and Covid-19
    - Severe vitamin D deficiency can worsen outcomes in patients with acute respiratory failure increasing morality risk.
     
- Research Questions:
  - Which respiratory features are most predictive of early-life diet type in mice? 
  - What are the physiological respiratory patterns associated with early-life vitamin D deficiency?
  - Does filtered and smog air affect respiratory function and is the effect different depending on diet type?
 
## Data
**Data Name**:`'Vitamin D and smog ECG.HRV.WBP data - Buxco-WBP.csv'`

**Data Source**: `Data.gov`

**Data Size**: 54 kB

**Data Shape** 646759 rows × 11 columns

**Row representation**: An animal subject(mice). There are multiple rows tied to each subject.

**Data Dictionary**:

| Column Name         | Data Type | Definition                                                               |
|---------------------|-----------|--------------------------------------------------------------------------|
| Animal ID           | INT       | Identifier for the mice                                                  |
| Diet                | STR       | Type of Diet                                                             |
| Exposure            | STR       | Type of air conditions                                                   |
| Log Time            | FLOAT     | Time each respiratory metric is recorded per mice (secs)                 |
| Breathing Frequency | FLOAT     | Number of breaths per minute                                             |
| Tidal Volume        | FLOAT     | Volume of air inhaled or exhaled per breath                              |
| Inspiratory Time    | FLOAT     | Period of inhale per breath (secs)                                       |
| Expiratory Time     | FLOAT     | Period of exhale per breath (secs)                                       |
| Penh                | FLOAT     | Enhanced Pause; Measures airway resistance                               |
| Age                 | STR       | Age of mouse at measurement                                              |
| Time of Experiment  | STR       | Identifier of experiment batch                                           |

---

**Targe/Label Column**: Diet 

**Feature Columns**: 
- Exposure
- Breathing Frequency
- Tidal Volume
- Inspiratory Time
- Expiratory TIme
- Penh

**Assumptions**
- The dataset contains longitudinal respiratory metrics for each mouse.
Since the total number of subjects is small (n = 24)  and the focus is on modeling ,
each row is treated as an indepenedent observation.
This assuems that within -subject correlation does not introduce signifcant bias to the model.
Features such as Log Time and Time of Experiment are dropped to avoid batch effects and temporal confounding, allowing the model to focus on respiratory metrics and exposure type as predictors of diet.

## Exploratory Data Analysis 
- This section will include:
  - Data Quality Check
  - Univariate and Multivariate data analysis
  - Data Preprocessing(Encoding)
 

**Data Quality Check**
|Feature           | Percent Missing|
|------------------|----------------|
|ID                |    0.00000     |
|DIET              |    0.00000     |
|Exposure          |    3.23428     |
|Log Time          |     0.00000    |
|Breathing Frequency|    0.00000    |
|Tidal volume      |     0.00000    |
|Inspiratory Time  |    0.00000     |
|Expiratory Time   |    0.00000     |
|Penh              |     0.00000    |
|Age               |    0.00000     |
|Time of Experiment|     0.00000    |

**Note**: Some observations in the Exposure column had placeholder values (.) so the true perecentage missing is 20%. These rows were kept since the other feature values were complete.
Missing Exposure values were filled with the category "Unknown" to preserve these rows for modeling.
