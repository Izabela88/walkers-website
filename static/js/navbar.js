// Code from https://codepen.io/JoseRosario/pen/BWqMwK*
function toggleHamburgerIcon() {
  let wrapperMenu = document.querySelector(".wrapper-menu");

  wrapperMenu.addEventListener("click", function () {
    wrapperMenu.classList.toggle("open");
  });
}

/* My code starts here
      Open and close sidebar for small devices*/
const hamburgerIcon = document.querySelector(".wrapper-menu");
const closeButtons = document.querySelectorAll(".close-sidebar");

let openSidebar = true;

toggleHamburgerIcon();


function openMenu() {
  document.getElementById("my-sidebar").classList.toggle('open-menu')
}

hamburgerIcon.addEventListener("click", function (e) {
  openMenu();
});

function toggleWrapperMenuOnResize() {
  if (window.innerWidth >= 1150) {
    closeMenu();
    openSidebar = true;
    let wrapperMenu = document.querySelector(".wrapper-menu.open");
    if (wrapperMenu) {
      wrapperMenu.classList.toggle("open");
    }
  }
}

window.addEventListener("resize", toggleWrapperMenuOnResize);

/* After pressing sidebar links and scrolling to a given section,
      the sidebar closes automatically*/
for (const button of closeButtons) {
  let wrapperMenu = document.querySelector(".wrapper-menu");
  button.addEventListener("click", function (e) {
    if (window.innerWidth < 1150) {
      wrapperMenu.classList.toggle("open");
      handleSidebar();
    }
  });
}

// Change navbar background color on scrolling
 window.addEventListener("scroll", () => {
  let header = document.querySelector("header");

  if (window.pageYOffset > 100 && window.innerWidth > 1150) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});


// Hide and show navbar on scrolling
// Variable which stores position of page
let previousPosition;
window.addEventListener("scroll", () => {
  let header = document.querySelector("header");
  // Get the scroll position
  let currentPosition =
    window.pageYOffset || document.documentElement.currentPosition;
  // Check weather the page is scrolled up or down
  if (currentPosition > previousPosition && window.innerWidth > 1150) {
    header.style.top = "-200px";
  } else {
    header.style.top = "0";
  }
  previousPosition = currentPosition;
});


// Control active class

function controlActiveClass() {
  let currentLocation = window.location.href
  let menuItem = document.querySelectorAll('#menu-list li a')
  let menuLength = menuItem.length

  for (let i = 0; i < menuLength; i++) {  
    if (menuItem[i].href === currentLocation) {
      menuItem[i].classList.add('active')
    } else {
      menuItem[i].classList.remove('active')
    }
  }
}

controlActiveClass()

const openModalButton = document.querySelector('#open-newsletter');
const closeModal = document.querySelector('.close-newsletter-btn');
// / Function opens Prices
function openModal() {
  let showDeleteModal = document.querySelector('.newsletter-wrapper');
  showDeleteModal.classList.toggle('show-newsletter-modal');
}

openModalButton.addEventListener('click', openModal);
closeModal.addEventListener('click', openModal);