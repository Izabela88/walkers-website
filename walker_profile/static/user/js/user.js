function displayCurrentTab(current) {
  let tabs = document.querySelector(".tabs");
  let tabsContents = tabs.querySelectorAll(".tabs-content");

  for (let i = 0; i < tabsContents.length; i++) {
    if (current === i) {
      tabsContents[i].classList.add('display-content')
    } else {
      tabsContents[i].classList.remove('display-content')
    }
  }

}

if (!document.querySelector('.display-content')) {
  displayCurrentTab(0)
}



function swapTabs() {
  let tabs = document.querySelector(".tabs");
  let tabsBtns = tabs.querySelectorAll(".tabs-button");

  tabs.addEventListener("click", (event) => {
    if (event.target.className.split(" ")[0] === "tabs-button") {
      for (let i = 0; i < tabsBtns.length; i++) {
        if (event.target === tabsBtns[i]) {
          displayCurrentTab(i);
          tabsBtns[i].classList.add('display-tab-white')
          tabsBtns[i].classList.remove('display-tab-orange')
        } else {
          tabsBtns[i].classList.add('display-tab-orange')
          tabsBtns[i].classList.remove('display-tab-white')
        }
      }
    }
  });
}

swapTabs()