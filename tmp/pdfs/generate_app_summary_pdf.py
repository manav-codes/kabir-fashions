from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "kabir-fashions-app-summary.pdf"


def bullet_list(items, style, bullet_color):
    return ListFlowable(
        [
            ListItem(Paragraph(item, style), leftIndent=0)
            for item in items
        ],
        bulletType="bullet",
        start="circle",
        bulletColor=bullet_color,
        leftIndent=10,
        bulletFontSize=7,
        bulletOffsetY=1,
        spaceBefore=0,
        spaceAfter=0,
    )


def section(title, body, styles):
    heading = Paragraph(title, styles["app_section"])
    return [heading, Spacer(1, 1.6 * mm), body]


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Kabir Fashions App Summary",
        author="OpenAI Codex",
    )

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="app_title",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=22,
            textColor=colors.HexColor("#6B3E2E"),
            spaceAfter=3 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="app_subtitle",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=10,
            textColor=colors.HexColor("#6B7280"),
            spaceAfter=4 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="app_section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=11,
            textColor=colors.HexColor("#6B3E2E"),
            spaceAfter=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="app_body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.3,
            leading=10.2,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="app_bullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.1,
            leading=9.6,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="app_small",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.4,
            leading=8.8,
            textColor=colors.HexColor("#374151"),
        )
    )

    what_it_is = Paragraph(
        "Kabir Fashions is a static clothing catalogue website for an Ahmedabad-based apparel business. "
        "It presents products, brand information, and contact paths for enquiries without accounts, checkout, or a custom backend.",
        styles["app_body"],
    )

    who_its_for = Paragraph(
        "Primary persona: clothing shoppers or wholesale/bulk enquiry customers who want to browse collections quickly and contact the business directly.",
        styles["app_body"],
    )

    features = bullet_list(
        [
            "Homepage hero and collection preview with direct calls to action.",
            "Product catalogue browsing across kurta, co-ord set, and 3 piece set categories.",
            "Client-side category filtering driven by <font name='Courier'>js/filter.js</font>.",
            "Individual product detail page with CSS-only image gallery panels and size options.",
            "Direct WhatsApp enquiry links on catalogue, detail, and contact surfaces.",
            "Contact page with AJAX form submission to Formspree and success-state handling.",
            "Responsive multi-page layout with shared navigation, footer, and scroll reveal animations.",
        ],
        styles["app_bullet"],
        colors.HexColor("#B16F55"),
    )

    architecture = bullet_list(
        [
            "Pages: root <font name='Courier'>index.html</font> plus <font name='Courier'>home/</font>, <font name='Courier'>about/</font>, <font name='Courier'>contact/</font>, and <font name='Courier'>product-detail/</font> HTML entry points; <font name='Courier'>home/products/</font> redirects to <font name='Courier'>/home/</font> using <font name='Courier'>sessionStorage</font>.",
            "Presentation layer: shared CSS files in <font name='Courier'>css/</font> for global layout, navbar, footer, product cards, responsive breakpoints, and animations.",
            "Client behavior: <font name='Courier'>js/filter.js</font> shows or hides product cards by normalized category text; <font name='Courier'>js/scroll-reveal.js</font> uses <font name='Courier'>IntersectionObserver</font> to reveal elements once in view.",
            "External services: Google Analytics tag on pages, Formspree endpoint on the contact form, WhatsApp deep links for enquiries, and embedded Google Maps/location links.",
            "Deployment/routing evidence: <font name='Courier'>vercel.json</font> enables clean URLs and trailing slashes; README also documents GitHub Pages deployment. Exact production hosting source is mixed in repo evidence.",
        ],
        styles["app_bullet"],
        colors.HexColor("#B16F55"),
    )

    run_steps = bullet_list(
        [
            "Open the repo folder. No package manager, build tool, or environment variables are defined in repo evidence.",
            "Launch <font name='Courier'>index.html</font> in a modern browser for the landing page, or open <font name='Courier'>home/index.html</font> directly for the main multi-page site shell.",
            "Optional: serve the folder with any static file server if you want cleaner local navigation behavior.",
        ],
        styles["app_bullet"],
        colors.HexColor("#B16F55"),
    )

    evidence_note = Paragraph(
        "Evidence basis: README, HTML entry pages, <font name='Courier'>js/filter.js</font>, <font name='Courier'>js/scroll-reveal.js</font>, and <font name='Courier'>vercel.json</font>.",
        styles["app_small"],
    )

    left = []
    left.append(Paragraph("Kabir Fashions App Summary", styles["app_title"]))
    left.append(Paragraph("One-page repo-based overview", styles["app_subtitle"]))
    left.extend(section("What It Is", what_it_is, styles))
    left.append(Spacer(1, 3 * mm))
    left.extend(section("Who It's For", who_its_for, styles))
    left.append(Spacer(1, 3 * mm))
    left.extend(section("What It Does", features, styles))

    right = []
    right.extend(section("How It Works", architecture, styles))
    right.append(Spacer(1, 3 * mm))
    right.extend(section("How To Run", run_steps, styles))
    right.append(Spacer(1, 4 * mm))
    right.append(evidence_note)

    table = Table(
        [[left, right]],
        colWidths=[88 * mm, 88 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LINEAFTER", (0, 0), (0, 0), 0.4, colors.HexColor("#D1D5DB")),
            ]
        )
    )

    story = [table]
    doc.build(story)
    return OUTPUT


if __name__ == "__main__":
    print(build_pdf())
