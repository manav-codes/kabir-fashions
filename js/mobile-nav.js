// Close CSS-only hamburger menu when clicking/tapping outside the nav on mobile
(function() {
  var navToggle = document.getElementById('nav-toggle');
  if (!navToggle) return; // no-op on pages without the checkbox

  // Elements we treat as "inside the nav" and should NOT close the menu
  var ignoreSelector = 'nav, .nav-links, .nav-toggle-label, label[for="nav-toggle"]';

  function handleOutsideClick(e) {
    try {
      if (!navToggle.checked) return; // already closed
      if (!e.target || e.target.closest(ignoreSelector)) return; // clicked inside nav
      navToggle.checked = false;
    } catch (err) {
      // swallow any unexpected errors to avoid breaking page scripts
      console && console.warn && console.warn('mobile-nav handler error', err);
    }
  }

  // Use capture to notice touches/clicks early (works better on some mobile browsers)
  document.addEventListener('click', handleOutsideClick, true);
  document.addEventListener('touchstart', handleOutsideClick, true);
})();
