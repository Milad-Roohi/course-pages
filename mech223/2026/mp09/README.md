# MECH 223 MP09 Study Guide

**Muddiest Point 09** — Wednesday, Sep 23, 2026  
**Exam 1 week review / freeze week**

---

## Files

- **`index.html`** — Main study guide (public, GitHub Pages)
- **`instructor-themes-summary.md`** — Theme analysis and deployment notes (private, instructor reference)
- **`README.md`** — This file

---

## Deployment Status

### Branch
- Feature branch: `cursor/mp09-study-guide-32c4`
- Pull request: [#1](https://github.com/Milad-Roohi/course-pages/pull/1)
- Status: Ready for merge

### GitHub Pages URL (after merge)
`https://milad-roohi.github.io/course-pages/mech223/2026/mp09/`

### Canvas Embedding
After merge, run:

```bash
python3 tools/publish.py --src mech223/2026/mp09/index.html \
  --course mech223 --year 2026 --slug mp09 \
  --canvas-course 20760 \
  --title "Muddiest Point 09 study guide (Wed Sep 23)" \
  --module "Week 5" --publish
```

---

## Content Summary

### Student Response Analysis
- **Total responses**: 31 (all with text)
- **Quiz ID**: 310034
- **Canvas course**: 20760

### Theme Clusters
1. **λ (lambda) / 3D unit vectors** (n=3) → Section 1
2. **Springs & tension** (n=2) → Section 2
3. **Simultaneous equations** (n=1) → Section 3
4. **Visualizing z / diagram → equations** (n=2-3) → Section 4
5. **Equation sheet** (n=2) → noted, posted to Canvas
6. **Clear / no muddy point** (n≈17) → acknowledged

### Interactive Features
- **2 Plotly 3D visualizations**
  - Lambda unit vector (A to B in 3D)
  - 3D particle equilibrium with cables
- Drag to rotate, scroll to zoom, responsive
- Print-friendly fallbacks

### Math Rendering
- **KaTeX** for LaTeX math
- 18 display equations (`\[ ... \]`)
- 94 inline math expressions (`\( ... \)`)
- 5 Beer textbook references (Eq. 2.19, 2.21-22, 2.24, 2.27)

---

## Quality Checks

✅ **HTML Structure**
- Valid HTML5 doctype
- Proper closing tags
- Robots meta tag present (`noindex, nofollow`)

✅ **Design Consistency**
- Matches mp08 pattern
- Latin Modern fonts
- Nebraska red accent (#b31b1b)
- Responsive CSS (mobile, tablet, desktop, print)

✅ **Privacy Compliance**
- No student names on public page
- No verbatim quotes on public page
- Themes summarized only
- Raw response data NOT in repo

✅ **Dependencies**
- KaTeX 0.16.22 (CDN)
- Plotly.js 2.36.0 (CDN)
- Latin Modern fonts 5.2.5 (CDN)

✅ **File Size**
- 519 lines
- 24 KB (reasonable for GitHub Pages)

---

## Technical Details

### Page Structure
1. Kicker (course, context)
2. Title + subtitle
3. Introduction
4. Snapshot table (themes, counts)
5. Summary of student feedback
6. 4 content sections (λ, springs, equations, 3D viz)
7. Final exam tips
8. Footer

### JavaScript
- Auto-render KaTeX on page load
- Two Plotly 3D plots with camera controls
- No external dependencies beyond CDNs

### Accessibility
- Semantic HTML
- ARIA labels on interactive plots
- Print-friendly CSS

---

## Next Steps

1. ✅ PR created ([#1](https://github.com/Milad-Roohi/course-pages/pull/1))
2. ⏳ Review PR
3. ⏳ Merge to `main`
4. ⏳ Wait for GitHub Pages rebuild (~2 min)
5. ⏳ Run `tools/publish.py` to embed in Canvas
6. ⏳ Verify Canvas iframe works
7. ⏳ Confirm Week 5 module shows page

---

**Created**: Sep 28, 2026  
**Ready**: Yes  
**Live URL**: Pending merge
