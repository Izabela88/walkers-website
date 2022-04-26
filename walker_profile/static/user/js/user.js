// Display tabs content
function displayCurrentTab(current) {
  let tabs = document.querySelector(".tabs");
  let tabsContents = tabs.querySelectorAll(".tabs-content");

  for (let i = 0; i < tabsContents.length; i++) {
    if (current === i) {
      tabsContents[i].classList.add("display-content");
    } else {
      tabsContents[i].classList.remove("display-content");
    }
  }
}

if (!document.querySelector(".display-content")) {
  displayCurrentTab(0);
}

// Handle tabs buttons and change their colors on click
function swapTabs() {
  let tabs = document.querySelector(".tabs");
  let tabsBtns = tabs.querySelectorAll(".tabs-button");

  tabs.addEventListener("click", (event) => {
    if (event.target.className.split(" ")[0] === "tabs-button") {
      for (let i = 0; i < tabsBtns.length; i++) {
        if (event.target === tabsBtns[i]) {
          displayCurrentTab(i);
          tabsBtns[i].classList.add("display-tab-white");
          tabsBtns[i].classList.remove("display-tab-orange");
        } else {
          tabsBtns[i].classList.add("display-tab-orange");
          tabsBtns[i].classList.remove("display-tab-white");
        }
      }
    }
  });
}

swapTabs();

// Handle functionality related to pet sitter profile forms

const tabs = document.querySelector(".wrapper");
const tabButton = document.querySelectorAll(".tab-button");
const contents = document.querySelectorAll(".content");
const activeContent = document.getElementsByClassName("content active");

tabs.onclick = (e) => {
  const id = e.target.dataset.id;
  if (id) {
    tabButton.forEach((btn) => {
      btn.classList.remove("active");
    });
    e.target.classList.add("active");

    contents.forEach((content) => {
      content.classList.remove("active");
    });
    const element = document.getElementById(id);
    element.classList.add("active");
  }
};

const enableDisablePrice = (isActive, perHour, perDay) => {
  // Enable and disable price inputs, depends on dog size checkbox
  if (isActive.checked) {
    perHour.readOnly = false;
    perDay.readOnly = false;
  } else {
    perHour.readOnly = true;
    perDay.readOnly = true;
  }
};

const getPriceInputs = (formId, size) => {
  // Get price per hour and per day for given dog size
  perHour = document
    .getElementById(formId)
    .querySelector(`#id_${size}_price_hour`);
  perDay = document
    .getElementById(formId)
    .querySelector(`#id_${size}_price_day`);
  return [perHour, perDay];
};

const toggleActive = (e) => {
  // Function disable/enable price inputs
  let formId = e.currentTarget.parentElement.parentElement.id;

  let isActive = document
    .getElementById(formId)
    .querySelector(`#${e.currentTarget.id}`);

  if (e.currentTarget.id === "id_is_small_dog") {
    [perHour, perDay] = getPriceInputs(formId, "s");
  } else if (e.currentTarget.id === "id_is_medium_dog") {
    [perHour, perDay] = getPriceInputs(formId, "m");
  } else {
    [perHour, perDay] = getPriceInputs(formId, "b");
  }

  enableDisablePrice(isActive, perHour, perDay);
};

const activePrice = () => {
  // Get all petsitter profile form tabs (excluding `Description`)
  const petsitterForms = document.querySelectorAll(".petsitter-profile-label");
  petsitterForms.forEach((form) => {
    // Get checkboxes for each dog size
    let isSmallActive = document
      .getElementById(form.dataset.id)
      .querySelector("#id_is_small_dog");
    let isMediumActive = document
      .getElementById(form.dataset.id)
      .querySelector("#id_is_medium_dog");
    let isBigActive = document
      .getElementById(form.dataset.id)
      .querySelector("#id_is_big_dog");

    // Add event listener on click to toggle price
    isSmallActive.addEventListener("click", toggleActive);
    isMediumActive.addEventListener("click", toggleActive);
    isBigActive.addEventListener("click", toggleActive);

    // Get price inputs for each size
    [sPerHour, sPerDay] = getPriceInputs(form.dataset.id, "s");
    [mPerHour, mPerDay] = getPriceInputs(form.dataset.id, "m");
    [bPerHour, bPerDay] = getPriceInputs(form.dataset.id, "b");

    // Initial price active/disable state
    enableDisablePrice(isSmallActive, sPerHour, sPerDay);
    enableDisablePrice(isMediumActive, mPerHour, mPerDay);
    enableDisablePrice(isBigActive, bPerHour, bPerDay);
  });
};

activePrice();

function defaultOpenTab() {
  if (!activeContent.length) {
    document.getElementsByClassName("tab-button")[0].click();
  }
}

defaultOpenTab();
