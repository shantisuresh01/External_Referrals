'''
A concrete patient repository in terms of the infrastructure for the abstract
patient repository from the domain model
'''
from repository import AbstractRepository
from bounded_context.domain.Patient import root_entity

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, patient):
        self.session.add(patient)

    def _get(self, patient_id):
        return self.session.query(root_entity.Patient).filter_by(reference = patient_id).first()

    def _get_by_batchref(self, batchref):
        return (
            self.session.query(model.Product)
            .join(model.Batch)
            .filter(orm.batches.c.reference == batchref)
            .first()
        )
