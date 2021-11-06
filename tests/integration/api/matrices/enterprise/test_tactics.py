from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.tactic import Tactic


class TestTactics(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_tactic_by_id(self):
        tactic = next(self.mitre_attack.enterprise.iter_tactics())
        tactic_id = tactic.id

        expected = tactic
        result = self.mitre_attack.enterprise.get_tactic(tactic_id=tactic_id)
        self.assertEqual(expected, result)

    def test_get_tactic_by_name(self):
        tactic = next(self.mitre_attack.enterprise.iter_tactics())
        tactic_name = tactic.name

        expected = tactic
        result = self.mitre_attack.enterprise.get_tactic(tactic_name=tactic_name)
        self.assertEqual(expected, result)

    def test_iter_tactics(self):
        tactics = list(self.mitre_attack.enterprise.iter_tactics())
        self.assertGreater(len(tactics), 0)
        for tactic in tactics:
            self.assertIsInstance(tactic, Tactic)

    def test_iter_tactics_by_id(self):
        tactic = next(self.mitre_attack.enterprise.iter_tactics())

        expected = [tactic.id]
        result = [tactic.id for tactic in self.mitre_attack.enterprise.iter_tactics(tactic_ids=[tactic.id])]
        self.assertEqual(expected, result)

    def test_iter_tactics_by_name(self):
        tactic = next(self.mitre_attack.enterprise.iter_tactics())

        expected = [tactic.name]
        result = [tactic.name for tactic in self.mitre_attack.enterprise.iter_tactics(tactic_names=[tactic.name])]
        self.assertEqual(expected, result)
