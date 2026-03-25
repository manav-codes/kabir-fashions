// Product Filter Functionality
document.addEventListener("DOMContentLoaded", function () {
  var filterButtons = document.querySelectorAll(".filter-btn");
  var productCards = document.querySelectorAll(".product-card");

  function normalizeText(text) {
    return text
      .toLowerCase()
      .replace(/[\u2010\u2011\u2012\u2013\u2014\u2212]/g, "-")
      .replace(/\s+/g, " ")
      .trim();
  }

  var categoryMap = {
    "all": null,
    "kurtas": "kurtas",
    "co-ord sets": "co-ord set",
    "3 piece sets": "3 piece set"
  };

  filterButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filterButtons.forEach(function (b) {
        b.classList.remove("filter-btn--active");
      });
      btn.classList.add("filter-btn--active");

      var filterKey = normalizeText(btn.textContent);
      var matchText = categoryMap[filterKey];

      if (typeof matchText === "undefined") {
        matchText = filterKey;
      }

      productCards.forEach(function (card) {
        if (matchText === null) {
          card.style.display = "";
        } else {
          var category = card.querySelector(".product-card__category");
          var normalizedCategory = category ? normalizeText(category.textContent) : "";
          if (normalizedCategory.includes(matchText)) {
            card.style.display = "";
          } else {
            card.style.display = "none";
          }
        }
      });
    });
  });
});
