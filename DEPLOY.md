# Deploying this site to jiehou-lab.github.io

## How the Markdown becomes web pages

You do not build anything. **GitHub Pages runs Jekyll on its own servers.** When you push, GitHub reads
`_config.yml`, wraps every `.md` file in `_layouts/default.html`, converts the Markdown to HTML, and publishes
the result. The `.md` files in this repo are the *source*; the HTML is generated on GitHub every time you push.

This is the same setup as <https://badriadhikari.github.io/ccsc-workshop-2026/> — that site is also Markdown in
a repo, not hand-written HTML.

## Why a separate repo, not a folder inside `jiehou-lab.github.io`

Your `jiehou-lab.github.io` repo is a plain HTML site — `index.html`, `css/`, `js/`, no Jekyll. Dropping a
Jekyll site into a subfolder of it does not work: GitHub only reads **one** `_config.yml`, at the repo root, so
a nested `_config.yml` is ignored and your layouts and nav would never load.

Use a project repo instead. That is exactly what the CCSC workshop site does.

| | Repo | Published at |
|---|---|---|
| Your homepage (already live) | `jiehou-lab/jiehou-lab.github.io` | `https://jiehou-lab.github.io/` |
| This course site | `jiehou-lab/urban-ai` | `https://jiehou-lab.github.io/urban-ai/` |

Both live under `jiehou-lab.github.io`. They do not interfere with each other.

## Publish it

```bash
# 1. On github.com, create a new PUBLIC repo named exactly:  urban-ai
#    Do not add a README, .gitignore, or license — this folder already has them.

# 2. From this folder:
git init -b main
git add .
git commit -m "Urban AI course site, syllabus, labs, and materials"
git remote add origin https://github.com/jiehou-lab/urban-ai.git
git push -u origin main
```

Then: **repo → Settings → Pages → Source: _Deploy from a branch_ → Branch `main`, folder `/ (root)` → Save.**

Wait about a minute. The site is live at <https://jiehou-lab.github.io/urban-ai/>.

Every later change is just `git add . && git commit -m "..." && git push` — the site rebuilds in under a minute.

### If you name the repo something else

Change one line in `_config.yml` to match, with a leading slash:

```yaml
baseurl: "/whatever-you-named-it"
```

Everything else adjusts automatically, because every internal link uses `relative_url`.

## Link it from your homepage

Paste this into `index.html` in your `jiehou-lab.github.io` repo, wherever your teaching or projects section is:

```html
<a href="https://jiehou-lab.github.io/urban-ai/">
  Urban AI: AI-Driven Decision Support for Real-World Urban Challenges
</a>
<span>— 20-hour online non-credit course, MSU AI-Ready Initiative</span>
```

## Editing after it is live

- **Text change** — edit the `.md` file on github.com (pencil icon), commit. Live in ~1 minute.
- **New page** — add a `.md` file with front matter (`layout: default`, `title:`, `permalink:`), then add one
  line to `nav:` in `_config.yml`.
- **Schedule, dates, links** — `_config.yml` for cohort dates and the D2L/Zoom/registration URLs;
  `schedule.md` for the meeting-by-meeting detail.
- **Structural change** — edit `COURSE_SPEC.md` first. It is the source of truth that keeps the site, the
  syllabus, and the grant report from drifting apart.

## Still to replace before you announce it

| What | Where |
|---|---|
| Registration form URL | `_config.yml` → `register_url` |
| D2L Brightspace URL | `_config.yml` → `d2l_url` |
| Live session (Zoom) URL | `_config.yml` → `zoom_url` |
| Confirmed cohort dates | `_config.yml` → `cohort_dates`, and `schedule.md` |
| TA full names | `team.md`, class and lab pages |
| Instructor photos | `team.md` — add images to `assets/img/`, swap the `<div class="avatar">` for `<img ... alt="...">` |
| Approved AI tool list | keep it in D2L, link from `responsible-ai.md` |

Find anything still outstanding:

```bash
grep -rn "TBD\|tentative\|\"#\"" _config.yml *.md classes/ labs/
```

## Preview locally (optional)

You do not need this — pushing is the fastest way to see the site. But if you want a local preview:

```bash
bundle install
bundle exec jekyll serve
# → http://127.0.0.1:4000/urban-ai/
```

## Troubleshooting

**Site is live but has no styling.** `baseurl` does not match the repo name. It must be `/urban-ai` exactly —
leading slash, no trailing slash.

**404 after enabling Pages.** Give it two minutes, then check the repo's **Actions** tab for the
`pages build and deployment` run. A red X there shows the build error.

**A page is blank or shows raw text.** The front matter block at the top is malformed — it must be exactly
three dashes, the YAML, then three dashes, with no blank line before the first `---`.

**Markdown inside a `<div>` renders as one paragraph.** Jekyll's Markdown parser does not process Markdown
inside raw HTML blocks. Write plain HTML (`<ul><li>`) inside HTML containers, or add `markdown="1"` to the div.
