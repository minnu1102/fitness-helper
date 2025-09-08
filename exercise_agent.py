from datetime import datetime
import openai

class ExerciseAgent:
    def start(self):
        openai.api_key = "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"
        self.data = {}
    
    def makeplan(self, userid, name, age, weight, height, goal, days, equipment):
        # build the message for AI
        msg = "Make workout for "
        msg = msg + name
        msg = msg + ". Age "
        msg = msg + str(age)
        msg = msg + ", weight "
        msg = msg + str(weight)
        msg = msg + "kg, height "
        msg = msg + str(height)
        msg = msg + "cm. Goal is "
        msg = msg + goal
        msg = msg + ". "
        msg = msg + str(days)
        msg = msg + " days weekly. Has "
        msg = msg + equipment
        msg = msg + ". Give exercises."
        
        # try to get workout from AI
        workout = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=300
            )
            workout = response.choices[0].message.content
        except:
            # if AI fails, make simple plan
            workout = "Plan for "
            workout = workout + name
            workout = workout + ":\n"
            workout = workout + "Day 1: pushups, squats\n"  
            workout = workout + "Day 2: cardio stuff\n"
            workout = workout + "Use your "
            workout = workout + equipment
        
        # get today's date
        now = datetime.now()
        day = str(now.day)
        month = str(now.month) 
        year = str(now.year)
        
        # put date together
        time = day
        time = time + "/"
        time = time + month
        time = time + "/"
        time = time + year
        
        # make a record
        record = {}
        record["time"] = time
        record["plan"] = workout
        
        # check if user exists
        if userid not in self.data:
            self.data[userid] = []
        
        # save the record
        self.data[userid].append(record)
        
        # give back the workout
        return workout
    
    def gethistory(self, userid):
        # check if user has history
        if userid in self.data:
            # give back their stuff
            return self.data[userid]
        
        # no history found
        return []