#!/usr/bin/env python3
import os
import re
from collections import Counter, defaultdict

# Define paths
exam_folder = "/Users/amn/amn_local/dev/projects/credibleinc/inhouse/teach/bscit_sem5_ai_practicals_ameen/workspace/examprep/class10"

# Dictionary to store questions and their answers
question_info = {}

# Function to extract questions and answers from text files
def extract_questions_from_file(file_path, year):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split content by lines for easier processing
    lines = content.split('\n')
    
    # Regular expressions to identify question patterns
    question_patterns = [
        r'[Q|q]\.?\d*\.?\s*\([a-z]\)\s*(.*?)(?:\(\d+\)|\n)',  # Q1(a) pattern
        r'[Q|q]\.?\d*\.?\([a-z]\)\s*(.*?)(?:\(\d+\)|\n)',     # Q1(a) without space
        r'[a-z]\)\s*(.*?)(?:\(\d+\)|\n)',                     # a) pattern
        r'[Q|q]\d+\.?\([a-z]\)\s*(.*?)(?:\(\d+\)|\n)',        # Q1(a) pattern
        r'[Q|q]\d+[a-z]\.\s*(.*?)(?:\(\d+\)|\n)'             # Q1a. pattern
    ]
    
    current_question = None
    current_answer = []
    in_answer = False
    
    # Process each line
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this is a question line
        is_question_line = False
        for pattern in question_patterns:
            matches = re.findall(pattern, line + '\n')
            if matches:
                # If we were collecting an answer, save it
                if current_question and in_answer:
                    save_question_answer(current_question, '\n'.join(current_answer), year)
                    current_answer = []
                
                # Extract the question text
                current_question = matches[0].strip()
                # Remove marks indicators like (5)
                current_question = re.sub(r'\(\d+\)', '', current_question).strip()
                
                # Initialize for new answer
                in_answer = True
                is_question_line = True
                break
        
        # If not a question line and we're collecting an answer, add to current answer
        if not is_question_line and in_answer and current_question:
            # Skip lines that are likely not part of the answer (e.g. page numbers)
            if not re.match(r'^MUQuestionPapers\.com', line) and not re.match(r'^\d+$', line):
                current_answer.append(line)
    
    # Save the last question-answer pair
    if current_question and in_answer:
        save_question_answer(current_question, '\n'.join(current_answer), year)

# Alternative extraction method for papers with different structure
def extract_questions_alternative(file_path, year):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Find all question sections using patterns like "Q1. " or "Q1 " or "a) " etc.
    sections = re.split(r'(?:\n|\s)(?:[Qq]\d+\.?[\s\(][a-z]\)|[a-z]\))', content)
    
    # Clean up each section to get question and answer
    for i, section in enumerate(sections[1:], 1):  # Skip first section which is usually header
        lines = section.strip().split('\n')
        
        # First line is usually part of the question
        question_line = lines[0].strip()
        
        # Skip very short question lines that are likely not questions
        if len(question_line) < 5:
            continue
        
        # Clean up question line
        question = question_line.strip()
        question = re.sub(r'\(\d+\)', '', question).strip()  # Remove marks indicators like (5)
        
        # Skip if it's not a proper question
        if len(question) < 10 or question.lower().startswith('muquestionpapers'):
            continue
        
        # Everything after is the answer
        answer_lines = lines[1:]
        answer = '\n'.join(answer_lines).strip()
        
        # Clean up answer
        answer = re.sub(r'MUQuestionPapers\.com\s*\d+', '', answer)
        
        if question and answer:
            save_question_answer(question, answer, year)

def save_question_answer(question, answer, year):
    # Clean up question
    question = re.sub(r'\s+', ' ', question).strip()
    # Skip questions that are too short or look like headers
    if len(question) < 10 or question.lower().startswith('muquestionpapers') or question.lower().startswith('attempt'):
        return
    
    # Clean up answer
    answer = re.sub(r'MUQuestionPapers\.com\s*\d+', '', answer)
    answer = re.sub(r'\s+', ' ', answer).strip()
    
    # Normalize question text to help identify duplicates
    normalized_question = question.lower().strip()
    
    # Store question information
    if normalized_question not in question_info:
        question_info[normalized_question] = {
            'original_text': question,
            'appearances': [],
            'answers': []
        }
    
    # Update appearances and answers
    if year not in question_info[normalized_question]['appearances']:
        question_info[normalized_question]['appearances'].append(year)
        question_info[normalized_question]['answers'].append({
            'year': year,
            'text': answer
        })

# Alternative extraction specifically for Enterprise Java papers
def extract_enterprise_java_questions(file_path, year):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Pattern to find Q1(a), a), etc. style questions
    pattern = r'(?:[Qq]\d+\s*\([a-z]\)|[a-z]\))\s*([^.?]*[\w\s]+[.?])'
    
    # Find all matches
    matches = re.finditer(pattern, content)
    
    for match in matches:
        full_match = match.group(0)  # The full matched text
        question_text = match.group(1).strip()  # Just the question part
        
        # Skip if the question looks invalid
        if len(question_text) < 10 or 'muquestionpapers' in question_text.lower():
            continue
        
        # Find the position where this question appears
        pos = match.start()
        
        # Find the next question by looking for another pattern match
        next_match = re.search(pattern, content[pos + len(full_match):])
        
        if next_match:
            next_pos = pos + len(full_match) + next_match.start()
            # Answer is everything between this question and the next
            answer_text = content[pos + len(full_match):next_pos].strip()
        else:
            # For the last question, take a reasonable chunk
            answer_text = content[pos + len(full_match):pos + len(full_match) + 1000].strip()
        
        # Clean up answer
        answer_text = re.sub(r'MUQuestionPapers\.com\s*\d+', '', answer_text)
        answer_text = re.sub(r'\(\d+\)', '', answer_text).strip()
        
        save_question_answer(question_text, answer_text, year)

# Process all text files
for filename in os.listdir(exam_folder):
    if filename.endswith('.txt'):
        year_match = re.search(r'(\d{4})_(\w+)', filename)
        if year_match:
            year = f"{year_match.group(1)} {year_match.group(2).capitalize()}"
            file_path = os.path.join(exam_folder, filename)
            print(f"Processing {filename}...")
            
            # Use different extraction methods and combine results
            extract_questions_from_file(file_path, year)
            extract_questions_alternative(file_path, year)
            extract_enterprise_java_questions(file_path, year)

# Manual cleanup - remove duplicates based on similarity
def clean_duplicates():
    # First, create a list from the dictionary
    questions_list = list(question_info.items())
    
    # Sort by length of appearances (frequency)
    questions_list.sort(key=lambda x: len(x[1]['appearances']), reverse=True)
    
    # For each question, check if there's a very similar question already processed
    to_remove = set()
    for i, (q1, info1) in enumerate(questions_list):
        if q1 in to_remove:
            continue
            
        for j, (q2, info2) in enumerate(questions_list[i+1:], i+1):
            if q2 in to_remove:
                continue
                
            # Simple similarity check - if one contains the other
            if q1 in q2 or q2 in q1 or similarity_score(q1, q2) > 0.8:
                # Keep the one with more appearances
                if len(info1['appearances']) >= len(info2['appearances']):
                    to_remove.add(q2)
                    # Merge appearances and answers
                    for year in info2['appearances']:
                        if year not in info1['appearances']:
                            info1['appearances'].append(year)
                    for answer in info2['answers']:
                        if answer['year'] not in [a['year'] for a in info1['answers']]:
                            info1['answers'].append(answer)
                else:
                    to_remove.add(q1)
                    # Merge appearances and answers
                    for year in info1['appearances']:
                        if year not in info2['appearances']:
                            info2['appearances'].append(year)
                    for answer in info1['answers']:
                        if answer['year'] not in [a['year'] for a in info2['answers']]:
                            info2['answers'].append(answer)
                    break  # Break because q1 is now marked for removal
    
    # Remove the duplicates
    for q in to_remove:
        if q in question_info:
            del question_info[q]

# Simple text similarity function
def similarity_score(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    if not words1 or not words2:
        return 0
    
    intersection = words1.intersection(words2)
    return len(intersection) / max(len(words1), len(words2))

# Clean up duplicates
clean_duplicates()

# Sort questions by frequency
sorted_questions = sorted(question_info.items(), key=lambda x: len(x[1]['appearances']), reverse=True)

# Generate HTML
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise Java Exam Preparation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-top: 20px;
            background-color: #f8f9fa;
        }
        .question-card {
            margin-bottom: 20px;
            border-left: 5px solid #007bff;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .frequency-badge {
            font-size: 0.9rem;
            margin-right: 10px;
            background-color: #0d6efd;
        }
        .answer-container {
            display: none;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
            margin-top: 10px;
            border: 1px solid #dee2e6;
        }
        .detail-btn {
            margin-top: 10px;
        }
        .search-container {
            margin-bottom: 30px;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .years-appeared {
            font-style: italic;
            color: #6c757d;
            margin-bottom: 10px;
        }
        .question-number {
            font-weight: bold;
            margin-right: 10px;
            color: #0d6efd;
        }
        .card-header {
            background-color: #e7f1ff;
            font-weight: 500;
        }
        .header-container {
            background-color: #0d6efd;
            color: white;
            padding: 20px 0;
            margin-bottom: 30px;
            border-radius: 10px;
        }
        .btn-toggle {
            color: white;
            background-color: #0d6efd;
            border-color: #0d6efd;
            margin-right: 10px;
        }
        .btn-toggle:hover {
            background-color: #0b5ed7;
            border-color: #0b5ed7;
        }
        .btn-detail {
            color: white;
            background-color: #6c757d;
            border-color: #6c757d;
        }
        .btn-detail:hover {
            background-color: #5a6268;
            border-color: #5a6268;
        }
        .filter-buttons {
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-container text-center">
            <h1 class="mb-3">Enterprise Java Exam Preparation</h1>
            <p class="lead">Questions sorted by frequency of appearance in previous papers</p>
        </div>
        
        <div class="search-container">
            <input type="text" id="searchInput" class="form-control form-control-lg" placeholder="Search for topics or keywords...">
            <div class="filter-buttons mt-3">
                <button class="btn btn-outline-primary" data-year="all">All Years</button>
                <button class="btn btn-outline-primary" data-year="2018">2018</button>
                <button class="btn btn-outline-primary" data-year="2019">2019</button>
                <button class="btn btn-outline-primary" data-year="2022">2022</button>
                <button class="btn btn-outline-success ms-3" id="showAllAnswers">Show All Answers</button>
                <button class="btn btn-outline-danger ms-2" id="hideAllAnswers">Hide All Answers</button>
            </div>
        </div>
        
        <div id="questions-container">
'''

# Add questions to HTML
for i, (_, info) in enumerate(sorted_questions):
    question = info['original_text']
    freq = len(info['appearances'])
    appearances = ", ".join(info['appearances'])
    
    # Skip very short questions or invalid entries
    if len(question) < 10:
        continue
    
    html_content += f'''
        <div class="card question-card" data-years="{','.join(info['appearances'])}">
            <div class="card-header">
                <div class="d-flex align-items-center">
                    <span class="question-number">Q{i+1}.</span>
                    <span class="badge frequency-badge">{freq} times</span>
                    <span>{question}</span>
                </div>
            </div>
            <div class="card-body">
                <p class="years-appeared">Appeared in: {appearances}</p>
                <button class="btn btn-sm btn-primary toggle-answer">Show/Hide Answer</button>
                <div class="answer-container">
                    <h5>Answer:</h5>
                    <div class="answer-text">
                        {info['answers'][0]['text']}
                    </div>
                    <button class="btn btn-sm btn-secondary detail-btn mt-3" data-bs-toggle="modal" data-bs-target="#detailModal{i}">
                        More Detailed Explanation
                    </button>
                </div>
            </div>
        </div>
    '''
    
    # Add modal for detailed explanation
    html_content += f'''
        <div class="modal fade" id="detailModal{i}" tabindex="-1" aria-labelledby="detailModalLabel{i}" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header bg-primary text-white">
                        <h5 class="modal-title" id="detailModalLabel{i}">Detailed Explanation</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="question-detail mb-4">
                            <h4 class="mb-3">{question}</h4>
                            <div class="badge bg-info text-dark mb-3">Appeared {freq} times: {appearances}</div>
                        </div>
                        <hr>
                        <div class="detailed-answer">
                            <h5 class="text-primary">Comprehensive Answer:</h5>
                            <div class="p-3 bg-light rounded mb-4">
                                {info['answers'][0]['text']}
                            </div>
                            
                            <h5 class="text-primary mt-4">Historical Answers by Year:</h5>
                            <div class="accordion" id="answerHistory{i}">
    '''
    
    # Add historical answers in accordion
    for j, answer_info in enumerate(info['answers']):
        html_content += f'''
                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading{i}_{j}">
                        <button class="accordion-button {"" if j == 0 else "collapsed"}" type="button" data-bs-toggle="collapse" 
                                data-bs-target="#collapse{i}_{j}" aria-expanded="{'true' if j == 0 else 'false'}" 
                                aria-controls="collapse{i}_{j}">
                            {answer_info['year']}
                        </button>
                    </h2>
                    <div id="collapse{i}_{j}" class="accordion-collapse collapse {"show" if j == 0 else ""}" 
                         aria-labelledby="heading{i}_{j}" data-bs-parent="#answerHistory{i}">
                        <div class="accordion-body">
                            {answer_info['text']}
                        </div>
                    </div>
                </div>
            '''
    
    html_content += '''
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    '''

# Complete HTML
html_content += '''
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Toggle answer visibility
            const toggleButtons = document.querySelectorAll('.toggle-answer');
            toggleButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const answerContainer = this.nextElementSibling;
                    if (answerContainer.style.display === 'block') {
                        answerContainer.style.display = 'none';
                        this.textContent = 'Show Answer';
                    } else {
                        answerContainer.style.display = 'block';
                        this.textContent = 'Hide Answer';
                    }
                });
            });
            
            // Search functionality
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('input', filterQuestions);
            
            // Year filter buttons
            const yearButtons = document.querySelectorAll('[data-year]');
            yearButtons.forEach(button => {
                button.addEventListener('click', function() {
                    // Remove active class from all buttons
                    yearButtons.forEach(btn => btn.classList.remove('active', 'btn-primary', 'text-white'));
                    // Add active class to clicked button
                    this.classList.add('active', 'btn-primary', 'text-white');
                    
                    filterQuestions();
                });
            });
            
            // Show/Hide all answers
            document.getElementById('showAllAnswers').addEventListener('click', function() {
                document.querySelectorAll('.answer-container').forEach(container => {
                    container.style.display = 'block';
                });
                document.querySelectorAll('.toggle-answer').forEach(button => {
                    button.textContent = 'Hide Answer';
                });
            });
            
            document.getElementById('hideAllAnswers').addEventListener('click', function() {
                document.querySelectorAll('.answer-container').forEach(container => {
                    container.style.display = 'none';
                });
                document.querySelectorAll('.toggle-answer').forEach(button => {
                    button.textContent = 'Show Answer';
                });
            });
            
            function filterQuestions() {
                const searchText = searchInput.value.toLowerCase();
                const activeYearBtn = document.querySelector('[data-year].active');
                const yearFilter = activeYearBtn ? activeYearBtn.getAttribute('data-year') : 'all';
                
                const questionCards = document.querySelectorAll('.question-card');
                
                questionCards.forEach(card => {
                    const questionText = card.querySelector('.card-header').textContent.toLowerCase();
                    const answerContainer = card.querySelector('.answer-container');
                    const answerText = answerContainer ? answerContainer.textContent.toLowerCase() : '';
                    const cardYears = card.getAttribute('data-years').split(',');
                    
                    // Check if card matches search text
                    const matchesSearch = searchText === '' || 
                                         questionText.includes(searchText) || 
                                         answerText.includes(searchText);
                    
                    // Check if card matches year filter
                    const matchesYear = yearFilter === 'all' || 
                                       cardYears.some(year => year.includes(yearFilter));
                    
                    if (matchesSearch && matchesYear) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
            
            // Initialize with "all" filter active
            document.querySelector('[data-year="all"]').classList.add('active', 'btn-primary', 'text-white');
        });
    </script>
    
    <footer class="mt-5 py-3 text-center">
        <div class="container">
            <p class="text-muted">Enterprise Java Exam Preparation Guide</p>
        </div>
    </footer>
</body>
</html>
'''

# Write HTML to file
with open(os.path.join(exam_folder, "improved_exam_prep_guide.html"), 'w') as html_file:
    html_file.write(html_content)

print("Improved HTML exam preparation guide has been created successfully!")
