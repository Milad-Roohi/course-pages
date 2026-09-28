# MP09 Instructor Theme Summary

**Course**: MECH 223 Engineering Statics Fall 2026  
**Canvas Course**: 20760  
**Quiz**: Muddiest Point 09 — W5 Wed Sep 23  
**Quiz ID**: 310034  
**Date**: Wednesday, Sep 23, 2026  
**Context**: Exam 1 week / freeze week review  
**Responses**: 31 with text (31 submissions total)  

---

## Theme Clusters

### 1. λ (lambda) / 3D Unit Vectors / Getting to λ (n=3)

**Student concerns**: How to find lambda, understanding the 3D unit vector, the process of "getting to lambda" from two points.

**Responses mentioning**:
- Response 15: "getting to lambda"
- Response 17: "Finding lambda"  
- Response 27 (partial): mentions "lambda"

**Study guide section**: Section 1 — comprehensive walkthrough of:
- What λ is (direction cosines, Beer Eq. 2.19, 2.21-22, 2.24)
- Step-by-step method from two points (Beer Eq. 2.27)
- Worked example: A(2,3,0) to B(5,7,6)
- Interactive 3D Plotly visualization
- Check: λ_x² + λ_y² + λ_z² = 1

---

### 2. Springs / Tension in Exam-Style Problems (n=2)

**Student concerns**: Incorporating springs into equations, distinguishing spring force from tension.

**Responses mentioning**:
- Response 3: "I had some difficulty incorporating the spring into the equation during the exam question"
- Response 19 (partial): "The Tension and spring problems make sense now that you've spent time in"

**Study guide section**: Section 2 — covers:
- Hooke's law: F_spring = k·ΔL
- Tension (unknown, T≥0) vs. spring (F=k·ΔL, known if ΔL known)
- Worked example: 5 kg block on spring, k=200 N/m
- Common mistake: confusing ΔL (change) with L (final length)

---

### 3. Systems of Two Simultaneous Equations (n=1)

**Student concern**: Never had simultaneous equations explained in an understandable way.

**Response mentioning**:
- Response 25: "systems of equations and solving two equations at the same time has never been really explained to me in an understandable way before"

**Study guide section**: Section 3 — includes:
- Why you need two equations (2D equilibrium → 2 unknowns)
- Substitution method (step-by-step)
- Elimination method (mentioned)
- Worked example: 100 N weight, two cables at 30° and 60°
- Check procedure

---

### 4. Visualizing z / Diagrams → Equations; ΣFx ΣFy Components (n=2-3)

**Student concerns**: Visualizing the z-plane, turning diagrams into component equations, knowing what to put in ΣFx and ΣFy.

**Responses mentioning**:
- Response 21: "I think it was knowing exactly what to put in when calculating sum of the forces in the x direction and y direction."
- Response 26 (partial): "The muddiest points for me were how to analyze the diagram displayed, represent it into wo"
- Response 27: "It would have to be solving and visualizing the z planes and lambda."

**Study guide section**: Section 4 — addresses:
- Visualizing +z (out of page, right-hand rule)
- Diagram → equations step list (FBD → vector form → sum components → solve)
- Worked example: 3D particle with three cables
- Interactive 3D Plotly visualization showing forces in 3D space

---

### 5. Equation / Explanation Sheet from Class (n=2)

**Student request**: Post the equation/explanation sheet reviewed in class.

**Responses mentioning**:
- Response 2: "Could you please post the sheet of explanations that we reviewed during class today?"
- Response 12: "nothing seemed really muddy to me. I just had a question if you could post the equation sheet on canvas"

**Action**: Noted prominently on study guide page with instruction that equation sheet is posted on Canvas (Files or course home page). Instructor handles Canvas posting separately.

---

### 6. Clear / No Muddy Point (n≈17)

**Student feedback**: Lecture was clear, review was helpful, no confusion.

**Representative responses**:
- Response 1: "There were no muddy points in class today"
- Response 5: "I thought this lecture was very clear."
- Response 9: "There was no muddy point, I appreciated the review greatly."
- Response 11: "There was no muddiest point, thank you for working through problems!"
- Response 20: "Todays lecture was very clear, I really liked walking through problems."
- Response 28: "This was a good lecture."
- Response 29: "No muddiest point today. Everything was clear"
- Response 31: "there were no muddy points today, everything went well."
- Plus responses 6, 7, 8, 10, 13, 14, 18, 22, 30 (partial/cut off)

**Count**: Approximately 17 of 31 responses (55%) indicated clarity.

**Note**: Acknowledged on study guide page. Remaining 45% had specific questions addressed in Sections 1-4.

---

## Additional Context

### Partial/Cut-off Responses
Some responses appear truncated (likely character limit):
- Response 19: "...that you've spent time in" (incomplete)
- Response 23: "...which makes it easy to" (incomplete)
- Response 24: "If the 2 cables didn't have the same m" (incomplete)
- Response 26: "...represent it into wo" (incomplete)
- Response 30: "Todays lecture was very helpful b" (incomplete)

These were interpreted based on context and clustered appropriately.

---

## Study Guide Deployment

### File Location
- Source: `mech223/2026/mp09/index.html`
- GitHub Pages URL: `https://milad-roohi.github.io/course-pages/mech223/2026/mp09/`
- PR: #1 on `cursor/mp09-study-guide-32c4` branch

### Canvas Embedding
Instructor uses `tools/publish.py`:

```bash
python3 tools/publish.py \
  --src mech223/2026/mp09/index.html \
  --course mech223 --year 2026 --slug mp09 \
  --canvas-course 20760 \
  --title "Muddiest Point 09 study guide (Wed Sep 23)" \
  --module "Week 5" \
  --publish
```

This:
1. Copies to `mech223/2026/mp09/index.html` (if changed)
2. Commits and pushes to GitHub
3. Waits for GitHub Pages rebuild (~2 min)
4. Creates/updates Canvas Page with iframe embed
5. Adds to "Week 5" module

---

## Content Quality Notes

### What's Included
- 4 major sections addressing all non-clear themes
- Interactive 3D Plotly visualizations (2 plots)
- Worked examples for every concept
- Step-by-step procedures in styled boxes
- Final exam tips checklist
- KaTeX math rendering throughout
- Responsive design (mobile, tablet, desktop, print)

### What's NOT Included (per privacy requirements)
- Student names
- Verbatim student quotes on public page (themes summarized only)
- Raw response data
- This instructor summary (kept separate, not published to Pages)

### Design Consistency
- Matches mp08 quality and structure
- Nebraska red (#b31b1b) accent color
- Latin Modern fonts
- Same CSS variables and layout
- Professional academic presentation

---

## Follow-Up Actions for Instructor

1. ✅ Merge PR #1 to deploy to GitHub Pages
2. ⏳ Wait ~2 min for Pages rebuild
3. ⏳ Run `tools/publish.py` to embed in Canvas
4. ⏳ Verify Canvas iframe displays correctly
5. ⏳ Confirm equation sheet is posted separately to Canvas Files

---

**Document prepared**: Sep 28, 2026  
**Study guide built from**: 31 anonymous MP09 responses  
**Privacy compliance**: ✓ No student data on public Pages  
**Ready for deployment**: ✓ Yes
