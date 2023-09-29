function submitForm(formId, endpoint) {
    document.getElementById(formId).addEventListener("submit", function(event) {
        event.preventDefault();

        // Collect form data
        let formData = {};
        for (let input of this.elements) {
            if (input.id) {
                  formData[input.id] = input.value;
            }
        }

        // Send the data to your specified endpoint using fetch or another AJAX library
        fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("response").innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error(error);
            document.getElementById("response").innerHTML = "An error occurred.";
        });
    });
}

