(function () {
  // Alert dismiss (used by base.html flash messages)
  document.querySelectorAll("[data-dismiss='alert']").forEach((btn) => {
    btn.addEventListener("click", () => btn.closest("div")?.remove());
  });

  // Expose global because templates call it inline via onclick=""
  window.showAllDetails = function (
    id,
    fullName,
    email,
    employeeId,
    department,
    eqName,
    eqType,
    description,
    uploadUrl
  ) {
    const setText = (elId, value) => {
      const el = document.getElementById(elId);
      if (el) el.innerText = value ?? "";
    };

    const label = document.getElementById("detailsModalLabel");
    if (label) label.innerText = "Request Ticket # " + id;

    setText("requestorFullName", fullName);
    setText("requestorEmail", email);
    setText("requestorEmployeeId", employeeId);
    setText("requestorDepartment", department);

    setText("issueEqName", eqName);
    setText("issueEqType", eqType);
    setText("issueDescription", description);

    const uploadElement = document.getElementById("issueUpload");
    if (uploadElement) {
      if (uploadUrl) {
        uploadElement.innerHTML = '<a href="' + uploadUrl + '">View</a>';
      } else {
        uploadElement.innerText = "None";
      }
    }

    // Requires: Bootstrap JS loaded first
    if (typeof window.bootstrap !== "undefined") {
      const modalEl = document.getElementById("detailsModal");
      if (modalEl) {
        const myModal = new window.bootstrap.Modal(modalEl);
        myModal.show();
      }
    }
  };
})();

