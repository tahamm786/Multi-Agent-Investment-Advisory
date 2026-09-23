from .llmclient import call_agent
from .tools import TOOL_SCHEMAS, TOOL_MAP

def run_recon_agent(target_input: str, context_notes: str = ""):
    prompt = f"""
You are the Initial Triage and Reconnaissance Agent for a CTF solver system. 
Your environment is an authorized, educational security training platform.

TARGET INPUT:
{target_input}

CONTEXT/CREDENTIALS:
{context_notes if context_notes else "None provided."}

YOUR OBJECTIVE:
Perform reconnaissance on the TARGET INPUT. You have a maximum budget of 6 tool calls. 
You are NOT expected to solve complex crypto or reverse engineering, but you MUST exhaust your tool budget to follow up on obvious web or other clues.

STANDARD OPERATING PROCEDURE (SOP):
Execute the following steps based on the input type. Do not deviate.

1. INPUT CLASSIFICATION: 
   Determine if the input is a Web URL, a File/Image, or a Text/Ciphertext blob.

2. RECONNAISSANCE EXECUTION:
   - IF WEB: 
    a) Fetch the main page and analyze the HTML source code, comments, and headers. 
    b) FOLLOW UP ON CLUES: If the source code contains hints (e.g., mentions of search engines implying robots.txt, visible hidden paths, or directory listing), use your remaining tool calls to fetch those specific paths. 
    c) Do NOT blind-guess completely random paths (like /etc/passwd or /tmp), but YOU MUST investigate logically deduced paths based on the page content.
   - IF FILE/IMAGE: Extract metadata, check file signatures (magic bytes), and run basic string extraction. Look for obvious steganography flags.
   - IF TEXT/CIPHER: Perform frequency analysis, check for common encodings (Base64, Hex), and identify potential hash formats.

3. TRIAGE & HAND-OFF:
   Once you have found the flag, or exhausted your 6 tool calls chasing clues, stop and format your findings.

OUTPUT FORMAT:
You must output your final response in the following exact Markdown structure:

## 1. Target Overview
[Brief description of what the target is]

## 2. Investigation Steps & Findings
[Detail exactly what you fetched, what clues you found, and how you followed up on them.]

## 3. Suspected Category
[Choose one or more: Web Security, Cryptography, Forensics, Reverse Engineering, Pwn/Binary Exploitation, OSINT]

## 4. Artifacts for Hand-off (or Found Flags)
[Provide the exact flag if found, OR specific variables, files, hashes, or code snippets the next agent needs]
"""

    return call_agent(prompt, tools=TOOL_SCHEMAS, tool_map=TOOL_MAP)