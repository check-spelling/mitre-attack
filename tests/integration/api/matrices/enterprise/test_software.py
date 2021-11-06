from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.software import Software


class TestSoftware(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_software_by_id(self):
        software = next(self.mitre_attack.enterprise.iter_software())
        software_id = software.id

        expected = software
        result = self.mitre_attack.enterprise.get_software(software_id=software_id)
        self.assertEqual(expected, result)

    def test_get_software_by_name(self):
        software = next(self.mitre_attack.enterprise.iter_software())
        software_name = software.name

        expected = software
        result = self.mitre_attack.enterprise.get_software(software_name=software_name)
        self.assertEqual(expected, result)

    def test_iter_software(self):
        software = list(self.mitre_attack.enterprise.iter_software())
        self.assertGreater(len(software), 0)
        for software in software:
            self.assertIsInstance(software, Software)

    def test_iter_software_by_id(self):
        software = next(self.mitre_attack.enterprise.iter_software())

        expected = [software.id]
        result = [software.id for software in self.mitre_attack.enterprise.iter_software(software_ids=[software.id])]
        self.assertEqual(expected, result)

    def test_iter_software_by_name(self):
        software = next(self.mitre_attack.enterprise.iter_software())

        expected = [software.name]
        result = [software.name for software in self.mitre_attack.enterprise.iter_software(software_names=[software.name])]
        self.assertEqual(expected, result)
