from unittest import TestCase
from mitre_attack.api.client import MitreAttack
from mitre_attack.data.types.tool import Tool


class TestTools(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mitre_attack = MitreAttack()

    def test_get_tool_by_id(self):
        tool = next(self.mitre_attack.enterprise.iter_tools())
        software_id = tool.id

        expected = tool
        result = self.mitre_attack.enterprise.get_tool(software_id=software_id)
        self.assertEqual(expected, result)

    def test_get_tool_by_name(self):
        tool = next(self.mitre_attack.enterprise.iter_tools())
        software_name = tool.name

        expected = tool
        result = self.mitre_attack.enterprise.get_tool(software_name=software_name)
        self.assertEqual(expected, result)

    def test_iter_tools(self):
        tools = list(self.mitre_attack.enterprise.iter_tools())
        self.assertGreater(len(tools), 0)
        for tool in tools:
            self.assertIsInstance(tool, Tool)

    def test_iter_tools_by_id(self):
        tool = next(self.mitre_attack.enterprise.iter_tools())

        expected = [tool.id]
        result = [tool.id for tool in self.mitre_attack.enterprise.iter_tools(software_ids=[tool.id])]
        self.assertEqual(expected, result)

    def test_iter_tools_by_name(self):
        tool = next(self.mitre_attack.enterprise.iter_tools())

        expected = [tool.name]
        result = [tool.name for tool in self.mitre_attack.enterprise.iter_tools(software_names=[tool.name])]
        self.assertEqual(expected, result)
