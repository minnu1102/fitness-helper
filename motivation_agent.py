from datetime import datetime
import openai

class MotivationAgent:
    def start(self):
        openai.api_key = "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"
        self.data = {}
    
    def give_boost(self, profile):
        # get name from profile
        name = profile["name"]
        
        # make simple message for AI
        msg = "motivate "
        msg = msg + name
        
        # try to get motivation from AI
        boost = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=100
            )
            boost = response.choices[0].message.content
        except:
            # make backup message
            boost = "hey "
            boost = boost + name
            boost = boost + " keep going!"
        
        # get today's date
        now = datetime.now()
        day = str(now.day)
        month = str(now.month)
        
        # make date string
        date = day
        date = date + "/"
        date = date + month
        
        # check if name exists in data
        if name not in self.data:
            self.data[name] = []
        
        # make record
        thing = {}
        thing["date"] = date
        thing["msg"] = boost
        
        # save it
        self.data[name].append(thing)
        
        # give back the boost
        return boost
    
    def encourage(self, person, name, target):
        # build message for AI
        msg = name
        msg = msg + " wants "
        msg = msg + target
        msg = msg + " help"
        
        # try to get encouragement
        message = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=50
            )
            message = response.choices[0].message.content
        except:
            # make backup message
            message = name
            message = message + " you can do "
            message = message + target
        
        # save the message
        self.save(person, message)
        
        # give it back
        return message
    
    def dailymotivation(self, person, feeling):
        # build message
        msg = "feeling "
        msg = msg + feeling
        msg = msg + " motivate"
        
        # try AI
        boost = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=60
            )
            boost = response.choices[0].message.content
        except:
            # backup message
            boost = "feeling "
            boost = boost + feeling
            boost = boost + " is ok keep trying"
        
        # save it
        self.save(person, boost)
        return boost
    
    def goalreminder(self, person, goal, days):
        # build message
        msg = goal
        msg = msg + " goal "
        msg = msg + str(days)
        msg = msg + " days left"
        
        # try AI
        push = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=80
            )
            push = response.choices[0].message.content
        except:
            # backup message
            push = str(days)
            push = push + " days for "
            push = push + goal
            push = push + " you got this"
        
        # save it
        self.save(person, push)
        return push
    
    def celebrate(self, person, achievement):
        # build message
        msg = "celebrate "
        msg = msg + achievement
        
        # try AI
        response_msg = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=40
            )
            response_msg = response.choices[0].message.content
        except:
            # backup message
            response_msg = "good job on "
            response_msg = response_msg + achievement
        
        # save it
        self.save(person, response_msg)
        return response_msg
    
    def toughday(self, person, problem):
        # build message
        msg = "tough day "
        msg = msg + problem
        
        # try AI
        response_msg = ""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}],
                max_tokens=70
            )
            response_msg = response.choices[0].message.content
        except:
            # backup message
            response_msg = problem
            response_msg = response_msg + " is hard but you can handle it"
        
        # save it
        self.save(person, response_msg)
        return response_msg
    
    def save(self, person, msg):
        # get today's date
        now = datetime.now()
        day = str(now.day)
        month = str(now.month)
        
        # make date string
        date = day
        date = date + "/"
        date = date + month
        
        # check if person exists
        if person not in self.data:
            self.data[person] = []
        
        # make record
        record = {}
        record["date"] = date
        record["text"] = msg
        
        # save it
        self.data[person].append(record)
    
    def getall(self, person):
        # check if person has data
        if person in self.data:
            # give back their stuff
            return self.data[person]
        
        # no data found
        return []
    
    def recent(self, person):
        # get all their stuff
        stuff = self.getall(person)
        
        # check if they have any
        if len(stuff) > 0:
            # get the last one
            last_one = stuff[-1]
            # get the text from it
            return last_one["text"]
        
        # nothing found
        return "nothing"