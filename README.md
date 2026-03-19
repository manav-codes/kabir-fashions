# Kabir Fashions – Static Catalogue Website

This project is a simple, elegant, **B2B clothing catalogue** for an Indian clothing manufacturer called **Kabir Fashions**.  
Customers can browse products and contact the owner directly on WhatsApp. There is **no cart, no login and no payment flow** – it is a pure catalogue plus contact site.

---

## File Structure

```text
kabir-fashions/
├── index.html
├── products.html
├── product-detail.html
├── about.html
├── contact.html
├── css/
│   ├── style.css
│   ├── navbar.css
│   ├── footer.css
│   ├── products.css
│   └── responsive.css
├── images/
│   ├── hero/
│   ├── products/
│   └── logo/
└── README.md
```

### HTML Pages

- **index.html**  
  Homepage with hero banner, quick brand strip, featured products and a WhatsApp call‑to‑action.

- **products.html**  
  Full catalogue page with filter buttons (visual only) and a 12‑product demo grid.

- **product-detail.html**  
  Example product detail page with a CSS‑only image gallery, size selector and WhatsApp enquiry button.

- **about.html**  
  Brand story, values and a simple image placeholder section.

- **contact.html**  
  Contact details, WhatsApp CTA and a basic contact form (no backend).

### CSS Files

- **css/style.css**  
  Global variables, typography, layout utilities and page‑level sections (hero, strips, contact form, values etc.).

- **css/navbar.css**  
  Sticky top navigation bar with desktop links and a CSS‑only hamburger menu for mobile.

- **css/footer.css**  
  Three‑column footer layout and bottom copyright bar.

- **css/products.css**  
  Product card styles, catalogue grid, filter bar and product‑detail layout including the gallery and size selector.

- **css/responsive.css**  
  Responsive tweaks for mobile and tablet breakpoints (grids, hero, contact layout, footer, etc.).

Images should be placed inside the `images/` folders if you want to replace the CSS placeholders.

---

## Fonts & Colours

- **Fonts (Google Fonts)**  
  - Headings: `Playfair Display`  
  - Body: `Lato`

The fonts are loaded in each HTML file via Google Fonts.

- **Colour Palette (defined in `:root` in `style.css`)**

```css
:root {
  --color-primary: #a47764;
  --color-secondary: #f0ebd8;
  --color-text-dark: #2C1A12;
  --color-text-mid: #6B4F3A;
  --color-text-light: #f0ebd8;
  --color-border: #c9a990;
  --color-white: #FFFFFF;
  --color-whatsapp: #25D366;
}
```

All layout and components use only these colours.

---

## WhatsApp Contact

All WhatsApp buttons link to:

```text
https://wa.me/919327769799
```

To change this number globally, search in the HTML files for `wa.me/919327769799` and replace it with the new number in the same format (no `+` sign).

---

## How to View the Site

1. Copy the entire `kabir-fashions` folder to your machine.  
2. Open `index.html` in any modern browser (Chrome, Edge, Firefox, etc.).  
3. Navigate via the top navbar links between **Home**, **Products**, **About** and **Contact**.

No build step or server is required – it is a purely static website.

---

## How to Update Products Manually

Because there is no database or admin panel, **all updates are done by editing HTML files directly**.

### 1. Update Featured Products on the Homepage

1. Open `index.html` in a code editor.  
2. Search for the comment “Featured Products” or for `<section class="section featured-products">`.  
3. Inside this section you will see several `article` elements with the class `product-card`.
4. For each card you can change:
   - **Category**: text inside `<p class="product-card__category">…</p>`
   - **Name**: text inside `<h3 class="product-card__name">…</h3>`
   - **Price**: text inside `<p class="product-card__price">…</p>`
   - **Detail link**: the `href` of `<a class="product-card__link">` (usually `product-detail.html`)

If you want to add a new featured product, duplicate one whole `<article class="product-card">…</article>` block and edit the text.

### 2. Update the Main Catalogue (12 Products)

1. Open `products.html`.  
2. Find the section `<section class="section">` containing `<div class="product-grid grid grid-3">`.  
3. Each `article.product-card` here represents **one product** in the catalogue.
4. Update the same fields as above (category, name, price and link).
5. To add or remove products, simply duplicate or delete entire `article.product-card` blocks.

> **Note:** The filter buttons (`All | Kurtas | Shirts | …`) are visual only. They do not filter products yet. JavaScript can be added later if interactive filtering is required.

### 3. Update the Product Detail Page

1. Open `product-detail.html`.  
2. In the right‑hand column (`product-detail-info`), change:
   - The **category** line (`Kurtas`)  
   - The **product name** (`Classic Cotton Kurta`)  
   - The **price** (`₹1,499`)  
   - The **description paragraphs** below the divider  
3. In the gallery section (`product-gallery`), the large image placeholders and three thumbnails are purely visual.  
   - If you want to use real images, you can replace the placeholder `<div class="image-placeholder …">` blocks with `<img>` tags pointing to files from `images/products/`.

### 4. Update “You May Also Like”

1. In `product-detail.html`, scroll to the section with heading “You May Also Like”.  
2. Edit or duplicate the `article.product-card` elements in the same way as the main catalogue.

---

## Replacing Placeholder Images

Currently all product and hero images are **CSS placeholders** with a warm border colour and the text “Product Image”.

To use real images:

1. Save your product photos in the appropriate folders (for example `images/products/kurta-01.jpg`).  
2. In the relevant HTML file, replace:

```html
<div class="product-card__image image-placeholder image-placeholder--square">
  Product Image
</div>
```

with:

```html
<div class="product-card__image">
  <img src="images/products/kurta-01.jpg" alt="Classic Cotton Kurta by Kabir Fashions" />
</div>
```

3. Keep the `alt` text descriptive for accessibility.

You can do the same for hero or brand images on the homepage and about page.

---

## Navbar & Footer Reuse

The **navbar** and **footer** markup is repeated across all HTML files for simplicity.  
If you change a link label, phone number or email address in one page, remember to update it in the other pages as well.

Key places:

- Navbar: search for `<nav class="navbar">` in each HTML file.
- Footer: search for `<footer class="site-footer">` in each HTML file.

---

## Adding New Pages

1. Duplicate one of the existing HTML files (for example `about.html`).  
2. Rename the file (e.g. `wholesale.html`).  
3. Update the `<title>` tag and the main heading inside `<main>`.  
4. Add a new link in the navbar and footer of **all** pages if you want the new page to appear in navigation.

---

## Notes

- The site intentionally uses **no JavaScript**, so all interaction is via standard links and CSS (including the mobile hamburger menu and the product gallery).  
- Layout is mobile‑first and uses simple CSS Grid and Flexbox for responsiveness.  
- All text, prices and product names are **demo content** and can be safely replaced with real catalogue data when available.

