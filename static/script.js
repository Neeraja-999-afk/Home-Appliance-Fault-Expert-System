const applianceButtons = document.querySelectorAll(".appliance");
const faultsBox = document.getElementById("faults");
const help = document.getElementById("help");
const result = document.getElementById("result");

applianceButtons.forEach((btn) => {
    btn.addEventListener("click", async () => {
        applianceButtons.forEach((x) => x.classList.remove("active"));
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

            const data = await response.json();

            if (!response.ok) {
                throw new Error("Could not load faults.");
            }

            faultsBox.className = "faults";
            faultsBox.innerHTML = "";

            if (!data.faults || data.faults.length === 0) {
                faultsBox.innerHTML = `
                    <div class="empty">
                        ⚠️
                        <strong>No faults found</strong>
                        <span>No faults are available for this appliance.</span>
                    </div>
                `;
                return;
            }

            data.faults.forEach((fault) => {
                const button = document.createElement("button");

                button.className = "fault";
                button.textContent = fault;

                button.addEventListener("click", () => {
                    document
                        .querySelectorAll(".fault")
                        .forEach((x) => x.classList.remove("active"));

                    button.classList.add("active");

                    diagnose(appliance, fault);
                });

                faultsBox.appendChild(button);
            });

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

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(
                data.message || "Unable to diagnose the selected fault."
            );
        }

        result.innerHTML = `
            <div class="box">

                <div class="heading">
                    <small>
                        DIAGNOSIS FOR ${data.appliance.toUpperCase()}
                    </small>

                    <h3>${data.fault}</h3>
                </div>

                <div class="content">

                    <strong>Possible fault:</strong>
                    <p>${data.possible_fault}</p>

                    <h4>🔧 Basic Troubleshooting</h4>

                    <p>${data.solution}</p>

                    <div class="rule">
                        <b>IF–THEN RULE USED</b>
                        <br>
                        ${data.rule}
                    </div>

                </div>
            </div>
        `;

    } catch (error) {

        result.innerHTML = `
            <div class="welcome">
                ⚠️
                <h2>Unable to diagnose</h2>
                <p>${error.message}</p>
            </div>
        `;
    }
}
