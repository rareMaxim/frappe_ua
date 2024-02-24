function set_user_project(wizard) {
    frappe.call({
        method: "frappe_ua.translate.doctype.translate_wizard.translate_wizard.set_user_project",
        args: {
            "user": frappe.session.user,
            "wizard": wizard,
        },
        callback: (r) => {
            console.log(r);
            frappe.show_alert({
                message: __('Generate main.pot file: done'),
                indicator: 'green'
            }, 5);
        }
    });
}

function add_app_selector(listview) {
    let field = listview.page.add_field({
        label: 'Project',
        fieldtype: 'Link',
        fieldname: 'target_app',
        options: "Translate Wizard",
        change() {
            console.log(field.get_value());
            set_user_project(field.get_value())
        }
    });
};

frappe.listview_settings["Translate Message"] = {
    // hide_name_column: true, // hide the last column which shows the `name`
    // hide_name_filter: true, // hide the default filter field for the name column
    onload(listview) {
        // triggers once before the list is loaded
        add_app_selector(listview);
    },
}