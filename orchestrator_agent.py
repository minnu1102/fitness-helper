from datetime import datetime

class OrchestratorAgent:
    def start(self, assessor, nutrition, exercise, motivation):
        self.assessor = assessor
        self.nutrition = nutrition
        self.exercise = exercise
        self.motivation = motivation
        self.data = {}
    
    def buildplan(self, userid, profile):
        try:
            # get assessment
            assessment = self.assessor.assess(profile)
            
            # make nutrition plan
            nutrition = self.nutrition.make_meal_plan(
                userid,
                profile["name"],
                profile["age"],
                profile["weight"],
                profile["height"],
                assessment["goal"]
            )
            
            # make exercise plan
            days = 3
            equipment = "bodyweight only"
            if "days" in profile:
                days = profile["days"]
            if "equipment" in profile:
                equipment = profile["equipment"]
            
            exercise = self.exercise.makeplan(
                userid,
                profile["name"],
                profile["age"],
                profile["weight"],
                profile["height"],
                assessment["goal"],
                days,
                equipment
            )
            
            # get motivation
            motivation = self.motivation.give_boost(profile)
            
            # make timestamp
            now = datetime.now()
            day = str(now.day)
            month = str(now.month)
            year = str(now.year)
            hour = str(now.hour)
            minute = str(now.minute)
            when = day + "/" + month + "/" + year + " " + hour + ":" + minute
            
            # put everything together
            plan = {}
            plan["when"] = when
            plan["assessment"] = assessment
            plan["nutrition"] = nutrition
            plan["exercise"] = exercise
            plan["motivation"] = motivation
            
            # save it
            if userid not in self.data:
                self.data[userid] = []
            
            self.data[userid].append(plan)
            return plan
            
        except:
            error = {}
            error["error"] = "something went wrong"
            return error
    
    def gethistory(self, userid):
        if userid in self.data:
            return self.data[userid]
        return []