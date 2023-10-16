function convertInputValue(input) {
    return !isNaN(input.value) ? parseFloat(input.value) : input.value;
}

function submitForm(formId, endpoint) {
    document.getElementById(formId).addEventListener("submit", function(event) {
        event.preventDefault();

        // Collect form data
        let formData = {};
        for (let input of this.elements) {
            if (input.id) {
                formData[input.id] = convertInputValue(input);
            }
        }

        const itemsData = [];
        const itemRows = document.querySelectorAll("#items-table tr");


        for (let i = 1; i < itemRows.length; i++) { // Start from 1 to skip the header row
            const row = {};
            const inputs = itemRows[i].querySelectorAll("input");
            for (let input of inputs) {     
                   row[input.name] = convertInputValue(input);

                    }
            itemsData.push(row);
        }



        // Add the items data to the formData
        formData.items = itemsData;
        if (itemsData.length === 0) {
            delete formData.items;
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
            console.log("Received response from server: ", data);
        })
        .catch(error => {
            console.error(error);
            document.getElementById("response").innerHTML = "An error occurred.";
            console.log("An error occurred while sending the request.");
        });
    });
}
