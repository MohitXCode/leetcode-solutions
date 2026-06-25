<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:1e3a8a&height=200&section=header&text=LeetCode%20Solutions&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=by%20MohitXCode&descAlignY=58&descSize=18" width="100%"/>

<br/>

<a href="https://mohitxcode.space">
  <img src="https://img.shields.io/badge/Portfolio-mohitxcode.space-0f172a?style=for-the-badge&logo=vercel&logoColor=white" />
</a>
<a href="https://leetcode.com/u/mohitxcode/">
  <img src="https://img.shields.io/badge/LeetCode-mohitxcode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" />
</a>
<a href="https://github.com/MohitXCode">
  <img src="https://img.shields.io/badge/GitHub-MohitXCode-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=800&color=3B82F6&center=true&vCenter=true&width=600&lines=Solving+one+problem+at+a+time...;Auto-synced+from+LeetCode+%E2%9A%A1;Organized+by+topic%2C+not+by+chaos;Ship+%3E+Perfect" alt="Typing SVG" />

</div>

<br/>

## 📊 Live Stats

<div align="center">

<img src="https://leetcode-stats-card.streamlit.app/?username=mohitxcode" alt="LeetCode Stats" width="48%"/>
<img src="https://streak-stats.demolab.com/?user=MohitXCode&theme=dark&hide_border=true&background=0D1117&stroke=3B82F6&ring=3B82F6&fire=F59E0B&currStreakLabel=3B82F6" alt="GitHub Streak" width="48%"/>

</div>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=MohitXCode&show_icons=true&theme=dark&hide_border=true&bg_color=0D1117&title_color=3B82F6&icon_color=3B82F6&text_color=c9d1d9&count_private=true" alt="GitHub Stats" width="48%"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohitXCode&layout=compact&theme=dark&hide_border=true&bg_color=0D1117&title_color=3B82F6&text_color=c9d1d9" alt="Top Languages" width="48%"/>

</div>

> **Note:** Stats above pull from public APIs and refresh automatically on every page load — no manual updates needed. LeetCode card requires a public LeetCode profile.

<br/>

## 🗂️ Repo Structure

Every solved problem auto-commits here the moment it's Accepted on LeetCode — synced via a self-hosted [MyLeetSync](#-how-this-stays-up-to-date) extension, organized **by topic**, not by date or difficulty:

```text
leetcode-solutions/
├── Array/
│   └── 0001-two-sum/
│       ├── solution.py
│       └── README.md      ← AI-generated approach + complexity notes
├── Dynamic-Programming/
│   └── 0070-climbing-stairs/
│       ├── solution.py
│       └── README.md
├── Graph/
│   └── 0200-number-of-islands/
│       ├── solution.py
│       └── README.md
├── Hash-Table/
├── Binary-Search/
├── Two-Pointers/
└── ...
```

Each problem folder's `README.md` follows the same format:

```markdown
## Problem
Plain-English restatement

## Approach
How the solution works, in a few sentences

## Complexity
- Time: O(...)
- Space: O(...)
```

<br/>

## 📈 Progress by Difficulty

<div align="center">

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'pie1': '#22c55e', 'pie2': '#f59e0b', 'pie3': '#ef4444'}}}%%
pie showData
    title Problems Solved by Difficulty
    "Easy" : 0
    "Medium" : 0
    "Hard" : 0
```

</div>

<sub>This chart is static — update the numbers above as you solve more, or swap it for the live LeetCode card above once your profile has volume.</sub>

<br/>

## 🏷️ Problems by Topic

<div align="center">

```mermaid
%%{init: {'theme': 'dark'}}%%
graph LR
    A[Solved Problems] --> B[Array]
    A --> C[Dynamic Programming]
    A --> D[Graph]
    A --> E[Hash Table]
    A --> F[Two Pointers]
    A --> G[Binary Search]

    style A fill:#1e3a8a,stroke:#3B82F6,color:#fff
    style B fill:#0f172a,stroke:#22c55e,color:#fff
    style C fill:#0f172a,stroke:#22c55e,color:#fff
    style D fill:#0f172a,stroke:#22c55e,color:#fff
    style E fill:#0f172a,stroke:#22c55e,color:#fff
    style F fill:#0f172a,stroke:#22c55e,color:#fff
    style G fill:#0f172a,stroke:#22c55e,color:#fff
```

</div>

<br/>

## ⚙️ How This Stays Up to Date

This repo doesn't get manual commits. Solutions land here automatically through a Chrome extension I built myself — **MyLeetSync** — instead of trusting a third-party OAuth app with broad GitHub permissions:

1. Solve on LeetCode → submit → Accepted
2. Extension intercepts the verdict client-side, pulls problem metadata
3. [Groq](https://groq.com) (Llama 3.3 70B) generates the approach + complexity writeup
4. Commits `solution.<ext>` + `README.md` here, topic-sorted, via a GitHub fine-grained token scoped to **only this repo**

No standing access to any other repo. No org-wide scopes. Token expires every 90 days by design.

<br/>

## 🛠️ Tech Used Across Solutions

<div align="center">

<img src="https://skillicons.dev/icons?i=python,cpp,js,ts&theme=dark" />

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a8a,100:0f172a&height=100&section=footer"/>

**⭐ If this structure is useful to you, feel free to fork it for your own LeetCode journey.**

</div>
