from . import __version__ as app_version

app_name = "used_oil_re_refining"
app_title = "Used Oil Re-refining "
app_publisher = "alantechnologies"
app_description = "Used Oil Re-refining "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jayakumar@alantechnologies.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/used_oil_re_refining/css/used_oil_re_refining.css"
# app_include_js = "/assets/used_oil_re_refining/js/used_oil_re_refining.js"

# include js, css files in header of web template
# web_include_css = "/assets/used_oil_re_refining/css/used_oil_re_refining.css"
# web_include_js = "/assets/used_oil_re_refining/js/used_oil_re_refining.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "used_oil_re_refining/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "used_oil_re_refining.install.before_install"
# after_install = "used_oil_re_refining.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "used_oil_re_refining.uninstall.before_uninstall"
# after_uninstall = "used_oil_re_refining.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "used_oil_re_refining.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"used_oil_re_refining.tasks.all"
# 	],
# 	"daily": [
# 		"used_oil_re_refining.tasks.daily"
# 	],
# 	"hourly": [
# 		"used_oil_re_refining.tasks.hourly"
# 	],
# 	"weekly": [
# 		"used_oil_re_refining.tasks.weekly"
# 	]
# 	"monthly": [
# 		"used_oil_re_refining.tasks.monthly"
# 	]
# }
fixtures = [

	{
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Purchase Receipt-waste_oil_details",                    
                    "Purchase Receipt-tickect_no",
                    "Purchase Receipt-net_weight",
                    "Purchase Receipt-ltr_no",
                    "Purchase Receipt-desity_per_sg",
                    "Purchase Receipt-astm_test_method__density",
                    "Purchase Receipt-flash_point",
					"Purchase Receipt-water_contant",
					"Purchase Receipt-astm_test_method__water_contant",
					"Purchase Receipt-qty_in_litters",
					"Purchase Receipt-astm_test_method__flash_point",
					"Purchase Receipt-column_break_51",					
                    
                ),
            ]
        ],
    },
	{ "doctype": "Client Script", "filters": [ ["name", "in", ( "Purchase Receipt-Form", )] ] },

]
# Testing
# -------

# before_tests = "used_oil_re_refining.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "used_oil_re_refining.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "used_oil_re_refining.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"used_oil_re_refining.auth.validate"
# ]

