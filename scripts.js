// Add the Bootstrap JS and Popper.js scripts here
document.addEventListener("DOMContentLoaded", function () {
  var bootstrapScript = document.createElement("script");
  bootstrapScript.src = "https://code.jquery.com/jquery-3.3.1.slim.min.js";
  document.head.appendChild(bootstrapScript);

  var popperScript = document.createElement("script");
  popperScript.src =
    "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js";
  document.head.appendChild(popperScript);

  var bootstrapJS = document.createElement("script");
  bootstrapJS.src =
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js";
  document.head.appendChild(bootstrapJS);
});

document.getElementById("cvTextForm").addEventListener("submit", function (e) {
  e.preventDefault();
  var cvText = document.getElementById("cvText").value;

  // Send the CV text to the Flask server
  fetch("http://127.0.0.1:5000/submit-cv", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ cvText: cvText }), // Convert the CV text to JSON format
  })
    .then((response) => response.json()) // Parse the JSON response
    .then((data) => {
      // Display the result on the webpage
      console.log(data); // For now, log the response to the console
      document.getElementById("result").innerText = data.message;
    })
    .catch((error) => console.error("Error:", error));
});
