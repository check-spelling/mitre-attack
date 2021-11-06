from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.relationship import Relationship


class TestRelationships(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_relationship_by_id(self):
        relationship = next(self.mitre_attack.enterprise.iter_relationships())
        relationship_id = relationship.id

        expected = relationship
        result = self.mitre_attack.enterprise.get_relationship(relationship_id=relationship_id)
        self.assertEqual(expected, result)

    def test_iter_relationships(self):
        relationships = list(self.mitre_attack.enterprise.iter_relationships())
        self.assertGreater(len(relationships), 0)
        for relationship in relationships:
            self.assertIsInstance(relationship, Relationship)

    def test_iter_relationships_by_id(self):
        relationship = next(self.mitre_attack.enterprise.iter_relationships())

        expected = [relationship.id]
        result = [relationship.id for relationship in self.mitre_attack.enterprise.iter_relationships(relationship_ids=[relationship.id])]
        self.assertEqual(expected, result)
