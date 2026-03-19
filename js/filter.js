// Product Filter Functionality
document.addEventListener("DOMContentLoaded", function () {
  var filterButtons = document.querySelectorAll(".filter-btn");
  var productCards = document.querySelectorAll(".product-card");

  var categoryMap = {
    "All": null,
    "Kurtas": "Kurtas",
    "Co-ord Sets": "2 Piece Set",
    "3 Piece Sets": "3 Piece Set"
  };

  filterButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filterButtons.forEach(function (b) {
        b.classList.remove("filter-btn--active");
      });
      btn.classList.add("filter-btn--active");

      var filterKey = btn.textContent.trim();
      var matchText = categoryMap[filterKey];

      productCards.forEach(function (card) {
        if (!matchText) {
          card.style.display = "";
        } else {
          var category = card.querySelector(".product-card__category");
          if (category && category.textContent.includes(matchText)) {
            card.style.display = "";
          } else {
            card.style.display = "none";
          }
        }
      });
    });
  });
});
