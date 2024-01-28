// Copyright (c) 2024, Maxim Sysoev and contributors
// For license information, please see license.txt

frappe.listview_settings["KATOTTG Entity Category"] = {
    hide_name_column: false,
    onload(listview) {
        setInterval(() => {
            if (listview.list_view_settings.disable_auto_refresh) {
                return;
            }
            // if (!listview.enabled) return;
            const route = frappe.get_route() || [];
            if (route[0] != "List" || "KATOTTG Entity Category" != route[1]) {
                return;
            }
            listview.refresh();
        }, 5000);
    },
};
