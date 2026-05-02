# . Design a class Vehicle that:
# Keeps a record of service charge rate common to all vehicles.
# Each vehicle has a model, kilometers_run, and service history.
# Has a function to calculate service charge based on km and rate.
# Provides a method to update the service rate for all vehicles.
# Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# Creating vehicles with different km and models.
# Updating the service rate.
# Showing charges and eligibility checks.




class Vehicle:
    service_charge_rate=2
    def __init__ (self,model,kilometers_run,service_history):`
            self.model=model
            self.kilometers_run=kilometers_run
            self.service_history=service_history
    def calculate_service_charge(self):
            return  self.kilometers_run*Vehicle.service_charge_rate
    @classmethod
    def update_service_rate(cls,new_rate):
            cls.servie_charge_rate=new_rate
    @staticmethod
    def  is_eligible(model):
        if model<15:
            return True
        else:
            return False
vehicle1=Vehicle("KTM",20,15)
vehicle2=Vehicle("Duke",18,19)
print(vehicle1.model,vehicle1.kilometers_run,vehicle1.service_history)
print(vehicle2.model,vehicle2.kilometers_run,vehicle2.service_history)
print(vehicle1.calculate_service_charge())
print(vehicle2.calculate_service_charge())
print(Vehicle.is_eligible(18))
print(Vehicle.is_eligible(12))

