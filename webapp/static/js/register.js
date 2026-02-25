document.getElementById("RegisterForm").addEventListener("submit", function() {
    // Show the progress bar container
    const progressBar = document.getElementById("progressBar");
    progressBar.classList.remove("hidden");

    // Simulate progress
    var progressBarFill = document.getElementById("progressBarFill");
    var width = 0;
    var interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width += 30; // Adjust increment speed as needed
            progressBarFill.style.width = width + "%";
        }
    }, 500); // Adjust interval (milliseconds) for smoother or faster animation
});