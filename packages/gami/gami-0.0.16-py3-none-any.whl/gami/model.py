from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class PatientDemographic(Base):
    """Patient demographics."""

    __tablename__ = "patient_demographic"

    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    gender_cd = Column(String(1))
    birth_dt = Column(Date)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    claims = relationship("ClaimHeader", backref="patient")
    eligibility = relationship("PatientEligibility", backref="patient")


class PatientEligibility(Base):
    """Benefit eligibility start/end dates."""

    __tablename__ = "patient_eligibility"

    patient_id = Column(
        Integer, ForeignKey("patient_demographic.patient_id"), primary_key=True
    )
    sequence_id = Column(Integer, primary_key=True)
    benefit_plan_cd = Column(String(10))
    start_dt = Column(Date)
    end_dt = Column(Date)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class ClaimHeader(Base):
    """Claim header."""

    __tablename__ = "claim_header"

    patient_id = Column(Integer, ForeignKey("patient_demographic.patient_id"))
    claim_id = Column(Integer, primary_key=True)
    claim_type_cd = Column(String(1))
    service_start_dt = Column(Date)
    service_end_dt = Column(Date)
    provider_performing_id = Column(Integer)
    provider_billing_id = Column(Integer)
    provider_prescribing_id = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    details = relationship("ClaimDetail", backref="header")


class ClaimDetail(Base):
    """Claim detail."""

    __tablename__ = "claim_detail"

    claim_id = Column(Integer, ForeignKey("claim_header.claim_id"), primary_key=True)
    sequence_id = Column(Integer, primary_key=True)

    ndc_cd = Column(String(11))
    revenue_cd = Column(String(5))

    provider_performing_id = Column(Integer)
    provider_billing_id = Column(Integer)
    provider_prescribing_id = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class ProviderDemographic(Base):
    """Provider demographic."""

    __tablename__ = "provider_demographic"

    provider_id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    specialties = relationship("ProviderSpecialty", backref="provider")


class ProviderSpecialty(Base):
    """Provider specialty."""

    __tablename__ = "provider_specialty"

    provider_id = Column(
        Integer, ForeignKey("provider_demographic.provider_id"), primary_key=True
    )
    provider_specialty_cd = Column(String(2))
    start_dt = Column(Date)
    end_dt = Column(Date)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
