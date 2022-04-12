// https://stackoverflow.com/questions/9737655/django-message-once-logged-in
// Make messages disappear after 3.5s
$(document).ready(function () {
  $(".info-msg").delay(3500).fadeOut();
});

// Show and hide scroll to top button
const btn = $("#scroll-top-button");

$(window).scroll(function () {
  if ($(window).scrollTop() > 200) {
    btn.addClass("show");
  } else {
    btn.removeClass("show");
  }
});

// Scroll to top on click
btn[0].addEventListener("click", () => {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});
