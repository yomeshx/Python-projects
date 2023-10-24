students =[
    {"name":"yomesh","grade":"13","batch":"2020"},
    {"name":"john","grade":"12","batch":"2021"},
    {"name":"alan","grade":"10","batch":"2020"},
    {"name":"kelly","grade":"13","batch":None}
]

for student in students:
    print(student["name"],student["grade"],student["batch"],sep = "-")#prints student names and grades