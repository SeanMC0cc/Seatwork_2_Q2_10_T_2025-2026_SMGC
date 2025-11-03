from pyscript import display, document

def calculate_grade(e):
    fname = document.getElementById("input_name1").value
    lname = document.getElementById("input_name2").value
    math = int(document.getElementById("input_grade1").value)
    science = int(document.getElementById("input_grade2").value)
    english = int(document.getElementById("input_grade3").value)
    ICT = int(document.getElementById("input_grade4").value)
    PE = int(document.getElementById("input_grade5").value)
    TLE = int(document.getElementById("input_grade6").value)

    average = (math + science + english + ICT + PE + TLE) / 6


    result = f"Student: {fname} {lname}\nAverage Grade: {average}"
    display(result, target="output")