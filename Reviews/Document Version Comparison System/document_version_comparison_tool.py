'''Problem 10: Document Version Comparison Tool

An internal tool compares different versions of textual documents.

Your system should:
1. Normalize document text
2. Identify structural differences
3. Ignore irrelevant formatting changes
4. Highlight meaningful content changes
5. The solution must use appropriate data structures for comparison and include Pytest-based validation.'''

import re

def normalize_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)  
    return text.strip().lower()

def compare_documents(doc1: str, doc2: str) -> dict:
    doc1 = normalize_text(doc1)
    doc2 = normalize_text(doc2)
    

    words1 = doc1.split(' ')
    words2 = doc2.split(' ')

    changes = {
        'added': [],
        'removed': []
    }

    set1 = set(words1)
    set2 = set(words2)

    diff1 = set2 - set1
    diff2 = set1 - set2
    
    
    for word in diff1:
        changes['added'].append(word)

    for word in diff2:
        changes['removed'].append(word)
    
    return changes
doc1 = '''Meeting Notes
The project deadline is Friday.
All team members must submit their reports.
'''
doc2 = '''MEETING notes
The project deadline is Monday.
All team members should submit their reports.
'''

changes = compare_documents(doc1, doc2)
print("Changes between documents:", changes)



