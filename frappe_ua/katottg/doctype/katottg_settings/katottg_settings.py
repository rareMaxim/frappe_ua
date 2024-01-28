# Copyright (c) 2024, Maxim Sysoev and contributors
# For license information, please see license.txt

# import frappe
import os
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.csvutils import get_csv_content_from_google_sheets, read_csv_content
from frappe.utils.xlsxutils import (
    read_xls_file_from_attached_file,
    read_xlsx_file_from_attached_file,
)


class KatottgSettings(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        file_doc: DF.Attach | None
    # end: auto-generated types

    def importKatottg(self, file: str):
        self.file_doc = self.file_path = self.google_sheets_url = None
        if isinstance(file, str):
            if frappe.db.exists("File", {"file_url": file}):
                self.file_doc = frappe.get_doc("File", {"file_url": file})
            elif "docs.google.com/spreadsheets" in file:
                self.google_sheets_url = file
            elif os.path.exists(file):
                self.file_path = file

        if not self.file_doc and not self.file_path and not self.google_sheets_url:
            frappe.throw(_("Invalid template file for import"))

        self.raw_data = self.get_data_from_template_file()
        self.parse_data_from_template()

    def get_data_from_template_file(self):
        content = None
        extension = None
        if self.file_doc:
            parts = self.file_doc.get_extension()
            extension = parts[1]
            content = self.file_doc.get_content()
            extension = extension.lstrip(".")
        elif self.file_path:
            content, extension = self.read_file(self.file_path)
        elif self.google_sheets_url:
            content = get_csv_content_from_google_sheets(self.google_sheets_url)
            extension = "csv"
        if not content:
            frappe.throw(_("Invalid or corrupted content for import"))
        if not extension:
            extension = "csv"
        if content:
            return self.read_content(content, extension)

    def read_content(self, content, extension):
        error_title = _("Template Error")
        if extension not in ("csv", "xlsx", "xls"):
            frappe.throw(
                _("Import template should be of type .csv, .xlsx or .xls"),
                title=error_title,
            )

        if extension == "csv":
            data = read_csv_content(content)
        elif extension == "xlsx":
            data = read_xlsx_file_from_attached_file(content)
        elif extension == "xls":
            data = read_xls_file_from_attached_file(content)

        return data

    def parse_data_from_template(self):
        header = None
        data = []
        print(self.raw_data)
        # for i, row in enumerate(self.raw_data):
        #     if all(v in INVALID_VALUES for v in row):
        #         # empty row
        #         continue

        #     if not header:
        #         header = Header(
        #             i, row, self.doctype, self.raw_data[1:], self.column_to_field_map
        #         )
        #     else:
        #         row_obj = Row(i, row, self.doctype, header, self.import_type)
        #         data.append(row_obj)

        # self.header = header
        # self.columns = self.header.columns
        # self.data = data

        # if len(data) < 1:
        #     frappe.throw(
        #         _("Import template should contain a Header and atleast one row."),
        #         title=_("Template Error"),
        #     )
