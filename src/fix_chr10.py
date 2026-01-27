#!/usr/bin/env python3
"""
Fix chr(10).join() in f-strings - Python syntax error
"""

import re
import sys
from pathlib import Path

def fix_file(filepath):
    """Fix all chr(10).join() patterns in file"""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: Line 244 - specialists menu
    content = content.replace(
        '''{chr(10).join([f"- `/{s['id']}` - Load {s['name']}" for s in specialists])}''',
        '''"""
    
    # Build specialists menu
    for s in specialists:
        content += f"\\n- `/{s['id']}` - Load {s['name']}"
    
    content += """'''
    )
    
    # Pattern 2: Line 313 - skills list
    content = content.replace(
        '''{chr(10).join([f"- {skill}" for skill in specialist['skills']])}''',
        '''"""
    
    # Build skills list
    for skill in specialist['skills']:
        content += f"\\n- {skill}"
    
    content += """'''
    )
    
    # Pattern 3: Line 323 - principles list
    content = content.replace(
        '''{chr(10).join([f"- {principle}" for principle in specialist.get('principles', ['Maintain domain best practices', 'Ensure quality and consistency'])])}''',
        '''"""
    
    # Build principles list
    for principle in specialist.get('principles', ['Maintain domain best practices', 'Ensure quality and consistency']):
        content += f"\\n- {principle}"
    
    content += """'''
    )
    
    # Pattern 4: Line 406 - routing table
    content = content.replace(
        '''{chr(10).join([f"| {s['trigger_conditions']} | {s['name']} | {s['domain']} |" for s in specialists])}''',
        '''"""
    
    # Build routing table rows
    for s in specialists:
        content += f"\\n| {s['trigger_conditions']} | {s['name']} | {s['domain']} |"
    
    content += """'''
    )
    
    # Pattern 5: Line 469 - tree structure
    content = content.replace(
        '''{chr(10).join([f"    ├─→ {s['name']}" for s in specialists[1:-1]])}''',
        '''"""
    
    # Build tree structure for middle specialists
    for s in specialists[1:-1]:
        content += f"\\n    ├─→ {s['name']}"
    
    content += """'''
    )
    
    # Pattern 6: Line 482 - specialists list with details
    content = content.replace(
        '''{chr(10).join([f"**{i+1}. {s['name']}**  \\n**File**: `agents/specialist-{s['id']}.md`  \\n**Domain**: {s['domain']}\\n" for i, s in enumerate(specialists)])}''',
        '''"""
    
    # Build specialists list with details
    for i, s in enumerate(specialists):
        content += f"\\n**{i+1}. {s['name']}**  \\n**File**: `agents/specialist-{s['id']}.md`  \\n**Domain**: {s['domain']}\\n"
    
    content += """'''
    )
    
    if content == original_content:
        print("❌ No changes made - patterns not found")
        return False
    
    # Backup original
    backup_path = filepath.parent / f"{filepath.name}.backup"
    with open(backup_path, 'w') as f:
        f.write(original_content)
    print(f"✅ Backup saved: {backup_path}")
    
    # Write fixed version
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Fixed: {filepath}")
    
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_chr10.py <path_to_init_bmad_skill.py>")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    
    success = fix_file(filepath)
    sys.exit(0 if success else 1)