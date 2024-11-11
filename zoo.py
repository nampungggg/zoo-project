class Zoo:
 def get_ticket_price(self,age):
        if age <13 and age > 0 or age==0:
            return 50
        elif  age < 21:
            return 100
        elif  age < 61:
            return 150
        elif age > 60:
            return 100
        else:
            return "invalid"
