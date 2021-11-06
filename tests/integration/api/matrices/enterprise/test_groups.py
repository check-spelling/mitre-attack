from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.group import Group


class TestGroups(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_group_by_id(self):
        group = next(self.mitre_attack.enterprise.iter_groups())
        group_id = group.id

        expected = group
        result = self.mitre_attack.enterprise.get_group(group_id=group_id)
        self.assertEqual(expected, result)

    def test_get_group_by_name(self):
        group = next(self.mitre_attack.enterprise.iter_groups())
        group_name = group.name

        expected = group
        result = self.mitre_attack.enterprise.get_group(group_name=group_name)
        self.assertEqual(expected, result)

    def test_iter_groups(self):
        groups = list(self.mitre_attack.enterprise.iter_groups())
        self.assertGreater(len(groups), 0)
        for group in groups:
            self.assertIsInstance(group, Group)

    def test_iter_groups_by_id(self):
        group = next(self.mitre_attack.enterprise.iter_groups())

        expected = [group.id]
        result = [group.id for group in self.mitre_attack.enterprise.iter_groups(group_ids=[group.id])]
        self.assertEqual(expected, result)

    def test_iter_groups_by_name(self):
        group = next(self.mitre_attack.enterprise.iter_groups())

        expected = [group.name]
        result = [group.name for group in self.mitre_attack.enterprise.iter_groups(group_names=[group.name])]
        self.assertEqual(expected, result)
