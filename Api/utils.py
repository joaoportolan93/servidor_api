import random
from models import Lead, db

# Função para gerar leads fictícios
def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
    emails = ['alisia50@uorak.com', 'cherlyn4935@uorak.com', 'olympia6221@uorak.com', 'erika2729@uorak.com', 'firdaous1969@uorak.com']
    
    for _ in range(100):
        name = random.choice(names)
        email = random.choice(emails)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        telefone = f"({random.randint(10, 99)}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        interest = random.choice(interests)
        lead = Lead(name, email, telefone, latitude, longitude, temperature, interest)
        db.session.add(lead)

        db.session.commit()
