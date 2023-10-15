function submitForm(formId, endpoint) {
    document.getElementById(formId).addEventListener("submit", function(event) {
        event.preventDefault();
        console.log("Form submission prevented.");

        // Collect form data
        let formData = {};
        for (let input of this.elements) {
            if (input.id) {
                if (input.type === "number") {
                    formData[input.id] = parseFloat(input.value);
                    console.log("Added numeric input to formData: ", input.id, formData[input.id]);
                } else {
                    formData[input.id] = input.value;
                    console.log("Added non-numeric input to formData: ", input.id, formData[input.id]);
                }
            }
        }
        console.log(" formData: ", formData);

        // Collect data from dynamically added rows
        const itemsData = [];
        const itemRows = document.querySelectorAll("#items-table tr");
        for (let i = 1; i < itemRows.length; i++) { // Start from 1 to skip the header row
            const item = {};
            const inputs = itemRows[i].querySelectorAll("input");
            item.id = parseFloat(inputs[0].value);
            item.quantity_numeric = parseFloat(inputs[1].value);
            item.quantity_weight = parseFloat(inputs[2].value);
            itemsData.push(item);
            console.log("Added item to item: ", item);
            console.log("Added item to itemsData: ", itemsData);

        }

        // Add the items data to the formData
        console.log("formDataaa: ", itemsData);
        console.log("formDataaaa: ", formData );
        formData.items = itemsData;
        console.log("Added itemsData to itemsData: ", itemsData);

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
            console.log("Received response from server: ", data);
        })
        .catch(error => {
            console.error(error);
            document.getElementById("response").innerHTML = "An error occurred.";
            console.log("An error occurred while sending the request.");
        });
    });
}
