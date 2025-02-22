// Add a listener to detect when a link is hovered
document.addEventListener("mouseover", function (event) {
  var target = event.target;

  // Check if the hovered element is a link
  if (target.tagName === "H3" || (target.tagName === "A" && target.href && target.href.startsWith("http"))) {
    var websiteParent = null;
    var websiteUrl = target.href; // Retrieve the href attribute

    if (target.tagName === "H3") {
      websiteParent = target.parentNode.href;
    }

    // Fetch website information here (e.g., using an API)
    const url = websiteUrl ? websiteUrl : websiteParent;
    console.log(url);

    fetchData(url)
      .then(content => {
        createDialogBox(websiteUrl ? websiteUrl : websiteParent, content, event.clientX, event.clientY);
      })
      .catch(error => {
        console.error(error);
      });
  }
});


async function fetchData(url) {
  const response = await fetch('http://localhost:8889/predict', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ link: url })
  });
  return await response.json();
}

console.log(content.prediction);



function createDialogBox(websiteUrl, content, clientX, clientY) {
  // Create a temporary dialog box
  var dialogBox = document.createElement("div");
  dialogBox.style.position = "absolute";
  dialogBox.style.top = clientY + "px";
  dialogBox.style.left = clientX + "px";
  dialogBox.style.padding = "10px";
  dialogBox.style.backgroundColor = "white";
  dialogBox.style.border = "1px solid #ccc";
  dialogBox.style.zIndex = "9999";

  // Populate the dialog box with website information
  dialogBox.innerHTML = `
    <p>URL: ${websiteUrl ? websiteUrl : websiteParent}</p>
    <p>prediction: ${content.prediction ? "Safe" : "Not Secure!!"}</p>
    <p><button className="btn btn-primary">Ads: 0</button></p>
  `;

  // Append the dialog box to the body
  document.body.appendChild(dialogBox);

  // Remove the dialog box when the mouse moves out of the link
  document.addEventListener("mouseout", function (event) {
    if (event.target === dialogBox || dialogBox.contains(event.target)) {
      return;
    }
    document.body.removeChild(dialogBox);
  });
}
