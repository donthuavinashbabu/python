(function () {
  // Used when this site is served from GitHub Pages (/docs folder).
  // Relative ../ links work locally; on Pages they are rewritten to the repo on github.com.
  var REPO = {
    owner: "donthuavinashbabu",
    repo: "python",
    branch: "main"
  };

  var links = document.querySelectorAll(".nav-link");
  var pages = document.querySelectorAll(".page");
  var sidebar = document.getElementById("sidebar");
  var overlay = document.getElementById("overlay");
  var menuToggle = document.getElementById("menuToggle");

  function isGitHubPages() {
    return /\.github\.io$/i.test(window.location.hostname);
  }

  function repoPathFromRelative(href) {
    // "../decorators/decorators.py" -> "decorators/decorators.py"
    return href.replace(/^\.\.\//, "");
  }

  function rewriteRepoPathsForPages() {
    if (!isGitHubPages()) return;

    var blobBase =
      "https://github.com/" +
      REPO.owner +
      "/" +
      REPO.repo +
      "/blob/" +
      REPO.branch +
      "/";
    var rawBase =
      "https://raw.githubusercontent.com/" +
      REPO.owner +
      "/" +
      REPO.repo +
      "/" +
      REPO.branch +
      "/";

    document.querySelectorAll('a[href^="../"]').forEach(function (anchor) {
      var href = anchor.getAttribute("href");
      anchor.setAttribute("href", blobBase + repoPathFromRelative(href));
      anchor.setAttribute("target", "_blank");
      anchor.setAttribute("rel", "noopener");
    });

    document.querySelectorAll('img[src^="../"]').forEach(function (img) {
      var src = img.getAttribute("src");
      img.setAttribute("src", rawBase + repoPathFromRelative(src));
    });
  }

  function showPage(pageId) {
    pages.forEach(function (page) {
      page.classList.toggle("active", page.id === "page-" + pageId);
    });

    links.forEach(function (link) {
      link.classList.toggle("active", link.dataset.page === pageId);
    });

    var activeLink = document.querySelector(
      '.nav-link[data-page="' + pageId + '"]'
    );
    if (activeLink) {
      activeLink.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }

    window.scrollTo({
      top: 0,
      behavior: "instant" in window ? "instant" : "auto"
    });
    closeMenu();
  }

  function pageFromHash() {
    var hash = (window.location.hash || "#home").slice(1);
    var exists = document.getElementById("page-" + hash);
    return exists ? hash : "home";
  }

  function openMenu() {
    sidebar.classList.add("open");
    overlay.classList.add("show");
  }

  function closeMenu() {
    sidebar.classList.remove("open");
    overlay.classList.remove("show");
  }

  links.forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      var pageId = link.dataset.page;
      if (!pageId) return;
      history.pushState(null, "", "#" + pageId);
      showPage(pageId);
    });
  });

  document.querySelectorAll(".goto").forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      var pageId = link.dataset.page;
      if (!pageId) return;
      history.pushState(null, "", "#" + pageId);
      showPage(pageId);
    });
  });

  window.addEventListener("hashchange", function () {
    showPage(pageFromHash());
  });

  if (menuToggle) {
    menuToggle.addEventListener("click", function () {
      if (sidebar.classList.contains("open")) {
        closeMenu();
      } else {
        openMenu();
      }
    });
  }

  if (overlay) {
    overlay.addEventListener("click", closeMenu);
  }

  rewriteRepoPathsForPages();
  showPage(pageFromHash());
})();
