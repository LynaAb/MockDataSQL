from faker import Faker
import pandas as pd
import random
from datetime import date, datetime

faker = Faker(['en_CA'])

# Generate a RAMQ number
def ramq_generator(DDN, last_name, first_name, sex, admin_code):
    ramq = last_name[:3].upper() + first_name[0].upper()
    year, month, day = DDN.split('-')
    ramq += year[2:4]

    # Adjust month for gender
    month = str(int(month) + 50) if sex == "F" else month
    ramq += month + day + admin_code
    return ramq

# Function to calculate age from birthdate
def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Function to assign an age factor for Charlson Score
def facteur_age(age):
    if age < 50:
        return 0
    elif 50 <= age <= 59:
        return 1
    elif 60 <= age <= 69:
        return 2
    elif 70 <= age <= 79:
        return 3
    else:
        return 4

# Track unique RAMQ numbers
existing_ramq = set()

# Generate mock data
data = []
for _ in range(20):
    while True:  # Ensure unique RAMQ
        sex = random.choice(["M", "F"])
        record_id = faker.unique.random_int(min=10000, max=99999)
        first_name = faker.first_name_male() if sex == "M" else faker.first_name_female()
        last_name = faker.last_name()
        ddn = str(faker.date_of_birth(minimum_age=18, maximum_age=115))
        age = calculate_age(ddn)
        facteur_age_score = facteur_age(age)
        admin_code = str(random.randint(10, 99))

        ramq = ramq_generator(ddn, last_name, first_name, sex, admin_code)

        if ramq not in existing_ramq:
            existing_ramq.add(ramq)
            break  # Exit loop once a unique RAMQ is found

    code_postal = faker.postcode()
    date_sortie = faker.date_time()
    date_index = faker.date_time()
    date_gem = faker.date_time()
    adresse = faker.street_address()
    no_dossier = faker.unique.random_int(min=100000, max=999999)
    territoire_clsc = faker.city()

    # Generate random Charlson comorbidities
    comorbidities = {
        "infarctus": random.randint(0, 1),
        "congestive_heart_failure": random.randint(0, 1),
        "dementia": random.randint(0, 1),
        "pulmonary_disease": random.randint(0, 1),
        "rheumatologic_disease": random.randint(0, 1),
        "peptic_ulcer": random.randint(0, 1),
        "liver_disease": random.randint(0, 1),
        "diabetes": random.randint(0, 1),
        "hemiplegia": random.randint(0, 1),
        "renal_disease": random.randint(0, 1),
        "cancer": random.randint(0, 1),
        "metastatic_cancer": random.randint(0, 1),
        "AIDS": random.randint(0, 1)
    }

    charlson_score = sum(comorbidities.values()) + facteur_age_score

    data.append({
        'RecordID': record_id,
        'Sex': sex,
        'First_Name': first_name,
        'Last_Name': last_name,
        'DDN': ddn,
        'Age': age,
        'Facteur_Age': facteur_age_score,
        'CodePostal': code_postal,
        'Date_Heure_sortie': date_sortie,
        'Date_Heure_index': date_index,
        'Date_Gem': date_gem,
        'Adresse': adresse,
        'No_dossier': no_dossier,
        'Territoire_CLSC': territoire_clsc,
        'Motif': "Motif temporaire",
        'RAMQ': ramq,
        'Charlson_Score': charlson_score,
        **comorbidities  # Add all comorbidities to the dataset
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Remove any accidental duplicates
df.drop_duplicates(inplace=True)

# Save to CSV
df.to_csv("mock_clinical_data.csv", index=False)

print("Mock clinical data successfully generated and saved.")