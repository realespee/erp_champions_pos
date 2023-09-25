import frappe
from erpnext.controllers.selling_controller import SellingController
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

class CustomSalesInvoice(SalesInvoice, SellingController):
    
    def before_submit(self):
        if self.is_pos:
            pos_coupon = frappe.get_doc("POS Coupon", self.posa_coupons[0].coupon)
            
            sales_partner = pos_coupon.custom_sales_partner
            commission_rate = pos_coupon.custom_commission_rate

            self.sales_partner = sales_partner
            self.commission_rate = float(commission_rate)
            self.total_commission = (self.commission_rate / 100) * self.amount_eligible_for_commission
