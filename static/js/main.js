document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("navbar");
  const onScroll = () => navbar.classList.toggle("scrolled", window.scrollY > 24);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("visible");
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));

  document.querySelectorAll(".toast-close").forEach((btn) => {
    btn.addEventListener("click", () => btn.closest(".pcm-toast").remove());
  });
  setTimeout(() => {
    document.querySelectorAll(".pcm-toast").forEach((t) => t.remove());
  }, 6000);

  document.querySelectorAll(".navbar-collapse .nav-link, .navbar-collapse .btn").forEach((link) => {
    link.addEventListener("click", () => {
      const collapse = document.querySelector(".navbar-collapse");
      if (collapse.classList.contains("show")) {
        bootstrap.Collapse.getOrCreateInstance(collapse).hide();
      }
    });
  });
});