#!/usr/bin/env python3
import os
import re
from collections import Counter, defaultdict

# Define paths
exam_folder = "/Users/amn/amn_local/dev/projects/credibleinc/inhouse/teach/bscit_sem5_ai_practicals_ameen/workspace/examprep/class10"

# Dictionary to store questions and their answers
questions = defaultdict(list)
question_freq = Counter()
question_info = {}

# Function to extract questions and answers from text files
def extract_questions_from_file(file_path, year):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Extract questions and answers
    q_pattern = r"(?:Q\d+\s*\([a-z]\)|[a-z]\)\s*)[^.?]*[\w\s]+\?"  # Pattern to match questions
    
    # Find all questions using regex
    questions_found = re.findall(r"(?:[Qq]\d*\s*\([a-z]\)|[a-z]\)\s*)([^.?]*[\w\s]+[.?])", content)
    
    # Clean up questions
    clean_questions = []
    for q in questions_found:
        q = q.strip()
        # Remove line breaks and extra spaces
        q = re.sub(r'\s+', ' ', q)
        # Remove marks indicators like (5)
        q = re.sub(r'\(\d+\)', '', q)
        if len(q) > 10:  # Avoid too short strings that are not questions
            clean_questions.append(q)
    
    # Find answers (text between questions)
    for i, q in enumerate(clean_questions):
        question_text = q
        
        # Find the answer text
        if i < len(clean_questions) - 1:
            next_q_pos = content.find(clean_questions[i+1])
            q_pos = content.find(q)
            if q_pos >= 0 and next_q_pos > q_pos:
                answer_text = content[q_pos + len(q):next_q_pos].strip()
            else:
                answer_text = "Answer not found"
        else:
            # For the last question, take everything after it
            q_pos = content.find(q)
            if q_pos >= 0:
                answer_text = content[q_pos + len(q):].strip()
                # Limit answer length for last question
                answer_text = answer_text[:1000] if len(answer_text) > 1000 else answer_text
            else:
                answer_text = "Answer not found"
        
        # Clean up answers
        answer_text = re.sub(r'\s+', ' ', answer_text)
        
        # Update question frequency counter
        question_freq[question_text] += 1
        
        # Store question and answer info
        if question_text not in question_info:
            question_info[question_text] = {
                'appearances': [],
                'answers': []
            }
        
        question_info[question_text]['appearances'].append(year)
        question_info[question_text]['answers'].append({
            'year': year,
            'text': answer_text
        })

# Process all text files
for filename in os.listdir(exam_folder):
    if filename.endswith('.txt'):
        year_match = re.search(r'(\d{4})_(\w+)', filename)
        if year_match:
            year = f"{year_match.group(1)} {year_match.group(2).capitalize()}"
            file_path = os.path.join(exam_folder, filename)
            extract_questions_from_file(file_path, year)

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
        }
        .question-card {
            margin-bottom: 20px;
            border-left: 5px solid #007bff;
        }
        .frequency-badge {
            font-size: 1rem;
            margin-right: 10px;
        }
        .answer-container {
            display: none;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-top: 10px;
        }
        .detail-btn {
            margin-top: 10px;
        }
        .search-container {
            margin-bottom: 30px;
        }
        .years-appeared {
            font-style: italic;
            color: #6c757d;
        }
        .question-number {
            font-weight: bold;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Enterprise Java Exam Preparation</h1>
        <div class="search-container">
            <input type="text" id="searchInput" class="form-control" placeholder="Search for questions...">
        </div>
        <div id="questions-container">
'''

# Add questions to HTML
for i, (question, info) in enumerate(sorted_questions):
    freq = len(info['appearances'])
    appearances = ", ".join(info['appearances'])
    
    html_content += f'''
        <div class="card question-card">
            <div class="card-header">
                <span class="question-number">Q{i+1}.</span>
                <span class="badge bg-primary frequency-badge">{freq} times</span>
                <span>{question}</span>
            </div>
            <div class="card-body">
                <p class="years-appeared">Appeared in: {appearances}</p>
                <button class="btn btn-sm btn-primary toggle-answer">Show/Hide Answer</button>
                <div class="answer-container">
                    <h5>Answer:</h5>
                    <p>{info['answers'][0]['text']}</p>
                    <button class="btn btn-sm btn-secondary detail-btn" data-bs-toggle="modal" data-bs-target="#detailModal{i}">
                        More Detailed Explanation
                    </button>
                </div>
            </div>
        </div>
    '''
    
    # Add modal for detailed explanation
    html_content += f'''
        <div class="modal fade" id="detailModal{i}" tabindex="-1" aria-labelledby="detailModalLabel{i}" aria-hidden="true">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="detailModalLabel{i}">Detailed Explanation</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <h4>{question}</h4>
                        <hr>
                        <div class="detailed-answer">
                            <h5>Comprehensive Answer:</h5>
                            <p>{info['answers'][0]['text']}</p>
                            
                            <h5>Historical Answers:</h5>
                            <div class="accordion" id="answerHistory{i}">
    '''
    
    # Add historical answers in accordion
    for j, answer_info in enumerate(info['answers']):
        if j > 0:  # Skip the first one as it's already shown
            html_content += f'''
                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading{i}_{j}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" 
                                data-bs-target="#collapse{i}_{j}" aria-expanded="false" aria-controls="collapse{i}_{j}">
                            {answer_info['year']}
                        </button>
                    </h2>
                    <div id="collapse{i}_{j}" class="accordion-collapse collapse" 
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
                    } else {
                        answerContainer.style.display = 'block';
                    }
                });
            });
            
            // Search functionality
            const searchInput = document.getElementById('searchInput');
            searchInput.addEventListener('keyup', function() {
                const searchText = this.value.toLowerCase();
                const questionCards = document.querySelectorAll('.question-card');
                
                questionCards.forEach(card => {
                    const questionText = card.querySelector('.card-header').textContent.toLowerCase();
                    const answerText = card.querySelector('.answer-container').textContent.toLowerCase();
                    
                    if (questionText.includes(searchText) || answerText.includes(searchText)) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>
'''

# Write HTML to file
with open(os.path.join(exam_folder, "exam_prep_guide.html"), 'w') as html_file:
    html_file.write(html_content)

print("HTML exam preparation guide has been created successfully!")
