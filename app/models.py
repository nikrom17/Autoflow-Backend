import os
from sqlalchemy import Column, ARRAY, String, Integer, Boolean, DateTime, Float, create_engine, ForeignKey
from sqlalchemy.orm import relationship

from .extensions import db


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
    todo = relationship("Todo", back_populates="lead")
    
    
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
    quotedPrice = Column(Float, nullable=True)
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

'''
Todos

'''

class Todo(db.Model):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    completed = Column(Boolean)
    datecompleted = Column(String, nullable=True)
    dateCreated = Column(String)
    description = Column(String)
    leadId = Column(Integer, ForeignKey('lead.id'))
    priorityRank = Column(Integer)
    
    lead = relationship("Lead", back_populates="todo")

    def __init__(
        self,
        completed,
        datecompleted,
        dateCreated,
        description,
        leadId,
        priorityRank,
    ):
        self.completed = completed
        self.datecompleted = datecompleted
        self.dateCreated = dateCreated
        self.description = description
        self.leadId = leadId
        self.priorityRank = priorityRank

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
            'completed': self.completed,
            'datecompleted': self.datecompleted,
            'dateCreated': self.dateCreated,
            'description': self.description,
            'leadId': self.leadId,
            'priorityRank': self.priorityRank,
        }
        