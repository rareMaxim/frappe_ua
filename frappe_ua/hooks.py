app_name = "frappe_ua"
app_title = "Frappe Ua"
app_publisher = "Maxim Sysoev"
app_description = "Українська локалізація для Frappe Framework"
app_email = "maks4a@gmail.com"
app_license = "mit"
export_python_type_annotations = True
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_ua/css/frappe_ua.css"
# app_include_js = "/assets/frappe_ua/js/frappe_ua.js"
app_include_js = [
    "/assets/frappe_ua/js/map_defaults.js"
    # ...
]

# include js, css files in header of web template
# web_include_css = "/assets/frappe_ua/css/frappe_ua.css"
# web_include_js = "/assets/frappe_ua/js/frappe_ua.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_ua/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "frappe_ua/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "frappe_ua.utils.jinja_methods",
# 	"filters": "frappe_ua.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_ua.install.before_install"
# after_install = "frappe_ua.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_ua.uninstall.before_uninstall"
# after_uninstall = "frappe_ua.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "frappe_ua.utils.before_app_install"
# after_app_install = "frappe_ua.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "frappe_ua.utils.before_app_uninstall"
# after_app_uninstall = "frappe_ua.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_ua.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_ua.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_ua.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_ua.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_ua.tasks.weekly"
# 	],
# 	"monthly": [
# 		"frappe_ua.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "frappe_ua.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_ua.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_ua.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["frappe_ua.utils.before_request"]
# after_request = ["frappe_ua.utils.after_request"]

# Job Events
# ----------
# before_job = ["frappe_ua.utils.before_job"]
# after_job = ["frappe_ua.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"frappe_ua.auth.validate"
# ]
