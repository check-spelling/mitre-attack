from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.technique import EnterpriseTechnique


class TestTechniques(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_technique_by_id(self):
        technique = next(self.mitre_attack.enterprise.iter_techniques())
        technique_id = technique.id

        expected = technique
        result = self.mitre_attack.enterprise.get_technique(technique_id=technique_id)
        self.assertEqual(expected, result)

    def test_get_technique_by_name(self):
        technique = next(self.mitre_attack.enterprise.iter_techniques())
        technique_name = technique.name

        expected = technique
        result = self.mitre_attack.enterprise.get_technique(technique_name=technique_name)
        self.assertEqual(expected, result)

    def test_iter_techniques(self):
        techniques = list(self.mitre_attack.enterprise.iter_techniques())
        self.assertGreater(len(techniques), 0)
        for technique in techniques:
            self.assertIsInstance(technique, EnterpriseTechnique)

    def test_iter_techniques_by_id(self):
        technique = next(self.mitre_attack.enterprise.iter_techniques())

        expected = [technique.id]
        result = [technique.id for technique in self.mitre_attack.enterprise.iter_techniques(technique_ids=[technique.id])]
        self.assertEqual(expected, result)

    def test_iter_techniques_by_name(self):
        technique = next(self.mitre_attack.enterprise.iter_techniques())

        expected = [technique.name]
        result = [technique.name for technique in self.mitre_attack.enterprise.iter_techniques(technique_names=[technique.name])]
        self.assertEqual(expected, result)
