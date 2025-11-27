from pyscript import display, document

def calculate_grade(e):
    fname = str(document.getElementById("input_name1").value)
    lname = str(document.getElementById("input_name2").value)
    math = int(document.getElementById("input_grade1").value)
    science = int(document.getElementById("input_grade2").value)
    english = int(document.getElementById("input_grade3").value)
    ICT = int(document.getElementById("input_grade4").value)
    PE = int(document.getElementById("input_grade5").value)
    TLE = int(document.getElementById("input_grade6").value)
    document.getElementById("output").innerHTML = ""

    average = (math + science + english + ICT + PE + TLE) / 6
    result = f'''{fname} {lname}'s average grade is {average:.2f}. 
    math: {math}
    science: {science}
    english: {english}
    ICT: {ICT}
    PE: {PE} 
    TLE: {TLE}'''
    display(result, target="output")