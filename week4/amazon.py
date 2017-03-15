
class PO:
    def __init__(self, customer, category):
        self.customer = customer
        self.category = category

def count_exclusive_customers(po_list):
    #dictionary of categories - 
    #dictionary of customers - 
    for po in po_list:
        if po.customer in cuts:
            cuts[po.customer].add(po.category)
        else:
            cuts[po.customer] = {po.category}

        if po.category in cats:
            cats[po.category].append(po.customer)
        else:
            cats[po.category] = [po.customer]
    
            


