from flask import Flask, render_template, request, jsonify
from rules import APPLIANCE_FAULTS

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        appliances=list(APPLIANCE_FAULTS.keys())
    )


@app.route("/faults/<appliance>")
def get_faults(appliance):
    appliance = appliance.strip()

    if appliance not in APPLIANCE_FAULTS:
        return jsonify({"faults": []})

    faults = list(APPLIANCE_FAULTS[appliance].keys())

    return jsonify({"faults": faults})


@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.get_json()

    appliance = data.get("appliance", "").strip()
    fault = data.get("fault", "").strip()

    if appliance not in APPLIANCE_FAULTS:
        return jsonify({
            "success": False,
            "message": "Invalid appliance selected."
        })

    if fault not in APPLIANCE_FAULTS[appliance]:
        return jsonify({
            "success": False,
            "message": "Invalid fault selected."
        })

    rule = APPLIANCE_FAULTS[appliance][fault]

    return jsonify({
        "success": True,
        "appliance": appliance,
        "fault": fault,
        "possible_fault": rule["possible_fault"],
        "solution": rule["solution"],
        "rule": rule["rule"]
    })


if __name__ == "__main__":
    app.run(debug=True)