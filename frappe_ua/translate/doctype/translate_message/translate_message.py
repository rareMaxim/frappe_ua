# Copyright (c) 2024, Maxim Sysoev and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.gettext.translate import get_catalog
from babel.messages.catalog import Catalog
from babel.messages.catalog import Message

class TranslateMessage(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        auto_comments: DF.SmallText | None
        context: DF.Data | None
        lineno: DF.Int
        locations: DF.SmallText | None
        string: DF.Data | None
        title: DF.Data | None
        user_comments: DF.SmallText | None
    # end: auto-generated types

    
    @staticmethod
    def message2json(id:int, msg: Message):
        return ({
            "name": id,
            "title": msg.id,
            "string": msg.string,
            "context": msg.context,
            "user_comments": ''.join(str(x) for x in msg.user_comments),
            "auto_comments": ''.join(str(x) for x in msg.auto_comments),
            "locations": ''.join(str(x) for x in msg.locations),
            "flags":msg.flags,
            "lineno":msg.lineno,
            "previous_id":msg.previous_id,
        })

    @staticmethod
    def get_catalog()->Catalog:
        return get_catalog ('asc', 'uk')
    
    def db_insert(self, *args, **kwargs):
        # {'name': '65083879a3', 'owner': 'Administrator', 'creation': '2024-02-24 18:35:01.335664', 
        # 'modified': '2024-02-24 18:35:01.335664', 'modified_by': 'Administrator', 'docstatus': 0, 
        # 'idx': 0, 'title': 'Test', 'string': 'twat', 'context': 'kjnk', 'auto_comments': ',m l/kn', 
        # 'user_comments': "'lkjk", 'locations': None, 'lineno': 0}
        d = self.get_valid_dict(convert_dates_to_str=True)
        print(d)
        catalog: Catalog = TranslateMessage.get_catalog()
        catalog.add(id=d.title,
                    string=d.string,
                    context=d.context
                    )

    def load_from_db(self):
        d = self.get_valid_dict(convert_dates_to_str=True)
        print(d)
        data = TranslateMessage.get_catalog()
        id = int(self.name)
        d = TranslateMessage.message2json(id, list(data)[id])
        super(Document, self).__init__(d)

    def db_update(self):
       pass
   
   
    @staticmethod
    def get_list(args):
        # wizard = frappe.get_doc("Translate Wizard",  )
        # catalog: Catalog = get_catalog (wizard.get('target_app'), wizard.get('language'))
        catalog = list(TranslateMessage.get_catalog())
        result = []
        print(f"\n\n\n {args} \n\n\n\n\n")
        if not 'start' in dict(args):
            return
        i =  int(args.start)+1
        while len(result) < int(args.page_length):
            if i >= len(catalog):
                break
            msg = catalog[i]
           
            if not msg.id:
                continue
            result.append(TranslateMessage.message2json(i, msg))  
            i += 1          
        return result
    
        
    @staticmethod
    def get_count(args):
        print(f"\n\n{args}")
        return len( TranslateMessage.get_catalog()) - 1

    @staticmethod
    def get_stats(args):
        pass

