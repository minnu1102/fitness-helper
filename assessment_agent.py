from datetime import datetime
import openai

class AssessmentAgent:
    
    def start(self):
        openai.api_key = "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"
        self.data = {}
    
    def assess(self, profile):
        # get basic info from profile
        name = profile["name"]
        age = profile["age"] 
        weight = profile["weight"]
        height = profile["height"]
        
        # set defaults
        goal = "stay fit"
        activity = "normal"
        
        # check if goal exists
        if "goal" in profile:
            goal = profile["goal"]
        
        # check if activity level exists
        if "activity_level" in profile:
            activity = profile["activity_level"]
        
        # build message for AI bit by bit
        msg = "fitness expert make plan for "
        msg = msg + name
        msg = msg + " age "
        msg = msg + str(age)
        msg = msg + " weight "
        msg = msg + str(weight)
        msg = msg + "kg height "
        msg = msg + str(height)
        msg = msg + "cm goal "
        msg = msg + goal
        msg = msg + " activity "
        msg = msg + activity
        
        # try to get plan from AI
        plan = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=180
            )
            plan = response.choices[0].message.content
        except:
            # make backup plan if AI fails
            plan = "hi "
            plan = plan + name
            plan = plan + " for age "
            plan = plan + str(age)
            plan = plan + " weight "
            plan = plan + str(weight)
            plan = plan + "kg do light exercise 2-3 times week focus on "
            plan = plan + goal
        
        # get today's date
        now = datetime.now()
        day = str(now.day)
        month = str(now.month)
        
        # make date string
        date = day
        date = date + "/"
        date = date + month
        
        # make record to save
        record = {}
        record["date"] = date
        record["plan"] = plan
        
        # check if person exists in data
        if name not in self.data:
            self.data[name] = []
        
        # add record to person's data
        self.data[name].append(record)
        
        # make result to return
        result = {}
        result["plan"] = plan
        result["goal"] = goal
        
        # give back result
        return result
    
    def gethistory(self, person):
        # check if person has history
        if person in self.data:
            # return their stuff
            return self.data[person]
        
        # no history found
        return []