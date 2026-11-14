"""Offline tests voor ori.py: python3 -I tools/test_ori.py"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori  # noqa: E402


class OriTests(unittest.TestCase):
    def test_fts_query(self):
        self.assertEqual(ori.fts_query('"rood voor groen"'), '"rood voor groen"')
        self.assertEqual(ori.fts_query("kosten/baten"), '"kosten baten"')
        self.assertEqual(ori.fts_query('a" OR b'), '"a" AND "OR" AND "b"')  # operatoren worden gewone woorden
        self.assertEqual(ori.fts_query("!!!"), "")

    def test_current_entities_laatste_wint_en_delete(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "records.ndjson"), "w") as f:
                for r in ({"op": "upsert", "entity_id": "a", "v": 1}, {"op": "upsert", "entity_id": "a", "v": 2},
                          {"op": "upsert", "entity_id": "b"}, {"op": "delete", "entity_id": "b"}):
                    f.write(json.dumps(r) + "\n")
                f.write('{"op": "upsert", "entity_id": "c"')  # afgebroken regel
            ents = ori.current_entities(d)
            self.assertEqual(list(ents), ["a"])
            self.assertEqual(ents["a"]["v"], 2)

    def test_entity_to_md(self):
        md = ori.entity_to_md({"entityId": "document:x:1", "title": "T", "markdownText": "tekst",
                               "sortDate": "2026-03-02 00:00:00", "downloadUrl": "https://x"})
        self.assertTrue(md.startswith("---\n"))
        self.assertIn('vergaderdatum: "2026-03-02"', md)
        self.assertIn("tekst", md)

    def test_search_cost(self):
        self.assertEqual(ori.search_cost(24), 1.0)
        self.assertAlmostEqual(ori.search_cost(100), 1.304, places=2)


if __name__ == "__main__":
    unittest.main()
