import json


json_file = open('out.json')
json_str = json_file.read()
json_data = json.loads(json_str)

courses = json_data['courses']



def getPrereqs(courses,courseName):
    return courses[courseName]['prereqs']

def getCoreqs(courses,courseName):
    return courses[courseName]['coreqs']

#separated by ands/ OR courses are in 2d list
def getPreArray(courses,courseName):
    if getPrereqs(courses,courseName) == None: return None
    pre = removeParenthesAndWhite(getPrereqs(courses,courseName))
    pre = pre.split('and')
    for i in range(len(pre)):
        pre[i] = pre[i].split('or')
    return pre

def getCoArray(courses,courseName):
    co = removeParenthesAndWhite(getCoreqs(courses,courseName))
    co = co.split('and')
    for i in range(len(co)):
        co[i] = co[i].split('or')
    return co

def removeParenthesAndWhite(s):
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace(" ", "")
    return s

def prereqsFuture(courses,courseName):
    result = set()
    for course in courses:
        #reqs = course["prereqs_obj"]["reqs_list"]
        reqs = getPreArray(courses,course)
        if reqs == None:
            continue
        print(course,reqs,"hello")
        for prereqs in reqs:
            if courseName in prereqs:
                result.add(course)
    return result
        


# print(getPreArray(courses,"15-150"))
# print(getCoArray(courses,"15-122"))
# print(getPreArray(courses,"10-601"))
# print(prereqsFuture(courses,"15-112"))


