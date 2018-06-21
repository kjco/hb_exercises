"""Classes for melon orders."""
class AbstractMelonOrder:
    
    base_price = 5
    shipped = False
    
    # Default variables used in methods
    # You must set them when subclassing
    tax = None
    order_type = None


    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
       
    def get_total(self):
        """Calculate price, including tax."""

        # self.base_price = 5
        # base_price is a class attribute, so its the same for every object in the class
        if self.species == "Christmas":
            self.base_price *= 1.5
        total = (1 + self.tax) * self.qty * self.base_price
        if self.qty < 10 and self.order_type == "international":
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True  


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = 'domestic'
    tax = 0.08

    # def __init__(self, species, qty):
       # """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08

    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
     
    def __init__(self, species, qty, country_code):
        
        super().__init__(species, qty)
        self.country_code = country_code

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

   
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
