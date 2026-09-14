# Urban AI — course website and materials

**Live site: <https://jiehou-lab.github.io/urban-ai/>**

Course site, syllabus, slide decks, student templates, and lab notebooks for
**Urban AI: AI-Driven Decision Support for Real-World Urban Challenges** — a 20-hour online, non-credit
learning experience at Michigan State University (MSU AI-Ready Initiative, Category 3).

- **PI:** Si Chen, Ph.D. — School of Planning, Design and Construction
- **Co-PI:** Jie Hou, Ph.D. — Computational Mathematics, Science and Engineering
- **Teaching assistants:** Sean (analytics labs) · Yura (decision-support labs)

The site is a plain [Jekyll](https://jekyllrb.com/) site served by GitHub Pages. There is no theme gem, no
build step, and no JavaScript framework. **GitHub builds the site for you**: you push Markdown, and GitHub
runs Jekyll on its servers to produce the HTML. The `.md` files are the source; the HTML never lives in this
repo.

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
├── build_site_pages.py         regenerates the class/lab pages
├── COURSE_SPEC.md              canonical design spec — the source of truth
└── DEPLOY.md                   GitHub Pages hosting details
```

---

## Everyday workflow

This is all you need once setup is done. Run it from the repo folder:

```bash
cd ~/Documents/msu/Projects/Funding_proposal/2026_MSU_edu_ai/course_designs/website
```

**1. Pull before you start.** Always. It costs a second and prevents the most common conflict.

```bash
git pull
```

**2. Edit files.** Any `.md` file, `_config.yml`, or anything under `assets/`.

**3. See what you changed.**

```bash
git status              # which files changed
git diff                # what changed inside them
```

**4. Stage, commit, push.**

```bash
git add -A
git commit -m "Update cohort dates and TA names"
git push
```

The site rebuilds automatically. Give it 30–90 seconds, then hard-refresh (**⌘⇧R**) — your browser caches
aggressively and will happily show you the old page.

**Watch the build:** the repo's **Actions** tab shows a run called *pages build and deployment*.
Green check = published. Red X = a Jekyll error; click into it to read the log.

### Small text edits without touching your computer

For a typo or a date change, edit right on github.com: open the file, click the **pencil** icon, edit, then
**Commit changes**. Same result, same rebuild. Just remember to `git pull` next time you work locally, or
your next push will be rejected.

---

## One-time setup on a new computer

Two ways to authenticate with GitHub. **GitHub does not accept your account password for git operations** —
that was disabled in 2021. You need either an SSH key or a Personal Access Token.

### Option A — SSH key (recommended: set once, never expires)

```bash
# 1. Create a key dedicated to GitHub. Press Enter at BOTH passphrase prompts
#    (an empty passphrase is what you want for a key that only pushes to your own repos).
ssh-keygen -t ed25519 -C "github-jiehou-lab" -f ~/.ssh/id_ed25519_github

# 2. Print the PUBLIC key — the file ending in .pub
cat ~/.ssh/id_ed25519_github.pub
```

Copy the whole single line (starts with `ssh-ed25519`, ends with the comment). On GitHub:
**avatar → Settings → SSH and GPG keys → New SSH key** → Key type **Authentication Key** → paste →
**Add SSH key**.

> Never paste `~/.ssh/id_ed25519_github` (no `.pub`). That is the **private** key — it starts with
> `-----BEGIN OPENSSH PRIVATE KEY-----`. If it ever leaves your machine, delete both files and make a new pair.

```bash
# 3. Tell SSH to use this key for GitHub specifically.
cat >> ~/.ssh/config <<'EOF'

Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github
  IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config

# 4. Verify BEFORE trying to push.
ssh -T git@github.com
# want: "Hi jiehou-lab! You've successfully authenticated, but GitHub does not provide shell access."
```

`IdentitiesOnly yes` matters. Without it, SSH offers every key in `~/.ssh` in turn — including older
passphrase-protected ones — and you get stuck at a passphrase prompt for a key you don't remember.

### Option B — Personal Access Token (HTTPS)

**avatar → Settings → Developer settings** (bottom of the left sidebar) **→ Personal access tokens →
Fine-grained tokens → Generate new token**:

| Field | Value |
|---|---|
| Token name | `urban-ai push` |
| Expiration | 90 days (you will have to redo this) |
| Resource owner | `jiehou-lab` |
| Repository access | **Only select repositories** → `urban-ai` |
| Repository permissions | **Contents → Read and write** ← required; without it the push fails with 403 |

Generate and copy the token — it starts `github_pat_` and is shown **once**.

```bash
git remote set-url origin https://github.com/jiehou-lab/urban-ai.git
git config --global credential.helper osxkeychain    # so you type it only once
git push
# Username: jiehou-lab
# Password: paste the token  (nothing appears while pasting — that is normal)
```

If it still rejects a correct token, macOS is handing git an old cached password:

```bash
printf "protocol=https\nhost=github.com\n\n" | git credential-osxkeychain erase
```

### Cloning this repo somewhere new

```bash
git clone git@github.com:jiehou-lab/urban-ai.git          # SSH
git clone https://github.com/jiehou-lab/urban-ai.git      # HTTPS + token
```

### How this repo was first created

For reference, the sequence that produced it:

```bash
cd website
git init -b main
git add -A
git commit -m "Urban AI course site and materials"
# create an EMPTY repo named urban-ai at github.com/new — no README, no .gitignore, no license
git remote add origin git@github.com:jiehou-lab/urban-ai.git
git push -u origin main
```

Then **Settings → Pages → Deploy from a branch → `main` / `(root)` → Save**.
See [DEPLOY.md](DEPLOY.md) for the hosting details.

---

## Troubleshooting

Every one of these came up while setting this repo up.

**`Password authentication is not supported for Git operations`**
Your account password will never work. Use an SSH key or a token — see the setup section above.

**`Permission denied (publickey)`**
Your public key is not on your GitHub account, or SSH is offering the wrong key. Run
`ssh -T git@github.com` to test in isolation, and confirm `~/.ssh/config` has `IdentitiesOnly yes`.

**`Enter passphrase for key` / `Bad passphrase, try again`**
That key has a passphrase you don't have. Don't overwrite the key — it may belong to another server. Make a
**separate** GitHub key with an empty passphrase, as in Option A.

**`error: remote origin already exists`**
`origin` is already set. Use `git remote set-url origin <url>` instead of `git remote add`.
Check what you're on with `git remote -v`.

**`! [rejected] main -> main (fetch first)`**
The remote has commits you don't. Normally the fix is `git pull` then `git push`. But if this happened on
your very first push because GitHub created the repo with a README, the two histories are unrelated and
`git pull` will refuse them (`fatal: refusing to merge unrelated histories`). In that one case, overwrite the
remote's placeholder commit:

```bash
git push -u origin main --force
```

Only ever do this on a first push. Once the site is live and others may have cloned it, `--force` destroys
their work.

**`There isn't a GitHub Pages site here` (404)**
Pages is not enabled. **Settings → Pages** → Source **Deploy from a branch**, Branch **`main`**, folder
**`/ (root)`**, then click **Save**. The dropdowns alone do nothing — the Save button is the step people miss.
Confirm it took: a **github-pages** entry appears under *Environments* on the repo home page.

**Site loads but has no styling**
`baseurl` in `_config.yml` doesn't match the repo name. It must be `/urban-ai` — leading slash, no trailing
slash. If you rename the repo, change this too.

**A page renders as raw text, or shows `{{ }}` / `{% %}`**
The front matter block at the top is malformed. It must be exactly three dashes, the YAML, three dashes, with
no blank line before the first `---`.

**Markdown inside a `<div>` collapses into one paragraph**
Jekyll does not process Markdown inside raw HTML blocks. Write plain HTML (`<ul><li>`) inside HTML
containers, or add `markdown="1"` to the div.

**`Unable to create index.lock: File exists`**
Only happens if git was run against this folder through the Claude Cowork device bridge, which cannot delete
lock files. Remove them and carry on:

```bash
rm -f .git/index.lock .git/HEAD.lock
find .git/objects -name 'tmp_obj_*' -delete
```

---

## Editing conventions

- **`COURSE_SPEC.md` is the source of truth.** Change hours, titles, or deliverables there first, then
  propagate to `schedule.md`, the class and lab pages, and the syllabus. That file exists so the site, the
  syllabus, and the grant report never drift apart.
- **Class and lab pages are generated** by `build_site_pages.py`. Small edits directly in the Markdown are
  fine; large restructures are easier in the generator. Note that rerunning it overwrites manual edits.
- **Every internal link uses `relative_url`.** Keep it that way or links break under `baseurl`.
- **Nav lives in `_config.yml`** under `nav:`. A new page means a Markdown file with front matter
  (`layout: default`, `title:`, `permalink:`) plus one line in that list.
- **Commit messages:** say what changed, not "update". `Add Fall 2026 cohort dates` beats `changes`.

## Still to fill in

| What | Where |
|---|---|
| Registration form URL | `_config.yml` → `register_url` (currently `"#"`) |
| D2L Brightspace URL | `_config.yml` → `d2l_url` (currently `"#"`) |
| Live session / Zoom URL | `_config.yml` → `zoom_url` (currently `"#"`) |
| Confirmed cohort dates | `_config.yml` → `cohort_dates`, and `schedule.md` |
| TA full names | `team.md`, plus the class and lab pages |
| Instructor photos | `team.md` — add images to `assets/img/`, swap `<div class="avatar">` for `<img ... alt="...">` |
| Approved AI tool list | keep it in D2L; link to it from `responsible-ai.md` |

Find what's outstanding:

```bash
grep -rn 'TBD\|tentative\|"#"' _config.yml *.md classes/ labs/
```

## Working with collaborators

To give Dr. Chen or a TA push access: repo → **Settings → Collaborators → Add people**. They accept the
invitation, then clone and use the same workflow above with their own key or token.

With more than one person pushing, the rule is simple: **`git pull` before you start, `git pull` before you
push.** If a push is rejected, pull first, resolve anything git flags, then push.

## Preview locally (optional)

You don't need this — pushing is the fastest way to see the site. But if you want it:

```bash
bundle install
bundle exec jekyll serve
# → http://127.0.0.1:4000/urban-ai/
```

Requires Ruby 3.x.

## Accessibility

The site targets WCAG 2.1 AA: semantic headings, a skip link, visible focus rings, 4.5:1 contrast in light
and dark modes, no color-only meaning, responsive to 320px, and a print stylesheet. When you add images, add
real `alt` text. When you add tables, keep a `<thead>`.

## License and reuse

Course materials are shared for educational use. The structure — two-track labs, AI use log, output audit
worksheet, scenario matrix, decision brief — transfers to any domain where students need to use AI critically
rather than credulously.
