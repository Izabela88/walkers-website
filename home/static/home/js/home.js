// Change active menu item (link) on page scroll
function addActiveOnScroll() {
  window.addEventListener("scroll", (e) => {
    let sections = document.querySelectorAll(".section");
    let navLinks = document.querySelectorAll(".nav-link");

    for (let [i, section] of sections.entries()) {
      let box = section.getBoundingClientRect();
      if ( box.top <= 200 && box.bottom >= 300) {
        navLinks[i].classList.add("active");
      } else {
        navLinks[i].classList.remove("active");
      }
    }
  });
}

addActiveOnScroll();

