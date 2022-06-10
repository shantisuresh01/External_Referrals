'''
A concrete patient repository in terms of the infrastructure for the abstract
patient repository from the domain model
'''

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, product):
        self.session.add(patient)

    def _get(self, patientid):
        return self.session.query(model.Patient).filter_by(reference = patientid).first()

    def _get_by_batchref(self, batchref):
        return (
            self.session.query(model.Product)
            .join(model.Batch)
            .filter(orm.batches.c.reference == batchref)
            .first()
        )
