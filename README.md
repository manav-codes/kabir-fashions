1. Open the relevant 'index.html' file (e.g. inside the 'home' or 'products' folder) in a code editor.
2. Find the product card you want to edit — each is an 'article.product-card' block.
3. Update the name, category or image as needed.
   * **To add a product** — duplicate an entire 'article.product-card' block and edit it.
   * **To remove a product** — delete the entire 'article.product-card' block.
4. Save, commit and push — live site updates in 30 seconds.

**To add a real product image:**

**Live site:** [kabirfashions.in](https://kabirfashions.in)

*A clean, professional clothing catalogue website built for a real client â€” browsable on any device, with direct WhatsApp ordering.*

---

## Overview
Kabir Fashions is an Indian clothing manufacturer based in Ahmedabad, Gujarat. They needed a simple, beautiful online presence to showcase their clothing line to customers.

This website lets customers browse the full product catalogue, filter by category, view product details, and contact the owner instantly via WhatsApp. No accounts, no checkout, no friction â€” just browse and connect.

Built as a freelance project using only HTML, CSS, and a small amount of JavaScript. No frameworks, no backend, no database â€” intentionally lightweight so it loads fast and is easy to maintain.

---

## Screenshots
> *Add screenshots here once the site has real product images.*

---

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
* Co-ord Sets (2 Piece â€” Top & Bottom)
* 3 Piece Sets (Top, Bottom & Dupatta)

## Pages
* `index.html` â€” Homepage with hero banner and full product catalogue
* `products.html` â€” Full catalogue with live category filtering
* `product-detail.html` â€” Single product with image gallery and size selector
* `about.html` â€” Brand story and values
* `contact.html` â€” Contact details, Google Maps link and enquiry form

---

## File Structure
```text
kabir-fashions/
â”œâ”€â”€ home.html
â”œâ”€â”€ products.html
â”œâ”€â”€ product-detail.html
â”œâ”€â”€ about.html
â”œâ”€â”€ contact.html
â”œâ”€â”€ css/
â”‚   â”œâ”€â”€ style.css        â€” global styles, variables, layout
â”‚   â”œâ”€â”€ navbar.css       â€” sticky navbar and mobile hamburger
â”‚   â”œâ”€â”€ footer.css       â€” footer layout
â”‚   â”œâ”€â”€ products.css     â€” product cards, grid, filter, detail page
â”‚   â””â”€â”€ responsive.css   â€” breakpoints for mobile and tablet
â”œâ”€â”€ js/
â”‚   â””â”€â”€ filter.js        â€” category filter logic
â”œâ”€â”€ images/
â”‚   â”œâ”€â”€ logo.jpeg
â”‚   â”œâ”€â”€ products/        â€” product images go here
â”‚   â””â”€â”€ hero/            â€” hero banner images go here
â””â”€â”€ README.md
```

---

1. Open the relevant 'index.html' file (e.g. inside the 'home' or 'products' folder) in a code editor.
2. Find the product card you want to edit — each is an 'article.product-card' block.
3. Update the name, category or image as needed.
   * **To add a product** — duplicate an entire 'article.product-card' block and edit it.
   * **To remove a product** — delete the entire 'article.product-card' block.
4. Save, commit and push — live site updates in 30 seconds.

**To add a real product image:**

### Colour Palette
* **Primary:** `#a47764` (warm terracotta)
* **Secondary:** `#f0ebd8` (warm off-white)
* **Text Dark:** `#2C1A12`
* **Text Mid:** `#6B4F3A`

### Fonts (Google Fonts)
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

1. Open the relevant 'index.html' file (e.g. inside the 'home' or 'products' folder) in a code editor.
2. Find the product card you want to edit — each is an 'article.product-card' block.
3. Update the name, category or image as needed.
   * **To add a product** — duplicate an entire 'article.product-card' block and edit it.
   * **To remove a product** — delete the entire 'article.product-card' block.
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
2. Go to Settings â†’ Pages
3. Set branch to `master`
4. Your site will be live at `https://yourusername.github.io/kabir-fashions`

**To connect a custom domain**, add your domain in Settings â†’ Pages â†’ Custom Domain, then add the following A records in your domain registrar's DNS settings:
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
- [ ] Add real product images when provided by client
- [ ] Add swipe gesture support for mobile image gallery
- [ ] Add smooth animation when filtering products
- [ ] Add Instagram feed or social links section
- [ ] Add a floating WhatsApp button on all pages

---

## Author
**Manav Sukhwani**
* ðŸ“© [sukhwanimanav24@gmail.com](mailto:sukhwanimanav24@gmail.com)
* ðŸ”— [github.com/manav-codes](https://github.com/manav-codes)
* ðŸ’¼ [linkedin.com/in/manavsukhwani](https://linkedin.com/in/manavsukhwani)

## Client
**Ashwin Panjwani, Kabir Fashions**
* ðŸ“ [E-501-502, Fifth Floor, Iscon Commercial Centre, 
VIP Market, Opp Safal 1, Raipur, 
Ahmedabad, Gujarat â€” 380001](https://maps.app.goo.gl/XWd8AeQRCsiqvExEA)
* ðŸ“© [kabirfashions.kmt@gmail.com](mailto:kabirfashions.kmt@gmail.com)
* ðŸŒ [kabirfashions.in](https://kabirfashions.in)

## License
This project was built for a private client. Code is publicly visible for portfolio purposes. Do not reuse or redistribute without permission.

