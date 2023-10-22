$(document).ready(function () {
    // Setup - add a select dropdown to each footer cell
    $('#example thead tr')
        .clone(true)
        .addClass('filters')
        .appendTo('#example thead');

    var table = $('#example').DataTable({
        autoFill: true,
        scrollX: true,
        "lengthMenu": [[3, 7, 10, 25, 50, 100, -1], [3, 7, 10, 25, 50, 100, "All"]],
        orderCellsTop: true,
        fixedHeader: true,
        initComplete: function () {
            var api = this.api();

            // For each column
            api.columns().eq(0).each(function (colIdx) {
                // Set the header cell to contain the select dropdown
                var cell = $('.filters th').eq($(api.column(colIdx).header()).index());
                var title = $(cell).text();
                $(cell).html('<select multiple="multiple" data-placeholder="' + title + '"><option></option></select>');

                // Fill the select dropdown with unique values from the column
                api.column(colIdx).data().unique().sort().each(function (d) {
                    $(cell).find('select').append('<option value="' + d + '">' + d + '</option>');
                });

                // Initialize select2 plugin for the select dropdown
                $(cell).find('select').select2();

                // On change event of the select dropdown
                $(cell).find('select').on('change', function () {
                    // Get selected values
                    var selectedValues = $(this).val();

                    // Search the column for the selected values
                    api.column(colIdx).search(selectedValues.join('|'), true, false).draw();
                });
            });
        },
    });
});