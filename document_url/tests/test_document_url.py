# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64

from odoo.tests import common


class TestDocumentUrl(common.TransactionCase):
    # The "ir.attachment.add_url" wizard of the upstream module was removed in
    # this fork (attachment handling moved to ir.attachment itself), so the
    # upstream wizard test no longer applies.

    def test_dont_broke_default_compute_mimetype(self):
        blob1 = b"blob1"
        blob1_b64 = base64.b64encode(blob1)
        attachment = self.env["ir.attachment"].create(
            {"name": "a2", "datas": blob1_b64, "mimetype": "image/png"}
        )
        self.assertEqual(attachment.mimetype, "image/png")
