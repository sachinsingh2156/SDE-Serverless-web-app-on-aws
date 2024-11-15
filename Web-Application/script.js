var navLinks = document.getElementById("navLinks");

function showMenu() {
  navLinks.style.right = "0";
}

function hideMenu() {
  navLinks.style.right = "-200px";
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");

  const apiUrl =
    "https://olpwgnoulpimeg6m3hh2273tum0lncsw.lambda-url.us-west-1.on.aws/";

  https: form.addEventListener("submit", async function (event) {
    if (form.checkValidity()) {
      event.preventDefault();

      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const subject = document.getElementById("subject").value;
      const message = document.getElementById("message").value;

      try {
        const response = await fetch(apiUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ name, email, subject, message }),
        });

        if (response.ok) {
          alert("Response submitted successfully");

          form.reset();
        } else {
          console.error(
            "Failed to store data in DynamoDB",
            response.statusText
          );
          alert(
            "There was an error submitting your response. Please try again."
          );
        }
      } catch (error) {
        console.error("Error submitting data:", error);
        alert("There was an error submitting your response. Please try again.");
      }
    }
  });
});
