const one = document.getElementById("id_stars_0");
const two = document.getElementById("id_stars_1");
const three = document.getElementById("id_stars_2");
const four = document.getElementById("id_stars_3");
const five = document.getElementById("id_stars_4");
const stars = document.querySelector("#id_stars");

const handleStarSelect = (size) => {
  const children = stars.children;
  console.log(children);

  for (let i = 0; i < children.length; i++) {
    if (i <= size) {
      children[i].classList.add("checked");
    } else {
      children[i].classList.remove("checked");
    }
  }
};

const handleSelect = (selection) => {
  switch (selection) {
    case "id_stars_0": {
      handleStarSelect(0);
      return;
    }
    case "id_stars_1": {
      handleStarSelect(1);
      return;
    }
    case "id_stars_2": {
      handleStarSelect(2);
      return;
    }
    case "id_stars_3": {
      handleStarSelect(3);
      return;
    }
    case "id_stars_4": {
      handleStarSelect(4);
      return;
    }
  }
};

const arr = [one, two, three, four, five];

arr.forEach((item) =>
  item.addEventListener("click", (event) => {
    handleSelect(event.target.id);
  })
);
