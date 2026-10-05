# Deploy replay: local repo → GitHub → Pages (as executed)

Everything below already happened and is verifiable on this machine.
Another agent can re-run the read-only checks blind.

## 0. Starting state

- Local folder `/home/md/src/si-power-gdp-nexus-benchmark-2026/`, code + docs done.
- Public GitHub repo exists: `M0-AR/si-power-gdp-nexus-benchmark-2026`
  (SSH: `git@github.com:M0-AR/si-power-gdp-nexus-benchmark-2026.git`).
- Canonical site files: `docs/preview.html` + `docs/index.html` (identical),
  `docs/.nojekyll`, assets in `assets/` referenced as `../assets/…` from `/docs`.
- Root mirrors: `preview.html` (same bytes, `assets/…` paths), `index.html`
  (redirect to `preview.html`), `.nojekyll` — so the site works whether Pages
  source is `/` (root) or `/docs`.

## 1. Confirm auth (read-only checks)

```bash
git config user.name   # expect: M0-AR
ssh -o BatchMode=yes -o ConnectTimeout=10 -T git@github.com
# expect: "Hi M0-AR! You've successfully authenticated…"
```

SSH worked, so the `git@github.com:…` remote was used.
(`gh auth` was NOT logged in — irrelevant.)

## 2. Stage, commit, branch, remote

```bash
git add -A
git commit -m "<message>"
git branch -M main
git remote add origin git@github.com:M0-AR/si-power-gdp-nexus-benchmark-2026.git
```

⚠️ Do NOT run GitHub's suggested `echo "# …" >> README.md` —
it would corrupt the finished README.

Commits on `main` (oldest → newest):

1. `4e43546` — base benchmark v1.0.0, live-verified 2026-10-05
2. `91348e3` — rich README + Pages preview + screenshots + demo slots
3. `ab9e0af` — demo GIF hosted directly in-repo, no placeholder
4. `0088357` — real Pages URL + clone URL, no placeholders
5. (this fix) — root `preview.html`/`index.html`/`.nojekyll` mirrors

## 3. Push + verify

```bash
git push -u origin main          # expect: main -> main
git status --short               # expect: empty (clean)
git ls-tree -r origin/main --name-only | grep -E "^(docs|assets)/"
# expect: docs/.nojekyll docs/index.html docs/preview.html
#         assets/preview.png assets/charts.png assets/demo.gif
```

## 4. Diagnose which Pages source is live (read-only, no login)

```bash
curl -sI "https://m0-ar.github.io/si-power-gdp-nexus-benchmark-2026/" | head -n 1
curl -sI "https://m0-ar.github.io/si-power-gdp-nexus-benchmark-2026/preview.html" | head -n 1
curl -sI "https://m0-ar.github.io/si-power-gdp-nexus-benchmark-2026/docs/preview.html" | head -n 1
```

Observed 2026-10-05: `/` → 200, `/preview.html` → 404,
`/docs/preview.html` → 200.

Conclusion: publishing source is `/` (root), not `/docs` —
URL paths mirror repo paths, so the file resolves at `/docs/preview.html`.
Per official Pages docs, the entry file must sit at the top level of the
chosen source — hence the root mirrors added in step 0.

## 5. Enable / fix Pages (the only manual click-path)

1. Repo → Settings → Pages.
2. Build and deployment → Deploy from a branch.
3. Branch `main`, folder `/docs` (recommended) — or `/` (root);
   this repo serves correctly under either (see step 0).
4. Wait ~1–2 min → Actions → "pages build and deployment" → Success.
5. Open `https://m0-ar.github.io/si-power-gdp-nexus-benchmark-2026/preview.html` ✅
   (fallback under root source: `…/docs/preview.html`).

## 6. If it fails — checklist for the agent

- 404 on page → wrong folder selected in Pages settings, or file not named
  exactly `preview.html` (case-sensitive); check the Actions deploy log first.
- Broken images → asset paths must be relative (`assets/…` from root,
  `../assets/…` from `/docs`), never absolute/local (`/home/…` breaks on Pages).
- Push rejected → `ssh -T git@github.com` must greet you; fix key before retrying.
- Re-verify after any change with the three `curl -sI` probes in step 4.
