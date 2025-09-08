from datetime import datetime
import openai

class NutritionAgent:
    def start(self):
        openai.api_key = "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"
        self.data = {}

    def make_meal_plan(self, name, age, weight, height, goal):
        # building the message for AI
        msg = "make meal plan for "
        msg = msg + name
        msg = msg + " age "
        msg = msg + str(age)
        msg = msg + " weight "
        msg = msg + str(weight)
        msg = msg + " goal is "
        msg = msg + goal
        msg = msg + " make it simple based"

        # trying to get plan from AI
        plan = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=250
            )
            plan = response.choices[0].message.content
        except:
            # make backup plan if AI fails
            plan = "meals for "
            plan = plan + name
            plan = plan + ":\n\n"
            plan = plan + "breakfast: oats with fruit\n"
            plan = plan + "lunch: chickensalad\n"
            plan = plan + "dinner: fish and veggies\n"
            plan = plan + "snacks: nuts\n\n"
            plan = plan + "drink water"

        # get todays date
        now = datetime.now()
        day = str(now.day)
        month = str(now.month)
        
        # make time string
        time = day
        time = time + "/"
        time = time + month

        # making the record to save
        record = {}
        record["time"] = time
        record["meals"] = plan

        # check if user exists
        if userid not in self.data:
            self.data[userid] = []
        
        # save the record
        self.data[userid].append(record)
        return plan

    def gethistory(self, userid):
        # checking whether user has history
        if userid in self.data:
            # give back their stuff
            return self.data[userid]
        
        # if no history found return
        return []