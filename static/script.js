const applianceButtons = document.querySelectorAll(".appliance");
const faultsBox = document.getElementById("faults");
const help = document.getElementById("help");
const result = document.getElementById("result");


// ===============================
// APPLIANCE SELECTION
// ===============================

applianceButtons.forEach((btn) => {

    btn.addEventListener("click", async () => {

        // Remove active state from all appliances
        applianceButtons.forEach((x) => {
            x.classList.remove("active");
        });

        // Activate selected appliance
        btn.classList.add("active");

        const appliance = btn.dataset.a;

        help.textContent =
            `Possible faults for ${appliance} are shown below. Select one to diagnose.`;

        faultsBox.innerHTML = `
            <div class="empty">
                ⏳
                <strong>Loading faults...</strong>
                <span>Reading the knowledge base.</span>
            </div>
        `;

        try {

            const response = await fetch(
                `/faults/${encodeURIComponent(appliance)}`
            );

            if (!response.ok) {
                throw new Error(
                    `Unable to load faults. Server returned ${response.status}.`
                );
            }

            const data = await response.json();

            faultsBox.className = "faults";
            faultsBox.innerHTML = "";

            if (!data.faults || data.faults.length === 0) {

                faultsBox.innerHTML = `
                    <div class="empty">
                        ⚠️
                        <strong>No faults found</strong>
                        <span>No rules are available for this appliance.</span>
                    </div>
                `;

                return;
            }


            // Create fault buttons
            data.faults.forEach((fault) => {

                const faultButton = document.createElement("button");

                faultButton.className = "fault";
                faultButton.textContent = fault;

                faultButton.addEventListener("click", () => {

                    document
                        .querySelectorAll(".fault")
                        .forEach((x) => x.classList.remove("active"));

                    faultButton.classList.add("active");

                    diagnose(appliance, fault);
                });

                faultsBox.appendChild(faultButton);
            });


            // Update result area
            result.innerHTML = `
                <div class="welcome">
                    🔎
                    <h2>${appliance} selected</h2>
                    <p>
                        Choose one of the ${data.faults.length}
                        related faults above.
                        The corresponding IF–THEN rule will be applied.
                    </p>
                </div>
            `;

        } catch (error) {

            console.error("Fault loading error:", error);

            faultsBox.innerHTML = `
                <div class="empty">
                    ⚠️
                    <strong>Could not load faults</strong>
                    <span>${error.message}</span>
                </div>
            `;
        }
    });

});


// ===============================
// DIAGNOSIS
// ===============================

async function diagnose(appliance, fault) {

    result.innerHTML = `
        <div class="welcome">
            🤖
            <h2>Applying rule...</h2>
            <p>
                Matching the selected appliance and fault
                with the knowledge base.
            </p>
        </div>
    `;


    try {

        const response = await fetch("/diagnose", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                appliance: appliance,
                fault: fault
            })

        });


        if (!response.ok) {

            throw new Error(
                `Diagnosis request failed. Server returned ${response.status}.`
            );

        }


        const data = await response.json();


        if (!data.success) {

            throw new Error(
                data.message || "Unable to diagnose the selected fault."
            );

        }


        // Flask returns these fields directly
        const possibleFault = data.possible_fault;
        const solution = data.solution;
        const rule = data.rule;


        // Convert solution to array if necessary
        let solutions = [];

        if (Array.isArray(solution)) {
            solutions = solution;
        } else {
            solutions = [solution];
        }


        // Create troubleshooting list
        const solutionList = solutions
            .map((item) => `<li>${item}</li>`)
            .join("");


        // Display diagnosis
        result.innerHTML = `
            <div class="box">

                <div class="heading">

                    <small>
                        DIAGNOSIS FOR ${escapeHtml(
                            appliance.toUpperCase()
                        )}
                    </small>

                    <h3>
                        ${escapeHtml(fault)}
                    </h3>

                </div>


                <div class="content">

                    <strong>Possible fault:</strong>

                    <br>

                    ${escapeHtml(possibleFault)}


                    <h4>🔧 Basic Troubleshooting</h4>

                    <ul>
                        ${solutionList}
                    </ul>


                    <div class="rule">

                        <b>IF–THEN RULE USED</b>

                        <br>

                        ${escapeHtml(rule)}

                    </div>

                </div>

            </div>
        `;


    } catch (error) {

        console.error("Diagnosis error:", error);

        result.innerHTML = `
            <div class="welcome">

                ⚠️

                <h2>Unable to diagnose</h2>

                <p>
                    ${escapeHtml(
                        error.message ||
                        "An error occurred while diagnosing the fault."
                    )}
                </p>

            </div>
        `;
    }
}


// ===============================
// HTML SAFETY HELPER
// ===============================

function escapeHtml(value) {

    if (value === null || value === undefined) {
        return "";
    }

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
