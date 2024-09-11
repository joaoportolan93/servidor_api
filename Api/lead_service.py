from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def create_lead(self, name, email, telefone):
        lead = Lead(name=name, telefone=telefone, email=email)
        self.db.session.add(lead)
        self.db.session.commit()

    def get_all_leads(self):
        return Lead.query.all()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def update_lead(self, lead_id, name, email, telefone):
        lead = self.get_lead_by_id(lead_id)
        lead.name = name
        lead.email = email
        lead.telefone = telefone
        
        self.db.session.commit()

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self
