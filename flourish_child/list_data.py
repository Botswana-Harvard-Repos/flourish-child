from edc_constants.constants import NOT_APPLICABLE, OTHER, NONE

from edc_list_data import PreloadData

list_data = {
    'flourish_child.childdiseases': [
        ('pneumonia', 'Pneumonia'),
        ('tuberculosis', 'Tuberculosis'),
        ('bronchiolitis', 'Bronchiolitis'),
        ('laryngotracheobronchitis', 'Laryngotracheobronchitis / Croup'),
        ('acute_diarrheal_disease ', 'Acute diarrheal disease '),
        ('persistent_diarrheal_disease  ', 'Persistent diarrheal disease'),
        ('meningitis', 'Meningitis'),
        ('malaria', 'Malaria'),
        ('measles', 'Measles'),
        ('trauma', 'Trauma'),
        ('febrile_seizure ', 'Febrile seizure '),
        ('malnutrition', 'Malnutrition'),
        ('anemia', 'Anemia'),
        ('surgical_reason', 'Surgical reason'),
        (OTHER, 'Other'),
    ],
    'flourish_child.chronicconditions': [
        ('asthma', 'Asthma'),
        ('headache', 'Headache (includes migraines, tension headaches)'),
        ('anemia', 'Anemia'),
        ('cardiac_murmur', 'Cardiac murmur'),
        ('seizure_other_epilepsy', 'Seizure disorder or other epilepsy'),
        ('diabetes', 'Diabetes'),
        ('high_blood_pressure', 'High Blood Pressure'),
        ('high_cholesterol', 'High Cholesterol'),
        ('depression', 'Depression'),
        ('systemic_lupus', 'Systemic Lupus'),
        ('juvenile_rheumatoid_arthritis ', 'Juvenile rheumatoid arthritis'),
        ('nephrotic_syndrome ', 'Nephrotic syndrome'),
        ('renal_insufficiency', 'Renal insufficiency'),
        ('nephrolithiasis', 'Nephrolithiasis (kidney stones)'),
        ('cancer_solid_tumor', 'Cancer (Solid tumor)'),
        ('cancer_leukemia_lymphoma_related', 'Cancer (Leukemia, lymphoma related) '),
        ('cardiac_arrhythmia ', 'Cardiac arrhythmia'),
        ('thyroid_disorder ', 'Thyroid disorder'),
        ('inflammatory_bowel_disease',
         'Inflammatory bowel disease (Crohn’s, ulcerative colitis)'),
        (OTHER, 'Other, Specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'flourish_child.childmedications': [
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Cholesterol medications', 'Cholesterol medications'),
        ('Vitamin D supplement', 'Vitamin D supplement'),
        (NONE, 'None'),
        ('Traditional medications', 'Traditional medications'),
        ('Hypertensive medications', 'Hypertensive medications'),
        ('Prenatal Vitamins', 'Prenatal Vitamins')
    ],
    'flourish_child.wcsdxadult': [
        ('Asymptomatic', 'Asymptomatic'),
        ('Persistent generalized lymphadeno',
         'Persistent generalized lymphadeno'),
        ('Unexplained moderate weight loss',
         'Unexplained moderate weight loss'),
        ('Recurrent resp tract infection', 'Recurrent resp tract infection'),
        ('Herpes zoster', 'Herpes zoster'),
        ('Angular cheilitis', 'Angular cheilitis'),
        ('Recurrent oral ulceration', 'Recurrent oral ulceration'),
        ('Papular pruritic eruptions', 'Papular pruritic eruptions'),
        ('Seborrhoeic dermatitis', 'Seborrhoeic dermatitis'),
        ('Fungal nail infections', 'Fungal nail infections'),
        ('Unexplained* severe weight loss', 'Unexplained* severe weight loss'),
        ('Unexplained persistent fever', 'Unexplained persistent fever'),
        ('Unexplained chronic diarrhoea', 'Unexplained chronic diarrhoea'),
        ('Persistent oral candidiasis', 'Persistent oral candidiasis'),
        ('Oral hairy leukoplakia', 'Oral hairy leukoplakia'),
        ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
        ('Severe bacterial infections', 'Severe bacterial infections'),
        ('stomatitis/gingivitis/periodontis',
         'Stomatitis/gingivitis/periodontis'),
        ('anaemia/neutropaenia/thrombocytopa',
         'Anaemia/neutropaenia/thrombocytopa'),
        ('HIV wasting syndrome', 'HIV wasting syndrome'),
        ('Pneumocystis pneumonia', 'Pneumocystis pneumonia'),
        ('Recurrent severe bacterial pneumo',
         'Recurrent severe bacterial pneumo'),
        ('Chronic herpes simplex infection',
         'Chronic herpes simplex infection'),
        ('Oesophageal candidiasis', 'Oesophageal candidiasis'),
        ('Extrapulmonary tuberculosis', 'Extrapulmonary tuberculosis'),
        ('Kaposi\u2019s sarcoma', 'Kaposi\u2019s sarcoma'),
        ('Cytomegalovirus infection', 'Cytomegalovirus infection'),
        ('CNS toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV encephalopathy', 'HIV encephalopathy'),
        ('Exp cryptococcosis/meningitis', 'Exp cryptococcosis/meningitis'),
        ('Diss non-TB mycobacterial infection',
         'Diss non-TB mycobacterial infection'),
        ('Prog multifocal leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('Chronic cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('Chronic isosporiasis', 'Chronic isosporiasis'),
        ('Disseminated mycosis', 'Disseminated mycosis'),
        ('Recurrent septicaemia', 'Recurrent septicaemia'),
        ('Lymphoma', 'Lymphoma'),
        ('Invasive cervical carcinoma', 'Invasive cervical carcinoma'),
        ('Atypical disseminated leishmaniasis',
         'Atypical disseminated leishmaniasis'),
        ('Sympt nephropathy/cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        (NONE, 'None')
    ],
    'flourish_child.childcovidsymptoms': [
        ('chest_pain', 'Chest pain'),
        ('chills', 'Chills'),
        ('Cough', 'Cough'),
        ('Diarrhea ', 'Diarrhea '),
        ('Fever', 'Fever > 37.5 Degree Celsius'),
        ('muscle_aches', 'Muscle aches'),
        ('nasal_congestion', 'Nasal Congestion/Runny Nose'),
        ('Nausea_or_vomiting  ', 'Nausea/vomiting'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('sore_throat', 'Sore throat'),
        ('headache', 'Headache'),
        ('loss_smell', 'Loss of Smell'),
        ('loss_taste', 'Loss of Taste'),
        ('no_symptoms', 'No Symptoms'),
    ],
    'flourish_child.childcovidsymptomsafter14days': [
        ('chest_pain', 'Chest pain'),
        ('chills', 'Chills'),
        ('Cough', 'Cough'),
        ('Diarrhea ', 'Diarrhea '),
        ('Fever', 'Fever > 37.5 Degree Celsius'),
        ('muscle_aches', 'Muscle aches'),
        ('nasal_congestion', 'Nasal Congestion'),
        ('Nausea_or_vomiting  ', 'Nausea/vomiting'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('sore_throat', 'Sore throat'),
        ('headache', 'Headache'),
        ('loss_smell', 'Loss of Smell'),
        ('loss_taste', 'Loss of Taste'),
        ('no_symptoms', 'No Symptoms'),
    ],
    'flourish_child.solidfoods': [
        ('grains_roots_tubers', 'Grains, roots and tubers'),
        ('legumes_nuts', 'Legumes and nuts'),
        ('dairy_products', 'Dairy products (milk, yogurt, cheese)'),
        ('flesh_foods', 'Flesh foods (meat, fish, poultry and liver/organ meat)'),
        ('eggs', 'Eggs'),
        ('porridge', 'Porridge'),
        ('vitamin_a_rich_fruits_vegies',
         'Vitamin A rich fruits and vegetables (carrots, pumpkin, sweet potato)'),
        ('other_fruits_vegies', 'Other fruits and vegetables'),
        ('other_solid_foods', 'Other solid foods'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
