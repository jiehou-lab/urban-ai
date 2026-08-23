# Urban AI — course website and materials

Course site, syllabus, slide decks, student templates, and lab notebooks for
**Urban AI: AI-Driven Decision Support for Real-World Urban Challenges** — a 20-hour online, non-credit
learning experience at Michigan State University (MSU AI-Ready Initiative, Category 3).

The site is a plain [Jekyll](https://jekyllrb.com/) site served by GitHub Pages. No theme gem, no build step,
no JavaScript framework. Edit Markdown, push, done.

---

## Publish it in five minutes

1. **Create the repo.** On GitHub, create a public repository named `urban-ai` under your account.
2. **Push these files** to the `main` branch (this folder is the repo root).
3. **Fix the two placeholder lines** in `_config.yml`:

   ```yaml
   url:     "https://YOUR-GITHUB-USERNAME.github.io"
   baseurl: "/urban-ai"          # must match the repo name, with a leading slash
   ```

   If you name the repo something else, `baseurl` must match it. If you publish at
   `YOUR-USERNAME.github.io` (a user site, not a project site), set `baseurl: ""`.
4. **Enable Pages.** Repo → Settings → Pages → Source: *Deploy from a branch* → Branch: `main`, folder `/ (root)` → Save.
5. Wait about a minute. The site is live at `https://YOUR-GITHUB-USERNAME.github.io/urban-ai/`.

### Then replace the remaining placeholders

Search the repo for these strings and replace all occurrences:

| Placeholder | Where | Replace with |
|---|---|---|
| `jiehou-lab` | `_config.yml`, lab pages, notebook Colab badges | your GitHub username |
| `site.course.register_url` | `_config.yml` | registration form URL |
| `site.course.d2l_url` | `_config.yml` | D2L Brightspace course URL |
| `site.course.zoom_url` | `_config.yml` | live session link |
| Cohort dates | `_config.yml`, `schedule.md` | confirmed dates |
| TA names | `_config.yml`, `team.md`, class/lab pages | full names |
| Instructor photos | `team.md` | `<img src="{{ '/assets/img/name.jpg' | relative_url }}" alt="...">` |

One command finds them all:

```bash
grep -rn "jiehou-lab\|TBD\|tentative" . --include="*.md" --include="*.yml" --include="*.ipynb"
```

---

## Run it locally (optional)

```bash
bundle install
bundle exec jekyll serve --livereload
# → http://127.0.0.1:4000/urban-ai/
```

Requires Ruby 3.x. If `bundle install` fails on `github-pages`, you can develop against plain Jekyll instead
(`gem install jekyll` then `jekyll serve`); GitHub Pages will still build the deployed site correctly.

---

## Repository layout

```
.
├── _config.yml                 site settings, nav, course metadata  ← edit this first
├── _layouts/default.html       the single page layout
├── assets/
│   ├── css/style.css           all styling (light + dark, responsive, print)
│   ├── slides/                 8 starter decks, one per class
│   ├── templates/              student templates + facilitator guide
│   └── Urban_AI_Syllabus.docx  full syllabus
├── index.md                    home
├── schedule.md                 8 meetings + hour accounting + meeting run-of-show
├── classes/                    8 class pages + index
├── labs/                       8 lab pages + index (Track A / Track B)
├── deliverables.md             the six deliverables + rubric
├── responsible-ai.md           course AI policy
├── resources.md                templates, notebooks, real data sources
├── team.md                     instructors and TAs
├── notebooks/                  8 Colab notebooks (Track B)
└── COURSE_SPEC.md              canonical design spec — the source of truth
```

## Editing conventions

- **`COURSE_SPEC.md` is the source of truth.** If you change hours, titles, or deliverables, change it there
  first, then propagate to `schedule.md`, the class/lab pages, and the syllabus. That file exists so the site,
  the syllabus, and the grant report never drift apart.
- **Class and lab pages are generated** by `build_site_pages.py` (kept at the top level of the materials bundle,
  not in the repo). Small edits are fine to make directly in the Markdown; large restructures are easier in the
  generator.
- **Every page uses `relative_url`** for internal links. Keep it that way or links break under `baseurl`.
- **Nav lives in `_config.yml`** under `nav:`. Adding a page means adding a Markdown file with front matter and
  one line in that list.

## Accessibility

The site is built to WCAG 2.1 AA intent: semantic headings, a skip link, visible focus rings, 4.5:1 text
contrast in both light and dark modes, no color-only meaning, responsive to 320px, and a print stylesheet.
When you add images, add real `alt` text. When you add tables, keep a `<thead>`.

## License and reuse

Course materials are shared for educational use. Adapt them for your own institution — the structure
(two-track labs, AI use log, audit worksheet, scenario matrix, decision brief) transfers to any domain where
students need to use AI critically rather than credulously.
