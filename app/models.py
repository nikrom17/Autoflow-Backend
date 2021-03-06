import os
from sqlalchemy import Column, ARRAY, String, Integer, DateTime, Float, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from .extensions import db


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    initializeDb()
    
def create_all():
    db.create_all()
    initializeDb()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # create_all()



'''
Leads

'''

class Lead(db.Model):
    __tablename__ = 'lead'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=True)
    chanceToConvert = Column(Float)
    dateCreated = Column(DateTime)
    email = Column(String, nullable=True)
    funnelStepId = Column(Integer, ForeignKey('funnelStep.id'))
    lastContact = Column(DateTime)
    name = Column(String)
    phone = Column(String)
    status = Column(String, nullable=True)

    funnelStep = relationship("FunnelStep", back_populates="lead")
    opportunityInfo = relationship("OpportunityInfo", back_populates="lead")
    
    def __init__(
        self,
        address,
        chanceToConvert,
        dateCreated,
        email,
        funnelStepId,
        lastContact,
        name,
        phone,
        status,
    ):
        self.address = address
        self.chanceToConvert = chanceToConvert
        self.dateCreated = dateCreated
        self.email = email
        self.funnelStepId = funnelStepId
        self.lastContact = lastContact
        self.name = name
        self.phone = phone
        self.status = status

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'address': self.address,
            'chanceToConvert': self.chanceToConvert,
            'dateCreated': self.dateCreated,
            'email': self.email,
            'funnelStepId': self.funnelStepId,
            'lastContact': self.lastContact,
            'name': self.name,
            'phone': self.phone,
            'status': self.status
        }


'''
Opportunities

'''

class Opportunity(db.Model):
    __tablename__ = 'opportunity'

    id = Column(Integer, primary_key=True)
    funnelSteps = Column("data", ARRAY(Integer), nullable=True)
    name = Column(String)
    
    funnelStep = relationship("FunnelStep", back_populates="opportunity")
    opportunityInfo = relationship("OpportunityInfo", back_populates="opportunity")

    def __init__(
        self,
        name,
        funnelSteps
    ):
        self.name = name
        self.funnelSteps = funnelSteps

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'funnelSteps': self.funnelSteps,
        }
        

# Eventually the user will be able to add their own fields to each opportunity 
# and these tables will be dynamically generated. This is a representation of
# a tax return opportunity and is used for all opportunites right now.
        
'''
Opportunity Info

'''

class OpportunityInfo(db.Model):
    __tablename__ = 'opportunity_info'

    id = Column(Integer, primary_key=True)
    filingStatus = Column(String)
    finalPrice = Column(String, nullable=True)
    leadId = Column(Integer, ForeignKey('lead.id'))
    occupation = Column(String, nullable=True)
    opportunityId = Column(Integer, ForeignKey('opportunity.id'))
    quotedPrice = Column(String, nullable=True)
    yearlyIncome = Column(String, nullable=True)

    lead = relationship("Lead", back_populates="opportunityInfo")
    opportunity = relationship("Opportunity", back_populates="opportunityInfo")
    
    def __init__(
        self,
        filingStatus,
        finalPrice,
        leadId,
        occupation,
        opportunityId,
        quotedPrice,
        yearlyIncome,
    ):
        self.filingStatus = filingStatus
        self.finalPrice = finalPrice
        self.leadId = leadId
        self.occupation = occupation
        self.opportunityId = opportunityId
        self.quotedPrice = quotedPrice
        self.yearlyIncome = yearlyIncome

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'filingStatus': self.filingStatus,
            'finalPrice': self.finalPrice,
            'leadId': self.leadId,
            'occupation': self.occupation,
            'opportunityId': self.opportunityId,
            'quotedPrice': self.quotedPrice,
            'yearlyIncome': self.yearlyIncome,
        }
        
        
'''
Funnel Steps

'''

class FunnelStep(db.Model):
    __tablename__ = 'funnelStep'

    id = Column(Integer, primary_key=True)
    leads = Column("data", ARRAY(Integer), nullable=True)
    name = Column(String)
    opportunityId = Column(Integer, ForeignKey('opportunity.id'))

    lead = relationship("Lead", back_populates="funnelStep")
    opportunity = relationship("Opportunity", back_populates="funnelStep")
    
    def __init__(
        self,
        name,
        opportunityId,
        leads
    ):
        self.name = name
        self.opportunityId = opportunityId
        self.leads = leads

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'leads' : self.leads,
            'name': self.name,
            'opportunityId' : self.opportunityId,
        }
        


# ---------------------------------------------------------------------------- #
# Initialize Database
# ---------------------------------------------------------------------------- #

def addLeadData():
    for data in leads_default_data:
        lead = Lead(
            data["address"],
            data["chanceToConvert"],
            data["dateCreated"],
            data["email"],
            data["funnelStepId"],
            data["lastContact"],
            data["name"],
            data["phone"],
            data["status"],
        )
        lead.insert()


def addOpportunityData():
    for data in opportunites_default_data:
        opportunity = Opportunity(
            data["name"],
            data["funnelSteps"],
        )
        opportunity.insert()

def addOpportunityInfoData():
    for data in opportunity_info_default_data:
        opportunityInfo = OpportunityInfo(
            data["filingStatus"],
            data["finalPrice"],
            data["leadId"],
            data["occupation"],
            data["opportunityId"],
            data["quotedPrice"],
            data["yearlyIncome"],
        )
        opportunityInfo.insert()
        
def addFunnelStepData():
    for data in funnel_step_default_data:
        funnelStep = FunnelStep(
            data["name"],
            data["opportunityId"],
            data["leads"],
        )
        funnelStep.insert()

def initializeDb():
    print('****** Initializing DB ******')
    addOpportunityData()
    addFunnelStepData()
    addLeadData()
    addOpportunityInfoData()

# ---------------------------------------------------------------------------- #
# Initial App Data
# ---------------------------------------------------------------------------- #

leads_default_data = [
{
    "address": "1355 Market St #900, San Franciso, CA, 94103",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "jdorsey@twitter.com",
    "funnelStepId": 1,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Jack Dorsey",
    "phone": "+14152229670",
    "status": "Follow Up"
},
{
    "address": "9665 Cleveland St, Waterloo, IA 50701",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "weidai@icloud.com",
    "funnelStepId": 1,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Mahaut Brennan",
    "phone": "+15039400326",
    "status": "Automated"
},
{
    "address": "8997 Summit St, Avon, IN 4612",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "cyrus@yahoo.com",
    "funnelStepId": 2,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Janice Perez",
    "phone": "+16315750173",
    "status": "Hot Lead"
},
{
    "address": "253 Edgewater Lane, Elyria, OH 44035",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "bolow@mac.com",
    "funnelStepId": 2,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Lawrence Lowe",
    "phone": "+16102496449",
    "status": "With Client"
},
{
    "address": "196 Armstrong Avenue, Leland, NC 28451",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "violinhi@yahoo.com",
    "funnelStepId": 3,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "George Wells",
    "phone": "+18068957878",
    "status": "Automated"
},
{
    "address": "711 East Shore St, Mays Landing, NJ 08330",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "greear@sbcglobal.net",
    "funnelStepId": 4,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Kelly Castillo",
    "phone": "+18145692368",
    "status": "On Hold"
},
{
    "address": "601 North St Louis Drive, Bedford, OH 44146",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "elflord@gmail.com",
    "funnelStepId": 8,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Owen Christensen",
    "phone": "+16206600336",
    "status": "Follow Up"
},
{
    "address": "29 Mountainview St, Matthews, NC 28104",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "sakusha@live.com",
    "funnelStepId": 8,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Janis Houston",
    "phone": "+16624035765",
    "status": "Follow Up"
},
{
    "address": "9783 Purple Finch St, Saint Petersburg, FL 33702",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "jshirley@gmail.com",
    "funnelStepId": 9,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Malcolm Ryan",
    "phone": "+19156131347",
    "status": "Hot Lead"
},
{
    "address": "9236 N. Grand Avenue, Webster, NY 14580",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "jkonit@live.com",
    "funnelStepId": 10,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Leah Reeves",
    "phone": "+15077972317",
    "status": "With Client"
},
{
    "address": "7675 Albany Street, North Canton, OH 44720",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "moonlapse@outlook.com",
    "funnelStepId": 15,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Trevor Fleming",
    "phone": "+15165758539",
    "status": "Automated"
},
{
    "address": "9266 W. Alton Court, Howell, NJ 07731",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "sopwith@msn.com",
    "funnelStepId": 22,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Raymond Rios",
    "phone": "+19707794663",
    "status": "With Client"
},
{
    "address": "8431 High Noon Drive, Dublin, GA 31021",
    "chanceToConvert": 0.35,
    "dateCreated": "2021-02-26T15:32:37.843Z",
    "email": "wetter@gmail.com",
    "funnelStepId": 23,
    "lastContact": "2021-02-26T15:32:37.843Z",
    "name": "Nathaniel Harris",
    "phone": "+12025550228",
    "status": "Follow Up"
}]

opportunites_default_data = [
    {
        'name': "Individual Tax Return",
        'funnelSteps': [1,2,3,4,5,6,7]
    },
    {
        'name': "Business Tax Return",
        'funnelSteps': [8,9,10,11,12,13,14]
    },
    {
        'name': "Accounting",
        'funnelSteps': [15,16,17,18,19,20,21]
    },
    {
        'name': "Payroll",
        'funnelSteps': [22,23,24,25,26,27,28]
    },
]
opportunity_info_default_data = [
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 1,
        "occupation": 'Software Engineer',
        "opportunityId": 1,
        "quotedPrice": '$150',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Married',
        "finalPrice": None,
        "leadId": 2,
        "occupation": 'Business Analyst',
        "opportunityId": 1,
        "quotedPrice": '$350',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Head of Household',
        "finalPrice": None,
        "leadId": 3,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": '$300',
        "yearlyIncome": '$150k+'
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 4,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": '$105',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 5,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": '$225',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Married',
        "finalPrice": None,
        "leadId": 6,
        'occupation': 'Senior Consultant',
        'opportunityId': 1,
        'quotedPrice': '$300',
        "yearlyIncome": '$150k+',
    },
    {
        'filingStatus': 'Single',
        "finalPrice": None,
        "leadId": 7,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": '$250',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 8,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        'quotedPrice': '$150',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": '$200',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": '$200',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 3,
        "quotedPrice": '$200',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        'opportunityId': 4,
        "quotedPrice": '$200',
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 4,
        "quotedPrice": '$200',
        "yearlyIncome": '$150k+',
    },
]

funnel_step_default_data= [
    # individual tax return
    {
        "name": "Initial Inquiry",
        "opportunityId": 1,
        "leads" : [1, 2],
    },
    {
        "name": "Took Questionnaire",
        "opportunityId": 1,
        "leads" : [3,4],
    },
    {
        "name": "Scheduled Phone Consult",
        "opportunityId": 1,
        "leads" : [5],
    },
    {
        "name": "Had a Phone Consult",
        "opportunityId": 1,
        "leads" : [6],
    },
    {
        "name": "Expressed Interest",
        "opportunityId": 1,
        "leads" : [],
    },
    {
        "name": "Created Portal Account",
        "opportunityId": 1,
        "leads" : [],
    },
    {
        "name": "Signed Engagement Letter",
        "opportunityId": 1,
        "leads" : [],
    },
    # business tax return
    {
        "name": "Initial Inquiry",
        "opportunityId": 2,
        "leads" : [7,8],
    },
    {
        "name": "Took Questionnaire",
        "opportunityId": 2,
        "leads" : [9],
    },
    {
        "name": "Scheduled Phone Consult",
        "opportunityId": 2,
        "leads" : [10],
    },
    {
        "name": "Had a Phone Consult",
        "opportunityId": 2,
        "leads" : [],
    },
    {
        "name": "Expressed Interest",
        "opportunityId": 2,
        "leads" : [],
    },
    {
        "name": "Created Portal Account",
        "opportunityId": 2,
        "leads" : [],
    },
    {
        "name": "Signed Engagement Letter",
        "opportunityId": 2,
        "leads" : [],
    },
    # accounting
    {
        "name": "Initial Inquiry",
        "opportunityId": 3,
        "leads" : [11],
    },
    {
        "name": "Took Questionnaire",
        "opportunityId": 3,
        "leads" : [],
    },
    {
        "name": "Scheduled Phone Consult",
        "opportunityId": 3,
        "leads" : [],
    },
    {
        "name": "Had a Phone Consult",
        "opportunityId": 3,
        "leads" : [],
    },
    {
        "name": "Expressed Interest",
        "opportunityId": 3,
        "leads" : [],
    },
    {
        "name": "Created Portal Account",
        "opportunityId": 3,
        "leads" : [],
    },
    {
        "name": "Signed Engagement Letter",
        "opportunityId": 3,
        "leads" : [],
    },
    # payroll
    {
        "name": "Initial Inquiry",
        "opportunityId": 4,
        "leads" : [12],
    },
    {
        "name": "Took Questionnaire",
        "opportunityId": 4,
        "leads" : [13],
    },
    {
        "name": "Scheduled Phone Consult",
        "opportunityId": 4,
        "leads" : [],
    },
    {
        "name": "Had a Phone Consult",
        "opportunityId": 4,
        "leads" : [],
    },
    {
        "name": "Expressed Interest",
        "opportunityId": 4,
        "leads" : [],
    },
    {
        "name": "Created Portal Account",
        "opportunityId": 4,
        "leads" : [],
    },
    {
        "name": "Signed Engagement Letter",
        "opportunityId": 4,
        "leads" : [],
    },
]