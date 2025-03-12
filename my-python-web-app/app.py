from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_cgpa(current_cgpa, total_credits, course_credits, old_grade_point, new_grade_point):
    old_gp = old_grade_point * course_credits
    new_gp = new_grade_point * course_credits
    total_quality_points = (current_cgpa * total_credits) - old_gp + new_gp
    updated_cgpa = total_quality_points / total_credits
    return round(updated_cgpa, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        current_cgpa = float(request.form["current_cgpa"])
        total_credits = float(request.form["total_credits"])
        course_credits = float(request.form["course_credits"])
        old_grade_point = float(request.form["old_grade_point"])
        new_grade_point = float(request.form["new_grade_point"])
        
        updated_cgpa = calculate_cgpa(current_cgpa, total_credits, course_credits, old_grade_point, new_grade_point)
        # The updated CGPA will now pre-fill the "current_cgpa" field.
        return render_template("index.html", updated_cgpa=updated_cgpa)
    
    return render_template("index.html", updated_cgpa=None)

if __name__ == '__main__':
    app.run(debug=True)