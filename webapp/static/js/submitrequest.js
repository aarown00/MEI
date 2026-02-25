document.getElementById("submitForm").addEventListener("submit", function() {
    // Show the progress bar container
    document.getElementById("progressBar").style.display = "block";

    // Simulate progress
    var progressBarFill = document.getElementById("progressBarFill");
    var width = 0;
    var interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width += 20; // Adjust increment speed as needed
            progressBarFill.style.width = width + "%";
            progressBarFill.setAttribute("aria-valuenow", width);
        }
    }, 500); // Adjust interval (milliseconds) for smoother or faster animation
});