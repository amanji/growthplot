\COPY growthplot_who_set2_length_for_age_male (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Length_for_Age_Male_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_length_for_age_female (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Length_for_Age_Female_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_weight_for_age_female (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Weight_for_Age_Female_0_19.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_weight_for_age_male (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Weight_for_Age_Male_0_19.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_weight_for_length_female (length, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Weight_for_Length_Female_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_weight_for_length_male (length, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Weight_for_Length_Male_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_bmi_female (month, "L", "M", "S", p3,p10, p25, p50, p75, p85, p97) FROM 'BMI_Female_0_19.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_bmi_male (month, "L", "M", "S", p3,p10, p25, p50, p75, p85, p97) FROM 'BMI_Male_0_19.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_head_circumference_female (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Head_Circumference_Female_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_head_circumference_male (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Head_Circumference_Male_0_2.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_height_for_age_female (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Height_for_Age_Female_2_19.csv' WITH (FORMAT CSV, HEADER true);

\COPY growthplot_who_set2_height_for_age_male (month, "L", "M", "S", p3,p10, p25, p50, p75, p90, p97) FROM 'Height_for_Age_Male_2_19.csv' WITH (FORMAT CSV, HEADER true);