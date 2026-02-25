(function () {
  // Requires: jQuery + DataTables loaded first
  if (typeof window.jQuery === "undefined" || typeof window.jQuery.fn?.DataTable === "undefined") {
    return;
  }

  window.jQuery(function () {
    const $table = window.jQuery("#it-request-table");
    if ($table.length === 0) return;

    $table.DataTable({
      paging: true,
      searching: true,
      ordering: false,
      language: {
        search: '<span class="fa fa-search"></span>',
        searchPlaceholder: "Enter RTN/Status here",
      },
      columnDefs: [
        { searchable: true, targets: [0, 2] },
        { searchable: false, targets: "_all" },
      ],
    });
  });
})();

