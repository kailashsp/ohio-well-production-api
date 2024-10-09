from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from data_processor import compute_annual_data,read_xls
Base = declarative_base()


class WellProduction(Base):
    __tablename__ = 'well_production'

    api_well_number = Column(Integer, primary_key=True)
    oil = Column(Float)
    gas = Column(Float)
    brine = Column(Float)

class DbProcessor:
    def __init__(self) -> None:
    
        self.engine = create_engine('sqlite:///oil_gas_production.db')
        self.Session = sessionmaker(bind=self.engine)


    def add_annual_data(self,annual_data):

        Base.metadata.create_all(self.engine)

        with self.Session() as session:
            for _, row in annual_data.iterrows():
                well_production = WellProduction(
                    api_well_number=int(row['API WELL  NUMBER']),
                    oil=int(row['OIL']),
                    gas=int(row['GAS']),
                    brine=int(row['BRINE'])
                )
                session.merge(well_production)
            session.commit()

    def filter_annual_data(self, well_number):
        with self.Session() as session:
            well_data = session.query(WellProduction).filter_by(api_well_number=well_number).first()

        return well_data
    
if __name__=="__main__":
    db_inst = DbProcessor()
    df = read_xls('dataset/production.xls')
    annual_data = compute_annual_data(df)
    db_inst.add_annual_data(annual_data)