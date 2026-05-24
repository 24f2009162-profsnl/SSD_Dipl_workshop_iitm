# SSD_Dipl_workshop_iitm
# 🎀 Custom Skin-Match Makeup Store
*A Spec-Driven Development (SDD) vs. Vibe Coding Experiment*

## 📖 Overview
This repository serves as a comparative study between unstructured AI-assisted coding ("Vibe Coding") and structured, architecture-first implementation ("Spec-Driven Development"). The core application is a lightweight Python CLI that recommends tailored makeup products based on a user's skin profile.

## 🌿 Branch Architecture
To demonstrate the workshop's core concepts, this repository is split into distinct workflows:

* **`vibe_coded_submission` Branch:** Features `makeup_store.py`, developed using raw, unstructured LLM prompting. It relies on heavy, nested `if/else` conditional logic.
* **`sdd_submission` Branch:** Features `makeup.py` and `project.md`, developed using strict Spec-Driven Development principles. The architecture was planned in Markdown first, resulting in a clean, scalable dictionary-mapping algorithm that completely avoids nested conditionals.

## ⚙️ How to Run
```bash
# Run the SDD version
python makeup.py

# Run the Vibe Coded version
python makeup_store.py

Acknowledgments
A sincere thank you to the professors and instructors of the Future of Software Development with LLM: Spec Driven Development workshop at IIT Madras. The insights provided regarding state management, AI agent workflows, and the transition from chaotic prompt engineering to structured SDD architecture have been incredibly valuable to my engineering toolkit.
