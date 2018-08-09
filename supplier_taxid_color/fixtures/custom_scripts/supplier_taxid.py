# validate Supplier taxid prefix aginst list from irs 
# change color of txt field if not on list 

frappe.ui.form.on("Supplier", "validate", function(frm,cdt,cdn) {
   if (frm.doc.tax_id != 'frm.doc.taxid_prefix' ()) {
      validated = false;

frappe.throw(("<b>Please enter tax id for supplier</b>"));
        }
     }
   });
 
