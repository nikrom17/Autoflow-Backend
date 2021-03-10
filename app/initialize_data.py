from .models import Lead, Opportunity, OpportunityInfo, FunnelStep, Todo

# ---------------------------------------------------------------------------- #
# Populate Database
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

def addTodoData():
    for data in todos_default_data:
        todo = Todo(
            data["completed"],
            data["datecompleted"],
            data["dateCreated"],
            data["description"],
            data["leadId"],
            data["priorityRank"],
        )
        todo.insert()
        
def addFunnelStepData():
    for data in funnel_step_default_data:
        funnelStep = FunnelStep(
            data["name"],
            data["opportunityId"],
            data["leads"],
        )
        funnelStep.insert()

def initialize_data():
    print('****** Initializing Data ******')
    addOpportunityData()
    addFunnelStepData()
    addLeadData()
    addOpportunityInfoData()
    addTodoData()

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
        "quotedPrice": 150,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Married',
        "finalPrice": None,
        "leadId": 2,
        "occupation": 'Business Analyst',
        "opportunityId": 1,
        "quotedPrice": 350,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Head of Household',
        "finalPrice": None,
        "leadId": 3,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": 300,
        "yearlyIncome": '$150k+'
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 4,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": 105,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 5,
        "occupation": 'Senior Consultant',
        "opportunityId": 1,
        "quotedPrice": 225,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Married',
        "finalPrice": None,
        "leadId": 6,
        'occupation': 'Senior Consultant',
        'opportunityId': 1,
        'quotedPrice': 300,
        "yearlyIncome": '$150k+',
    },
    {
        'filingStatus': 'Single',
        "finalPrice": None,
        "leadId": 7,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": 250,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 8,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        'quotedPrice': 150,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": 200,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 2,
        "quotedPrice": 200,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 3,
        "quotedPrice": 200,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        'opportunityId': 4,
        "quotedPrice": 200,
        "yearlyIncome": '$150k+',
    },
    {
        "filingStatus": 'Single',
        "finalPrice": None,
        "leadId": 9,
        "occupation": 'Senior Consultant',
        "opportunityId": 4,
        "quotedPrice": 200,
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

todos_default_data = [
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 1,
      "priorityRank": 1,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 2,
      "priorityRank": 2,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 3,
      "priorityRank": 3,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 4,
      "priorityRank": 4,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 5,
      "priorityRank": 5,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 6,
      "priorityRank": 6,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 7,
      "priorityRank": 7,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 8,
      "priorityRank": 8,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 9,
      "priorityRank": 9,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 10,
      "priorityRank": 10,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 11,
      "priorityRank": 11,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 12,
      "priorityRank": 12,
    },
    {
      "completed": False,
      "datecompleted": None,
      "dateCreated": "2021-02-26T15:32:37.843Z",
      "description": "Send email",
      "leadId": 13,
      "priorityRank": 13,
    },
]