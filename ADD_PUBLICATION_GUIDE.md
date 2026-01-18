# Guide: Adding New Publications to Your Website

## Quick Steps

### Step 1: Create a New Publication File

Create a new markdown file in the `_publications/` directory with the naming convention:
```
YYYY-MM-DD-VENUE-AUTHOR.md
```

For example:
- `2025-06-icra-cao.md` (ICRA 2025, first author: Cao)
- `2025-03-iros-smith.md` (IROS 2025, first author: Smith)

### Step 2: Use This Template

Copy this template and fill in your information:

```markdown
---
title: "Your Paper Title Here"
collection: publications
permalink: /publication/YYYY-MM-DD-VENUE-AUTHOR
excerpt: 'Brief description of your paper (1-2 sentences).'
date: YYYY-MM-DD
venue: 'Conference or Journal Name'
paperurl: 'https://your-paper-url.com'
authors: '**Cao, M.**, Other, A., Authors, B. and Last, C.'
break: 'yes'
---

Your detailed description here. You can include links like:
\[[Paper](https://your-paper-url.com)\]\[[Video](https://youtube.com/watch?v=...)\]\[[Code](https://github.com/...)\]

{% if post.teaser %}
<img style="float: center;" src="/images/your-image.gif">
{% endif %}
```

### Step 3: Required Fields

**Essential fields:**
- `title`: Full paper title (in quotes)
- `collection`: Always `publications`
- `permalink`: URL path (matches filename without .md)
- `date`: Publication date (YYYY-MM-DD format)
- `venue`: Conference or journal name
- `authors`: Author list (bold your name with `**Cao, M.**`)
- `break: 'yes'`: Keeps formatting consistent

**Optional fields:**
- `excerpt`: Short description (appears in card view)
- `paperurl`: Link to paper (or add to `paper_links.yml` instead)
- Content below `---`: Full description, links, images

### Step 4: Update Paper Links (Two Options)

#### Option A: Use the Central Config File (Recommended)

Edit `_data/paper_links.yml` and add your new paper:

```yaml
papers:
  "Your Paper Title Here":
    url: "https://your-paper-url.com"
    doi: "10.xxxx/xxxxx"  # Optional
    videos: 
      - "https://youtube.com/watch?v=..."
    code: 
      - "https://github.com/..."
    presentations: []
```

#### Option B: Run the Populate Script

After creating your publication file, run:

```bash
python populate_paper_links.py
```

This will automatically scan all publications and update `paper_links.yml`.

### Step 5: Add Images (Optional)

If you want to add a teaser image:

1. Place your image (GIF or PNG) in the `images/` directory
2. Reference it in your publication file:
   ```markdown
   <img style="float: center;" src="/images/your-image.gif">
   ```

### Step 6: Test Locally

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000/publications/` to see your new publication.

## Example: Complete Publication File

```markdown
---
title: "Novel Approach to Robot Navigation Using Machine Learning"
collection: publications
permalink: /publication/2025-06-icra-cao
excerpt: 'We present a novel machine learning approach for autonomous robot navigation in complex environments.'
date: 2025-06-01
venue: 'IEEE International Conference on Robotics and Automation (ICRA)'
paperurl: 'https://arxiv.org/abs/2506.01234'
authors: '**Cao, M.**, Smith, J., Brown, K. and Wilson, L.'
break: 'yes'
---

We present a novel machine learning approach for autonomous robot navigation in complex environments. Our method combines deep reinforcement learning with traditional path planning algorithms.

\[[Paper](https://arxiv.org/abs/2506.01234)\]\[[Video](https://youtube.com/watch?v=example)\]\[[Code](https://github.com/yourusername/code)\]

<img style="float: center;" src="/images/robot-navigation.gif">
```

## Notes

- **First-author papers** will automatically be highlighted and sorted first
- **Your name** (`**Cao, M.**`) will automatically get the crown highlight
- **Date format**: Use YYYY-MM-DD (the day doesn't matter, usually use 01)
- **Author formatting**: Bold your name, separate with commas, use "and" before last author
- **Paper links**: Use `paper_links.yml` for centralized link management

## Troubleshooting

**Publication not showing?**
- Check that `collection: publications` is set
- Verify the filename format matches the permalink
- Make sure date is in YYYY-MM-DD format

**Links not working?**
- Add paper URL to `_data/paper_links.yml`
- Or set `paperurl` in the front matter
- Run `python populate_paper_links.py` to sync

**Styling issues?**
- Ensure `break: 'yes'` is in front matter
- Check that author name uses `**Cao, M.**` format


