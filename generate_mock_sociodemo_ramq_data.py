from faker import Faker
import pandas as pd
import random

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

# Generate mock data
data = []
for _ in range(20):
    sex = random.choice(["M", "F"])
    record_id = faker.unique.random_int(min=10000, max=99999)
    first_name = faker.first_name_male() if sex == "M" else faker.first_name_female()
    last_name = faker.last_name()
    ddn = str(faker.date_of_birth(minimum_age=18, maximum_age=115))
    code_postal = faker.postcode()
    date_sortie = faker.date_time()
    date_index = faker.date_time()
    date_gem = faker.date_time()
    adresse = faker.street_address()
    no_dossier = faker.unique.random_int(min=100000, max=999999)
    territoire_clsc = faker.city()
    admin_code = str(random.randint(10, 99))

    data.append({
        'RecordID': record_id,
        'Sex': sex,
        'First_Name': first_name,
        'Last_Name': last_name,
        'DDN': ddn,
        'CodePostal': code_postal,
        'Date_Heure_sortie': date_sortie,
        'Date_Heure_index': date_index,
        'Date_Gem': date_gem,
        'Adresse': adresse,
        'No_dossier': no_dossier,
        'Territoire_CLSC': territoire_clsc,
        'Motif': "Tumeur à son petit cerveau",
        'RAMQ': ramq_generator(ddn, last_name, first_name, sex, admin_code)
    })

# Convert to DataFrame
df = pd.DataFrame(data)
df = df[['RecordID', 'First_Name', 'Last_Name', 'DDN', 'CodePostal', 'Date_Heure_sortie',
         'Date_Heure_index', 'Date_Gem', 'Adresse', 'No_dossier', 'Territoire_CLSC', 'RAMQ']]

# Save to CSV
df.to_csv("mock_sociodemo_ramq_data.csv", index=False)

print("Mock sociodemographic data successfully generated and saved.")