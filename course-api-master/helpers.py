import json

class ScottyLabsHandler(object):
    def __init__(self):
        self.json_file = open('out.json')
        self.json_str = self.json_file.read()
        self.json_data = json.loads(self.json_str)
        self.courses = self.json_data['courses']

    def getPrereqs(self,courses,courseName):
        return courses[courseName]['prereqs']

    def getCoreqs(self,courses,courseName):
        return courses[courseName]['coreqs']

    #separated by ands/ OR courses are in 2d list
    def getPreArray(self,courses,courseName):
        if self.getPrereqs(courses,courseName) == None: return None
        pre = self.removeParenthesAndWhite(self.getPrereqs(courses,courseName))
        pre = pre.split('and')
        for i in range(len(pre)):
            pre[i] = pre[i].split('or')
        return pre

    def getCoArray(self,courses,courseName):
        co = self.removeParenthesAndWhite(getCoreqs(courses,courseName))
        co = co.split('and')
        for i in range(len(co)):
            co[i] = co[i].split('or')
        return co

    def removeParenthesAndWhite(self,s):
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace(" ", "")
        return s

    def prereqsFuture(self,courses,courseName):
        result = list()
        for course in courses:
            reqs = self.getPreArray(courses,course)
            if reqs == None:
                continue
            for prereqs in reqs:
                if courseName in prereqs:
                    result.append(course)
        return result
        

handler = ScottyLabsHandler()
print(handler.prereqsFuture(handler.courses,"15-112"))


