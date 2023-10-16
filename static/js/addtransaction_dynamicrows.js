function addRow() {
    const table = document.getElementById("items-table");
    const newRow = document.createElement("tr");
    newRow.innerHTML = `
        <td><input type="text" class="item-id" name="item_id" required></td>
        <td><input type="number" class="quantity-numeric" name="quantity_numeric" required></td>
        <td><input type="number" class="quantity-weight" step="0.1" name="quantity_weight" required></td>
        <td><button type="button" onclick="removeRow(this)">Remove</button></td>
    `;
    table.appendChild(newRow);
}

function removeRow(button) {
    const row = button.parentElement.parentElement;
    row.remove();
}
