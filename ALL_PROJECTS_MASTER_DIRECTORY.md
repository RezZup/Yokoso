# 📚 Master Project Directory & Portfolio Reference
> **Author:** Gaurav Rajbhar (RezZup)  
> **GitHub:** [https://github.com/RezZup](https://github.com/RezZup)  
> **LinkedIn:** [https://www.linkedin.com/in/gauravrajbhar00](https://www.linkedin.com/in/gauravrajbhar00)  
> **Portfolio:** [https://rezzup.github.io/Yokoso/](https://rezzup.github.io/Yokoso/)  
> **Résumé:** [Google Drive](https://drive.google.com/file/d/1AzFnQRpkQEt-5lDo_UKrimBbRCY4qtZL/view?usp=sharing)  
> **Updated:** November 2026

---

## 🧭 Overview & Quick Navigation

This document is the long-form reference for my projects. It contains accurate technical summaries, feature breakdowns, architecture notes, metrics, tech stacks, and GitHub repository links — formatted for direct use in portfolios, resumes, and technical interviews.

### Quick Reference Matrix

| # | Project | Domain | GitHub Repo | Availability | Live Demo |
|---|---|---|---|---|---|
| 01 | **Yokoso** | WebGL / 3D Creative | [RezZup/Yokoso](https://github.com/RezZup/Yokoso) | ✅ Public | [Live Site](https://rezzup.github.io/Yokoso/) |
| 02 | **ClothyRec (Atelier)** | Computer Vision / AI Stylist | [RezZup/Clothy-.-Rec](https://github.com/RezZup/Clothy-.-Rec) | ✅ Public | — |
| 03 | **Suraksha Setu** | Applied AI / Disaster Early Warning | [RezZup/Suraksha-Setu](https://github.com/RezZup/Suraksha-Setu) | ✅ Public | — |
| 04 | **AI Air Quality (IBM)** | ML / Time-Series / XAI | [RezZup/AI-Powered-Air-Quality-Intelligence-AQI-Forecasting](https://github.com/RezZup/AI-Powered-Air-Quality-Intelligence-AQI-Forecasting) | ✅ Public | — |
| 05 | **AlumUnity (AlmuminiV3)** | Full-Stack / Alumni Platform | [RezZup/AlmuminiV3](https://github.com/RezZup/AlmuminiV3) | ✅ Public | — |
| 06 | **EnergiX** | Systems / CPU DVFS Simulator | [RezZup/EnergiX-Adaptive-Power-Optimized-Scheduler](https://github.com/RezZup/EnergiX-Adaptive-Power-Optimized-Scheduler) | ✅ Public | [Live App](https://energi-x-adaptive-power-optimized-s.vercel.app) |
| 07 | **GDMaxy (GCMaxy)** | Systems / GC Visualizer | [RezZup/GDMaxy](https://github.com/RezZup/GDMaxy) | ✅ Public | [Live App](https://gd-maxy-8dwf.vercel.app) |
| 08 | **ConnectHub (ChatRoom)** | Real-Time / WebSockets Chat | [RezZup/ChatRoom](https://github.com/RezZup/ChatRoom) | ✅ Public | — |
| 09 | **GlobalHeat** | Data Visualization / Climate | [RezZup/GlobalHeat](https://github.com/RezZup/GlobalHeat) | ✅ Public | — |
| 10 | **Nexora V2.0** | Full-Stack MERN / Incubation | [RezZup/NexoraV2.0](https://github.com/RezZup/NexoraV2.0) | ✅ Public | — |
| 11 | **DrishtiSetu (SIH 2026)** | Geospatial AI / Relocation DSS | [RezZup/-DrishtiSetu](https://github.com/RezZup/-DrishtiSetu) | ✅ Public | — |
| 12 | **SIHv2 Notification Hub** | Alert Delivery / Testing Suite | [RezZup/SIHv2](https://github.com/RezZup/SIHv2) | ✅ Public | — |
| 13 | **UNO Multiplayer** | Game Engine / Real-Time Full-Stack | [RezZup/UNO](https://github.com/RezZup/UNO) | ✅ Public | — |
| 14 | **Discord Fix English** | Browser Extension / AI Assistant | — | 💻 Not published yet | — |
| 15 | **n8n AI Workflows** | Workflow Automation / GenAI | [RezZup/n8n-workflows](https://github.com/RezZup/n8n-workflows) | ✅ Public | — |
| 16 | **RAKSHAMAP (ritik)** | Geospatial / PostGIS Decision | — | 💻 Not published yet | — |

---

# 📂 Detailed Project Profiles

```text
================================================================================
01. YOKOSO — 3D PROCEDURAL WEBGL KYOTO TEMPLE PORTFOLIO
================================================================================
```
* **Title:** Yokoso — Cinematic Scroll-Driven 3D Kyoto Temple Portfolio
* **GitHub Repository:** [https://github.com/RezZup/Yokoso](https://github.com/RezZup/Yokoso)
* **Live Deployment:** [https://rezzup.github.io/Yokoso/](https://rezzup.github.io/Yokoso/)
* **Domain:** Creative Development • WebGL • 3D Graphics • Front-End Engineering

#### 📖 Description
Yokoso is an immersive, single-page portfolio designed as a five-chapter night walk through an atmospheric Kyoto mountain temple. Instead of abrupt page jumps or standard flat layouts, the entire site is rendered as a continuous, full-viewport WebGL scene where scrolling dynamically drives the camera along a 3D Catmull-Rom spline through a torii gate, a stone stair flight, lantern-lit approaches and a lit worship hall.

Every element of the 3D environment — the worship hall, torii gate, stone lanterns with flame glow, wooded ridge, haze, falling rain, drifting leaves, embers, and the vermilion moon — is procedurally synthesized directly in code (Three.js geometry, materials and shaders) without requiring external 3D model files (.gltf / .obj). Each portfolio project card features an interactive mini-viewport that dynamically renders a real-time 3D Three.js scene upon hover.

#### 🌟 Key Features
- **Procedural 3D World:** Zero 3D model asset dependencies. Worship hall, torii, lanterns, maples, ridge, haze, rain, leaf fall, and moon generated in code.
- **Scroll-Driven Camera Path:** Continuous Catmull-Rom camera journey powered by Lenis smooth scrolling.
- **Interactive Mini-Viewports:** Live Three.js 3D canvas renderers embedded directly inside project cards.
- **Micro-Interactions & Visual Polish:** Word-by-word text reveals, multi-layer parallax foreground cutouts, bloom, film grain, and custom cursor.
- **Zero Build Tooling:** Pure HTML5, CSS3, and JavaScript — no bundlers or complex build setups required.
- **Performance & Accessibility:** Semantic landmarks, keyboard skip links, `prefers-reduced-motion` fallbacks, and 100% self-hosted assets.

#### 🛠️ Tech Stack
Three.js (WebGL), Lenis Smooth Scroll, Vanilla JavaScript (ES6+), Modern CSS3, HTML5 Semantic Markup, GitHub Pages, GitHub Actions CI.

---

```text
================================================================================
02. CLOTHYREC (ATELIER) — AI PERSONAL FASHION STYLIST & VISUAL RECOMMENDER
================================================================================
```
* **Title:** ClothyRec — AI-Powered Fashion Stylist & Visual Recommender
* **GitHub Repository:** [https://github.com/RezZup/Clothy-.-Rec](https://github.com/RezZup/Clothy-.-Rec)
* **Domain:** Computer Vision • Deep Learning • Recommendation Systems • Multimodal AI

#### 📖 Description
ClothyRec solves the problem of personal fashion discovery by combining deep visual feature extraction, fast vector similarity search, and conversational LLM reasoning. Traditional e-commerce fashion search relies heavily on textual tags that fail to capture aesthetic nuance, cut, pattern, or color harmony. ClothyRec extracts 512-dimensional visual embeddings using OpenCLIP (ViT-B/32) and indexes them using FAISS to enable sub-millisecond similarity retrieval across 44,000+ fashion items from the DeepFashion2 benchmark.

The pipeline incorporates YOLOv8 Pose for upper- and lower-body garment segmentation from user photos, combined with MTCNN facial landmarking to extract skin undertones for complementary color theory recommendations. A conversational Gemini AI stylist synthesizes the extracted visual attributes with natural language advice to deliver personalized outfit suggestions.

#### 🌟 Key Features & Metrics
- **Garment Classification Accuracy:** 96.06% top-1 accuracy on benchmark garment datasets (benchmarked across CNN, ResNet-50, and EfficientNet).
- **Sub-Millisecond Vector Retrieval:** Real-time visual similarity search powered by FAISS vector index and OpenCLIP (ViT-B/32).
- **Automated Body & Face Analysis:** YOLOv8 Pose body segmentation + MTCNN skin-tone extraction for color matching.
- **Multimodal AI Stylist:** Google Gemini API injected with local visual embeddings and color metadata to provide contextual styling advice.

#### 🛠️ Tech Stack
Python 3.10+, PyTorch, OpenCLIP, FAISS, YOLOv8 Pose, MTCNN, ResNet-50, EfficientNet, FastAPI, React 19, Tailwind CSS, Google Gemini API.

---

```text
================================================================================
03. SURAKSHA SETU — MULTI-HAZARD EARLY WARNING & DECISION PLATFORM
================================================================================
```
* **Title:** Suraksha Setu — AI-Powered Disaster Early Warning & Decision Support System
* **GitHub Repository:** [https://github.com/RezZup/Suraksha-Setu](https://github.com/RezZup/Suraksha-Setu)
* **Recognition:** 🏆 **State Winner & National Finalist** — OpenAI × NextWave Buildathon (500+ teams)
* **Domain:** Applied AI • Disaster Management • Geospatial Intelligence • Full-Stack Systems

#### 📖 Description
Suraksha Setu is a comprehensive disaster early warning and emergency response platform engineered to bridge the communication gap between scientific sensor networks, disaster response authorities, and vulnerable citizens. The platform ingests and fuses real-time data feeds from USGS (earthquakes), GDACS (global disasters), CPCB (air quality), OpenWeather, and 3-layer satellite imagery from MOSDAC (ISRO).

The system integrates a deterministic hazard risk engine with strict threshold gating and one-click alert retraction to completely prevent false panic. It features 4 role-based AI agents (Citizen, Student, Scientist, Administrator) powered by OpenAI GPT-4o with function calling, RAG knowledge retrieval, PyTorch disaster damage image classification, Whisper multilingual voice interaction (Hindi/English/regional), and interactive Leaflet GIS red-zone carrying capacity mapping.

#### 🌟 Key Features & Metrics
- **Automated Data Ingestion:** Real-time polling from USGS, GDACS, OpenWeather, CPCB, and ISRO MOSDAC satellite feeds.
- **High-Accuracy Computer Vision:** PyTorch multi-class disaster damage classifier trained on 9,000+ real-world disaster images, achieving **98.81% training accuracy** and **94.81% validation accuracy**.
- **Role-Based Multi-Agent Architecture:** 4 distinct agents (Citizen, Student, Scientist, Admin) equipped with tool-calling capabilities and RAG knowledge retrieval.
- **Voice & Accessibility:** Multilingual speech recognition via OpenAI Whisper supporting regional Indian languages.
- **Geospatial Red-Zone Intelligence:** Interactive Leaflet GIS maps tracking hazard radii, habitation risk, and carrying capacity for evacuation planning.
- **Civic Incident Reporting Hub:** Citizen photo/video damage reporting with crowdsourced verification to filter false alerts.

#### 🛠️ Tech Stack
React 19, FastAPI, PyTorch, OpenAI GPT-4o, Whisper, Leaflet GIS, PostgreSQL / SQLite / MongoDB, Redis, WebSockets, Tailwind CSS, Docker.

---

```text
================================================================================
04. AI-POWERED AIR QUALITY INTELLIGENCE & LEAKAGE-SAFE AQI FORECASTING
================================================================================
```
* **Title:** AI-Powered Air Quality Intelligence & Leakage-Safe AQI Forecasting
* **GitHub Repository:** [https://github.com/RezZup/AI-Powered-Air-Quality-Intelligence-AQI-Forecasting](https://github.com/RezZup/AI-Powered-Air-Quality-Intelligence-AQI-Forecasting)
* **Credential:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares
* **Domain:** Machine Learning • Time-Series Forecasting • Explainable AI (XAI)

#### 📖 Description
Conventional air quality forecasting models often suffer from temporal data leakage due to random train/test splitting, creating overly optimistic metrics that fail in production. This project implements a rigorous, leakage-safe machine learning pipeline trained on 29,531 daily observation records across 26 major Indian cities over 5 years (2015–2020) from the Central Pollution Control Board (CPCB).

The pipeline enforces strict chronological 80/20 train/test splitting per city, temporal interpolation, and rolling-window feature engineering (lag values, 7-day rolling means, min/max metrics). Benchmark evaluations compare Linear Regression, Random Forest, and XGBoost. An Isolation Forest model identifies anomalous pollution spikes (industrial emissions, stubble burning), while SHAP provides model explainability through global summary plots and single-day waterfall charts.

#### 🌟 Key Features & Metrics
- **Leakage-Safe Chronological Partitioning:** Eliminates future-to-past data leakage across 29,531 records and 26 Indian cities.
- **Model Performance:** Random Forest achieved **RMSE: 49.96** and **R²: 0.681** for next-day AQI prediction.
- **Anomaly Detection:** Isolation Forest identified **1,243 anomalies (5.0%)**, isolating seasonal pollution crises and industrial events.
- **Explainable AI (XAI):** SHAP summary, importance, and waterfall plots verified that PM2.5 and 7-day rolling AQI are the strongest predictive drivers of severe air quality.
- **Comprehensive Visualizations:** Correlation matrices, seasonal pollutant breakdowns, and actual-vs-predicted residual diagnostics.

#### 🛠️ Tech Stack
Python 3.10+, Pandas, NumPy, Scikit-learn, XGBoost, SHAP, Isolation Forest, Matplotlib, Seaborn, CPCB Open Dataset.

---

```text
================================================================================
05. ALUMUNITY (ALMUMINIV3) — ALUMNI ENGAGEMENT & NETWORKING PLATFORM
================================================================================
```
* **Title:** AlumUnity — Enterprise-Grade Alumni Engagement & Mentorship Platform
* **GitHub Repository:** [https://github.com/RezZup/AlmuminiV3](https://github.com/RezZup/AlmuminiV3)
* **Domain:** Full-Stack Web Development • Enterprise SaaS • Career Intelligence

#### 📖 Description
AlumUnity is a full-featured alumni community and career acceleration platform connecting students, alumni, faculty, recruiters, and university administration. Designed to solve the fragmentation of university networking, the application provides an integrated environment for professional mentorship, job opportunities, campus events, and alumni achievements.

The frontend is constructed with 42+ role-based pages and 90+ modular, reusable React components. The FastAPI backend implements strict Role-Based Access Control (RBAC) with JWT authentication. Key innovations include an interactive skill-graph visualization displaying career pathways, gamified contribution leaderboards, and cryptographically verifiable digital alumni ID cards featuring scannable QR codes.

#### 🌟 Key Features
- **Role-Based Architecture:** Dedicated portals for Students, Alumni, Mentors, Recruiters, and University Admins.
- **FastAPI RESTful Backend:** High-speed asynchronous Python backend with JWT authentication and granular RBAC.
- **Skill-Graph Visualization:** Dynamic interactive skill and career trajectory graphs powered by React and Recharts.
- **Job & Mentorship Portals:** Direct application tracking, interview scheduling, and 1-on-1 mentorship matching.
- **Gamification & Digital IDs:** Scannable QR-code digital alumni cards and community engagement leaderboards.

#### 🛠️ Tech Stack
React, FastAPI, MySQL, JWT, Docker, Firebase Auth, Tailwind CSS, Recharts.

---

```text
================================================================================
06. ENERGIX — CPU SCHEDULING SIMULATOR WITH ADAPTIVE DVFS
================================================================================
```
* **Title:** EnergiX — Energy-Aware CPU Scheduling Simulator with Adaptive DVFS
* **GitHub Repository:** [https://github.com/RezZup/EnergiX-Adaptive-Power-Optimized-Scheduler](https://github.com/RezZup/EnergiX-Adaptive-Power-Optimized-Scheduler)
* **Live Deployment:** [https://energi-x-adaptive-power-optimized-s.vercel.app](https://energi-x-adaptive-power-optimized-s.vercel.app)
* **Domain:** Systems Engineering • Operating Systems • Power Optimization • Web Simulators

#### 📖 Description
EnergiX is a web-based systems simulator investigating how operating systems can dramatically reduce CPU power consumption on mobile and embedded devices without violating process completion deadlines. It implements and benchmarks 6 classic scheduling algorithms (FCFS, SJF Preemptive, SJF Non-Preemptive, Round Robin, Priority Preemptive, Priority Non-Preemptive) against a custom **Energy-Aware Hybrid (EAH)** algorithm.

The EAH algorithm combines dynamic priority recalculation with an **Adaptive Dynamic Voltage and Frequency Scaling (DVFS)** model. By continuously evaluating queue density and remaining burst times, the CPU dynamically transitions between frequency tiers (1.2 GHz to 2.8 GHz), achieving up to **34.8% energy reduction** compared to standard First-Come-First-Served execution.

#### 🌟 Key Features & Metrics
- **6 Classical + 1 Novel Algorithm:** FCFS, SJF (P/NP), Round Robin, Priority (P/NP), and Energy-Aware Hybrid (EAH).
- **Up to 34.8% Power Savings:** Validated energy reduction through adaptive frequency scaling under mixed workloads.
- **Live Interactive Multi-Core Gantt Charts:** Real-time visual timeline showing task allocations, preemption, and idle states.
- **Real-Time Energy Curves:** Dynamic charts displaying power dissipation (Watts), cumulative energy (Joules), and DVFS frequency transitions.
- **Comprehensive Benchmarks:** Automated comparative matrix evaluating turnaround time, waiting time, CPU utilization, and energy consumption.

#### 🛠️ Tech Stack
Python 3.11, FastAPI, Chart.js, HTML5 Canvas, Modern JavaScript, Tailwind CSS, Vercel, Railway.

---

```text
================================================================================
07. GDMAXY (GCMAXY) — INTERACTIVE GARBAGE COLLECTION VISUALIZER
================================================================================
```
* **Title:** GCMaxy — Interactive Garbage Collection & Memory Management Simulator
* **GitHub Repository:** [https://github.com/RezZup/GDMaxy](https://github.com/RezZup/GDMaxy)
* **Live Deployment:** [https://gd-maxy-8dwf.vercel.app](https://gd-maxy-8dwf.vercel.app)
* **Domain:** Systems Programming • Runtime Internals • Memory Management • Interactive Tools

#### 📖 Description
GCMaxy is an educational and analytical web platform that renders the invisible mechanics of runtime memory management visible in real time. Designed for software engineers studying runtime performance, GCMaxy simulates 4 fundamental Garbage Collection strategies: Mark-Sweep, Reference Counting (with circular dependency detection), Generational Garbage Collection (Young Gen vs Tenured Gen), and Copying Semi-Space.

The application features a 2D memory block grid where every memory address is color-coded by its state (free, allocated, marked, orphaned). Accompanying the grid is a live D3.js force-directed object reference graph showing pointer links, reference cycles, and root pointers. Users can allocate objects, create circular references, trigger collections, and monitor real-time telemetry (GC pause latency, memory reclamation percentage, and allocation throughput).

#### 🌟 Key Features
- **4 Simulated GC Algorithms:** Mark-Sweep, Reference Counting, Generational GC, and Copying Semi-Space.
- **Live 2D Memory Grid:** Real-time memory heap visualizer showing contiguous blocks and fragmentation.
- **D3.js Object Reference Graph:** Dynamic force-directed graph visualizing pointer roots and circular dependency traps.
- **Real-Time Telemetry:** Monitors GC pause times (latency), allocation rates, and memory reclamation efficiency.
- **Interactive Workload Controls:** Step-by-step execution, automatic cycle generators, and custom heap size configurations.

#### 🛠️ Tech Stack
React, D3.js, Shadcn UI, FastAPI, Python, Tailwind CSS, Vercel, Railway.

---

```text
================================================================================
08. CONNECTHUB (CHATROOM) — REAL-TIME MESSAGING & COLLABORATION
================================================================================
```
* **Title:** ConnectHub — Real-Time Messaging Platform with WebSockets & WebRTC
* **GitHub Repository:** [https://github.com/RezZup/ChatRoom](https://github.com/RezZup/ChatRoom)
* **Domain:** Full-Stack • Real-Time WebSockets • Communications • WebRTC

#### 📖 Description
ConnectHub is a modern, responsive communication platform inspired by WhatsApp. Built with React on the frontend and an asynchronous FastAPI + MongoDB architecture on the backend, ConnectHub provides instant messaging capabilities with low latency via bidirectional WebSockets.

The application includes user authentication, live presence detection (online/offline indicators), typing notifications, emoji reactions, message thread replies, and multimedia file sharing (images, videos, documents). It also features WebRTC peer-to-peer video calling, offline message queueing, and a mobile-friendly responsive dark interface.

#### 🌟 Key Features
- **Bidirectional WebSockets:** Sub-50ms message delivery with typing indicators and live status updates.
- **WebRTC Video Calling:** Peer-to-peer audio/video calling directly in the browser.
- **Rich Message Interactions:** Emoji reactions, message replies, edit/delete options, and multimedia file uploads.
- **Presence & Friend Management:** Instant friend request system with real-time online status tracking.
- **Responsive Dark UI:** WhatsApp-inspired aesthetics with Framer Motion animations and dark mode.

#### 🛠️ Tech Stack
React, FastAPI, WebSockets, WebRTC, MongoDB (Motor), Framer Motion, Tailwind CSS, Vercel, Render.

---

```text
================================================================================
09. GLOBALHEAT — CLIMATE CHANGE AWARENESS PLATFORM
================================================================================
```
* **Title:** GlobalHeat — Interactive Climate Change Awareness & Data Platform
* **GitHub Repository:** [https://github.com/RezZup/GlobalHeat](https://github.com/RezZup/GlobalHeat)
* **Domain:** Front-End Development • Data Visualization • Climate Awareness

#### 📖 Description
GlobalHeat is an interactive, educational web platform created to raise public awareness about climate change and sustainable energy transitions. The platform translates complex environmental datasets into accessible, visually compelling charts and educational modules.

The website features dynamic data visualizations powered by Chart.js, covering global greenhouse gas emissions by economic sector, renewable energy growth curves, clean energy investment patterns, and building energy efficiency comparisons. The site utilizes Animate On Scroll (AOS) libraries, a carbon footprint calculation guide, and responsive layouts tailored for mobile, tablet, and desktop devices.

#### 🌟 Key Features
- **Interactive Data Visualizations:** Dynamic Chart.js visualizations (bar, doughnut, line) detailing global emissions and clean energy.
- **In-Depth Knowledge Modules:** Dedicated chapters covering industrial emissions, transportation, deforestation, and clean energy solutions.
- **Fluid Visual Polish:** Animate On Scroll (AOS) animations, modern card-based layouts, and responsive dark themes.
- **Actionable Sustainability Tools:** Carbon reduction checklists, interactive calculators, and sustainability guidelines.

#### 🛠️ Tech Stack
HTML5, CSS3, JavaScript (ES6+), Chart.js, AOS (Animate On Scroll), Font Awesome, GitHub Pages.

---

```text
================================================================================
10. NEXORA V2.0 — AI-POWERED STARTUP INCUBATION PLATFORM
================================================================================
```
* **Title:** Nexora V2.0 — AI-Powered Startup Incubation & Venture Management Platform
* **GitHub Repository:** [https://github.com/RezZup/NexoraV2.0](https://github.com/RezZup/NexoraV2.0)
* **Domain:** Full-Stack MERN • AI SaaS • Entrepreneurship & Venture Capital

#### 📖 Description
Nexora is a centralized startup lifecycle management platform built to unify the fragmented tools used by early-stage founders, mentors, and angel investors. Rather than juggling separate communication channels, pitch deck repositories, and scheduling software, Nexora integrates the complete incubation journey into a single web application.

The platform provides role-based workspaces for Founders, Mentors, Investors, and System Administrators. Founders can create company profiles, upload pitch decks, set milestones, and request mentorship meetings. Mentors review submissions via the Mentor Studio, while Investors evaluate traction metrics and submit funding inquiries. The platform incorporates AI-powered idea validation, automated market trend analysis, and intelligent growth recommendations.

#### 🌟 Key Features
- **4 Role-Based Workspaces:** Tailored dashboards for Founders, Mentors, Investors, and Administrators.
- **Startup Lifecycle Management:** Pitch deck storage, milestone progress tracking, and company KPI tracking.
- **Venture Discovery Desk:** Investor filtering portal with direct proposal submission and review workflows.
- **AI Venture Advisory:** AI-assisted idea feasibility validation, market opportunity assessment, and funding insights.
- **Integrated Community:** Real-time discussion forums and direct messaging between founders and advisors.

#### 🛠️ Tech Stack
React.js, Node.js, Express.js, MongoDB Atlas, Tailwind CSS, JWT Authentication, REST APIs, Git & GitHub.

---

```text
================================================================================
11. DRISHTISETU (SIH 2026) — GIS & AGENTIC DISASTER RELOCATION DSS
================================================================================
```
* **Title:** DrishtiSetu — AI-Assisted GIS Disaster Relocation Decision Support System
* **GitHub Repository:** [https://github.com/RezZup/-DrishtiSetu](https://github.com/RezZup/-DrishtiSetu)
* **Competition:** Smart India Hackathon (SIH 2026) Prototype
* **Domain:** Disaster Relocation • Geospatial Intelligence • Multi-Agent Systems • Explainable AI

#### 📖 Description
DrishtiSetu is an AI-assisted, GIS-enabled decision support system built for disaster management authorities tackling catastrophic land subsidence, landslides, and flash flooding in vulnerable Himalayan habitations (modeled after the Joshimath crisis in Chamoli district, Uttarakhand). Relocation planning is historically hindered by isolated data silos: GIS hazard maps, structural damage reports, carrying capacity limits, and resettlement regulations rarely interact.

DrishtiSetu synthesizes these disparate streams into a unified executive decision interface. The system employs an agentic orchestration layer that evaluates candidate relocation sites against terrain slope stability, road connectivity, water access, and carrying capacities. A transparent, deterministic scoring engine provides explainable recommendations, ensuring that relocation priorities are backed by traceable evidence rather than black-box algorithms.

#### 🌟 Key Features
- **GIS Multi-Hazard Visualization:** Interactive mapping overlaying landslide risk zones, seismic faults, and habitation boundaries.
- **Relocation Suitability Analysis:** Multi-criteria site ranking evaluating slope, drainage, road access, and environmental safety.
- **Carrying Capacity Auditing:** Automated verification ensuring recipient relocation zones can support incoming populations.
- **Retrieval-Augmented Policy Engine (RAG):** Natural language retrieval across official disaster management guidelines (NDMA/SDMA).
- **Agentic Orchestration:** Explainable AI decision workflows generating structured justification reports for district magistrates.

#### 🛠️ Tech Stack
Python, FastAPI, PostGIS, QGIS / Leaflet, RAG (Retrieval-Augmented Generation), Computer Vision, Docker.

---

```text
================================================================================
12. SIHV2 — MULTI-CHANNEL DISASTER NOTIFICATION & OPTIMIZATION HUB
================================================================================
```
* **Title:** SIHv2 — Pincode-Optimized Multi-Channel Disaster Alert Hub
* **GitHub Repository:** [https://github.com/RezZup/SIHv2](https://github.com/RezZup/SIHv2)
* **Domain:** High-Throughput Alert Infrastructure • Multi-Channel Messaging • Systems Verification

#### 📖 Description
SIHv2 is an emergency notification delivery infrastructure designed to broadcast critical evacuation alerts during natural catastrophes without causing telecommunications grid collapse. In rapid-onset disasters, broadcasting indiscriminately across entire states can overwhelm cell towers and induce widespread panic.

SIHv2 implements a pincode-level geographic optimization engine that filters recipient pools based on precise proximity to the hazard epicenter. The platform routes messages through an omnichannel delivery pipeline spanning SMS gateways, WhatsApp Business API, Telegram mini-app bots, and priority email. The codebase includes an automated 62-test verification suite validating ML inferences, computer vision models, GIS transformations, RAG lookups, and agent contracts.

#### 🌟 Key Features
- **Omnichannel Dispatch:** Simultaneous alert broadcast across SMS, WhatsApp, Telegram mini-app bots, and email.
- **Pincode Geographic Optimization:** Targeted notification routing that eliminates alert fatigue and prevents network congestion.
- **Automated Verification Suite:** 62 end-to-end tests covering ML risk predictions, CV damage classifiers, GIS geospatial queries, and contract integrity.
- **Telegram Mini-App Integration:** Interactive citizen emergency portal embedded directly within Telegram for two-way communication.

#### 🛠️ Tech Stack
Python 3.10+, FastAPI, Telegram Bot API, Twilio / SMS Gateways, WhatsApp Cloud API, Pytest, Docker.

---

```text
================================================================================
13. UNO — MULTIPLAYER REAL-TIME WEB CARD GAME
================================================================================
```
* **Title:** UNO — Full-Stack Real-Time Multiplayer Card Game
* **GitHub Repository:** [https://github.com/RezZup/UNO](https://github.com/RezZup/UNO)
* **Domain:** Game Development • Real-Time Web • Full-Stack Systems

#### 📖 Description
A full-stack, browser-based digital reproduction of the classic UNO card game featuring real-time multiplayer lobbies. Built with a Python FastAPI backend and a modern React frontend, this project demonstrates clean software architecture in state management, real-time synchronization, and ruleset execution.

The backend contains a custom game engine that enforces the official Mattel UNO ruleset: standard 108-card deck generation, color and number matching, Action cards (Skip, Reverse, Draw Two), and Wild cards (Wild, Wild Draw Four). The game engine manages turn rotations, penalty card accumulation, draw pile reshuffling, and win detection. The React frontend delivers fluid card flip and play animations, audio-visual feedback, and responsive player hand displays.

#### 🌟 Key Features
- **Complete Ruleset Implementation:** 108-card standard deck, Skip, Reverse, Draw Two, Wild, and Wild Draw Four.
- **Real-Time Multiplayer Lobbies:** Room creation, unique room codes, player joining, and turn synchronization.
- **Robust Turn & State Engine:** Server-authoritative turn management, card legality validation, and draw pile recycling.
- **Smooth Animated UI:** React-based card drag-and-drop, hand rendering, discard stack, and current color indicators.

#### 🛠️ Tech Stack
React, Python, FastAPI, WebSockets / REST API, CSS Animations, Uvicorn.

---

```text
================================================================================
14. DISCORD FIX ENGLISH — AI CHROME EXTENSION
================================================================================
```
* **Title:** Discord Fix English — Contextual AI Grammar & Tone Assistant
* **Domain:** Browser Extensions • AI Utilities • Natural Language Processing

#### 📖 Description
Discord Fix English is a developer productivity tool created as a Chrome Extension that seamlessly injects an AI-assisted grammar and tone refiner into Discord's desktop web application. Instead of copying text back and forth between external translation or grammar tools, the extension places a native "Fix English" action button directly beside Discord's message input bar.

Upon clicking the button, the extension intercepts the currently drafted message, transmits it to a local Node.js proxy server connected to Google Gemini API, and replaces the drafted input with grammatically polished, natural-sounding English in milliseconds while preserving the user's original intent and tone.

#### 🌟 Key Features
- **Seamless DOM Injection:** Injects directly into Discord's web client without breaking Discord UI or keyboard shortcuts.
- **One-Click Polish:** Corrects spelling, grammar, punctuation, and colloquial phrasing instantly.
- **Privacy-Centric Architecture:** Operates through a user-controlled local Node.js server with direct Google Gemini API integration.
- **Low-Latency Roundtrip:** Sub-second response time for real-time conversation flow.

#### 🛠️ Tech Stack
Chrome Extension Manifest V3, Vanilla JavaScript, CSS3 DOM Injection, Node.js, Express.js, Google Gemini API.

---

```text
================================================================================
15. AUTONOMOUS AI WORKFLOWS & SOCIAL MEDIA PIPELINES
================================================================================
```
* **Title:** Autonomous AI Content Creation & Scheduling Workflows
* **GitHub Repository:** [https://github.com/RezZup/n8n-workflows](https://github.com/RezZup/n8n-workflows)
* **Domain:** Workflow Automation • Generative AI Pipelines • Content Automation

#### 📖 Description
A collection of production-ready automation workflows built in n8n for fully autonomous video generation, voice synthesis, and multi-platform distribution. The primary pipeline automates the generation of viral YouTube Shorts from spreadsheet prompts with zero manual intervention.

The pipeline monitors a Google Sheet for new script concepts, invokes Sora 2 / InfiP AI video models to generate high-definition visual clips, synthesizes narration using ElevenLabs voice cloning, synchronizes subtitles and branding through Creatomate API, and schedules completed video assets for automated upload.

#### 🌟 Key Features
- **End-to-End Autonomous Pipeline:** Takes raw text prompts from Google Sheets and outputs fully rendered, voiced videos.
- **Multi-Service AI Integration:** Coordinates Sora 2 (video), ElevenLabs (voice), and Creatomate (video assembly).
- **Sanitized Template Distribution:** Parameterized workflows with credential placeholders safe for public open-source sharing.

#### 🛠️ Tech Stack
n8n Workflow Engine, Google Sheets API, ElevenLabs Voice AI, Creatomate API, Sora 2 / InfiP Video AI, Webhooks, REST APIs.

---

```text
================================================================================
16. RAKSHAMAP (RITIK) — POSTGIS RELOCATION DECISION SUPPORT SYSTEM
================================================================================
```
* **Title:** RAKSHAMAP — Spatial Database & Relocation Decision Engine
* **Domain:** Geospatial Databases • Spatial Relocation • PostGIS • Backend Architecture

#### 📖 Description
RAKSHAMAP provides the robust spatial data foundation for the SIH 26191 disaster relocation platform, piloted on Chamoli district in Uttarakhand. The codebase delivers an enterprise-grade backend architecture built around PostgreSQL and PostGIS, enabling sub-second spatial queries across complex geographic polygons, hazard buffer zones, and habitation coordinates.

The system features reproducible database provisioning via Docker Compose, Alembic schema migrations, and a high-performance FastAPI service exposing geospatial endpoints for slope stability, buffer zone generation, and carrying capacity computation.

#### 🌟 Key Features
- **PostGIS Spatial Modeling:** True spatial queries calculating buffer zones, intersecting hazard polygons, and elevation profiles.
- **Reproducible Infrastructure:** Multi-container Docker Compose environment encompassing PostGIS, FastAPI, and Vite React.
- **Alembic Database Migrations:** Version-controlled database schema management ensuring zero migration drift.
- **Spatial Analytics Endpoints:** RESTful APIs computing slope steepness, road network accessibility, and population density metrics.

#### 🛠️ Tech Stack
PostgreSQL 16, PostGIS 3.4, Python 3.10+, FastAPI, Alembic, Docker Compose, Vite, React, GeoJSON.

---
