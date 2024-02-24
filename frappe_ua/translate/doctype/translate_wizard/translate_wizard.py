# Copyright (c) 2024, Maxim Sysoev and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.gettext.translate import generate_pot
from babel.messages.catalog import Message


class TranslateWizard(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		language: DF.Link | None
		select_show_po_locales: DF.Literal
		target_app: DF.Literal
	# end: auto-generated types

	pass

@frappe.whitelist()
def get_installed_app():
    return frappe.get_all_apps(True)

@frappe.whitelist()
def generate_pot(target_app: str | None = None):
    from frappe.gettext.translate import generate_pot
    generate_pot(target_app=target_app)
    return {
        "generate_pot": True,
        "target_app": target_app,
        }

@frappe.whitelist()
def csv_to_po(app: str | None = None, locale: str | None = None):
    from frappe.gettext.translate import migrate
    
    migrate(app=app, locale = locale)
    generate_pot(target_app=app)
    return {
        "generate_pot": True,
        "target_app": app,
        }

@frappe.whitelist()
def get_translate_catalog(app: str, locale: str | None = None):
    from frappe.gettext.translate import get_catalog
    from babel.messages.catalog import Catalog
  
    
    catalog: Catalog = get_catalog(app=app, locale=locale) #
    print(catalog.__len__)
    for message in catalog:
        print(message2json(message))
    print( catalog.header_comment)
    return

@frappe.whitelist()
def get_locales(app: str) -> list[str]:
    from frappe.gettext.translate import get_locales
    locales = get_locales(app = app)
    return locales

@frappe.whitelist()
def new_po(locale, target_app: str | None = None):
    from frappe.gettext.translate import new_po
    new_po(locale = locale, target_app = target_app)

@frappe.whitelist()
def update_po(target_app: str | None = None, locale: str | None = None):
    from frappe.gettext.translate import update_po
    update_po(target_app = target_app, locale = locale)
        
@frappe.whitelist()
def compile_translations(target_app: str | None = None, locale: str | None = None, force=False):
    from frappe.gettext.translate import compile_translations
    compile_translations(target_app = target_app, locale = locale, force = force)    
    
@frappe.whitelist()
def set_user_project(user, wizard: str):
    frappe.cache.hset("translate", user, wizard)
  
    