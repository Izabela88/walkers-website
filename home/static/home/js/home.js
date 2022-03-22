// Change active menu item (link) on page scroll
function addActiveOnScroll() {
  window.addEventListener("scroll", (e) => {
    let sections = document.querySelectorAll(".section");
    let links = document.querySelectorAll("#menu-list li a");

    for (let [i, section] of sections.entries()) {
      let box = section.getBoundingClientRect();
      if ( box.top <= 200 && box.bottom >= 300) {
        links[i].classList.add("active");
      } else {
        links[i].classList.remove("active");
      }
    }
  });
}

addActiveOnScroll();

