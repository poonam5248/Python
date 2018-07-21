'''Ques 4. Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add,
display and update the following details. Create another class Mission which extends the class Cop. Define method
add_mission _details. Select an object of Cop and access methods of base class to get information for a particular
 cop and make it available for mission.'''


class Cop:

    def add(self,name,age,work_experience,designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation

    def display(self):
        print("\n\nDetails Will be:")
        print("\nName is: ",self.name)
        print("\nAge is: ",self.age)
        print("\nWork_Experience: ",self.work_experience)
        print("\nDestination: ",self.designation)


    def update(self,name,age,work_experience,designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation
class Mission(Cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)

m=Mission()
m.add_mission_details("Mission detail Assigned to HP :")
m.add("Poonam",19,8,"Engineer\n")
m.display()
m.update("Nikhil",21,2,"Engineer")
m.display()


