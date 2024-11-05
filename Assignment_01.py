#Load csv file
import pandas as pd
file_path = r"C:\Users\HP\Desktop\class\ASSIGNMENT\UserDetails.csv"
data = pd.read_csv(file_path)
df_data = pd.DataFrame(data)

#Add new column d_code
df_data['d_code'] = 11

#Define dictionary for department codes
department_codes = {
    'Quality': 33,
    'Finance': 44,
    'Human Resources': 66,
    'Information Technology': 77,
    'Marketing': 88,
    'Operations': 99
}

# Update 'd_code' based on the 'dept' column using the mapping
df_data['d_code'] = df_data['dept'].map(department_codes).fillna(11).astype(int)

#Define male_code and female_code
male_code = 3031
female_code = 4038

#Make new column g_code
df_data['g_code'] = None

#Assign unique codes based on gender with %2 checks
for index, row in df_data.iterrows():
    if row['gender'] == 'Male':
        # Ensure male_code is odd
        if male_code % 2 == 0:
            male_code += 2
        df_data.at[index, 'g_code'] = male_code
        male_code += 2  # Increment for the next code, keeping it odd
    elif row['gender'] == 'Female':
        # Ensure female_code is even
        if female_code % 2 != 0:
            female_code += 2
        df_data.at[index, 'g_code'] = female_code
        female_code += 2  # Increment for the next code, keeping it even

#Create new column b_code
df_data['b_code'] = ''

#Create 'b_code' column by converting 'date_of_birth' directly to the 'yyMMdd' format
df_data['b_code'] = pd.to_datetime(df_data['date_of_birth'], errors='coerce').dt.strftime('%y%m%d')

#Create new column NomborKadPengenalan
df_data['NomborKadPengenalan'] = ''

#Create 'Nombor Kad Pengenalan' column in the format 'b_code-d_code-g_code'
df_data['NomborKadPengenalan'] = df_data['b_code'].astype(str) + '-' + df_data['d_code'].astype(str) + '-' + df_data['g_code'].astype(str)

#Select the required columns for the new DataFrame
new_df = df_data[['userid', 'firstname', 'lastname', 'date_of_birth', 'gender', 'dept', 'NomborKadPengenalan']]

#Specify the path for the new CSV file
output_file_path = r"C:\Users\HP\Desktop\class\ASSIGNMENT\UserDetailsWithICNumberFINAL.csv"

#Save the new DataFrame to a CSV file
new_df.to_csv(output_file_path, index=False)

print("New DataFrame saved as 'UserDetailsWithICNumberFINAL.csv'.")

