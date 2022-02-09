

function displayCurrentTab(current) {
  let tabs = document.querySelector(".tabs");
  let tabsContents = tabs.querySelectorAll(".tabs-content");

  for (let i = 0; i < tabsContents.length; i++) {
    tabsContents[i].style.display = current === i ? "flex" : "none";
  }
}

displayCurrentTab(0);


function swapTabs() {
  let tabs = document.querySelector(".tabs");
  let tabsBtns = tabs.querySelectorAll(".tabs-button");

  tabs.addEventListener("click", (event) => {
    if (event.target.className.split(" ")[0] === "tabs-button") {
      for (let i = 0; i < tabsBtns.length; i++) {
        if (event.target === tabsBtns[i]) {
          displayCurrentTab(i);
          tabsBtns[i].style.backgroundColor = "#fff"
          tabsBtns[i].style.color = "#eea300"
        } else {
          tabsBtns[i].style.backgroundColor = "#eea300"
          tabsBtns[i].style.color = "#fff"
        }
  
      }
    }
  });
}

swapTabs()