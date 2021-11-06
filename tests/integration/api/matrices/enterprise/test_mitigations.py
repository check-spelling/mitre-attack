from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.mitigation import Mitigation


class TestMitigations(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_mitigation_by_id(self):
        mitigation = next(self.mitre_attack.enterprise.iter_mitigations())
        mitigation_id = mitigation.id

        expected = mitigation
        result = self.mitre_attack.enterprise.get_mitigation(mitigation_id=mitigation_id)
        self.assertEqual(expected, result)

    def test_get_mitigation_by_name(self):
        mitigation = next(self.mitre_attack.enterprise.iter_mitigations())
        mitigation_name = mitigation.name

        expected = mitigation
        result = self.mitre_attack.enterprise.get_mitigation(mitigation_name=mitigation_name)
        self.assertEqual(expected, result)

    def test_iter_mitigations(self):
        mitigations = list(self.mitre_attack.enterprise.iter_mitigations())
        self.assertGreater(len(mitigations), 0)
        for mitigation in mitigations:
            self.assertIsInstance(mitigation, Mitigation)

    def test_iter_mitigations_by_id(self):
        mitigation = next(self.mitre_attack.enterprise.iter_mitigations())

        expected = [mitigation.id]
        result = [mitigation.id for mitigation in self.mitre_attack.enterprise.iter_mitigations(mitigation_ids=[mitigation.id])]
        self.assertEqual(expected, result)

    def test_iter_mitigations_by_name(self):
        mitigation = next(self.mitre_attack.enterprise.iter_mitigations())

        expected = [mitigation.name]
        result = [mitigation.name for mitigation in self.mitre_attack.enterprise.iter_mitigations(mitigation_names=[mitigation.name])]
        self.assertEqual(expected, result)
