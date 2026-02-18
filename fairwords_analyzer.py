"""
FairWords Bias Analyzer
Rule-based detection engine - NO AI/ML to avoid inherited bias
"""

import re
from typing import List, Dict
from bias_patterns import get_all_patterns, get_patterns_by_category


class BiasAnalyzer:
    """
    Main bias detection engine.
    Uses ONLY rule-based pattern matching from peer-reviewed research.
    Zero machine learning to avoid inheriting historical bias.
    """
    
    def __init__(self):
        self.patterns = get_all_patterns()
        self.patterns_by_category = get_patterns_by_category()
    
    def analyze(self, text: str) -> Dict:
        """
        Analyze text for bias patterns.
        Returns complete analysis with findings, score, and explanations.
        """
        if not text or not text.strip():
            return {
                "error": "Empty text provided",
                "score": None,
                "findings": [],
                "categories_affected": []
            }
        
        # Detect all bias patterns
        findings = self._detect_patterns(text)
        
        # Calculate fairness score
        score = self._calculate_score(findings)
        
        # Get affected categories
        categories_affected = list(set([f["category"] for f in findings]))
        
        # Generate summary
        summary = self._generate_summary(findings, score)
        
        return {
            "score": score,
            "findings": findings,
            "total_issues": len(findings),
            "categories_affected": categories_affected,
            "summary": summary,
            "text_length": len(text),
            "word_count": len(text.split())
        }
    
    def _detect_patterns(self, text: str) -> List[Dict]:
        """
        Detect all bias patterns in text using regex matching.
        Returns list of findings with full context.
        """
        findings = []
        
        for pattern_def in self.patterns:
            # Compile regex pattern
            regex = re.compile(pattern_def["pattern"], re.IGNORECASE)
            
            # Find all matches
            matches = list(regex.finditer(text))
            
            if matches:
                # Get unique matched phrases
                unique_matches = list(set([m.group(0) for m in matches]))
                
                findings.append({
                    "id": pattern_def["id"],
                    "category": pattern_def["category"],
                    "severity": pattern_def["severity"],
                    "matches": unique_matches,
                    "count": len(matches),
                    "positions": [m.start() for m in matches],
                    "why": pattern_def["why"],
                    "excludes": pattern_def["excludes"],
                    "impact": pattern_def["impact"],
                    "research": pattern_def["research"],
                    "alternative": pattern_def["alternative"]
                })
        
        return findings
    
    def _calculate_score(self, findings: List[Dict]) -> int:
        """
        Calculate inclusivity score (0-100).
        Higher score = more inclusive.
        Formula based on severity and frequency of issues.
        """
        if not findings:
            return 100
        
        # Start with perfect score
        score = 100
        
        # Deduct points based on severity
        severity_weights = {
            "high": 15,    # High severity: -15 points per occurrence
            "medium": 8,   # Medium severity: -8 points per occurrence
            "low": 3       # Low severity: -3 points per occurrence
        }
        
        for finding in findings:
            severity = finding["severity"]
            count = finding["count"]
            deduction = severity_weights.get(severity, 5) * count
            score -= deduction
        
        # Cap between 0 and 100
        return max(0, min(100, score))
    
    def _generate_summary(self, findings: List[Dict], score: int) -> str:
        """Generate human-readable summary of analysis."""
        if not findings:
            return "No bias patterns detected. This job description uses inclusive language."
        
        total = len(findings)
        categories = len(set([f["category"] for f in findings]))
        high_severity = len([f for f in findings if f["severity"] == "high"])
        
        summary = f"Found {total} bias pattern{'s' if total > 1 else ''} across {categories} categor{'ies' if categories > 1 else 'y'}."
        
        if high_severity > 0:
            summary += f" {high_severity} high-severity issue{'s' if high_severity > 1 else ''} detected."
        
        if score < 50:
            summary += " This job description needs significant revision to attract diverse candidates."
        elif score < 80:
            summary += " Several improvements recommended to increase inclusivity."
        else:
            summary += " Minor adjustments would improve fairness."
        
        return summary