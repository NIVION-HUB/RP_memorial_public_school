# Clone Univet Blue Theme — Implementation Plan

## Site Architecture (All Local, Zero External Dependencies)

```
rp memorial school/
├── index.html              (Homepage)
├── about.html
├── admission.html
├── streams.html
├── facilities.html
├── gallery.html
├── contact.html
├── assets/
│   ├── css/
│   │   ├── fonts.css       (Local @font-face declarations)
│   │   └── style.css       (All styles)
│   ├── js/
│   │   └── main.js         (All interactivity)
│   ├── fonts/              (Downloaded .woff2 files)
│   └── images/             (Generated via AI tool)
└── previousimage/          (Existing folder, untouched)
```

---

## Sections to Clone (Top → Bottom from Screenshots)

| # | Section | Key Details |
|---|---------|------------|
| 1 | **Header/Navbar** | Sticky. Logo left ("UNIVERSITY OF UNIVET" + shield icon). Nav: Home, About Us, Pages, Academics, Blog, Contact. Right: Search icon, Hamburger, yellow "Apply Now" pill button. White text on transparent → solid navy on scroll. |
| 2 | **Hero Banner** | Full-width. University building photo bg. Giant faded "UNIVET" watermark text behind building. Subtitle: "Welcome to Univet University". Title: "Leading the Way in Higher Education". Play button for "Campus Tour" on right side. |
| 3 | **Academics & Programs** | Beige/cream bg (`#f6f4ee`). Tag: "Programs & Study". Title: "Academics & Programs". 3 cards in a row (Faculty of Law, Faculty of Science, Faculty of Engineering) with icons, text, yellow chevron expand button. Graduation cap illustration top-right. |
| 4 | **About Section** | Two stacked rounded-corner photos on left. Right: Tag "About Your University", Title "Empowering Students to Lead the Future", paragraph text, 3 checkmarks (World-Class Education, Global Internships, Modern Campus). Dark navy card "50+ Award Winning". "More About Us" button. |
| 5 | **Inside Univet (Tabbed)** | Dark navy bg rounded container. Tab filters: Academic Faculty, Faculty Program, Research. Left card: Shield icon, student avatars, "4558+ Admission", yellow "APPLY NOW" button. Right: 2×2 grid of faculty image cards (Education, Law, Social Sciences, Engineering). Bottom-left: white Notice board card with 3 notices + dates. |
| 6 | **Marquee/Ticker** | Horizontal scrolling gold text: "2024 BEST 10 UNIVERSITY AWARDS" with laurel icons. |
| 7 | **Events Section** | Cream bg. Tag: "Upcoming Events". Title: "Join Our Latest Events". "View More Events" button top-right. 2×2 grid of event cards (image left, date/time/title/location right). |
| 8 | **Vice-Chancellor Message** | Dark navy bg. Video thumbnail with play button left. Quote text right. Name: "Jackson David", Title: "Vice-chancellor". Signature image. "Read More" yellow pill button. |
| 9 | **Parallax Banner** | Full-width building photo with parallax scroll effect. |
| 10 | **Campus Life** | Cream bg. Tag: "Experience Campus Life". Title: "Univet Campus Life Where Learning Meets Living". Description paragraph right with left gold border. 3 large rounded portrait-orientation photos below (graduates, students on lawn, students reading). |
| 11 | **CTA Section** | Gradient navy-to-teal bg. Tag: "Interested?". Title: "Want to learn more about Univet University?". Description. Yellow "LEARN MORE UNIVET UNIVERSITY" button. Right side: scrolling horizontal photo strip. |
| 12 | **Footer** | Dark navy bg. Logo + description + Email/Phone. Columns: "Our Campus" links, "Useful Links" links, "Newsletter" email subscribe form with yellow submit button. Bottom bar: copyright text, social media icons. |

---

## Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| `--navy` | `#0b2545` | Primary dark bg, headings |
| `--gold` | `#d4a843` / `#e8b84b` | Accent buttons, tags, highlights |
| `--cream` | `#f6f4ee` | Page background |
| `--white` | `#ffffff` | Cards, text on dark |
| `--text-dark` | `#1a1a2e` | Body text |
| `--text-muted` | `#6b7280` | Secondary text |

## Fonts (Download locally)
- **Bitter** — Headings (serif)
- **Inter** — Body (sans-serif)
- **Maitree** — Decorative/quotes (serif)

---

## Execution Plan (Token-Efficient Order)

### Phase 1: Foundation
1. Download fonts locally via Python script
2. Create `assets/css/fonts.css`
3. Create `assets/css/style.css` (full design system + all section styles)
4. Create `assets/js/main.js`

### Phase 2: Generate Images
5. Generate hero building image
6. Generate student/campus images for cards (about, faculties, events, campus life)

### Phase 3: Build Pages
7. Create `index.html` (homepage with all 12 sections above)
8. Create `about.html`, `admission.html`, `streams.html`, `facilities.html`, `gallery.html`, `contact.html`

### Phase 4: Verify
9. Run local server, test all pages, check no external requests

---

## Open Questions

> [!IMPORTANT]
> Should I adapt all the content text to be about **RP Memorial School** (your school) instead of "Univet University"? Or do you want the exact same text as the Univet site for now and customize later?
