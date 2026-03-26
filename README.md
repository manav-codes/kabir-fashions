# Kabir Fashions — Clothing Catalogue Website

**Live site:** [kabirfashions.in](https://kabirfashions.in)

*A clean, professional clothing catalogue website built for a real client — browsable on any device, with direct WhatsApp ordering.*

---

## Overview
Kabir Fashions is an Indian clothing manufacturer based in Ahmedabad, Gujarat. They needed a simple, beautiful online presence to showcase their clothing line to customers.

This website lets customers browse the full product catalogue, filter by category, view product details, and contact the owner instantly via WhatsApp. No accounts, no checkout, no friction — just browse and connect.

Built as a freelance project using only HTML, CSS, and a small amount of JavaScript. No frameworks, no backend, no database — intentionally lightweight so it loads fast and is easy to maintain.

---

## Screenshots
<img width="1920" height="2063" alt="capture" src="https://github.com/user-attachments/assets/41175cc2-3968-45d8-a314-7f55aca5af57" />


## What
A static clothing catalogue website with:
* Full product catalogue across 3 categories
* Live category filtering
* Individual product detail pages
* WhatsApp contact on every product
* Contact form with email delivery via Formspree
* Fully responsive across all devices

## Why
The client needed an affordable, professional online catalogue without the complexity or monthly cost of platforms like Shopify. The target audience needed a clean, trustworthy, easy-to-navigate experience.

## How
Built with vanilla HTML, CSS, and JavaScript. No build tools, no package managers, no dependencies. Open the folder and it works. 

**Key technical decisions:**
* Pure CSS hamburger menu (no JS needed)
* CSS `:target` trick for product image gallery
* Vanilla JS for category filtering (no jQuery or libraries)
* Formspree for contact form email delivery (no backend)
* GitHub Pages for free, reliable hosting
* Custom domain via Spaceship registrar

---

## Product Categories
* Kurtas
* Co-ord Sets (2 Piece — Top & Bottom)
* 3 Piece Sets (Top, Bottom & Dupatta)

## Pages
* `/` — Homepage with hero banner and full product catalogue
* `/products/` — Full catalogue with live category filtering
* `/product-detail/` — Single product with image gallery and size selector
* `/about/` — Brand story and values
* `/contact/` — Contact details, Google Maps link and enquiry form

---

## File Structure
```text
kabir-fashions/
├── index.html              — Root homepage (serves content directly)
├── home/
│   └── index.html          — Homepage with hero banner and full product catalogue
├── products/
│   └── index.html          — Full catalogue with live category filtering
├── product-detail/
│   └── index.html          — Single product with image gallery and size selector
├── about/
│   └── index.html          — Brand story and values
├── contact/
│   └── index.html          — Contact details, Google Maps link and enquiry form
├── css/
│   ├── style.css           — global styles, variables, layout
│   ├── navbar.css          — sticky navbar and mobile hamburger
│   ├── footer.css          — footer layout
│   ├── products.css        — product cards, grid, filter, detail page
│   ├── responsive.css      — breakpoints for mobile and tablet
│   └── animations.css      — scroll reveal and fade animations
├── js/
│   ├── filter.js           — category filter logic
│   └── scroll-reveal.js    — scroll animation triggers
├── images/
│   ├── logo.png
│   ├── whatsapp.svg
│   ├── products/           — product images go here
│   └── hero/               — hero banner images go here
└── README.md
```

---

## Design

### Colour Palette
* **Primary:** `#b16f55` (warm terracotta)
* **Secondary:** `#f0ebd8` (warm off-white)
* **Text Dark:** `#2C1A12`
* **Text Mid:** `#6B4F3A`

### Fonts (Google Fonts)
* **Logo:** Samarkan
* **Headings:** Playfair Display
* **Body:** Lato

---

## Build & Run Instructions
No installation, no environment variables, no build step required. 

**To run locally:**

1. Clone the repository:
```bash
git clone [https://github.com/manav-codes/kabir-fashions.git](https://github.com/manav-codes/kabir-fashions.git)
```

2. Navigate into the folder:
```bash
cd kabir-fashions
```

3. Open `index.html` in any modern browser (Chrome, Firefox, Edge).

*That's it. No server needed.*

---

## How to Update Products

1. Open `index.html` (root) or `products/index.html` in any code editor.
2. Find the product card you want to edit — each is an `article.product-card` block.
3. Update the name, category or image as needed.
   * **To add a product** — duplicate an entire `article.product-card` block and edit it.
   * **To remove a product** — delete the entire `article.product-card` block.
4. Save, commit and push — live site updates in 30 seconds.

**To add a real product image:**

1. Save the image to `images/products/filename.jpg`
2. In the HTML, replace:
```html
<div class="product-card__image image-placeholder image-placeholder--square">
  Product Image
</div>
```
*with:*
```html
<div class="product-card__image">
  <img src="images/products/filename.jpg" alt="Product name" />
</div>
```
3. Commit and push.

---

## Deployment
The site is hosted on **GitHub Pages** and deploys automatically on every push to the `master` branch.

**To deploy your own version:**
1. Fork this repository
2. Go to Settings → Pages
3. Set branch to `master`
4. Your site will be live at `https://yourusername.github.io/kabir-fashions`

**To connect a custom domain**, add your domain in Settings → Pages → Custom Domain, then add the following A records in your domain registrar's DNS settings:
```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

---

## Testing

### Manual testing checklist:
- [x] All 5 pages load correctly
- [x] Navbar links work on all pages
- [x] Mobile hamburger menu opens and closes
- [x] Category filter shows and hides correct products
- [x] WhatsApp buttons open correct number
- [x] Contact form submits and email is received
- [x] Google Maps link opens correct location
- [x] Phone and email links work on mobile
- [x] Site looks correct on mobile, tablet and desktop

---

## Known Issues & To-Do

### Known Issues:
* No animation on product filter hide/show
* No swipe support on mobile for product image gallery

### To-Do / Future Features:
- [✅] Add real product images when provided by client
- [ ] Add swipe gesture support for mobile image gallery
- [ ] Add smooth animation when filtering products
- [✅] Add a floating WhatsApp button on all pages

---

## Author
**Manav Sukhwani**
* 📩 [sukhwanimanav24@gmail.com](mailto:sukhwanimanav24@gmail.com)
* 🔗 [github.com/manav-codes](https://github.com/manav-codes)
* 💼 [linkedin.com/in/manavsukhwani](https://linkedin.com/in/manavsukhwani)

## Client
**Ashwin Panjwani, Kabir Fashions**
* 📍 [E-501-502, Fifth Floor, Iscon Commercial Centre, 
VIP Market, Opp Safal 1, Raipur, 
Ahmedabad, Gujarat — 380001](https://maps.app.goo.gl/Jzz3LBLCxeBLvmLN8)
* 📩 [kabirfashions.kmt@gmail.com](mailto:kabirfashions.kmt@gmail.com)
* 🌐 [kabirfashions.in](https://kabirfashions.in)

## License
This project was built for a private client. Code is publicly visible for portfolio purposes. Do not reuse or redistribute without permission.
