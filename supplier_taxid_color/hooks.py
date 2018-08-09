from . import __version__ as app_version

app_name = "supplier_taxid_color"
app_title = "Supplier Taxid Color"
app_publisher = "iXsystems.com"
app_description = "Change collor of the text for supplier taxid if the first two digits of a taxid prefix do not match those from the IRS EIN asignment list."
app_icon = "icon-book"
app_color = "red"
app_email = "jason@ixsystems.com"
app_url = "https://github.com/jasonbrowne/supplier-taxid-color"
app_license = "MIT"
app_version = "0.0.1"
fixtures = ["Custom Field","Custom Script"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/supplier_taxid_color/css/supplier_taxid_color.css"
# app_include_js = "/assets/supplier_taxid_color/js/supplier_taxid_color.js"

# include js, css files in header of web template
# web_include_css = "/assets/supplier_taxid_color/css/supplier_taxid_color.css"
# web_include_js = "/assets/supplier_taxid_color/js/supplier_taxid_color.js"

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

# Website user home page (by function)
# get_website_user_home_page = "supplier_taxid_color.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "supplier_taxid_color.install.before_install"
# after_install = "supplier_taxid_color.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "supplier_taxid_color.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
       "Supplier": {
               "validate": "supplier_taxid_color.supplier_taxid_color.fixtures.custom_scripts.supplier_taxid.validate"
       }
  }

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
# 		"supplier_taxid_color.tasks.all"
# 	],
# 	"daily": [
# 		"supplier_taxid_color.tasks.daily"
# 	],
# 	"hourly": [
# 		"supplier_taxid_color.tasks.hourly"
# 	],
# 	"weekly": [
# 		"supplier_taxid_color.tasks.weekly"
# 	]
# 	"monthly": [
# 		"supplier_taxid_color.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "supplier_taxid_color.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "supplier_taxid_color.event.get_events"
# }

