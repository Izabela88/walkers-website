// https://stackoverflow.com/questions/9737655/django-message-once-logged-in
$(document).ready(function () {
  $(".info-msg").delay(3500).fadeOut();
});

const btn = $("#scroll-top-button");

$(window).scroll(function () {
  if ($(window).scrollTop() > 200) {
    btn.addClass("show");
  } else {
    btn.removeClass("show");
  }
});

btn.addEventListener("click", () => {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});
