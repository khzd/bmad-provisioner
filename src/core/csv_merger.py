#!/usr/bin/env python3
"""
Smart CSV Merger - Preserve custom user data during re-provisioning
"""

import csv
from pathlib import Path
from typing import List, Dict, Set, Tuple, Optional
from dataclasses import dataclass


@dataclass
class CSVMergeResult:
    """Result of CSV merge operation"""
    merged_rows: List[List[str]]
    new_rows: int
    preserved_rows: int
    updated_rows: int
    custom_rows: int


class SmartCSVMerger:
    """Intelligently merge CSV files preserving custom user data"""
    
    def __init__(self, primary_key_column: int = 0):
        """
        Initialize merger
        
        Args:
            primary_key_column: Column index to use as primary key (default: 0)
        """
        self.primary_key_column = primary_key_column
    
    def read_csv(self, csv_path: Path) -> Tuple[List[str], List[List[str]]]:
        """
        Read CSV file
        
        Returns:
            Tuple of (headers, rows)
        """
        if not csv_path.exists():
            return [], []
        
        with open(csv_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if not rows:
                return [], []
            
            headers = rows[0]
            data_rows = rows[1:]
            
            return headers, data_rows
    
    def write_csv(self, csv_path: Path, headers: List[str], rows: List[List[str]]) -> None:
        """Write CSV file"""
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
    
    def merge(
        self,
        csv_path: Path,
        new_rows: List[List[str]],
        headers: Optional[List[str]] = None
    ) -> CSVMergeResult:
        """
        Merge new rows with existing CSV, preserving custom data
        
        Strategy:
        1. Read existing CSV
        2. Build key map of existing rows
        3. Build key map of new rows
        4. Preserve custom rows (keys not in new_rows)
        5. Update existing rows with new data (preserve user modifications)
        6. Add completely new rows
        
        Args:
            csv_path: Path to CSV file
            new_rows: New rows to merge (without headers)
            headers: Optional headers (will read from existing if not provided)
        
        Returns:
            CSVMergeResult with statistics
        """
        # Read existing CSV
        existing_headers, existing_rows = self.read_csv(csv_path)
        
        # Use provided headers or existing headers
        if headers is None:
            if existing_headers:
                headers = existing_headers
            else:
                # No headers available - just write new rows
                self.write_csv(csv_path, [], new_rows)
                return CSVMergeResult(
                    merged_rows=new_rows,
                    new_rows=len(new_rows),
                    preserved_rows=0,
                    updated_rows=0,
                    custom_rows=0
                )
        
        # Build key maps
        existing_map = self._build_key_map(existing_rows)
        new_map = self._build_key_map(new_rows)
        
        # Track keys
        existing_keys = set(existing_map.keys())
        new_keys = set(new_map.keys())
        
        # Identify row types
        custom_keys = existing_keys - new_keys  # Only in existing (user added)
        common_keys = existing_keys & new_keys  # In both (check for updates)
        fresh_keys = new_keys - existing_keys   # Only in new (provisioner added)
        
        merged_rows = []
        stats = {
            'new': 0,
            'preserved': 0,
            'updated': 0,
            'custom': 0
        }
        
        # Add custom rows first (user-added, not in template)
        for key in sorted(custom_keys):
            merged_rows.append(existing_map[key])
            stats['custom'] += 1
        
        # Add common rows (prefer existing to preserve user edits)
        for key in sorted(common_keys):
            existing_row = existing_map[key]
            new_row = new_map[key]
            
            # Check if user modified any non-key columns
            user_modified = self._has_user_modifications(existing_row, new_row)
            
            if user_modified:
                # Keep existing (user modified)
                merged_rows.append(existing_row)
                stats['preserved'] += 1
            else:
                # Use new (no user modifications)
                merged_rows.append(new_row)
                stats['updated'] += 1
        
        # Add fresh rows (new from provisioner)
        for key in sorted(fresh_keys):
            merged_rows.append(new_map[key])
            stats['new'] += 1
        
        # Write merged CSV
        self.write_csv(csv_path, headers, merged_rows)
        
        return CSVMergeResult(
            merged_rows=merged_rows,
            new_rows=stats['new'],
            preserved_rows=stats['preserved'],
            updated_rows=stats['updated'],
            custom_rows=stats['custom']
        )
    
    def _build_key_map(self, rows: List[List[str]]) -> Dict[str, List[str]]:
        """Build map of primary key -> row"""
        key_map = {}
        for row in rows:
            if not row or len(row) <= self.primary_key_column:
                continue
            
            key = row[self.primary_key_column].strip().lower()
            if key:
                key_map[key] = row
        
        return key_map
    
    def _has_user_modifications(self, existing_row: List[str], new_row: List[str]) -> bool:
        """
        Check if user modified any non-key columns
        
        Strategy: Compare non-key columns. If different, assume user modified.
        """
        if len(existing_row) != len(new_row):
            return True
        
        # Compare all columns except primary key
        for i, (existing_val, new_val) in enumerate(zip(existing_row, new_row)):
            if i == self.primary_key_column:
                continue
            
            # Normalize for comparison
            existing_normalized = existing_val.strip().upper()
            new_normalized = new_val.strip().upper()
            
            if existing_normalized != new_normalized:
                return True
        
        return False


def merge_csv_safely(
    csv_path: Path,
    new_rows: List[List[str]],
    headers: Optional[List[str]] = None,
    primary_key_column: int = 0,
    verbose: bool = False
) -> CSVMergeResult:
    """
    Convenience function for safe CSV merging
    
    Args:
        csv_path: Path to CSV file
        new_rows: New rows to merge
        headers: Optional headers
        primary_key_column: Column to use as key
        verbose: Print merge statistics
    
    Returns:
        CSVMergeResult
    """
    merger = SmartCSVMerger(primary_key_column=primary_key_column)
    result = merger.merge(csv_path, new_rows, headers)
    
    if verbose:
        print(f"📊 CSV Merge Results for {csv_path.name}:")
        print(f"   ✅ New rows: {result.new_rows}")
        print(f"   🔄 Updated rows: {result.updated_rows}")
        print(f"   💾 Preserved rows: {result.preserved_rows}")
        print(f"   ⭐ Custom rows: {result.custom_rows}")
        print(f"   📋 Total rows: {len(result.merged_rows)}")
    
    return result