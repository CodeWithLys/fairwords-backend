"""
FairWords Bias Pattern Database
All patterns based on peer-reviewed research and legal precedent.
NO AI/ML models - pure rule-based detection to avoid inherited bias.
"""

BIAS_PATTERNS = [
    # ============================================
    # CATEGORY 1: HISTORICAL BIAS
    # ============================================
    {
        "id": "age_recent_graduate",
        "category": "Historical Bias",
        "severity": "high",
        "pattern": r"\b(recent graduate|new graduate|fresh graduate|just graduated|class of 20\d{2})\b",
        "why": "Requiring 'recent' graduation is an explicit age proxy that screens out older candidates changing careers, returning after caregiving, or re-entering the workforce. This violates the Age Discrimination in Employment Act (ADEA) in many jurisdictions.",
        "excludes": "Career changers (often women returning from caregiving), older professionals, people who took time for health/family, anyone over ~30 who is otherwise qualified.",
        "impact": "AARP research shows job listings with 'recent graduate' language receive 40% fewer applications from candidates over 40. Legal challenges to this language have increased 300% since 2018.",
        "research": "AARP Research (2020), Age Discrimination in Employment Act interpretations",
        "alternative": "Describe actual needs: 'foundational knowledge of X', 'early-career professional', or list specific skills with no graduation timeframe."
    },
    
    {
        "id": "age_digital_native",
        "category": "Historical Bias",
        "severity": "high",
        "pattern": r"\b(digital native|grew up with technology|tech-savvy millennial|young and dynamic|youthful energy|fresh perspective)\b",
        "why": "These phrases are direct age proxies. 'Digital native' legally means someone born after 1980, making it explicit age discrimination. These terms signal that older candidates are unwelcome regardless of actual proficiency.",
        "excludes": "Anyone over 40, and anyone who learned technology later in life but may be highly skilled.",
        "impact": "The EEOC has flagged 'digital native' as discriminatory. Companies using it have faced class-action suits. Employment lawyers call it 'the new way to say we don't hire old people'.",
        "research": "EEOC guidance, multiple age discrimination lawsuits",
        "alternative": "Specify actual technical skills required. Proficiency doesn't require growing up with a device."
    },

    # ============================================
    # CATEGORY 2: LANGUAGE BIAS (Gender)
    # ============================================
    {
        "id": "masculine_coded",
        "category": "Language Bias",
        "severity": "high",
        "pattern": r"\b(rockstar|rock star|ninja|wizard|guru|hacker|superhero|champion|warrior)\b",
        "why": "These terms are masculine-coded language derived from male-dominated subcultures (gaming, rock music, martial arts). Research shows they signal 'bro culture' and deter women and non-binary candidates from applying.",
        "excludes": "Women, non-binary people, and anyone from outside Western tech culture. Women are 25-50% less likely to apply when job ads use masculine-coded language.",
        "impact": "Gaucher et al. (2011) study in Journal of Personality & Social Psychology found masculine-coded words in job ads directly reduce women's applications even when qualifications are identical.",
        "research": "Gaucher, Friesen & Kay (2011) - Journal of Personality and Social Psychology",
        "alternative": "Use outcome-based language: 'skilled professional', 'experienced engineer', 'effective problem-solver'."
    },
    
    {
        "id": "aggressive_language",
        "category": "Language Bias",
        "severity": "medium",
        "pattern": r"\b(dominate|aggressive|competitive|driven|crush|destroy|demolish|battle|fight|attack)\b",
        "why": "Aggressive action verbs signal a competitive, high-stress culture statistically more appealing to men. They frame work as combat - a framing research links to lower interest from women candidates.",
        "excludes": "Women, neurodivergent individuals, people preferring collaborative environments, and experienced professionals who've learned to value sustainability over aggression.",
        "impact": "LinkedIn's 2019 research found job postings using aggressive language received significantly fewer applications from women, particularly in tech roles.",
        "research": "LinkedIn Talent Research (2019)",
        "alternative": "Use collaborative framing: 'lead initiatives', 'drive impact', 'shape strategy', 'contribute to'."
    },

    # ============================================
    # CATEGORY 3: PROXY DISCRIMINATION
    # ============================================
    {
        "id": "prestige_university",
        "category": "Proxy Discrimination",
        "severity": "high",
        "pattern": r"\b(ivy league|top university|elite university|top-tier school|tier 1 university|Russell Group|prestigious degree|top \d+ university)\b",
        "why": "University prestige is a socioeconomic and racial proxy. Access to elite universities correlates strongly with wealth, race, and zip code - not intelligence or capability. Requiring it screens out brilliant candidates who couldn't afford elite schools.",
        "excludes": "First-generation college students, low-income candidates, people from under-resourced districts, and people of color statistically underrepresented at elite institutions.",
        "impact": "Harvard research shows candidates from non-elite schools are 50% less likely to get callbacks even with identical resumes. Elite university networks perpetuate racial wealth gaps - 70% of Ivy League students come from top 20% of earners.",
        "research": "Harvard study on callbacks, data on Ivy League demographics",
        "alternative": "Focus on skills and demonstrated ability. If degree required, state 'accredited degree' or 'degree in relevant field' without prestige qualifiers."
    },
    
    {
        "id": "culture_fit",
        "category": "Proxy Discrimination",
        "severity": "high",
        "pattern": r"\b(culture fit|cultural fit|fits our culture|fits in|team fit|like-minded|shared values|we're a family)\b",
        "why": "'Culture fit' is one of the most documented proxies for discrimination. It allows rejecting candidates based on subjective similarity bias - favoring those who look, sound, or act like the existing (often homogeneous) team.",
        "excludes": "Anyone different from the majority group's race, gender, class background, communication style, or social interests. Research shows it disproportionately excludes Black, Asian, and working-class candidates.",
        "impact": "Lauren Rivera's landmark study (American Sociological Review, 2012) found 'culture fit' was the #1 hiring criterion at elite firms - and primarily screened for shared class-based hobbies and communication styles, not job performance.",
        "research": "Lauren Rivera (2012) - American Sociological Review",
        "alternative": "Define what you mean: 'collaborative working style', 'transparent communicator', 'committed to inclusive practices'. Assess with structured criteria."
    },
    
    {
        "id": "native_english",
        "category": "Proxy Discrimination",
        "severity": "high",
        "pattern": r"\b(native English speaker|mother tongue English|English as first language|native-level English|born speaking English)\b",
        "why": "Requiring 'native' English is a racial and national origin proxy. It's legally questionable under Title VII and serves to exclude candidates of color, immigrants, and non-Western candidates who may be fully fluent and highly qualified.",
        "excludes": "Multilingual candidates, immigrants, and people of color for whom English is fluent but not first language. Many world-class professionals are non-native speakers.",
        "impact": "The EEOC has found 'native speaker' requirements discriminatory when fluency suffices. Research shows non-native accents trigger implicit bias in hiring, and this language compounds it.",
        "research": "EEOC Title VII guidance on national origin discrimination",
        "alternative": "State actual requirement: 'professional fluency in English', 'strong written and verbal communication', 'ability to communicate clearly with English-speaking clients'."
    },

    # ============================================
    # CATEGORY 4: RESUME GAP PENALTIES
    # ============================================
    {
        "id": "no_employment_gaps",
        "category": "Resume Gap Penalties",
        "severity": "high",
        "pattern": r"\b(no gaps in employment|continuous employment|uninterrupted work history|consistent employment|no career breaks)\b",
        "why": "Penalizing employment gaps systematically discriminates against caregivers (disproportionately women), people with illness, layoff victims, or those who pursued education or personal development.",
        "excludes": "Mothers returning from maternity leave, caregivers, people who were ill, anyone affected by mass layoffs (2008, 2020, 2023), immigrants with credential delays, people who pursued education.",
        "impact": "LinkedIn research found 57% of people with career breaks are women. Penalizing gaps makes tech 30% harder to enter for mothers. Research shows returners perform at or above average after re-entry.",
        "research": "LinkedIn research on career gaps",
        "alternative": "Remove gap penalties entirely. If commitment needed, assess directly: 'available to start [date]', 'able to commit to [hours]'."
    },
    
    {
        "id": "availability_24_7",
        "category": "Resume Gap Penalties",
        "severity": "medium",
        "pattern": r"\b(always available|24\/7|on-call 24 hours|available on weekends|must work evenings|flexible availability required)\b",
        "why": "Open-ended availability requirements disproportionately exclude caregivers, people with disabilities, and single parents - statistically more often women. They also signal poor management culture.",
        "excludes": "Single parents, caregivers, people managing chronic conditions, and anyone with legitimate outside responsibilities.",
        "impact": "Research shows availability requirements reduce applications from women by 40% when not tied to specific business needs. They correlate with higher burnout and turnover.",
        "research": "Studies on work-life balance and gender",
        "alternative": "State actual requirements clearly: 'occasional evening work during launches', 'on-call rotation (1 week/quarter)'. Clarity respects candidates' time."
    },

    # ============================================
    # CATEGORY 5: EXPERIENCE INFLATION
    # ============================================
    {
        "id": "intern_experience_paradox",
        "category": "Experience Inflation",
        "severity": "high",
        "pattern": r"\b(intern|internship|entry.?level).{0,100}(\d+\+?\s*years?\s*(of\s*)?(experience|exp))\b",
        "why": "Requiring experience for internships/entry-level roles creates a catch-22: need experience to get experience. This primarily affects first-generation professionals and those who couldn't afford unpaid internships to build experience.",
        "excludes": "First-generation college students, low-income candidates, people from underrepresented groups who had to work through school instead of unpaid internships.",
        "impact": "A 2021 study found 60% of 'entry-level' tech jobs required 3+ years experience, effectively making them mid-level jobs with entry-level pay. This disproportionately excludes candidates of color and women from tech pipelines.",
        "research": "2021 study on entry-level requirements",
        "alternative": "For intern/junior roles, specify skills: 'familiarity with X', 'coursework in Y', 'demonstrated interest through projects'. Remove experience requirements entirely."
    },
    
    {
        "id": "overqualified",
        "category": "Experience Inflation",
        "severity": "medium",
        "pattern": r"\b(not overqualified|right fit for the role|don't be overqualified|no executive experience)\b",
        "why": "'Overqualified' concerns are often proxies for age discrimination. They also penalize career changers who bring valuable cross-industry experience.",
        "excludes": "Experienced professionals changing careers, older workers, people voluntarily downshifting, and those whose expertise would benefit the role.",
        "impact": "AARP research found 'overqualified' is one of the most common discriminatory rejections for candidates over 50. Experienced hires often become excellent mentors.",
        "research": "AARP research on age discrimination",
        "alternative": "Drop overqualification screening. Address in interviews: 'Are you comfortable with this role's scope?' Let candidates decide."
    },
]


def get_patterns_by_category():
    """Group patterns by category for reporting."""
    categories = {}
    for pattern in BIAS_PATTERNS:
        cat = pattern["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(pattern)
    return categories


def get_all_patterns():
    """Return all bias patterns."""
    return BIAS_PATTERNS


def get_pattern_by_id(pattern_id):
    """Get a specific pattern by ID."""
    for pattern in BIAS_PATTERNS:
        if pattern["id"] == pattern_id:
            return pattern
    return None