var isSuperuser = {{ request.user.is_superuser|yesno:"true,false" }};
var csrfToken = '{{ csrf_token }}';

let requestIdToCancel = null;
    let requestIdToApprove = null;
    let requestIdToComplete = null;
    let requestIdToClose = null;

    function openModal(id) {
        const modal = document.getElementById(id);
        if (!modal) return;
        modal.classList.remove('hidden');
        modal.setAttribute('aria-hidden', 'false');
    }

    function closeModal(id) {
        const modal = document.getElementById(id);
        if (!modal) return;
        modal.classList.add('hidden');
        modal.setAttribute('aria-hidden', 'true');
    }

    function showAdminDetails(id, fullName, email, employeeId, department, eqName, eqType, description, uploadUrl) {
        const setText = (elId, value) => {
            const el = document.getElementById(elId);
            if (el) el.innerText = value ?? '';
        };

        const label = document.getElementById('detailsModalLabel');
        if (label) label.innerText = 'Request Ticket # ' + id;

        setText('requestorFullName', fullName);
        setText('requestorEmail', email);
        setText('requestorEmployeeId', employeeId);
        setText('requestorDepartment', department);

        setText('issueEqName', eqName);
        setText('issueEqType', eqType);
        setText('issueDescription', description);

        const uploadElement = document.getElementById('issueUpload');
        if (uploadElement) {
            if (uploadUrl) {
                uploadElement.innerHTML = '<a href="' + uploadUrl + '" class="text-indigo-700 hover:text-indigo-900 underline">View</a>';
            } else {
                uploadElement.innerText = 'None';
            }
        }

        openModal('detailsModal');
    }

    function confirmCancel(requestId) {
        requestIdToCancel = requestId;
        openModal('cancelModal');
    }

    function confirmApprove(requestId) {
        requestIdToApprove = requestId;
        openModal('approveModal');
    }

    function confirmDone(requestId) {
        requestIdToComplete = requestId;
        openModal('completeModal');
    }

    function confirmClose(requestId) {
        requestIdToClose = requestId;
        openModal('closeModal');
    }

    document.querySelectorAll('[data-modal-close]').forEach((btn) => {
        btn.addEventListener('click', () => {
            const target = btn.getAttribute('data-modal-close');
            if (target) closeModal(target);
        });
    });

    document.querySelectorAll('[data-modal-backdrop="true"]').forEach((backdrop) => {
        backdrop.addEventListener('click', (event) => {
            if (event.target === backdrop) {
                closeModal(backdrop.id);
            }
        });
    });

    document.getElementById('confirmCancelBtn').addEventListener('click', function () {
        if (requestIdToCancel) {
            const form = document.createElement('form');
            form.method = 'POST';

            // Set the form action URL based on user status
            if (isSuperuser) {
                form.action = `/it_request/${requestIdToCancel}/cancel/admin/`;
            } else {
                form.action = `/it_request/${requestIdToCancel}/cancel/employee/`;
            }

            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken';
            csrfTokenInput.value = '{{ csrf_token }}';

            form.appendChild(csrfTokenInput);
            document.body.appendChild(form);
            form.submit();
        }
    });

    document.getElementById('confirmApproveBtn').addEventListener('click', function () {
        if (requestIdToApprove) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/it_request/${requestIdToApprove}/approve/`;

            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken';
            csrfTokenInput.value = '{{ csrf_token }}';

            form.appendChild(csrfTokenInput);
            document.body.appendChild(form);
            form.submit();
        }
    });

    document.getElementById('confirmDoneBtn').addEventListener('click', function () {
        if (requestIdToComplete) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/it_request/${requestIdToComplete}/done/`;

            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken';
            csrfTokenInput.value = '{{ csrf_token }}';

            form.appendChild(csrfTokenInput);
            document.body.appendChild(form);
            form.submit();
        }
    });

    document.getElementById('confirmCloseBtn').addEventListener('click', function () {
        if (requestIdToClose) {
            const form = document.createElement('form');
            form.method = 'POST';

            // Set the form action URL based on user status
            if (isSuperuser) {
                form.action = `/it_request/${requestIdToClose}/close/admin/`;
            } else {
                form.action = `/it_request/${requestIdToClose}/close/employee/`;
            }
            const csrfTokenInput = document.createElement('input');
            csrfTokenInput.type = 'hidden';
            csrfTokenInput.name = 'csrfmiddlewaretoken';
            csrfTokenInput.value = '{{ csrf_token }}';

            form.appendChild(csrfTokenInput);
            document.body.appendChild(form);
            form.submit();
        }
    });