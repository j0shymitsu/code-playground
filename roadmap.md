# ROADMAP

---

## Foundations

### Networking

- Cisco Networking Academy “Introduction to Networks” / “Introduction to Cybersecurity” (free, well‑structured, very aligned with cyber roles) 
    - https://www.netacad.com/courses/networking-basics?courseLang=en-US
    - https://www.netacad.com/courses/introduction-to-cybersecurity?courseLang=en-US
- TryHackMe: “Pre‑Security”
    - https://tryhackme.com/path/outline/presecurity
    - 
- Packet Tracer & GNS3 labs (often used alongside Cisco NetAcad) to actually build and break small networks.
    - 

### Linux

Best intros:
- freeCodeCamp “Linux for Hackers – Basics for Cybersecurity Beginners” for file system, package management, and CLI basics.
- HackTheBox: “Learn Linux (fast)” guide + their Linux beginner modules give a cyber‑oriented on‑ramp.

Hands‑on:
- TryHackMe: “Linux Fundamentals 1–3” and “Intro to Offensive Security” (you’ll use Linux while hacking).
- LabEx: browser‑based Linux labs if you want guided terminal tasks without setting up VMs.
- Your own daily driver: keep using Linux day‑to‑day and routinely do tasks only via terminal (editing config, managing services, SSH, logs).

### Python

Best fundamentals:
- freeCodeCamp Python curriculum or a single focused course on Coursera/Udemy if you prefer structured video.
- Boot.dev’s Python track (since you’re already there) for CS‑ish fundamentals and back‑end flavour.

Hands‑on:
- Build tiny tools that support cyber:  
  - Log parser (read auth/web logs and aggregate failed logins).  
  - Simple port scanner or HTTP checker.  
- Many platforms (LabEx, Cybrary) include Python‑based security labs where you script small tasks.

### Web security

Core resources:
- PortSwigger Web Security Academy: free, gold‑standard interactive labs on XSS, SQLi, auth, access control, SSRF, etc..
- OWASP resources (Cheat Sheet Series, OWASP Top 10) to connect each vuln to recommended defences.

Hands‑on:
- PortSwigger labs are already hands‑on; aim to work systematically through the “Apprentice” and “Practitioner” levels.
- TryHackMe: “Intro to Offensive Security”, “Web Fundamentals”, and web‑hacking rooms give guided exploitation practice in a browser.

### DSA, networks (academic side), ethical hacking

DSA:
- Use your uni material + one clear external reference for practice problems (LeetCode easy/medium or similar).  
- Many CS/cyber roadmaps recommend mixing theoretical DSA with small CLI tools that use those structures (e.g., a log indexer using hash maps / trees).

Networks (degree‑level):
- Pair your lectures with CCNA‑style practice from Cisco NetAcad; these courses mirror what infosec recruiters expect as “good networking fundamentals”.

Ethical hacking:
- TryHackMe is widely recommended as the best starting platform for hands‑on hacking with paths like “Pre‑Security” and “Jr Penetration Tester”.
- SANS Cyber Aces plus LetsDefend for SOC‑ish skills if you want more blue‑team context.

Ongoing: daily Linux usage and a small Python/TypeScript script every week or two that solves a real problem (log analysis, recon helper, etc.)








