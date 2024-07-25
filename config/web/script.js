document.addEventListener("DOMContentLoaded", function () {
  // Function to fetch IP information
  fetch("http://ip-api.com/json")
    .then((response) => response.json())
    .then((data) => {
      // Show IP information
      document.getElementById("ip-address").innerText = data.query;
      document.getElementById("isp-hostname").innerText = data.isp;
      document.getElementById("country").innerText = data.country;
      document.getElementById("city").innerText = data.city;
    })
    .catch((error) => {
      console.error("Error fetching IP info:", error);
      // Handle errors gracefully
      document.getElementById("ip-address").innerText = "Error fetching IP";
      document.getElementById("isp-hostname").innerText = "Error fetching ISP";
      document.getElementById("country").innerText = "Error fetching country";
      document.getElementById("city").innerText = data.city;
    });

  // Function to update time
  function updateTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const ampm = hours >= 12 ? "PM" : "AM";
    const formattedHours = hours % 12 || 12;
    const formattedMinutes = minutes < 10 ? "0" + minutes : minutes;
    const timeString = `${formattedHours}:${formattedMinutes} ${ampm}`;
    document.getElementById("time").innerText = timeString;
  }

  updateTime();
  setInterval(updateTime, 60000); // Update time every minute

  // Handle Enter key press in the search bar
  document
    .querySelector(".search-bar")
    .addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault(); // Prevent form submission if needed
        document.getElementById("search-form").submit(); // Trigger form submission
      }
    });

  // Fetch and display the articles
  fetch(
    "https://raw.githubusercontent.com/MuntasirArafat/MuntasirArafat/main/shield-news.json"
  )
    .then((response) => response.json())
    .then((data) => {
      const newsSection = document.querySelector(".news-section");
      data.forEach((article) => {
        const articleCard = document.createElement("div");
        articleCard.classList.add("card");
        articleCard.innerHTML = `
        <a href="${article.blogUrl}" class="text" target="_blank">   
        <img src="${article.img}" class="card-img-top" alt="Article Image" />
            <div class="card-body">
              <h5 class="card-title">${article.title}</h5>
              <p class="card-text">${article.about}</p>
            </div>
         </a>
          `;

        newsSection.appendChild(articleCard);
      });
    })
    .catch((error) => {
      console.error("Error fetching article:", error);
      // Handle errors gracefully
      const articleCard = document.createElement("div");
      articleCard.classList.add("card");
      articleCard.style.width = "18rem";
      articleCard.innerHTML = `
          <div class="skeleton skeleton-img" style="height: 180px;"></div>
          <div class="card-body">
            <div class="skeleton skeleton-title" style="width: 80%; height: 20px;"></div>
            <div class="skeleton skeleton-about" style="width: 100%; height: 60px;"></div>
            <div class="skeleton skeleton-link" style="width: 50%; height: 30px;"></div>
          </div>
        `;
      document.querySelector(".news-section").appendChild(articleCard);
    });
});
