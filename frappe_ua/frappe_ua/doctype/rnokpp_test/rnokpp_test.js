// Copyright (c) 2024, Maxim Sysoev and contributors
// For license information, please see license.txt

frappe.ui.form.on("rnokpp-test", {
    refresh(frm) {
        updateRnokppUI(frm);
    },
    rnokpp(frm) {
        updateRnokppUI(frm);
    }
});
function updateRnokppUI(frm) {
    frappe.require('/assets/frappe_ua/js/rnokpp.js', () => {
        data = rnokppInfo(frm.doc.rnokpp);
        frm.set_value('sex', data.gender);
        frm.set_value('birthday', data.birthday);

        console.log(data);
    })

}

