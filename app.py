from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze-pm", methods=["POST"])
def analyze_pm():
    site_id = request.form.get("site_id")
    battery_voltage = float(request.form.get("battery_voltage"))
    dg_hours = int(request.form.get("dg_hours"))

    # PM Scoring Logic (Simple Demo)
    score = 100

    if battery_voltage < 48:
        score -= 30

    if dg_hours > 40:
        score -= 20

    if score >= 80:
        status = "GOOD ✅"
    elif score >= 50:
        status = "WARNING ⚠️"
    else:
        status = "CRITICAL ❌"

    result = f"Site {site_id} | PM Score: {score} | Status: {status}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="o.o.o.o", port=8000)