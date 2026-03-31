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

![Image](https://github.com/user-attachments/assets/23e6e38e-6fe7-400b-9a5b-6df795fcd03d)

**Class Balance**

|Class             | Count          |
|------------------|----------------|
|VDD               |    340515      |
|ND                |    306244      |

- The target classes are roughly balanced

![Image](https://github.com/user-attachments/assets/41090cc8-e8a0-4f40-ab0e-94f9f9e909e4)



**Univariate Analysis on Respiratory Metrics**

![Image](https://github.com/user-attachments/assets/3e470e56-4d60-4238-806d-aa8d2e583824)




![Image](https://github.com/user-attachments/assets/75a35f78-3821-4774-b668-27e0bd0276f6)




![Image](https://github.com/user-attachments/assets/2cdb6a57-5d80-4901-9dc5-3c81a1f5cf74)




![Image](https://github.com/user-attachments/assets/df08e5a8-df05-4469-879f-1f4535b79dcd)



![Image](https://github.com/user-attachments/assets/80ff73b4-f0dc-4b22-bc4e-41e139ae78ca)



- All the distributions of the respiratory metrics are rightly skewed meaning most of the observations are found in the lower value range with outliers in higher value range. This may make the model more sensitive to extreme observations potentially affecting the models ability to generalize.

- To address the right-skewedness found in the distributions log transformation will be applied to compresses the range of the data, making the distribution more symmetric.


**Multivariate Analysis**

![Image](https://github.com/user-attachments/assets/d3f7b329-0221-46e7-b877-b7666adb30a1)

- The median breathing frequency was slightly higher in VDD mice compared to ND mice. The VDD mice had a larger IQR and low and high outliers IQR while the ND mice and only showed high outliers showing  greater variability in the VDD group.

![Image](https://github.com/user-attachments/assets/2eb59165-4cd5-4143-8cdb-c224dcc025c4)


- The VDD mice showed lower median tidal volume than ND mice with ND mice showing greater variablity (Larger IQR) Both groups exhibiting high-value outliers.
  
![Image](https://github.com/user-attachments/assets/3a134a69-4779-4e8e-904f-85897cbc253a)

![Image](https://github.com/user-attachments/assets/0bc7c6c4-e005-45c0-8333-a6716f5575a1)

- The VDD mice showed lower median inspiratory and expiratory time than ND mice with ND mice showing slightly greater variability in inspiratory and VDD mice showing greater variability with expiratory time. Both groups exhibit high-value outliers

![Image](https://github.com/user-attachments/assets/e97d29c0-599d-4382-8a34-48d0a24c7fe2)
- The VDD mice showed lower median Penh than ND mice with higher variability being seen in VDD mice and both groups wxhibiting high-value outliers(more in ND Mice)



**Correlation between Respiratory Metrics**

![Image](https://github.com/user-attachments/assets/0f9e2d85-bf2c-4b63-87d6-d5d94b7429e0)

- There is a strong negative correlation between Breathing Frequency and Inspiratory Time and Expiratory Time showing that higher breathing rates are associated with shorter inhalation and exhalation periods. While all the other associations were weak to moderate suggesting a limited relationship between the other respiratory metrics.










